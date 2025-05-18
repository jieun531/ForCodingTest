import sys
input = sys.stdin.readline

row = int(input())
upList = [0] * 10001
for _ in range(row):
    num = int(input())
    upList[num] += 1

for i in range(10001) :
    if upList[i] > 0:
        for _ in range(upList[i]) :
            print(i)

#////////////////////////////////////////////////////////////#
# 단순 입력받아 정렬 = 메모리 초과
# 생각한 방법 = [0] * 최대값 리스트 만들고 i 입력 시 i열에 +1 하고
# 출력 시 1 이상인 i 인덱스 들만 저장된 값만큼 i 출력하기
#////////////////////////////////////////////////////////////#