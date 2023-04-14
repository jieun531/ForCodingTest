import sys
score = []
for i in range(8):
    score.append(int(sys.stdin.readline()))

sorted_score = sorted(score)
max_score = []

for _ in range(3):
    sorted_score.pop(0)
print(sum(sorted_score))
for i in range(5) :
    max_score.append(score.index(sorted_score[i]) + 1)

sorted_score = sorted(max_score)

for i in sorted_score :
    print(i, end = " ")