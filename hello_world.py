# Python 3.7
intro_msg = ["hello world", "hi universe", "hey python"]

print("--------------------------------------------------")
print("chapters 1, 2, 3".title().center(50))
print("--------------------------------------------------")

# sort list alphabetically
# intro_msg.sort()

# sort list alphabetically (reversed)
# intro_msg.sort(reverse=True)

# sort a list temporarily
# print(sorted(intro_msg))

# print list in reverse order
# intro_msg.reverse()

# appending elements to the end of a list
# intro_msg.append("mic check")

# inserting elements into a list
# intro_msg.insert(0, "knock knock")

# deleting an element from a list
# del intro_msg[0]

# popping an element from a list
# popped_intro_msg= intro_msg.pop()

# pop from any position in a list
# second_msg = intro_msg.pop(1)

# removing an item by value
# intro_msg.remove("hi universe")

# finding length of a list
# print(len(intro_msg))

print(intro_msg[0].title() + "! I'm new to Python...\n")
# print(intro_msg)

print("\n" + "--------------------------------------------------")
print("chapter 4: working with lists".title().center(50))
print("--------------------------------------------------")

# iterate through list
for message in intro_msg:
    print(message.title() + "! ", end = '')

print("\n")

# create numerical lists with range()
for value in range(1, 4):
    print("I've completed chapter ".title() + str(value) + " ☑\n")

# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function. When you wrap list() around
# a call to the range() function, the output will be a list of numbers.
numbers = list(range(1, 6))
print("List of numbers from 1-5: " + str(numbers))

# use the range() function to tell Python to skip numbers in a given range.
even_numbers = list(range(2,11,2))
print("List of even numbers from 1-10: " + str(even_numbers))

# make a list of the first 10 square numbers
square_numbers = []
for value in range(1,11):
    square = value**2
    square_numbers.append(square)

print("List of square numbers from 1-10: " + str(square_numbers))

# finding the minimum, maximum and sum of a list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("\nSum of list: " + str(sum(digits)))
print("Maximum of list: " + str(max(digits)))
print("Minimum of list: " + str(min(digits)))

# list comprehension
square_numbers = [value**2 for value in range(1,11)]
print("\nList comprehension of square numbers from 1-10: " + str(square_numbers))

# slicing a list
print("First 3 square numbers: " + str(square_numbers[:3]))
print("Last 3 square numbers: " + str(square_numbers[-3:]))

# iterate through slice
print("\nHere are the first three square numbers:")
for square in square_numbers[:3]:
    print("\t" + str(square))

# copy lists
new_digits = digits[:]
print("\nOriginal list: " + str(digits))
print("Copied list: " + str(new_digits))

# defining tuples
digits_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
for digits in digits_tuple:
    print(str(digits), end = " ")

# You can't change specific values in a tuple but you can change
# the values of the whole tuple

print("\n\n" + "--------------------------------------------------")
print("chapter 5: if statements".title().center(50))
print("--------------------------------------------------")

# simple IF-else statement example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking multiple conditions (AND)
if cars[0] == 'audi' and cars[1] == 'bmw':
    print("\nI love cars!", end= " ")

# checking multiple conditions (OR)
if cars[0] == 'audi' or cars[1] == 'audi':
    print("But I hate Audi...")

# look for value in a list
if 'audi' in cars:
    cars.remove("audi")
if 'audi' not in cars:
    print("These are my favourite cars:", end=" ")
for car in cars:
    print(car.title(), end= " ")

# The if-elif-else chain
if 'audi' not in cars:
    cars.insert(0, "audi")
elif 'jaguar' not in cars:
    cars.append("jaguar")
else:
    print(cars)