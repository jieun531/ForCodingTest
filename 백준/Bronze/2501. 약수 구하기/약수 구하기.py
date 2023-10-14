big, num = map(int, input().split())

#지금까지 구한 약수의 갯수
n_of_yak = 0
#n번째 약수 or 0 저장용
yak = 0                
for n in range(1, big+1):
    if big % n == 0 :
        # 약수 총 갯수 1 증가
        n_of_yak += 1

        # num>1 조건 추가
        if n_of_yak == num and n_of_yak >= 1: 
            yak = n
            break

print(yak)