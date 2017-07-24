from itertools import groupby

# Read in a string into the groupby function. Here whe then iterate over the unordered group.
for key, group in groupby((raw_input())):
    for index in group:
        print (len(list(group))+1, int(index)),