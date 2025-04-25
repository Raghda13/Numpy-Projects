import numpy as np

# Sample data_nan for example; replace with your actual data
# Make sure data_nan is loaded correctly as a 2D array
data_nan = np.array([[-1, np.nan], [3, np.nan], [np.nan, 8], [-1, 10]])

# Check if data_nan is 2D; reshape if necessary
if data_nan.ndim == 1:
    data_nan = data_nan.reshape(-1, 1)  # Adjust based on your data shape

# Calculate mean, avoiding empty slices
data_mean = np.nanmean(data_nan, axis=0) if np.any(~np.isnan(data_nan)) else np.zeros(data_nan.shape[1])

# Copy data_nan to data_filled for filling missing values
data_filled = data_nan.copy()

# Ensure data_filled is 2D as well
if data_filled.ndim == 1:
    data_filled = data_filled.reshape(-1, 1)  # Adjust as needed

# Fill missing values in the second column (index 1)
data_filled[:, 1] = np.where(np.isnan(data_filled[:, 1]), data_mean[1], data_filled[:, 1])

# Replace -1 values in the first column (index 0) with the mean if needed
data_filled[:, 0] = np.where(data_filled[:, 0] == -1, data_mean[0], data_filled[:, 0])

# Display final result
print("Final processed data:\n", data_filled)
