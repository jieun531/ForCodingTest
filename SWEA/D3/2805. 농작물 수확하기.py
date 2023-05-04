test_case = int(input().rstrip())

for i in range(test_case):
    len_land = int(input().rstrip())
    mid_land = len_land//2
    num_list = []
    selled = 0

    for a in range(len_land) :
        num_list.append(list(map(int, input().rstrip())))
        selled += sum(num_list[a])

    for j in range(mid_land):
        selled -= sum(num_list[j][:mid_land-j])
        selled -= sum(num_list[j][len_land-mid_land+j:])

        selled -= sum(num_list[len_land-mid_land+j][:j+1])
        selled -= sum(num_list[len_land-mid_land+j][-1-j:])

    print("#%d %d" % (i+1, selled))
