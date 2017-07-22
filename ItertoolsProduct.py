import sys
from itertools import product

# Read in standard input and split on lines.
input = sys.stdin.read().splitlines()

# Create a list of list for each of the input lines and map elements to integers.
list_of_list = [map(int,x.split(" ")) for x in input]

# Create a list of for the Cartesian product of the lists.
cartesian_product_list = list(product(*list_of_list))

# Map each Cartesian element to a string, join and print the result to standard output.
print ' '.join(map(str,cartesian_product_list))