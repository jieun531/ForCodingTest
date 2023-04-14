import sys
num_gae = int(sys.stdin.readline().rstrip())
num_list = []
for _ in range(num_gae) :
    a=int(sys.stdin.readline().rstrip())
    if a != 0 :
        num_list.append(a)
    else :
        num_list.pop(-1)

print(sum(num_list))