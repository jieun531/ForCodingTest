num_of_try = int(input())

for i in range(num_of_try):
    input_string = input()
    result = 0

    for j in range (1, 15):
        s = input_string[0:j]
        if s == input_string[j:2*j]: #바로 다음에 이어지는 문자열과 비교
            result = len(s)
            break
    print("#%d %d" % (i + 1, result))
