# sequence of anytype and immutable
name__ = ('M', 'Ahmad', 'Mujtaba')


# example code for tuple
def function():
    return 'M', 'Ahmad', 'Mujtaba'


print(function())

# receiving the tuple and spliting it
firstName, middleName, lastName = function()
print(firstName, middleName, lastName)

# how to get index of the string in list
winners = ['Ahmad', 'Areeb', 'Hamid', 'Mehar']
for index, winner in enumerate(winners):
    print("{} - {}".format(index + 1, winner))


# example of tuple
def full_email(people):
    result = []
    for name, email in enumerate(people):
        result.append("{} <{}>".format(name, email))

    return result


print(full_email([('Ahmad', 'Hamid', 'Muneeb'), ('ahmad@gmail.com', 'hamid@gmail.com', 'muneeb@gmail.com')]))

# examples of list
multiple = []
for x in range(1,11):
    multiple.append(x*7)
print(multiple)

# list comprehensions (important): help us to create list based on sequence or range
multiples = [x*3 for x in range(1,11)]
print(multiples)

# examples of list comprehension: calculating the length of each string in list of string
languages = ["Java","C++","Go","Python","Ruby"]
length = [len(language) for language in languages]
print(length)

# another example of list comprehension: printing only divisible of 3 using condition blocks in list comprehension
create = [x for x in range(1,101) if x%3==0]
print(create)
