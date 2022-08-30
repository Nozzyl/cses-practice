sequence = input()
last_char = ""
current_char = ""
current_repetition = 1
repetitions = [1]                                # list of all repetitions
for i in range(len(sequence)):
    last_char = current_char                     # after every loop, the previously current_char becomes last_char
    current_char = sequence[i]                   # the current_char
    if current_char == last_char:
        current_repetition += 1                  # if the char being checked is the same as the last, add 1 to the
        repetitions.append(current_repetition)   # current repetition, then record it in the list of repetitions
    else:
        current_repetition = 1                   # minor bit of optimization - not recording repetitions of 1
print(max(repetitions))

# This works by checking every char - for each char, check if it's the same as the last, if so, add 1 to the current
# repetition. If more than 2 chars repeat, this system handles that. If it then sees that the current number is not
# the same as the last, the current repetition is reset. Every time a repetition is longer than 1, is is recorded in
# the repetitions array. The last line finds the maximum value recorded in the array and prints that.
