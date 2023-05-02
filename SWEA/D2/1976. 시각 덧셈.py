num_of_try = int(input().rstrip())

for i in range(num_of_try):
    cur_time = list(map(int, input().rstrip().split(' ')))
    after_time = [cur_time[0] + cur_time[2] , cur_time[1] + cur_time[3]]

    if after_time[1] > 59 :
        after_time[1] %= 60
        after_time[0] += 1

    if after_time[0] > 12:
        after_time[0] = after_time[0] % 12

    if after_time[0] == 0:
        after_time[0] += 12

    print("#%d %d %d" % (i + 1, after_time[0], after_time[1]))
