import sys
pri = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split(' ')))
pri = 0

for i in num:
    for j in range(2,i + 1) :
        if i % j == 0:
            if i == j :
                pri += 1

            break

print(pri)