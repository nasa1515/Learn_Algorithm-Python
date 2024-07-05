
line = input().upper()
line_u = list(set(line))
cnt = []
for x in line_u:
    cnt.append(line.count(x))

if cnt.count(max(cnt)) > 2:
    print("?")
else:
    print(line_u[cnt.index(max(cnt))])