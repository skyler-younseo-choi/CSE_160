"""
* Name: Skyler Choi
* Date: January 16th
* CSE 160, Winter 2024
* Homework 1
* Description:
"""

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1
print("Problem 1 solution follows:")
a = 3
b = -5.86
c = 2.5408
x1 = (-b - (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
x2 = (-b + (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
print("Root 1:", x1)
print("Root 2:", x2)
# Problem 2
print("\nProblem 2 solution follows:")
result2 = 0
for n2 in range(2, 11, 1):  # Range Function to assign n from 2 to 10
    result2 = (1 / n2)  # Assigning results in 1/n to decimal forms
    print("1/" + str(n2) + ": " + str(result2))  # Printing out results
# Problem 3
print("\nProblem 3 solution follows:")
# Provided partially-working solution to problem 3
# `...` are placeholders and should be replaced
n = 10
triangular = 0
for i in range(1, n + 1, 1):
    triangular = triangular + i
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)


# Problem 4
print("\nProblem 4 solution follows:")
n4 = 10
factorial = 1
for i in range(1, n4+1, 1):
    factorial = factorial * i
print(str(n4) + "!: " + str(factorial))


# Problem 5
print("\nProblem 5 solution follows:")
num_lines = 10
for i in range(1, num_lines + 1, 1):  # repeat the folw seqs 10 times:
    multiple_fact = 1  # resets to value
    for j in range(1, num_lines + 1, 1):
        multiple_fact = multiple_fact*j
    print(str(num_lines) + "!" + ": " + str(multiple_fact))
    num_lines = num_lines - 1
# Problem 6
print("\nProblem 6 solution follows:")
num_lines2 = 10
e = 1
for i in range(1, num_lines2 + 1, 1):  # repeat the folw seqs 10 times:
    multiple_fact2 = 1  # resets to value
    for j in range(1, num_lines2 + 1, 1):
        multiple_fact2 = multiple_fact2 * j
    Reciprocal = 1 / (multiple_fact2)
    e = e + Reciprocal
    num_lines2 = num_lines2 - 1
print("e:", e)
