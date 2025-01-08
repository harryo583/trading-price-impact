import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('merged_data.csv')
data['ts_event'] = pd.to_datetime(data['ts_event'])

# Parameters for the models
lambda_ow = 0.01  # linear impact coefficient for OW model
lambda_afs = 0.01  # impact coefficient for AFS model
p_afs = 0.5  # nonlinearity parameter for AFS model

# Compute price impacts
data['price_impact_ow'] = data['best_bid'] + lambda_ow * data['Signed Volume']  # OW model
data['price_impact_afs'] = data['best_bid'] + lambda_afs * np.sign(data['Signed Volume']) * np.abs(data['Signed Volume'])**p_afs  # AFS model

# Calculate differences between impacted price and mid-price
data['impact_difference_ow'] = data['price_impact_ow'] - data['mid_price']
data['impact_difference_afs'] = data['price_impact_afs'] - data['mid_price']

# Visualize the distribution of price impacts
plt.figure(figsize=(12, 6))
plt.hist(data['impact_difference_ow'], bins=30, alpha=0.5, label='OW Model', density=True)
plt.hist(data['impact_difference_afs'], bins=30, alpha=0.5, label='AFS Model', density=True)
plt.title('Distribution of Price Impact Differences')
plt.xlabel('Impact Difference (Impacted Price - Mid Price)')
plt.ylabel('Density')
plt.legend()
plt.show()

# Scatter plot of Signed Volume vs Price Impact
plt.figure(figsize=(12, 6))
plt.scatter(data['Signed Volume'], data['impact_difference_ow'], alpha=0.5, label='OW Model')
plt.scatter(data['Signed Volume'], data['impact_difference_afs'], alpha=0.5, label='AFS Model', marker='x')
plt.title('Signed Volume vs Price Impact Difference')
plt.xlabel('Signed Volume')
plt.ylabel('Impact Difference')
plt.legend()
plt.show()
