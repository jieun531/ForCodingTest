height = [int(input()) for i in range(0,9)]         #입력받아 list로 저장
height.sort()                                       #오름차순 정리

gap = sum(height) - 100                             #두 키의 합이 gap과 같으면 pop하기

for i in range(0,8) :
    for j in range(i,9) :
        if height[i]+height[j] == gap :
            height.pop(j)
            height.pop(i)
            break
    if len(height) == 7 :
        break


for i in height :
    print(i)