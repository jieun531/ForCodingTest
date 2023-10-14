#잔돈 = 낸 돈 - 가격
change = 1000 - int(input())

#잔돈 리스트 & 잔돈 매수 저장용 변수
money = [500, 100, 50, 10, 5, 1]
gae = 0

for i in money :
    gae = gae + (change // i)
    change = change % i

print(gae)