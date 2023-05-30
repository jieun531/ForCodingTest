import sys

line_num = int(sys.stdin.readline())
bracket = []

for _ in range(line_num):
    bracket=0
    coupled = False
    putted = sys.stdin.readline().rstrip()

    for i in putted :
        if i == '(':
            bracket += 1
            coupled = False
        elif i == ')' and bracket > 0 :
            bracket -= 1
            coupled = True
        elif i == ')' and bracket == 0:
            coupled = False
            break

    if coupled and bracket == 0:
        print('YES')
    else :
        print("NO")