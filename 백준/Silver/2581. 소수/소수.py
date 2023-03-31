import sys
minimum = int(sys.stdin.readline())
maximum = int(sys.stdin.readline())
pris = []

for i in range(minimum, maximum + 1):
    for j in range(2,i+1) :
        if i % j == 0:
            if i == j :
                pris.append(j)

            break

if len(pris) == 0 :
    print(-1)
else :
    print(sum(pris))
    print(min(pris))