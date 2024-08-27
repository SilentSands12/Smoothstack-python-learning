"""
Prompt
Assignment 1:

You are given a dataset representing the daily temperatures (in Celsius) recorded
in a city over a month. Your task is to perform basic array operations and indexing
using NumPy to analyze the data and extract useful information.

Dataset:

temperatures = [25, 24, 23, 22, 25, 26, 27, 28, 28, 27, 26, 25, 25, 24, 24, 23, 23,
22, 21, 22, 24, 26, 27, 28, 29, 28, 27, 26, 25, 24]

Tasks:

Convert to NumPy Array:

Convert the given temperatures list to a NumPy array. Array Operations:

Find and print the following: Mean temperature over the month. Maximum temperature recorded.
 Minimum temperature recorded. Standard deviation of the temperatures. Array Indexing and Slicing:

Extract and print the temperatures recorded in the first week of the month (first 7 days).
Extract and print the temperatures recorded in the last 10 days of the month. Find and print
the index of the day with the maximum temperature. Find and print the index of the day with the
 minimum temperature. Data Modification:

Replace the temperatures recorded on the 15th and 20th days with 30°C.
"""
# import necessary numpy library
import numpy as np

# Given list of Celsius temperatures
celcius_temperatures = [25, 24, 23, 22, 25, 26, 27, 28, 28, 27, 26, 25, 25, 24, 24, 23, 23,
22, 21, 22, 24, 26, 27, 28, 29, 28, 27, 26, 25, 24]

# Convert the list into a NumPy array
numpyArray_ctemps = np.array(celcius_temperatures)
print(f'List of temps provided: {celcius_temperatures} and count of temps: {len(celcius_temperatures)}')

# ****************** Print out basic stats using math functions in NumPy ******************
print('\n****************** Print out basic stats using math functions in NumPy ******************')
print(f'This is the mean temperature over the month: {numpyArray_ctemps.mean()}')
print(f'This is the maximum temperature over the month: {numpyArray_ctemps.max()}')
print(f'This is the minimum temperature over the month: {numpyArray_ctemps.min()}')
print(f'This is the standard deviation of the temperatures for the month: {numpyArray_ctemps.std()}')

# ****************** Array indexing and slicing part ******************
print('\n****************** Array indexing and slicing part ******************')
print(f"This is the first week's temperatures of the month: {numpyArray_ctemps[:7].tolist()}")
print(f'This is the last 10 temperatures of the month: {numpyArray_ctemps[-10:].tolist()}')

# Max index
max_temp = numpyArray_ctemps.max()
max_temp_indices = np.where(numpyArray_ctemps == max_temp)[0]
print(
    f'\nThis is the index for the max temperature ({max_temp}): INDEX {max_temp_indices}'
)

# Min index
min_temp = numpyArray_ctemps.min()
min_temp_indices = np.where(numpyArray_ctemps == min_temp)[0]
print(
    f'This is the index for the min temperature ({min_temp}): INDEX {min_temp_indices}'
)

# ****************** Data Modification ******************
print('\n****************** Data Modification ******************')
print(f'Array before modification: {numpyArray_ctemps.tolist()}')
# Note: Array indices are zero-based, so 15th and 20th days are at index 14 and 19 respectively
numpyArray_ctemps[14] = 30
numpyArray_ctemps[19] = 30
print(f'Array after modification: {numpyArray_ctemps.tolist()}')
