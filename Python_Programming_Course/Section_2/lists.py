# Lists can have different types
list = [1,"Hello", 2.5, [4, 5]]

# To access an item
print(list[0])

# To see the items in a list that is in another list
print(list[3][0])

# To get from an element to another
print(list[1:3]) # The last value doesnt count [1,3)

# To get from an element to another with "jumps"
print(list[0:3:2])

# To add an element
list.append(2)

# To add some elements at the same time, but not together
list.extend([3,4,5,6])

# To remove an element
list.remove(2)

# To get an index
list.index(1)

# To count the times an element appears in the list
list.count(1)

# To get the reverse list
list.reverse()

# Empty list
emptyList = []

# To add an element in a specific position
list.insert(2, "World")

# To get the last element of a list
list.pop()

# Lenght of a list
print(len(list))

# If we copy a list into another
list1 = [1,2,3,4,5]
list2 = list1
# Both have the same memory id, so if we modify one list, we modify the second
print(id(list1) + " " + id(list2))
# Use copy to do the same
list3 = list1.copy()
print(id(list1) + " " + id(list3))
# Other way is using slicing we get the same list but different id
list4 = list[:]
print(id(list1) + " " + id(list4))
# We can use deepcopy to get different id
import copy
list5 = copy.deepcopy(list)