test_num = int(input())

for i in range (test_num):
    t_num = int(input())
    t_list = []
    for j in range (t_num):
        t_list.append([1] * (j+1))
    for k in range(2, t_num):
        for l in range(1,k):
            t_list[k][l] = t_list[k-1][l-1] + t_list[k-1][l]

    print("#%d" % (i+1))
    for i in range(t_num):
        print(*t_list[i], sep=' ')