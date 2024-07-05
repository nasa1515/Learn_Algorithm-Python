
import sys

N, M = map(int, sys.stdin.readline().split())

poket_idx = {}

for i in range(1, N+1):
    name = input().strip()
    poket_idx[name] = i
    poket_idx[i] = name
        
for _ in range(M):
    seach = sys.stdin.readline().rstrip()
    if seach.isdigit():
        print(poket_idx[int(seach)])
    else:
        print(poket_idx[seach])