from itertools import combinations

# Read in values from the standard input.
combination_string, combination_length = raw_input().split(" ")

# Initialise a combination list to store the combination values.
combination_list = []

# Cast the combination length to an integer to be referenced further.
combination_length = int(combination_length)

# Append to the initialised combination_list the combinations of the input string and iterate up from zero
for index in range(1,combination_length+1):
    combination_list.append(list(combinations(sorted(combination_string),index)))

# Iterate over the combination_list, within each element, join on the tuple and print the output.
for combination in combination_list:
    for index_tuple in combination:
        print "".join(index_tuple)