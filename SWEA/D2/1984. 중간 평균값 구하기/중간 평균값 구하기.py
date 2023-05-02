num_of_try = int(input().rstrip())

for i in range(num_of_try):
    num_sco = list(map(int,input().rstrip().split(' ')))
    num_sco.sort()
    num_sco.pop(0)
    num_sco.pop(-1)

    print("#%d %d" % (i + 1, round(sum(num_sco) / 8 )))