# dict are mutable
# initialising the dict, key & value can be any data type
x = {
    "bear": 10,
    "lion": 5,
    25: 6,
    15.5: "Ahmad"
}
# accessing the dict using key
print(x[25])
print(x[15.5])
print(x["bear"])

# getting the value of the key which is not present in dict will give "KeyError"

# modifying the value of a key in dict
x["bear"] = 15
x[15.5] = "Ameer"

# deleting the key and its value
print(x)  # before deleting
del x["bear"]
print(x)  # after deleting

# getting only values of dict
print(x.values())
# getting only keys of dict
print(x.keys())

# checking keys in dict
print("bear" in x)
print('lion' in x)


# example codes
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters("aaaaaAhmmm"))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
print(wardrobe.update(new_items))