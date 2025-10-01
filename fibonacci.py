#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
while True:
    try:
        i = int(input("Please enter a POSITIVE number corresponding to the term you would like to know: "))
        if i > 0:
            break
        print("Please input a POSITIVE number.")
    except ValueError:
        print("Please input a positive INTEGER.")
# Use a for loop to print the Fibonacci sequence up to that many terms.
term1, term2, term3 = 0, 1, 0

if i == 1:
  term3 = term1
  print(term1)
elif i == 2:
  term3 = term2
  print(term1, term2, end=" ")
else:
  print(term1, term2)
  for _ in range(3, i + 1):
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    print(term3, end=" ")


