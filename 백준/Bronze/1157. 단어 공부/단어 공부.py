import sys
input = sys.stdin.readline

word = list(input().upper())
word.pop(-1)

count = [0] * 27
for i in word:
    count[ord(i) - 65] += 1

s_count = sorted(count)
maxV = s_count[-1]
if maxV == s_count[-2] :
    print('?')
else :
    print(chr(count.index(maxV)+65))

#////////////////////////////////////////////////////////////#
# 본격 백준 레벨 올리기 프로젝트 : 브론즈5 없애기
# 슬라이스 리스트 -> 같은 길이의 리스트로 값 대입 가능
# 문자 -> 숫자 : ord , 숫자 -> 문자 : chr
# 가장 큰 값이 2개 이상인 경우 = s_count[-1] == s_count[-2]
#////////////////////////////////////////////////////////////#