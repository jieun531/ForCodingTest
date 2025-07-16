import sys
input = sys.stdin.readline

p_total = int(input())
cate = int(input())
r_total = 0

for i in range(cate):
    cost, num = map(int, input().split())
    r_total+= cost*num

if r_total == p_total :
    print('Yes')
else:
    print(('No'))


#////////////////////////////////////////////////////////////#
# 왜 있는지 모를 문제이지만 문제집 하나 완성 시키고 싶어서 품
# 가짓 수만큼 입력받아 실제 토탈값 쪽에 저장
# loop 끝난 후 인쇄 토탈과 실제 토탈 비교 후 출력
#////////////////////////////////////////////////////////////#