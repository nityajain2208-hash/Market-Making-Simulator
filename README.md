# Market-Making-Simulator
## Overview
This project simulates the core mechanics of an automated market maker (AMM) / algorithmic trading strategy. It dynamically calculates bid and ask prices based on underlying asset fair value while adjusting for inventory risk to manage portfolio exposure.

### Key Features
Inventory Risk Skewing: Dynamically adjusts bid-ask quotes relative to current inventory holding to encourage balanced trading and limit directional exposure.
Execution & Cash Tracking: Simulates client order fills, tracking real-time cash flow and inventory positions.
Mark-to-Market Valuation: Computes ongoing portfolio performance and total PnL across market iterations.
Visual Diagnostics: Generates performance plots tracking inventory drift and total strategy PnL over time (`market_making.png`).
