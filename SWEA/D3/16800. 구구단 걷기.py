"""
import sys
num_of_try = int(sys.stdin.readline().rstrip())
for tries in range(1,num_of_try+1) :
    moves = 0
    num_move = int(sys.stdin.readline().rstrip())
    mini = num_move - 1

    for j in range(1, int(num_move ** 0.5)):
        if (num_move % j == 0) and mini > (j - 1) + (num_move // j - 1) > 0 :
                mini = (j - 1) + (num_move // j - 1)


    print("#%d %d" % (tries, mini))
#입력방식 sys.stdin.readline()으로 구현했을 때
"""

num_of_try = int(input())
for tries in range(1,num_of_try+1) :
    moves = 0
    num_move = int(input())
    mini = num_move - 1
    j = 1
    for j in range(1, int(num_move ** 0.5)):
        if (num_move % j == 0) and mini > (j - 1) + (num_move // j - 1) > 0 :
                mini = (j - 1) + (num_move // j - 1)
    if j >= int(num_move ** 0.5) and mini > num_move - 1 :
        mini = num_move - 1

    print("#%d %d" % (tries, mini))
