
T = int(input())

# T 만큼 반복 O(N)
# T의 문자열 갯수 만큼 +
# O(2N)

for _ in range(T):
    stack = []
    words = input()
    for item in words:
        if item == "(":
            stack.append(item)
        elif item == ")":
            if stack:
                stack.pop()
            else:
                stack.append(item)
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else: 
            print("YES")
            
