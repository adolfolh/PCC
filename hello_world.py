# Python 3.7
intro_msg = ["hello world", "hi universe", "hey python"]

print("--------------------------------------------------------------------------------")
print("chapters 1, 2, 3".title().center(80))
print("--------------------------------------------------------------------------------")

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

print("--------------------------------------------------------------------------------")
print("chapter 4: working with lists".title().center(80))
print("--------------------------------------------------------------------------------")

# iterate through list
for message in intro_msg:
    print(message.title() + "! ", end='')

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
even_numbers = list(range(2, 11, 2))
print("List of even numbers from 1-10: " + str(even_numbers))

# make a list of the first 10 square numbers
square_numbers = []
for value in range(1, 11):
    square = value ** 2
    square_numbers.append(square)

print("List of square numbers from 1-10: " + str(square_numbers))

# finding the minimum, maximum and sum of a list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("\nSum of list: " + str(sum(digits)))
print("Maximum of list: " + str(max(digits)))
print("Minimum of list: " + str(min(digits)))

# list comprehension
square_numbers = [value ** 2 for value in range(1, 11)]
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
    print(str(digits), end=" ")

# You can't change specific values in a tuple but you can change
# the values of the whole tuple

print("\n\n" + "--------------------------------------------------------------------------------")
print("chapter 5: if statements".title().center(80))
print("--------------------------------------------------------------------------------")

# simple IF-else statement example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking multiple conditions (AND)
if cars[0] == 'audi' and cars[1] == 'bmw':
    print("\nI love cars!", end=" ")

# checking multiple conditions (OR)
if cars[0] == 'audi' or cars[1] == 'audi':
    print("But I hate Audi...")

# look for value in a list
if 'audi' in cars:
    cars.remove("audi")
if 'audi' not in cars:
    print("These are my favourite cars:", end=" ")
for car in cars:
    print(car.title(), end=" ")

# The if-elif-else chain
if 'audi' not in cars:
    cars.insert(0, "audi")
elif 'jaguar' not in cars:
    cars.append("jaguar")
else:
    print(cars)

print("\n\n" + "--------------------------------------------------------------------------------")
print("chapter 6: dictionaries".title().center(80))
print("--------------------------------------------------------------------------------")

# a simple dictionary
alien_0 = {"color": "green", "points": 5}

print("Alien Color: " + alien_0["color"])
print("Points: " + str(alien_0["points"]))

# adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# removing key-value pairs
del alien_0["points"]
print(alien_0)

# Using keys in square brackets to retrieve the value you’re interested in
# from a dictionary might cause one potential problem: if the key you ask
# for doesn’t exist, you’ll get an error.

# use get() to look for a key and handle the error if it occurs...
point_value = alien_0.get('weapon', 'No weapon assigned.')
print(point_value)

# dictionary of similar objects
favorite_languages = {
    "jen": "python",
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("\n")

# iterate through dictionary
for key, value in favorite_languages.items():
    print(key.title() + "'s favorite language is " + value.title() + ".")

# iterate through keys
print("\nKeys:")
for key in favorite_languages.keys():
    print("\t- " + key.title())
# you can also use the following code instead...
# for key in favorite_languages:

# iterate though the values
print("\nValues:")
for value in favorite_languages.values():
    print("\t- " + value.title())

# a set is a collection in which each item must be unique
print("\nSet of Favorite Languages:")
for language in set(favorite_languages.values()):
    print(f"\t- {language.title()}")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# nesting dictionaries
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(f"\n{alien}")

print("...")

# make an empty list to store aliens
aliens = []

# make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == "green":
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == "yellow":
        alien['color'] = 'green'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("...")

# show how many aliens have been created
print(f"\nTotal number of aliens: {len(aliens)}")

# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("\nWelcome to Domino's:".upper())
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t- {topping}")

print("\n" + "--------------------------------------------------------------------------------")
print("chapter 7: user input and while loops".title().center(80))
print("--------------------------------------------------------------------------------")

# input() function for user input
prompt = "Tell me something, and I will repeat it back to you."
prompt += "\nType 'quit' to end the conversation... "
message =""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print("\n" + message + "\n")

# flags
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print("\n" + message + "\n")

# break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# continue (returns to the start of a loop)
print("\nOdd Numbers (0 - 10):")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(f"\t- {current_number}")

# use while loops to modify lists and dictionaries // don't use for loops to modify lists

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary.
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
