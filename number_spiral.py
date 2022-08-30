def number_finder(input_string):
    x_and_y = input_string.split(' ')
    y = int(x_and_y[0])
    x = int(x_and_y[1])
    if x % 2 == 1:
        x_one = x * x
    else:
        x_one = (x-1) * (x-1) + 1
    if y % 2 == 1:
        one_y = (y-1) * (y-1) + 1
    else:
        one_y = y * y

    if x >= y:
        if x % 2 == 1:
            return x_one - y + 1
        else:
            return x_one + y - 1
    elif x < y:
        if y % 2 == 1:
            return one_y + x - 1
        else:
            return one_y - x + 1


t = int(input())
t_list = []
for i in range(t):
    t_list.append(input())
for test in t_list:
    print(number_finder(test))
