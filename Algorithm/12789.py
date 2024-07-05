import sys

N = int(input())

s_list = list(map(int, sys.stdin.readline().split()))
stack = []
target = 1

for s in s_list:
    stack.append(s)
    
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    
else: 
    if stack:
        print("Sad")
    else: 
        print("Nice")
