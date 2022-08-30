n = int(input())
if (n*(n+1)) % 4 != 0:
    print("NO")
elif n == 3:
    print("YES")
    print("1")
    print("3")
    print("2")
    print("1 2")
else:

    print("YES")
    s = list(range(1, n + 1))
    s_one = list(range(1, int(n*3/4 + 1)))
    s_one_total = int((int(n*3/4)) * (int(n*3/4 + 1)) * 1/2)
    s_two = list(range(int(n * 3/4) + 1, n + 1))
    s_two_total = int((n * (n + 1)) * 1/2 - int((int(n*3/4)) * (int(n*3/4 + 1)) * 1/2))


    if s_one_total > s_two_total:
        while s_one_total - s_two_total > s_one[0] * 2:
            s_two.append(s_one[0])
            s_two_total += s_one[0]
            s_one_total -= s_one[0]
            s_one.remove(s_one[0])
        needed_num = int((s_one_total - s_two_total)/2)
        s_two_total += needed_num
        s_two.append(needed_num)
        s_one_total -= needed_num
        s_one.remove(needed_num)

        print(len(s_one))
        print(' '.join([str(e) for e in s_one]))
        print(len(s_two))
        print(' '.join([str(e) for e in s_two]))

    elif s_one_total < s_two_total:
        while s_two_total - s_one_total > s_two[0] * 2:
            s_one.append(s_two[0])
            s_one_total += s_two[0]
            s_two_total -= s_two[0]
            s_two.remove(s_two[0])
        needed_num = int((s_two_total - s_one_total)/2)
        s_one_total += needed_num
        s_one.append(needed_num)
        s_two_total -= needed_num
        s_two.remove(needed_num)

        print(len(s_one))
        print(' '.join([str(e) for e in s_one]))
        print(len(s_two))
        print(' '.join([str(e) for e in s_two]))
