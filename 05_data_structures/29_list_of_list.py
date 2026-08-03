

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sublist = numbers[1]
print(sublist)

print(sublist[2])

print(numbers[2][1]) # two dimensional list

print()

# iterating over a list
for x in numbers:
    for y in x:
        # print(y)
        # to put them in one line
        print(y, end="")

print()

# alternatively
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end="")


    
print()

# dictionary of lists
people = {
    "Al": ["Running", "Programming"],
    "Clare": ["Hiking", "Reading", "Skiing"]
}


print(people["Clare"][1])

print()

for names, hobbies in people.items():
    print(names)
    print("========")

    for hobby in hobbies:
        print(hobby)