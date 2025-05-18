import sys
input = sys.stdin.readline

size, quest = map(int, input().split())
origin = [[0] * (size+1)]
sOO = [[0] * (size + 1) for _ in range(size+1)]

#구간합 초기 세팅 (sumOfOrigin = sOO)

for i in range(size):
    temp = list(map(int, input().split()))
    origin.append([0] + temp)

#/2차원 리스트 구간합 구하는 과정//////////////////////////////////////////////////////////////#
# 1. 가로 세로를 0으로 채운다.
# 2. 합 리스트 설정 : i-1행 j열 총합 + i행 j-1열 총합 - 중복되는 i-1행 j-1열 까지의 총합 + i행 j열
# 3. a열 b행:i열 j행 까지 합 = sOO[i][j] - sOO[a-1][j] - sOO[i][b-1] + sOO[a-1][b-1]
#//////////////////////////////////////////////////////////////////////////////////////////#

for i in range(1, size+1):
    for j in range(1, size+1):
        sOO[i][j] = sOO[i - 1][j] + sOO[i][j-1] - sOO[i-1][j-1] + origin[i][j]

for _ in range(quest):
    sr, sc, er, ec = map(int, input().split())
    print(sOO[er][ec] - sOO[sr-1][ec] - sOO[er][sc-1] + sOO[sr-1][sc-1])

#/모범 답안 비교//////////////////#
# append 한번에 해서 연산값 줄이기
# sum 연산 최대한 줄이기
#///////////////////////////////#