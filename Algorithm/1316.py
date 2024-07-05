
loop = int(input())
group_cnt = loop

for _ in range(loop):
    work = input()
    for i in range(len(work)-1):
        if work[i] == work[i+1]:
            pass
        elif work[i] in work[i+1:]:
            group_cnt -= 1
            break
        
print(group_cnt)