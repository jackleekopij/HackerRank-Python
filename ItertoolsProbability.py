from itertools import combinations

# From standard input, read in parameters.
n, input_string, k = raw_input(), raw_input().split(" "), raw_input()

# Use itertools 'combinations' to create all combinations of input_string of length k.
combination_list =  list(combinations(input_string, int(k)))

# Append to list 'a_count', tuples in combination_list which include "a".
a_count = [i for i in combination_list if "a" in  i]

# Calculate the proportion of tuples that contain "a"
probability = float(len(a_count))/ float(len(combination_list))

# Print the probability value to console.
print probability