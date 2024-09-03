"""
Prompt
Assignment 2:

You are provided with two datasets: data1.npy and data2.npy. These datasets contain random numerical
values. Your task is to perform intermediate-level NumPy operations to manipulate the data, combine
the datasets, and analyze the results.

Datasets:

data1.npy: A NumPy array of shape (5, 3) containing random integers.
Example: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]] data2.npy: A NumPy array of shape
(5, 1) containing random integers.
Example: [[10], [20], [30], [40], [50]]

Loading Data:
Load the data1.npy and data2.npy files into NumPy arrays.

Data Manipulation:
Multiply all elements in data1 by 2 and store the result in a new array data1_modified. Calculate the
square of all elements in data2 and store the result in a new array data2_modified.

Broadcasting:
Use broadcasting to add data2_modified to each row of data1_modified. The final result should be stored
in a new array combined_data.

Data Analysis:
Find and print the sum of all elements in combined_data. Find and print the mean (average) of
all elements in combined_data. Find the row in combined_data with the highest sum of elements and print the row.

Save Results:
Save the combined_data array to a new file named result.npy.
"""
# import necessary numpy library
import numpy as np

# Load the data from .npy files
data1 = np.load('data1.npy')
data2 = np.load('data2.npy')

# Data Manipulation
# Multiply all elements in data1 by 2
data1_modified = data1 * 2

# Calculate the square of all elements in data2
data2_modified = data2 ** 2

# Broadcasting
# Add data2_modified to each row of data1_modified
combined_data = data1_modified + data2_modified

# Data Analysis
# Find and print the sum of all elements in combined_data
total_sum = np.sum(combined_data)
print(f"Sum of all elements in combined_data: {total_sum}")

# Find and print the mean (average) of all elements in combined_data
mean_value = np.mean(combined_data)
print(f"Mean of all elements in combined_data: {mean_value}")

# Find the row in combined_data with the highest sum of elements
row_sums = np.sum(combined_data, axis=1)
max_row_index = np.argmax(row_sums)
row_with_highest_sum = combined_data[max_row_index]
print(f"Row with the highest sum of elements: {row_with_highest_sum}")

# Save the combined_data array to a new file
np.save('result.npy', combined_data)
