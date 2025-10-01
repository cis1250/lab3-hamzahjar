#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
i = int(input("Please enter a POSITIVE number corresponding to the term you would like to know: "))
# Validate that the input is a positive integer.
if i<=0:
  print("Please input a POSITIVE number.")
  return
# Use a for loop to print the Fibonacci sequence up to that many terms.
term1, term2, term3 = 0, 1, 0

if i = 1:
  term3 = term1
elif i = 2:
  term3 = term2
else:
  for _ in range(3, i + 1)
    term3 = term1 + term2
    term1 = term2
    term2 = term3


