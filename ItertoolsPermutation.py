from itertools import permutations

# Read in the permutation string from the standard input.
permutation_string, permutation_length = input().split(" ")

# Create a permutation list that is sorted.
permutation_list = list(permutations(sorted(permutation_string), int(permutation_length)))

# Print each permutation via a join.
for permutation in permutation_list:
    print "".join(permutation)
