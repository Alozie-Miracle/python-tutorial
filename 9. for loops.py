# use for loops to iterate over a sequence of numbers

# print numbers from 0 to 4
for i in range(5):
    print(i)

print()

# to include 5 -> start from 1 - 5
for i in range(1, 6):
    print(i)

print()

# more on ranges
for i in range(0, 11, 2):  # start, stop, step
    print(i)  # prints even numbers from 0 to 8

print()

# printing multiples hellos, the variable name is not important, so we can use _ as a placeholder
for _ in range(3):
    print("Hello!")


for i in range(3):
    print(i)

    if i == 2:
        print("Done!")


# using "Break" statement to exit the loop
for i in range(5):
    print("Starting loop number " + str(i))

    stop = input("Do you want to stop the loop? (y/n): ")
    if stop.lower() == 'y':
        print("Exiting the loop...")
        break  # exit the loop if user wants to stop

print("Loop has ended.")

# using continue statement to skip the current iteration
for i in range(5):
    if i == 2:
        print("Skipping iteration for i =", i)
        continue  # skip the rest of the loop for this iteration
    print("Current value of i:", i)