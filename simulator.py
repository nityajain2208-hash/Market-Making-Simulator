import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

class MarketMaker:
    def __init__(self, fair_value=100, base_spread=0.10,
                 inventory_penalty=0.01):
        self.fair_value = fair_value
        self.base_spread = base_spread
        self.inventory_penalty = inventory_penalty
        self.inventory = 0
        self.cash = 0

    def quote(self):
        # Adjust quotes based on inventory to manage risk
        skew = self.inventory_penalty * self.inventory
        bid = self.fair_value - self.base_spread/2 - skew
        ask = self.fair_value + self.base_spread/2 - skew
        return bid, ask

    def update_fair_value(self, change):
        self.fair_value += change

    def execute(self, direction, size=1):
        bid, ask = self.quote()
        if direction == 'buy':   # client buys at ask
            self.cash += ask * size
            self.inventory -= size
        else:                    # client sells at bid
            self.cash -= bid * size
            self.inventory += size

    def mark_to_market(self):
        return self.cash + self.inventory * self.fair_value

# Simulate
mm = MarketMaker()
n_steps = 2000
pnl_series, inventory_series = [], []

for _ in range(n_steps):
    mm.update_fair_value(np.random.normal(0, 0.05))
    mm.execute('buy' if np.random.random() > 0.5 else 'sell')
    pnl_series.append(mm.mark_to_market())
    inventory_series.append(mm.inventory)

print(f'Final PnL: ${pnl_series[-1]:.2f}')
print(f'Max Inventory: {max(abs(i) for i in inventory_series)}')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
fig.patch.set_facecolor('#0D1B2A')
for ax in [ax1, ax2]:
    ax.set_facecolor('#0D1B2A')
    ax.tick_params(colors='white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#4a5a6a')
    ax.spines['left'].set_color('#4a5a6a')

pd.Series(pnl_series).plot(ax=ax1, color='#00D4FF')
ax1.set_title('Market Maker PnL Over Time', color='white', fontweight='bold')

pd.Series(inventory_series).plot(ax=ax2, color='#00D4FF')
ax2.axhline(0, color='white', linestyle='--', alpha=0.5)
ax2.set_title('Inventory Over Time', color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('market_making.png', dpi=150, bbox_inches='tight', facecolor='#0D1B2A')
plt.show()