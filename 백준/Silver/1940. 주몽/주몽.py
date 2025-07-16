import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

material = list(map(int, input().split()))
material.sort()

first = 0
second = N-1
count = 0
sum = 0

while first < second :
    sum = material[first] + material[second]
    if sum < M :
        first+=1
    elif sum > M :
        second-=1
    else:
        count+=1
        first+=1
        second-=1


print(count)
