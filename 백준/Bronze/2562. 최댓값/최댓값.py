import sys
input = sys.stdin.readline

Max = 0
origin = []
s_origin = []

for i in range(9):
    origin.append(int(input()))

s_origin = sorted(origin)
Max = s_origin[-1]
print(Max)
print(origin.index(Max)+1)

#////////////////////////////////////////////////////////////#
# 본격 백준 레벨 올리기 프로젝트 : 브론즈5 없애기
# 리스트를 두 개로 나눠 저장하기 : 원본, sorted
# sorted의 [-1]를 받아와서 리스트.index(max값)
#////////////////////////////////////////////////////////////#