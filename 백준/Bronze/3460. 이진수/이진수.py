test_case = int(input())

for i in range(test_case):
    num = int(input())
    bi_num = (str(bin(num))[2:])[::-1]

    for j in range(len(bi_num)):
        if bi_num[j] == '1':
            print(j,end=' ')
