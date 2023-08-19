# Initialize a variable

car_brand = 'Volvo'
car_model = 'XC 60'

favorite_fruit = 'apple'

prop1 = 'value'
prop_2 = 'prop2'

# example of case-sensitive variable
my_var = 5
my_Var = 10

# override
name = 'Maria'
print(name)
name = 'Ana'
print(name)

# a variable can have multiple values in one line, or same value for multiple variables
x, y, z = 'orange', 'apple', 'banana'
print(x)
print(y)
print(z)

print(x, y,z)

a = b = 'apple'
print(a)
print(b)

# define STRING variables
prop1 = 'Ana is outside'
prop2 = 'Maria is inside'

# String Concatenation
name = 'Bacter'
print(name)
first_name = 'Cosmina'
print(name + ' ' + first_name)
print('My name is ' + name + ' ' + first_name)

# DATA TYPES

# 1.
# a. Define a variable type integer, called 'width'
width = 10

# b. Define a variable type string, called 'decription'
decription = 'square'

# c. Define 2 variables type float
price = 2.5
discount = 0.5

# d. Define a variable type bool
initialized = True

# e. Print the variables defined above
print(width)
print(decription)
print(price)
print(discount)
print(initialized)

# Define a string variable and print the type of the variable
color = 'red'
print(type(color)) # <class 'str'>

price = 12.3
print(type(price)) # <class 'float'>

"""
Type casting function:
- helps us to convert the types of variables
Example: are number1 and number2 of the same type?
"""
number1 = 10 # int
number2 = '10' # string
number3 = int(number2) # we convert the number2 variable from string to integer
print(number3)

string1 = str(number1) # we convert the number1 variable from ineteger to string
print(string1) # => 10
print(type(string1)) # => <class 'str'>

product_name = 'Sofa'
price = 200
print('Product ' + product_name + ' costs ' + ' price ' + 'dollars') # => Product Sofa costs  price dollars
print('Product' + product_name + ' costs ' +  str(price)  + ' dollars ' ) # print('Product' + product_name + ' costs ' +  str(price)  + ' dollars ' )
print(f'Product {product_name} costs {price} dollars ') # f string

d1 = 10.5
d2 = 12.3
print(d1 + d2) # 22.8
print(str(d1) + ' ' + str(d2)) # 10.5 12.3 - becuase we converted them to str

"""
Define 2 variables: name (str) and age(int)
using f string, print a sentence with the 2 variables
"""
name = 'Jill'
age = 35
print(f'My friend {name} is {age} years old') # My friend Jill is 35 years old

# TYPE si TYPE CASTING
"""
a. Create a variable type integer, and print it. Print also the type
"""
a = 12
print(a)
print(type(a))

"""
b. Create a variable type float, and print it. Print also the type
"""
b = 50.55
print(b)
print(type(b))

"""
c. Create a variable type string, and print it. Print also the type
"""
c = '1985'
print(c)
print(type(c))

"""
d. Create a variable type boolean, and print it. Print also the type
"""
d = False
print(d)
print(type(d))

# ASSERT -  we check if something is true
# a = 1
# # I ask Python: does 1 equal 1?
# assert a == 1
# print('it does')
# assert a == 2
# print('it doesnt')

"""
Assert practice:
# a. Define a string variable with value 10
b. Check if the string is equal to '10'
c. Check if the string equals 10
"""
# str = 10
# assert str == 10
# print("It's true")
# assert str == "10"
# print("It's not true")

# EXERCISES:

# 1. Declare and initialize one variable of each of the following types: str, int, bool float

hobby = 'swimming' # string
date_of_birth = 2000 # integer
miles = 10.5 # float
driving_license = True # bool
with_parents = False # bool

# 2. Use the type() function to check if the variables declared in point 1 have the expected data type.

print(type(hobby)) # <class 'str'>
print(type(date_of_birth)) # <class 'int'>
print(type(miles)) # <class 'float'>
print(type(driving_license)) # <class 'bool'>
print(type(with_parents)) # <class 'bool'>

# 3. Round the variable defined as float type, using the round() function and save this change in the same
# variable (override). Then check its type.

# miles = miles.__round__()
# print(type(miles))

# OR

miles = round(miles)
print(type(miles))

# 4. Use the print() function to print 4 sentences to the console, using  4 variables.
# (Resolve type mismatches in any way you want)

# Sentence 1
first_name = 'Maria'
distance = 8.5
period = 8
print(f'My colleague {first_name}, over a period of {period} years, lived  {distance} km away from the city center ')

# Sentence 2
city = 'New York'
year = 2010
duration = 1.5
print(f'In the year of {year}, in New York there was a drought that lasted {duration} month. ')

# Sentence 3
is_open = True
print(f'If the shop is_open, we print {is_open}')

# Sentence 4
age = 3
print(f'The child turns {age} years old next month')

"""
5. Defines a float variable with the value 1.5
- Check if the variable is equal to 1.5.
- Check if the variable is equal to true. What do you notice?
- How can you make the assert at point c pass?
"""

my_ex = 1.5
assert my_ex == 1.5
# assert my_ex == True # error
assert bool(my_ex) == True # with type casting, we convert the variable from float to bool

# 6. Read an odd-sized string from the keyboard. Display the middle character.
# sentence =  input('Enter an odd-sized character string: ')
# mid_char = len(sentence) // 2
# print(f'The middle character is {sentence[mid_char]}')

# 7.Using assert, check if a string is a palindrome.
# palindrome = a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

# read a string from the keyboard and save the result in a variable
# prop = input('Write something here: ')

# we check if prop is equal to inverted prop
#  if prop is not a palindrome, we will have an error and the message "The entered word is not a palindrome" will be displayed

# assert prop == prop[::-1], 'The word is not palindrome'
#
# # if prop is  a palindrome:
# print('The word is palindrome')

# 8. Using a single line of code, read a string from the keyboard (ex: 'alabala portocala') and save each
#  word in a variable. Print the generated variables for verification.

# a, b = input('Write a string: ').split()
# print(a, b)
# print(a)
# print(b)

# 9. Reads a string from the keyboard (ex: 'alalabala portocala'). Save the first character from the string in a variable.
#  Capitalize this character everywhere in the string, except the first and last character.

# Example 1:
#   input: 'alabala portocala'
#   output: 'alAbAlA portocAla'
# Example 2:
#   input: 'maria are mere'
#   output: 'maria are Mere'
# Example 3:
#   input: 'aritmetica'
#   output: 'aritmetica'

# my_str = input('Write string: ')
# my_char = my_str[0]

# create a new string, using slicing, that will contain all the characters, except the first character
# my_str2 = my_str[1:]

# we use the helper method replace(), to replace all characters equal to the variable 'my_char',
#  with the capitalized version.
#  to capitalize a string/character, we use the upper() method

# my_str3 = my_str2.replace(my_char, my_char.upper())

"""
it is possible that the last character is the same as the first character in the string received as output.
 then we will transform the last character of 'my_str3', to make sure that it is always lowercase.
display the final result using f string
"""
# print(f'{my_char}{my_str3[:-1]}{my_str3[-1].lower()}')

"""
10. Read a user from the keyboard. 
Then read a password from the keyboard. 
It displays: 'The password for user x is *** and has y characters.', 
where x is the user read from the keyboard, and y is the length of the password entered on the keyboard.
 The number of * in the displayed string will be calculated dynamically, having as many * characters as there are in the password.
Example:
# - if the password entered is 'abcd', we will have ***
# - if the password entered is 'abcdef', we will have ******.
"""
user = input('User: ')
password = input('Password: ')
hidden_password = '*' * len(password)
print(f'The password for user {user} is {hidden_password} and has {len(password)} characters')