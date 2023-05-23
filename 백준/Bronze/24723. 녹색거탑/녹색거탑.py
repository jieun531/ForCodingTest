def fac(num):
    answer = 2
    if num == 1:
        return answer
    else :
        return answer * fac(num-1)

print(fac(int(input())))