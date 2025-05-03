inputted = []

while True :
    try:
        inputted.append(int(input()))
    except:
        break
        
for a in inputted :
    i = 1
    while i:
        if i % a != 0 :
            i = i * 10 + 1
            continue
            
            # i = 1 로 설정하고 배수가 아닐 때마다 i * 10 + 1해서 재진행
            # i = a 후 i += a 할 경우 시간 손실이 너무 컸음
            
        else:
            break

    print(len(str(i)))


