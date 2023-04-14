import sys
a = list(sys.stdin.readline().rstrip())
a.sort(reverse=True)
a = list(map(int,a))
rev_a = a[len(a)-1]
for i in range(1, len(a)):
    rev_a += (10 ** i) * a[-i-1]
print(rev_a)