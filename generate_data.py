import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

np.savetxt('file_data_non_gaussian.csv', x, delimiter=',')
