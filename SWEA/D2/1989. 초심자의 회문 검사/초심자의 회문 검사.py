num_of_try = int(input())

for i in range(num_of_try):
    input_string = input().rstrip()
    result = 0

    for j in range (len(input_string) // 2 + 1) :
        if input_string[j] != input_string[-1-j]:
            break
        elif input_string[j] == input_string[-1-j] and j == len(input_string) // 2 :
            result = 1

    print("#%d %d" % (i + 1, result))