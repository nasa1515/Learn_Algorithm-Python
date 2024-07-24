import itertools

P_list = [int(input()) for _ in range(9)]


for i in itertools.combinations(P_list, 7):
    print(i)