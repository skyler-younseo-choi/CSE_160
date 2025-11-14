# Name: ...
# CSE 160
# Autumn 2024
# Practice #1


# ~~~ Begin Problem 1 ~~~
'''
Given a list of integers, prints the sum of the even ints in the list.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
Assumptions:
    nums: a variable containing list of integers.

Prints: a integer representing the sum of the even numbers in the list

Examples:

nums = [5, 2, 6, 3, 4]  should print 12
nums = [3, 6, 11, 2, 5] should print 8
nums = []               should print 0
nums = [7]              should print 0
nums = [5, 8, 5]        should print 8
nums = [72, 2, 6, 1]    should print 80
nums = [6]              should print 6
nums = [4, 4, 4]        should print 12
nums = [1, 1, 1, 2]     should print 2

Try copying these values into the nums variable to see if your code works.
'''

nums = [5,2,6,3,4]
sum = 0

# Write your code for Problem 1 here!
for num in nums:
    if num%2==0: # to evaluate if the num is even. If true, num is even.
        sum=sum+num #Since true, adds nums into num
print(sum)

# ~~~ End Problem 1 ~~~

# ~~~ Begin Problem 2 ~~~
'''
Prints True if string hidden_char is found in the given string.
    You should use a for loop to determine where the hidden_char is.

Assumptions:
    input_str: a variable containing a string
    hidden_char: a variable containing the character to look for in input_str

Prints: A boolean representing whether or not hidden_char is in input_str

Examples:

with input_str = 'cse160' and hidden_char = 's',        code should print True
with input_str = 'c' and hidden_char = 'c',             code should print True
with input_str = 'a' and hidden_char = 'b',             code should print False
with input_str = 'coding' and hidden_char = 'g',        code should print True
with input_str = 'I love python' and hidden_char = 'z', code should print False
with input_str = 'Snakes' and hidden_char = 's',        code should print True
with input_str = '123' and hidden_char = 'g',           code should print False
with input_str = '' and hidden_char = 'a',              code should print False
'''

input_str = 'c'
hidden_char = 'c'
found = False

# Write your code for Problem 2 here!
for letter in input_str:
    if letter == hidden_char:
        found = True
print(found)

# ~~~ End Problem 2 ~~~

# ~~~ Begin Problem 3 ~~~
'''
Print the number of times the number find_num occurs in the given list

Assumptions:
    nums: a variable containing a list of ints
    find_num: a variable containing the integer to count the occurrences of

Prints:
    A integer representing the number of times find_num appears in nums

Examples:

with nums = [1, 5, 6, 2, 1] and find_num = 1   code should return 2
with nums = [] and find_num = 4                code should return 0
with nums = [1, 2, 3] and find_num = 1         code should return 1
with nums = [4, 5, 6] and find_num = 2         code should return 0
with nums = [160] and find_num = 1             code should return 0
with nums = [90] and find_num = 2              code should return 0
with nums = [5, 5, 5] and find_num = 5         code should return 3
with nums = [3, 6, 12, 9, 12] and find_num = 1 code should return 0
'''

nums = [1,2,3,2,2]
find_num = 2
count = 0

# Write your code for Problem 3 here!
for number in nums:
    if find_num == number:
        count = count+1
print(count)

# ~~~ End Problem 3 ~~~
