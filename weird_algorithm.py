user_input = int(input())
first_output = f"{user_input} "
while user_input != 1:                                         # when user_input approaches 1, stop the loop
    if user_input % 2 == 0:                                    # if user_input is even
        user_input = int(user_input / 2)                       # divide it by 2
        first_output = first_output + str(user_input) + " "    # then add it to the output
    else:                                                      # if user_input is odd
        user_input = int(user_input * 3 + 1)                   # multiply it by three and add one
        first_output = first_output + str(user_input) + " "    # then add that to the output
output = first_output.rstrip()                                 # removes the unwanted final space caused by line 9
print(output)

# The loop checks every time whether the number is even, this is technically unnecessary as it could be coded
# to only check once and go back and forth between the two operations
