

for _ in range(int(input())):
    words = input().split()
    for i in words:
        print(i[::-1], end=' ')
        