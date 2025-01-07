import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_ow = 0.0035 # impact level
beta_ow = 2.0 # decay rate

# Simulate trade sizes
np.random.seed(42)
num_trades = 1000
trade_sizes = np.random.normal(loc=0, scale=1000, size=num_trades)

# Define the decay kernel
def decay_kernel(beta, t):
    return np.exp(-beta * t)

# Price impact
def ow_model(trade_sizes, lambda_ow):
    return lambda_ow * trade_sizes

# Compute impacts
impact_ow = ow_model(trade_sizes, lambda_ow)

# Visualization
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(impact_ow, bins=50, color='blue', alpha=0.7, label='OW Model (Linear Impact)')
plt.xlabel('Price Impact')
plt.ylabel('Frequency')
plt.title('Price Impact Distribution (OW Model)')
plt.legend()

plt.tight_layout()
plt.show()
