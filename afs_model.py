import numpy as np
import matplotlib.pyplot as plt

lambda_afs = 0.0035 # impact level
p_afs = 0.5 # nonlinearity parameter
beta_afs = 2.0 # decay rate

# Simulate trade sizes
np.random.seed(42)
num_trades = 1000
trade_sizes = np.random.normal(loc=0, scale=1000, size=num_trades)

# Define the decay kernel
def decay_kernel(beta, t):
    return np.exp(-beta * t)

# Price impact of the AFS model
def afs_model(trade_sizes, lambda_afs, p_afs):
    return lambda_afs * np.sign(trade_sizes) * np.abs(trade_sizes) ** p_afs

# Compute impacts
impact_afs = afs_model(trade_sizes, lambda_afs, p_afs)

# Visualization
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 2)
plt.hist(impact_afs, bins=50, color='green', alpha=0.7, label='AFS Model (Nonlinear Impact)')
plt.xlabel('Price Impact')
plt.ylabel('Frequency')
plt.title('Price Impact Distribution (AFS Model)')
plt.legend()

plt.tight_layout()
plt.show()
