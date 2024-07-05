
a = int(input())
jum = list(map(int, input().split()))
M = max(jum)
total = 0

for i in range(a):
    total += (jum[i]/M*100)

print(total/a)