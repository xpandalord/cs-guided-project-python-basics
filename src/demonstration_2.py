"""
You have been asked to implement a line numbering feature in a text editor that
you are working on.

Write a function that takes a list of strings and returns a new list that
contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make
sure to put a colon and space in between the `line_number` and `string` value.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""
def number(lines):
    # Your code here
    output = []

    # line_number = 1
    # for line in lines:
    #    output.append(f"{line_number}: {line}")
    #    line_number += 1

    for i in range(len(lines)):
        output.append(f"{i + 1}: {lines[i]}")

    return output

