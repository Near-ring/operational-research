# Gas Supply Optimization

## Problem Description:

Consider a region of a gas network with demand nodes and four gas suppliers connected by gas pipelines. Your goal is to derive an optimal gas distribution strategy among these suppliers (specified by the problem set below), ensuring the region's daily demands are met cost-effectively.

## Data Details:

1. **nodes.csv**: Specifies the location (in kilometres) of each node and its daily demand (MJ).
2. **pipelines.csv**: Lists all pipelines interconnecting the nodes within the network.

Supplier nodes are nodes that supply gas for the gas network. Each of these supplier nodes is characterized by distinct daily capacities and gas supply costs, summarized in the table below:

|                  | Node 10 | Node 18 | Node 27 | Node 30 |
|------------------|---------|---------|---------|---------|
| Capacity (MJ)    | 417     | 875     | 914     | 637     |
| Cost ($/MJ)      | 72      | 77      | 72      | 87      |

**Note**: Usage of every kilometer of pipeline incurs an additional charge of $0.01 per MJ.

## Problem Set:
## Part 1 - Linear Programming
(My solution implementation can be found in `.\src\problem_1_3.py` file.)

### Problem 1:
Determine the optimal cost to meet the existing daily demand considering the suppliers, given the constraint that pipelines have a daily maximum capacity of 293 MJ.

### Problem 2:
Using the data from **nodes2.csv**, which provides forecasted daily demands for each node over the forthcoming two weeks (with D0 marking the initial Monday). Find the optimal cost for meeting the forecast demand over the next two weeks, with the constraint that each supplier should not exceed a total supply of 10,597 MJ.

### Problem 3:
Given the gas's compressibility, pipelines can function as a gas storage containers by accommodating daily flow imbalances. This flexibility means pipelines can exhibit temporary deficits or surpluses in their daily flow. Such imbalances attract a cost of $0.10 per MJ. However, these imbalances might enable more cost-efficient utilization of the available supply on days. 
Over the two weeks, a net-zero imbalance is required, ensuring the cumulative inflow aligns with the cumulative outflow for every pipeline (in 2 weeks). Incorporating these variables, deduce the optimal cost for meeting the forecast demand over the next two weeks period.

## Part 2 - Integer Programming
(My solution implementation can be found in `.\src\problem_4_7.py` file.)
### Introduction:

In light of the efforts to plan for the gas supply for the upcoming two weeks, the focus now shifts to strategizing for the long-term sustainability of the network operations.

- **nodes3.csv**: This data file forecasts the demand anticipated across the network in intervals of 5 and 10 years.

For the purpose of this planning phase, these previously given data including: node demands, pipeline capacities, supply costs, and flow costs, should be disregarded.

For each supplier node, three distinct upgrade options is available. The table below delineates the costs associated with each upgrade option and the consequent enhancement in capacity:

| Supplier | Current Capacity | Option 1 (Capacity, Cost) | Option 2 (Capacity, Cost) | Option 3 (Capacity, Cost) |
|----------|------------------|---------------------------|---------------------------|---------------------------|
| 10       | 417 MJ           | 84 MJ, $8,422,000         | 209 MJ, $19,585,000       | 419 MJ, $39,451,000       |
| 18       | 875 MJ           | 182 MJ, $17,581,000       | 448 MJ, $40,246,000       | 877 MJ, $80,333,000       |
| 27       | 914 MJ           | 178 MJ, $17,790,000       | 449 MJ, $43,071,000       | 910 MJ, $82,744,000       |
| 30       | 637 MJ           | 134 MJ, $12,975,000       | 319 MJ, $30,564,000       | 639 MJ, $58,881,000       |

**Note**: only one of the upgrade options can be applied to each supplier node. Alternatively, not upgrading is also possible.

### Problem 4:
Determine the optimal upgrade option to address the forecast demand in next 10 years. Find the optimal total cost for this upgrade strategy.

### Problem 5:
Due to new standards, Each existing pipeline can only be utilized to a maximum capacity of **280 MJ**. Given these constraints, the network will not be able to sufficiently deliver gas from the upgraded suppliers in 10 years.
However, we can choose to duplicate any existing pipelines, which will double their capacity. The cost associated with this duplication is **$200,000 per kilometer**. Determine the optimal upgrade strategies for suppliers and pipelines to meet the demand in 10 years. Find the optimal total cost for this upgrade strategy.

### Problem 6:
Consider the following Financial Modifiers:

- Upgrades executed in the **initial 5-year span** will remain as the same cost as previously mentioned in **Problem 5**.
- Upgrades scheduled for the **second 5-year period** will benefit from a **30% discount** on their cost.

Determine the optimal upgrade options for both suppliers and pipelines to meet the forecasted demand in the next 10 years. Find the optimal total upgrade cost.

### Problem 7:

There is less certainty regarding demands in 10 years. Consequently, planning is required around three potential scenarios:

1. Demand in 10 years is 20% lower than forecast.
2. The demand in 10 years is as forecasted.
3. Demand in 10 years is 20% higher than forecast.

The assumption is made that each scenario holds equal likelihood. Though the future scenario cannot be predicted currently, but it will be known in 5 years from now with certainty.

Which upgrade options for suppliers and pipes are to be selected to accommodate the forecasted uncertain demand scenarios? Find the optimal total expected upgrade cost.