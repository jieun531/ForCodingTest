import sys
input = sys.stdin.readline

K = int(input())
claList = []
for i in range(K):
    claList.append(list(map(int, input().split())))

maxV = 0
minV= 0
MaxGap = 0

for i in range(K):
    T = claList[i]

    myong = T.pop(0)
    T.sort(reverse=True)
    #학생들의 성적만 남기기


    maxV = T[0]
    minV = T[-1]
    MaxGap = 0

    for j in range(0, myong-1):
        curGap = T[j] - T[j+1]

        if MaxGap < curGap :
            MaxGap = curGap

    print("Class %d" % (i+1))
    print("Max %d, Min %d, Largest gap %d" % (maxV, minV, MaxGap))


#////////////////////////////////////////////////////////////#
# 일단 생각나는 대로 코딩
# 사용 알고리즘은 선형탐색(not sure)
#////////////////////////////////////////////////////////////#