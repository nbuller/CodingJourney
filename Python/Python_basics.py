# print to console
print("Hello, World!")

# variable creation
varName = "Nathan"
print(varName)

# collect input from user
color = input("What is your favorite color? ")
print(color)

# data types
# int --> integer
# str --> string
# data types dont't mix
num = 4
number = 5 # this is an int
number_str = "5" # this is a string
string = "Hello "
print(string + number_str) # put the strings side by side (concatenation)
print(f"{string} {number_str}") # prints string and number_str and adds a space between them
print(num + number) # add the numbers together

# casting a variable
print(string + str(number))
print(int(number_str) + number)

# contitional statements
# if a conition is met, we do something, otherwise we do something else
number1 = 1
number2 = 10
number3 = 20
userNumber = int(input("choose a number between 1 and 50 "))
if (userNumber <= number1):
    print("Your number is less than or equal to 1")
elif (userNumber > number1 and userNumber <= number2):
    print("Your number is between 1 and 10")
elif (userNumber > number1 and userNumber <= number2):
    print("Your number is between 10 and 20")
else:
    print("Your number is greater than 20")