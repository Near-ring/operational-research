# linear programming exmaple
# Gas Supply Optimization

## Problem Description:

Consider a region of a gas network with demand nodes and four gas suppliers conected by gas piplines. Your goal is to derive an optimal gas distribution strategy among these suppliers (specified by the problem set below), ensuring the region's daily demands are met cost-effectively.

## Data Details:

1. **nodes.csv**: Specifies the location (in kilometres) of each node and its daily demand (MJ).
2. **pipelines.csv**: Lists all pipelines interconnecting the nodes within the network.

Supplier nodes are nodes that supply gas for the gas network. Each of these supplier nodes is characterized by distinct daily capacities and gas supply costs, summarized in the table below:

|                  | Node 10 | Node 18 | Node 27 | Node 30 |
|------------------|---------|---------|---------|---------|
| Capacity (MJ)    | 417     | 875     | 914     | 637     |
| Cost ($/MJ)      | 72      | 77      | 72      | 87      |

**Note**: Usage of every kilometre of pipeline incurs an additional charge of $0.01 per MJ.

## Problem Set:

### Problem 1:
Determine the optimal cost to meet the existing daily demand considering the suppliers, given the constraint that pipelines have a daily maximum capacity of 293 MJ.

### Problem 2:
Using the data from **nodes2.csv**, which provides forecasted daily demands for each node over the forthcoming two weeks (with D0 marking the initial Monday), ascertain the optimal cost for addressing this projected demand. Over this two-week period, each supplier should not exceed a total supply of 10,597 MJ.

### Problem 3:
Given the gas's compressibility, pipelines can function as extensive gas storage containers by accommodating daily flow imbalances. This flexibility means pipelines can exhibit temporary deficits or surpluses in their daily flow. Such imbalances attract a cost of $0.10 per MJ. However, these imbalances might enable more cost-efficient utilization of the available supply on days with diminished demand. Over the two weeks, a net zero imbalance is required, ensuring the cumulative inflow aligns with the cumulative outflow for every pipeline. Incorporating these variables, deduce the optimal cost for catering to the projected demand over the subsequent two weeks from the suppliers.

