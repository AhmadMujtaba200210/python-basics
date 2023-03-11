x=['ahmad', 'mujtaba', 'qasuria', 'mahmood']
print(len(x))

# specific range of list

# for loop on list
for x in x:
    print("--".join(x))

# modifying the lists
fruit = ['orange']
fruit.append('mango')
fruit.append('banana')
print(fruit)
# using insert method to insert at specific position
fruit.insert(1,'leechy')
print(fruit)
# using remove methods
fruit.remove('mango')
print(fruit)
# using pop method
fruit.pop(2)
print(fruit)

# modifying list accessing the index
fruit[1]='peechy'
print(fruit)