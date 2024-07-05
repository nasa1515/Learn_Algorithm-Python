
r_list = []

for _ in range(10):
    a = int(input())
    r_list.append(a % 42)

print(len(set(r_list)))
    
