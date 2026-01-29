# Create a tuple
colors = ("green", "yellow", "red", "blue")
emptyTuple = ()

# Like an array
print(colors[:2])
print(colors[0])

# Length of the tuple
print(len(colors))

# Create a tuple but with one value
tupleUnit = (10,) # With out the coma it is not a tuple

# Package tuples
a = 10
b = 'b'
tuple = a,b
print(tuple)

# We can unpackage a tuple, but we need to put the same variables as values that the tuple has
a,b = tuple