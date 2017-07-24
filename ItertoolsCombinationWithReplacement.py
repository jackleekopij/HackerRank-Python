# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

# Read in from the standard console.
combination_string, combination_iterable = raw_input().split(" ")

# Create a length of the combination iterable.
combination_iterable = int(combination_iterable)

# Create a list of the sorted combinations.
combination_list = list(combinations_with_replacement(sorted(combination_string), combination_iterable))

# Iterate over the output list and print element to console.
for index in combination_list:
    print "".join(index)
