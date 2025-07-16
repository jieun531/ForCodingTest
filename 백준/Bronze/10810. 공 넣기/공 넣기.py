import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * (N+1)

for a in range(M) :
    i, j, k = map(int, input().split())
    basket[i:j+1] = [k] * (j-i + 1)

for a in basket[1:]:
    print(a, end=' ')

#////////////////////////////////////////////////////////////#
# 본격 백준 레벨 올리기 프로젝트 : 브론즈5 없애기
# 슬라이스 리스트 -> 같은 길이의 리스트로 값 대입 가능
#////////////////////////////////////////////////////////////#