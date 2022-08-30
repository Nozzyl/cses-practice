n = input()
n_integers = input()
n_integers_arr_str = n_integers.split(" ")
n_integers_arr = [int(i) for i in n_integers_arr_str]            # second input line is converted to number array
move_count = 0
for i in range(int(n) - 1):                                      # we need to check the array up to the second last int
    if n_integers_arr[i] > n_integers_arr[i + 1]:                # if the int being checked is larger than the one after
        move_count += n_integers_arr[i] - n_integers_arr[i + 1]  # we make n moves, where n is the {int} - {next int}
        n_integers_arr[i + 1] = n_integers_arr[i]                # the result of n moves being made
print(move_count)

# This works by checking every number in the list given up to the second to last one. For every number being checked,
# we check if it's larger than the one after it. If it is, the difference the between the number being checked and the
# one after it is the number of moves we make, therefore we add that difference to the move count (move_count), then we
# make the number after the one being checked equal to it, as that would be the result of the moves being made; if the
# number being checked is not larger than the one after it, we just check the next one.
