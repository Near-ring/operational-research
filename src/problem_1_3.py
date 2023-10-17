__author__ = "Chuan Tian"
import numpy as np
import gurobipy as gb
import pandas as pd
from numpy import ndarray
from gurobipy import MVar

# Read data from CSV files
raw_nodes = pd.read_csv("nodes.csv")
raw_piplines = pd.read_csv("pipelines.csv")
nodes = raw_nodes.to_numpy()
piplines = raw_piplines.to_numpy()

# Define column indices for nodes and pipelines
Node1, Node2, Demand = 1, 2, 3
E, N = len(piplines), len(nodes)

# Compute distances between nodes and create E array
START_NODES = piplines[:, 1].astype(int)
END_NODES = piplines[:, 2].astype(int)
START_NODES_XY = nodes[START_NODES, 1:3]
END_NODES_XY = nodes[END_NODES, 1:3]
distances = np.linalg.norm(START_NODES_XY - END_NODES_XY, axis=1)
distances = distances.reshape(-1)

# Create Gurobi model and variables
m = gb.Model("a1")
X: MVar = m.addMVar((E,))  # Decision variable for the amount of flow between nodes
Y: MVar = m.addMVar((N,))  # Decision variable for the generation amount at each node

# Define demand, capacity, and cost arrays
demand = nodes[:, Demand]
capacity_map = {10: 417, 18: 875, 27: 914, 30: 637}
cost_map = {10: 72, 18: 77, 27: 72, 30: 87}

capacity, cost = np.zeros(N), np.zeros(N)
np.put(capacity, list(capacity_map.keys()), list(capacity_map.values()))
np.put(cost, list(cost_map.keys()), list(cost_map.values()))

# Set objective function
m.setObjective((cost * Y).sum() + (0.01 * X * distances).sum(), gb.GRB.MINIMIZE)

for i in range(N):
    # Add capacity constraints
    m.addConstr(Y[i] <= capacity[i])
    # Add balance constraints
    m.addConstr(
        Y[i] + X[END_NODES == i].sum()
        ==
        X[START_NODES == i].sum() + demand[i]
    )


for i in range(E):
    m.addConstr(X[i] <= 309)

# Optimize the model
m.optimize()

# Print the results
print("Total cost=", m.objval)
for i in range(N):
    if Y[i].x > 0:
        print("Generator", i, "=", Y[i].x)

############################################################
# Promblem 2
raw_nodes2 = pd.read_csv("nodes2.csv")
nodes2 = raw_nodes2.to_numpy()
demand = nodes2[:, 3:]
l = 14

m2 = gb.Model()
X: MVar = m2.addMVar((E, l))  # Decision variable for the amount of flow between nodes over time
Y: MVar = m2.addMVar((N, l))  # Decision variable for the generation amount at each node over time

cost = cost.reshape(-1, 1)
distances = distances.reshape(-1, 1)

m2.setObjective(((cost * Y).sum(axis=0) + (0.01 * X * distances).sum(axis=0)).sum(), gb.GRB.MINIMIZE)

for j in range(l):
    for i in range(N):
        # Add capacity constraints
        m2.addConstr(Y[i, j] <= capacity[i])
        # Add balance constraints
        m2.addConstr(
            Y[i, j] + X[END_NODES == i, j].sum()
            ==
            X[START_NODES == i, j].sum() + demand[i, j]
        )

for j in range(l):
    for i in range(E):
        m2.addConstr(X[i, j] <= 309)

for i in range(N):
    m2.addConstr(gb.quicksum(Y[i, j] for j in range(l)) <= 8759)
#
# Optimize the model
m2.optimize()
# Print the results
print("Total cost=", m2.objval)

############################################################
# Problem 3
raw_nodes2 = pd.read_csv("nodes2.csv")
nodes2 = raw_nodes2.to_numpy()
demand = nodes2[:, 3:]
l = 14

m3 = gb.Model()
X: MVar = m3.addMVar((E, l))
Y: MVar = m3.addMVar((N, l))
Z1: MVar = m3.addMVar((E, l))
Z2: MVar = m3.addMVar((E, l))

cost = cost.reshape(-1, 1)
distances = distances.reshape(-1, 1)

m3.setObjective(((cost * Y).sum(axis=0) +
                 (0.01 * distances * X).sum(axis=0) + (0.1 * (Z1 + Z2)).sum(axis=0)).sum(), gb.GRB.MINIMIZE)

for j in range(l):
    for i in range(N):
        # Add capacity constraints
        m3.addConstr(Y[i, j] <= capacity[i])
        # Add balance constraints with positive and negative changes in flow on nodes
        m3.addConstr(
            Y[i, j] + X[END_NODES == i, j].sum() + (Z1 - Z2)[END_NODES == i, j].sum()
            ==
            X[START_NODES == i, j].sum() + demand[i, j] + (Z1 - Z2)[START_NODES == i, j].sum()
        )

# Add flow constraints for each edge
for j in range(l):
    for i in range(E):
        m3.addConstr(Z1[i, j] >= 0)
        m3.addConstr(Z2[i, j] >= 0)
        m3.addConstr(X[i, j] <= 309)

# Add constraint for the total imbalance over 2 weeks to be zero
m3.addConstr((Z1 - Z2).sum(axis=1) == np.zeros(E))

# Add constraint for the total generation amount over all days
for i in range(N):
    m3.addConstr(gb.quicksum(Y[i, j] for j in range(l)) <= 8759)

#
# Optimize the model
m3.optimize()
# Print the results
print("Total cost=", m3.objval)
