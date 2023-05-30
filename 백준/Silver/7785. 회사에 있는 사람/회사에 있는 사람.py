import sys

log_num = int(sys.stdin.readline())
people_left = dict()

for _ in range(log_num):
    name, type = sys.stdin.readline().rstrip().split()
    if type == 'enter':
        people_left[name] = type
    else :
        del people_left[name]

for i in sorted(people_left.keys(), reverse=True):
    print(i)

