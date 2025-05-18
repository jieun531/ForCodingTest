import sys

length, quest = map(int, sys.stdin.readline().split(' '))
origin = list(map(int, sys.stdin.readline().split(' ')))
listOfSum = [0]
#0번째 index에 0을 미리 저장해 놓음 으로써 구간합 사용 가능
temp = 0

for i in origin:
    temp += i
    listOfSum.append(temp)

for i in range(quest):
    start, end = map(int, sys.stdin.readline().split(' '))
    print(listOfSum[end] - listOfSum[start-1])

#//////////////////////////////////////////////////////////#
# 모범 답안 비교                                             #
# readline 함수가 길고 자주 쓰임                              #
#  - input= sys.stdin.readline overwrite 후 input 사용      #
#//////////////////////////////////////////////////////////#