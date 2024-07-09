
arr = []
for _ in range(int(input())):
    count = int(input())
    if count == 0:
        arr.pop()
    else:
        arr.append(count)
        
print(sum(arr))

 