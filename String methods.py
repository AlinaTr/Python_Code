# INPUT
"""
1. Read a product name from the keyboard.
product_name = input('This is the product')
 Save the result in a variable.
Display a message containing the saved variable.
"""

# product_name = input('This is the product: ')
# print(f' The product name is {product_name}')

"""
2. Read a price from the keyboard. Force the user to enter the price as a decimal number.
Save the result in a variable.
Displays a message containing the saved variable.
"""

# price = float(input('Write a number: '))
# print(f'The price is {price}')

# String methods:

info = 'Afara sunt 2 grade'
print(info[0]) # => 'A' (1st char dis at index 0)
print(info[1]) # => 'f'
print(info[5]) # => ' ' (at index 5 we have space)

# 1.
prop1 = 'Andy is short for Andrei'
#  a. 1st char .
# print(prop1[0]) # A
# # b. 4-th char.
# print(prop1[3]) # y
# # c. last char.
# print(prop1[-1]) # i

# String lenght - len()
info = 'Afara sunt 2 grade'
print(len(info)) # 18

# Slicing: We can access "slices" from the string, using the syntax my_str[start_pos:end_pos:pas]
info = 'Afara sunt 2 grade'
print(info[0:2]) # => 'Af'
# print(info[:2])

print(info[0:5]) # => 'Afara'
print(info[6:])  # => 'sunt 2 grade'
print(info[:5])  # => 'Afara'

# String reversal:
print(info[::-1]) # => 'edarg 2 tnus arafA'

# 3.We have the string prop3 = 'The concert is tomorrow."
# Save in a variable, using slicing, the first word.
# b. Extract the first 3 characters from prop3.
# c. Display prop3 with reversed characters.
prop3 = 'The concert is tomorrow.'
first_word = prop3[:3]
print(first_word)
char = prop3[0:3]
print(char)
print(prop3[::-1])

# String methods

# Upper case
# str1 = 'banana'
# str1.upper()
# print(str1.upper()) # BANANA

# find a char in a string
my_str = 'vacation'
print(my_str.find('a')) # se gaseste la poz. 1
print(my_str.find('ac')) # substring # spune tot 1

# 4. The string my_str = 'holiday' is given.
my_str = 'holiday'
# a. Use the find() method to find the first index at which the character 'a' is found.
print(my_str.find('a'))
# b. Use the count() method to find out how many times the character 'a' appears in my_str.
print(my_str.count('a'))
# c. Use  capitalize() method to capitalize the word.
print(my_str.capitalize())
# d. Use the upper() method to capitalize the word.
print(my_str.upper())


# To find if our string is number
name = 'bro code'
# print(name.isdigit()) # False

# To check if our string contains only alphabetical letter
print(name.isalpha()) # it will be False, because we have a space between words in Name

# We count how many  'o' characters are in our string
print(name.count('o')) # raspuns 2

# replace characters
print(name.replace('o', 'a'))

print(name * 3)

# EXERCISES:

# 1. Read the name from the keyboard,
# then read the first name from the keyboard.
# Shows how many characters the full name has (surname + surname)
# displaying the sentence 'The full name has x characters.', where x is the total number of characters.

# 2. Read the length from the keyboard,
# then read the width from the keyboard.
# Display the area of the rectangle with length and the width read from the keyboard
# display the sentence 'The area of the rectangle is x.', where x is the value of the area

"""
3. Having the string: 'Coral is either the stupidest animal or the smartest rock.', show how many times the word 'the' appears
"""

"""
# 4. Using the same string from point 2, replace the word 'the' with 'THE' everywhere in the sentence and print
the outcome.
"""

"""
5. Using the same string from point 2, use an assert to check if this string only contains
numbers.
"""

# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:
str1 = 'vara'
# a. endswith()
# print(str1.endswith('va')) # => False (da False pt ca string nu se termina in 'va'
# print(str1.endswith('a')) # True (da true, pt ca string se termina cu 'a'

# fruct_preferat = 'capsuni'
# assert fruct_preferat.endswith('i')
# b. index()
str2 = 'Buna ziua, zi frumoasa'
# Where in the text is the word "zi"?:
# print(str2.index('zi')) # => 5.

# Where in the text is the first occurrence of the letter "a"?:
# print(str2.index('a')) # => 3

# Where in the text is the first occurrence of the letter "a" when you only search between position 5 and 10?:
# print(str2.index('a', 5, 10)) # => 8

# c. lower()
# str3 = 'ContrAcT'
# print(str3.lower()) # => contract

# d. replace()
# str4= 'Imi place culoarea rosu'
# print(str4.replace('rosu', 'albastru')) # => inlocuieste rosu cu albastru

# e. strip(): remove spaces at the beginning and at the end of the string:
# str5 = '      cartofi prajiti       '
# print(str5.strip()) # => ne afiseaza fara spatii la inceput si la sfarsit

# f. split() : The split() method splits a string into a list.
# str6 = 'mere pere portocale capsuni'
# print(str6.split()) # => ['mere,', 'pere,', 'portocale,', 'capsuni']


