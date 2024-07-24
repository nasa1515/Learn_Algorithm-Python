import sys


def backtraking():
    # dfs 안에는 무조건 종료 시점에 대한 코드를 입력
    if len(Stack) == M: #수열의 갯수가 3이면 출력을 Return
        print(*Stack)
        return
    
    # 대조 할 수열의 수 ex) N=1 , M=1, M=2, M=3
    for i in range(1, N+1):
        if Check[i]: 
            continue
        Check[i] = True
        Stack.append(i)
        backtraking()
        Check[i] = False
        Stack.pop()        




# N = 수열의 갯수
# M = 출력할 수열의 아규먼트
N, M = map(int, sys.stdin.readline().split())

# 빈 Stack 
Stack = []

# 제외할 값 (자기 자신의 숫자는 제외해야 함) - 중복 값 제거
Check = [False]*(N+1) #N 값이 즉 수열의 갯수에서 자기 자신을 나타냄

backtraking()