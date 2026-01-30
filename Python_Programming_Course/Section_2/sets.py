# empty set
emptySet = set()

# To types on how to create a set
set1 = {1,2,3,4,5}
set2 = set([1,2,3,4,5])

# Add elements
set1.add('6')
print(set1)

# Remove an element
set1.remove(1)
print(set1)

# Join sets, remove duplicates
join = set1 | set2
print(join)

# Intersection
intersection = set1 & set2
print(intersection)

# Difference
diff = set1 - set2
print(diff)

# Simetric difference, which do not match
simDiff = set1 ^ set2
print(simDiff)

# Check an element
if 3 in set1:
    print("Is in it")
    
# Lenght
print(len(set1))

# To set from list, to remove any duplicates from the list
list = [1,2,3,4,5,65,6,2,2,1,2]
set3 = set(list)
print(set3)