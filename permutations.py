n = int(input())
if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")                             # hard coded because there are no better ways
else:
    el = list(range(1, n + 1))
    even_l = []
    odd_l = []
    for i in el:
        if i % 2 == 1:
            odd_l.append(i)
        elif i % 2 == 0:
            even_l.append(i)
    output_l = even_l + odd_l
    print(' '.join([str(e) for e in output_l]))

# Create a list of integers from 1 to n, then iterate through every of that list,
# whether the element is divisible by 2, put it into its corresponding list,
# then concatenate the two lists (with the even one first), then join elements of
# the final list together into a string.
