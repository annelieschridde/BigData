#!/usr/bin/env python

import sys

# The input will be in the form of key-value pairs
# It is sorted according to the key
# Each key value pair will be in a new line
# The key and the value are seperated by a tab (\t)
# The key is the payment type and the value is the sales

# Example input data (Key=Payment, Value=Sales)
# Input is ordered by the key
# Visa  205.96
# Cash  11.32
# Cash  444.19

# We want to sum all values with the same key
# Example output data (Key=Payment, Value=Sum of Sales)
# Visa  205.96
# Cash  455.51

# Sum of all sales (values) is initialized with zero, we just started
sum_of_values = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # The result is a tuple with 2 elements
    data = line.strip().split("\t")

    # Store the 2 elements of this line in seperate variables
    key, value = data

    # Do we have a previous_key (previous_key != None) and 
    # is the new key different than the previous key?
    # This means the line starts with a new key (key changes e.g. from "Visa" to "Cash")
    # Remember that our keys are sorted
    if previous_key != None and previous_key != key:
        # Then write the result of the old key (Key=category, Value= Sum of Sales)
        # to the standart output (stdout)
        # Key and value are seperated by a tab (\t)
        # Line ends with new line (\n)
        sys.stdout.write("{0}\t{1}\n".format(previous_key, sum_of_values))
        # Sum of sales starts again with 0
        sum_of_values = 0

    # Add the value to the total sales
    # a += b is the same as a = a + b
    # the float function transforms the value
    # to a float data type (like decimal)
    sum_of_values += float(value)
    # the previous key for the next iteration is the current key of the this iteration 
    previous_key = key

# write the last result to stdout
sys.stdout.write("{0}\t{1}\n".format(previous_key, sum_of_values))
