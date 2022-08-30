en = int(input())
en_minus_one_numbers = input()                      # two input lines
str_number_array = en_minus_one_numbers.split(" ")  # split input string into string array
number_array = [int(i) for i in str_number_array]   # then into number array - this is needed to make sort and check
number_array.sort()
if number_array[-1] != en:                          # if the last number in the array is not the same as n
    print(en)                                       # that means the missing number is n
else:                                               # for the other cases
    for i in range(1, en):                          # check each number in the full list and its match in the given list
        if number_array[i - 1] != i:                # if a number in the full list gets an incorrect match
            print(i)                                # that's our output
            break

# This works by sorting the list that's missing a number, then checking the complete list's numbers with each of its
# match in the incomplete list. When there's a incorrect match, we know that it's the missing number. Line 6 and 7
# are needed to handle the case where the last number of the complete list is that one that's missing.
