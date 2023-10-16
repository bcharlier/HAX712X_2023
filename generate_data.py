import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


mu, sigma = 100, 15
x_gaussian = mu + sigma * np.random.randn(10000)

np.savetxt('file_data.csv', x_gaussian, delimiter=',')

mu_non_gaussian, sigma_non_gaussian = 100, 5
x_non_gaussian = mu_non_gaussian + sigma_non_gaussian * (np.random.randn(10,10000) ** 2).sum(0)

np.savetxt('file_data_non_gaussian.csv', x_non_gaussian, delimiter=',')

