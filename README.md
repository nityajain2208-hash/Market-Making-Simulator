# Market Making Simulator

A Python-based simulation of an inventory-aware market maker. This project explores how a market maker generates bid and ask quotes, executes trades, manages inventory, and tracks portfolio profit and loss (PnL) in a simplified financial market.

## Project Overview

Market makers provide liquidity by quoting prices at which they are willing to buy and sell an asset. Their objective is to capture the bid-ask spread while managing the risks associated with changing market prices and accumulating inventory.

This project simulates these mechanics in a controlled environment using randomly generated price movements and customer orders. It provides a practical introduction to algorithmic trading, market microstructure, and inventory risk management.

## Key Features

- Simulates market price movements over multiple time steps.
- Generates bid and ask quotes around the estimated fair price.
- Adjusts quotes according to the market maker's inventory.
- Simulates customer buy and sell orders.
- Tracks cash balance and asset inventory after trades.
- Calculates portfolio value and mark-to-market P&L.
- Visualizes portfolio P&L and inventory over time.

## Mathematical Model

### 1. Bid and Ask Quote Generation

The market maker places buy and sell quotes around the current mid-price.

**Bid Price = Mid-Price - (Base Spread / 2) - (Inventory Skew × Inventory)**

**Ask Price = Mid-Price + (Base Spread / 2) - (Inventory Skew × Inventory)**

Where:

- **Mid-Price:** Estimated fair market price of the asset.
- **Base Spread:** Difference between the initial ask and bid quotes.
- **Inventory:** Current quantity of the asset held by the market maker.
- **Inventory Skew:** Parameter controlling how strongly quotes respond to inventory.

When inventory becomes positive, both quotes shift downward, making the market maker more inclined to sell and less inclined to accumulate additional inventory. Negative inventory shifts quotes upward, encouraging purchases.

### 2. Portfolio Valuation

The portfolio is valued at the current mid-price.

**Portfolio Value = Cash Balance + (Inventory × Mid-Price)**

**P&L = Current Portfolio Value - Initial Portfolio Value**

This captures both cash generated or spent through trades and changes in the market value of the remaining inventory.

## Simulation Workflow

1. Initialize the market price and market maker's portfolio.
2. Generate a change in the market price.
3. Calculate the bid and ask quotes using the current inventory.
4. Generate a customer buy or sell order.
5. Execute a trade if the simulated order interacts with a quote.
6. Update cash balance and inventory.
7. Recalculate portfolio value and P&L.
8. Repeat the process and visualize the results.

## Results and Visualizations

The simulation tracks the evolution of the market maker's portfolio and inventory.

Recommended plots to include:

- **P&L Over Time:** Shows how the portfolio's marked-to-market value changes throughout the simulation.
- **Inventory Over Time:** Shows how the market maker's asset exposure evolves as trades are executed.

These plots help illustrate the relationship between trading activity, inventory exposure, and portfolio performance.

*Insert your generated plots here once they are available in the repository.*

## Technology Stack

- Python
- NumPy
- pandas
- Matplotlib

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/nityajain2208-hash/Market-Making-Simulator.git
cd Market-Making-Simulator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation using the project's main Python script:

```bash
python simulator.py
```

If your main script has a different filename, replace `simulator.py` with the correct filename.

## Assumptions and Limitations

This project uses a simplified market environment to demonstrate the core mechanics of market making.

- Market prices and customer orders are simulated rather than obtained from a live exchange.
- The quoting mechanism uses a simplified inventory-adjustment rule.
- The simulation does not fully model a real limit order book, order queue priority, latency, or adverse selection.
- Transaction costs and exchange fees are not necessarily included.
- Simulated profitability should not be interpreted as evidence of real-world trading profitability.

## Future Improvements

- Introduce stochastic order-arrival and fill-probability models.
- Incorporate transaction costs and slippage.
- Add inventory limits and risk-management constraints.
- Compare fixed-spread and inventory-aware quoting strategies.
- Evaluate performance across multiple random seeds and market conditions.
- Analyze risk-adjusted returns, maximum drawdown, and inventory exposure.

## Learning Outcomes

This project explores practical concepts in quantitative finance, including bid-ask spread capture, inventory risk, portfolio valuation, stochastic simulation, and algorithmic market-making logic.
