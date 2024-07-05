import sys

N,M = map(int, sys.stdin.readline().split())


hear = set(input().strip() for _ in range(N))
see = set(input().strip() for _ in range(M))
result = []

for items in see:
    if items in hear:
        result.append(items)

print(len(result))
print(*sorted(result), end=" ")