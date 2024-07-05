import sys

def backtracking(start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start, N+1):
        if check[i]:
            continue
        result.append(i)
        check[i] = True
        backtracking(i + 1)
        check[i] = False
        result.pop()
    
result = []
N,M = map(int, sys.stdin.readline().split())
check = [False for _ in range(0, N+1)]

backtracking(1)