# thisIsCamelCase
# this_is_snake_case

# variables

aString = "Eleanor"
alsoAString = 'Eleanor'

anInteger = 3
aFloat = 3.2

a_boolean = True
also_a_boolean = False

# string concatenation (sans typecasting)
print("The person writing this is " + aString + ".")

# string interpolation (f-string)
print(f"The person writing this is {aString}.")

print(f"My favorite number is {anInteger}!")

# string concatentation (with typecasting)
print("My favorite number is " + str(anInteger) + "!")

# conditional statements

num = 12

if num > 10:
    print("That's a big number!")
elif num == 10:
    print("That's a medium-sized number!")
else:
    print("That's a small number!")

animal = 'dog'
color = ''

if animal != 'cat':
    print("The animal is not a cat")
if not animal == 'cat':
    print("The animal is not a cat (2)")

if not color: # falsiness of empty string
    print("Will this print?")

color = 'brown'

if animal == 'dog' and color == 'brown':
    print("The animal is a brown dog")

decimalNum = 3.5

if decimalNum > 3:
    print("The number is greater than 3!")
else:
    print("The number is not greater than 3!")
    
# (execute if true) if (condition) else (execute if false)
print("The number is greater than 3!") if decimalNum > 3 else print("The number is not greater than 3!") # ternary operator

# loops

for i in range(2, 10, 2): # for loop
    print(i)

for i in range(5): # default starting value of 0 and incrementation of 1 in sequence
    for j in range(5):
        print(i * j)

small_num = 7

while small_num > 1: # while loop
    print("small_num is still kinda big.")
    small_num = small_num - 1

password = "abc123"
guess = ""

while guess != password:
    guess = input("Guess what the password is! ") # reassigns guess value to user input

# functions

# function definition
def squareNum(num):
    if True:
        return num * num
    else:
        return None # null/void value in Python

# function call
print(squareNum(5))
returnedSquare = squareNum(10)
print(f"{returnedSquare} is the square of 10!")