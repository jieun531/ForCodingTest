import sys
num_of_people = []
for _ in range(10) :
    num_of_people.append(list(map(int, sys.stdin.readline().split(' '))))
max_people = 0
current = num_of_people[0][1]

for i in range(1,10) :
    current -= num_of_people[i][0]
    current += num_of_people[i][1]
    if current > max_people :
        max_people = current

print(max_people)