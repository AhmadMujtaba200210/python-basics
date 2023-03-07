# substring
color = 'Ahmad'
print(color[1:5])

# substring accessing from and accessing to
nation = 'Orange'
print(nation[:3])

# accessing the last index of string
first = 'Mujtaba'
print(first[-1])

# accessing the second last index of string
second = 'Mahmo0d'
print(second[-2])

# accessing the third last index of string
third = 'Muhammad'
print(third[-3])

# adding two sub strings to form new one
firstHalf = 'GreenFlag'
secondHalf = 'Yellow Nation'
print(firstHalf[:5] + secondHalf[7:])

# strings in python are immutable: they cannot be modified  once they are created

# how to get index of a character in string
example1 = 'checking'
print(example1.index('e'))
example2 = 'checkingAgain'
print(example2.index('Again'))

# how to check if a substring is present in a string: using keyword [in]
example3 = 'Change'
print("Again" in example3)  # False
print("Chan" in example3)  # True


# example of String practice
# for example you are working in a company, and it assigns you to change the old domain with new domain
def replaceolddomain(email, oldDomain, newDomain):
    if '@' + oldDomain in email:
        index = email.index("@" + oldDomain)
        new_email = email[:index] + '@' + newDomain
        return new_email
    return email


# upper and lower class
print("ahmad".upper())
print("AHMAD".lower())

# trim the surrounding spaces of string
print(" more ".strip())
print(" more".lstrip())
print("more ".rstrip())

# if string made up of just numbers
print("1234".isnumeric())
print("1234aa".isnumeric())

# to join strings
print(" ".join(['ahmad', 'mujtaba', 'mahmood']))
print("...".join(['ahmad', 'mujtaba', 'mahmood']))
print("---".join(['ahmad', 'mujtaba', 'mahmood']))

# to split strings
print("I am Ahmad Mujtaba Mahmood".split())

# format method in String
string = 'Ahmad Mujtaba'
number = len(string) * 3
print('Hi {}, your lucky number is {}'.format(string, number))

print('Hi your cgpa is {:.2f}'.format(3.4))  # printing the float value upto 2 decimal point


# example format function
def to_celsius(x):
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):
    print("{} | {:.3f}".format(x, to_celsius(x)))
