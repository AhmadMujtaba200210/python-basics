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


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for check in filenames:
    if ".hpp" in check:
        newfilenames.append((check[:-2]))
    else:
        newfilenames.append(check)



print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
  members=group + ": "
  for user in users:
    members += user + ","

  return members[members]

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"