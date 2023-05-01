num_of_try = int(input().rstrip())

for i in range(num_of_try):
    sum = 0
    j = 0
    num_list = list(map(int, input().rstrip().split(' ')))
    for j in range(10) :
        if num_list[j] % 2 != 0 :
            sum += num_list[j]

    print("#%d %d" % (i + 1, sum))
