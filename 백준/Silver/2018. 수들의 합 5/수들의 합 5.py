N = int(input())

sum = 1
start_ind = 1
end_ind = 1
count = 1                   #자기 자신 제외용

while end_ind != N:
    if sum > N :
        sum -= start_ind
        start_ind += 1

    elif sum < N :
        end_ind+=1
        sum += end_ind

    else :
        count+=1
        end_ind+=1
        sum += end_ind

print(count)


#////////////////////////////////////////////////////////////#
# two-pointer 통해 구하기
# start end 포인터 만들고 지금까지 구해온 sum 값에 end 값 더하거나 start 값 빼서 비교하기
# sum > 준 수 : 넘친다. sum에서 기존 start 빼기 start++
# sum = 준 수 : 찾던것! end++
# sum < 준 수 : 모자라다. end++ sum에 end더하기
# 리스트 입력 -> 구간합 리스트 -> 구간합을 M으로 나눈 나머지 리스트 -> 주어진 경우의 수 + 3의 결과가 0인 구간합 수 = 답
#////////////////////////////////////////////////////////////#