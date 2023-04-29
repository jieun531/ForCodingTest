import sys, math

num_of_class = int(sys.stdin.readline().rstrip())
num_of_stu = list(map(int,sys.stdin.readline().rstrip().split(' ')))
can_head_ins, can_sub_ins = map(int, sys.stdin.readline().rstrip().split(' '))

num_of_ins = 0

for i in range(num_of_class) :
    remain = num_of_stu[i] - can_head_ins
    num_of_ins += 1
    if remain > 0 :
        num_of_ins += math.ceil(remain / can_sub_ins)

print(num_of_ins)