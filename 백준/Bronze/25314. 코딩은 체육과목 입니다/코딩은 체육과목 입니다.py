import sys
input = sys.stdin.readline

byte = int(input())

for i in range(byte // 4):
    print('long ', end='')
print('int')

#////////////////////////////////////////////////////////////#
# 왜 있는지 모를 문제이지만 문제집 하나 완성 시키고 싶어서 품
# 입력받은 byte를 몫 나누기 후 몫만큼 loop. loop 끝난 후 int 따로 출력
#////////////////////////////////////////////////////////////#