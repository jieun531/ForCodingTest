import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hab = [0] * N
num = list(map(int, input().split()))
remain = [0] * N
sameRem = [0] * M
sub = 0
result = 0

for i in range(N):
    hab[i] = hab[i-1] + num[i]
    sub = hab[i] % M
    remain[i] = sub
    sameRem[sub] += 1

    if remain[i] == 0 :
        result += 1

for i in range(M):
    if sameRem[i] > 0 :
        result += (sameRem[i] * (sameRem[i] - 1) ) // 2

print(result)

#////////////////////////////////////////////////////////////#
# 구간합을 통해 구하기
# (a-b)%c = (a%c) - (b%c)
# 만약 두 수의 차가 c의 배수이면 나머지 0
# a 까지의 구간합 = b 까지의 구간합이면 나머지 0
# 리스트 입력 -> 구간합 리스트 -> 구간합을 M으로 나눈 나머지 리스트 -> 주어진 경우의 수 + 3의 결과가 0인 구간합 수 = 답
#////////////////////////////////////////////////////////////#