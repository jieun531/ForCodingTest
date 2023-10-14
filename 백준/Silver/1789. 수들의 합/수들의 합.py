num = int(input())

#자연수 개수 저장
n_of_nums = 0
for i in range(1, num+1):
    if num >= i :
        num -= i
        n_of_nums += 1
    else:
        break

print(n_of_nums)