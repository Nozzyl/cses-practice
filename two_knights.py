def position_counter(k):
    return int(((k*k)*(k*k-1))/2-4*(k-1)*(k-2))


n = int(input())
for i in range(1, n + 1):
    print(position_counter(i))
