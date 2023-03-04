# example 1
x = [1, 2, 3, 4]
for x in x:
    print(x)

values = ["ahmad", "hamid", "waheed", "mehar"]
for values in values:
    print(values)


# example 2
def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(x, to_celsius(x))

# example 3
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")  # end is new line parameter in python
    print()

# example 4
teams = ['Dragons', 'eagle', 'Wolves', 'Unicorns', 'Pandas']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
