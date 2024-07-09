import sys

a,c = map(int, sys.stdin.readline().split())

b = [0]*a

for _ in range(c):
     i,j,k = map(int, sys.stdin.readline().split())
     for x in range(i, j+1):
         b[x-1] = k

print(*b)