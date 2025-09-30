#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

print("How many terms for the Fibonacci Sequence would you like?")
fibln = int(input())
while (fibln < 0):
  print("Invalid! Must enter a positive integer. \n How many terms for the Fibonacci Sequence would you like?")
  fibln = input()

sequence = [0]
nextnum = 1
for i in range(fibln):
  sequence.append(nextnum)
  nextnum += sequence[i]

print(fibln)
print(sequence)


