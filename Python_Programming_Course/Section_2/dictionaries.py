# Create a dictionary
dic = {'a':1,'b':2,'c':3}
print(dic)
print(dic['a']) # To print the key if you got the value

# Other way to create a dictionary
dic2 = dict(a=1,b=2)
print(dic2)

# Other way
dic3 = dict(zip('ab', [1,2]))
print(dic3)

# If you want to see the elements as tuples
print(dic3.items)

# If you want to see only the keys or values
print(dic3.keys())
print(dic3.values())

# Clean a dictionary
dic2.clear()
print(dic2)