import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu_non_gaussian, sigma_non_gaussian = 100, 5
x_non_gaussian = mu_non_gaussian + sigma_non_gaussian * (np.random.randn(10,10000) ** 2).sum(0)

np.savetxt('file_data_non_gaussian.csv', x_non_gaussian, delimiter=',')
