test_case = int(input())

for i in range(test_case):
    num_a, num_b = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dif = num_b - num_a #a가 더 짧은 문자열이 되도록 설정
    if dif < 0 :
        temp = a
        a = b
        b = temp
        dif = abs(dif)
        num_a = len(a)
        num_b = len(b)
    mul_max = []
    m_mul = []

    for j in range(dif+1):
        mul_max.clear()
        for k in range(num_a):
            mul_max.append(a[k]*b[k])
        m_mul.append(sum(mul_max))
        b.pop(0)


    print("#%d %d" % (i+1, max(m_mul)))