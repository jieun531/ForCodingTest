test_case = int(input())

for i in range(test_case):
    case = input()
    cur = '0' * len(case)
    c_num = 0

    for j in range(len(case)) :
        if case[j] != cur[j] :
            cur = cur[0:j] + case[j] * len(cur[j:])
            c_num += 1

    print("#%d %d" % (i+1 , c_num))