import itertools

arr = [int(input()) for _ in range(9)]

for items in itertools.combinations(arr, 7):
    if sum(items) == 100:
        print("\n".join(str(x) for x in sorted(items)))
        break


    
     