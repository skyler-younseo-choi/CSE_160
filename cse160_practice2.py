# Name: Skyler Choi
# CSE 160
# Autumn 2024
# Practice #2


# Problem 1
'''
Write a function letter_count(word, letter) that returns the number
of times letter appears in word. letter is case-sensitive.

Arguments:
    word: a String
    letter: a character

Returns: An integer representing the count of letter in word.

Examples:
letter_count("hi", 'h') returns 1
letter_count("festival", 'q') returns 0
letter_count("astronomy", 'o') returns 2
'''
# your solution code should start here

# Problem 2
'''
Write a function letter_multiply(num, letter) that returns a String containing
letter num many times. If num is a negative integer, return the String
"invalid value for num".

Arguments:
    num: an integer
    letter: a character

Returns: A String made of num many repeats of letter.

Examples:
letter_multiply(7, 'b') returns "bbbbbbb"
letter_multiply(-2, '&') returns "invalid value for num"
letter_multiply(0, 'a') returns ""
'''


# Problem 3
'''
Write a function glitchy_message(msg) that repeats each char in msg the number
of times it appears in msg originally. Make function calls to letter_count
and letter_multiply above instead of coding their functionality from scratch.

Arguments:
    msg: a String

Returns: A String made of each char in msg repeating the number of times it
appears in msg.

Examples:
glitchy_message("letter") returns "leetttteer"
glitchy_message("banana") returns "baaannaaannaaa"
glitchy_message("paint") returns "paint"

'''
# your solution code should start here

# Problem 1


def letter_count(word, letter):
    counting = 0
    for character in word:
        if character == letter:
            counting = counting + 1
    return counting


print(letter_count("astronomy", 'o'))

# Problem 2


def letter_multiply(num, letter):
    result = ""
    if num < 0:
        result = "invalid value for num"
    else:
        for i in range(num):
            result = letter + result
    return result


print(letter_multiply(0, 'cat'))

# Problem 3
'''
Write a function glitchy_message(msg) that repeats each char in msg the number
of times it appears in msg originally. Make function calls to letter_count
and letter_multiply above instead of coding their functionality from scratch.

Arguments:
    msg: a String

Returns: A String made of each char in msg repeating the number of times it
appears in msg.

Examples:
glitchy_message("letter") returns "leetttteer"
glitchy_message("banana") returns "baaannaaannaaa"
glitchy_message("paint") returns "paint"
'''


def glitchy_message(msg):
    vocab = ""
    for char in msg:
        nums3 = letter_count(msg, char)
        temp = letter_multiply(nums3, char)
        vocab = vocab + temp
    return vocab


print(glitchy_message("letter"))
