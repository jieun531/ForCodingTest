import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    print(a+b)

#////////////////////////////////////////////////////////////#
# 왜 있는지 모를 문제이지만 문제집 하나 완성 시키고 싶어서 품
# 입력받은 수 만큼 loop. loop 마다 입력 받아보고 느리면 다른 방법으로 풀기
#////////////////////////////////////////////////////////////#