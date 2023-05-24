def fac(n):
    if n > 1 :
        return (n * fac(n-1))
    else :
        return 1

for _ in range(int(input())):
    west,east = map(int,input().split())
    bridge = (fac(east) // ( fac(west) * fac(east-west) ))
    print(bridge)