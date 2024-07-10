import sys

N = sys.stdin.readline()
SANGGEN = sorted(list(map(int, sys.stdin.readline().split())))

M = sys.stdin.readline()
CARD_LIST = list(map(int, sys.stdin.readline().split()))

dic = {}

for check_card in SANGGEN:
    if check_card in dic:
        dic[check_card] += 1
    else:
        dic[check_card] = 1

for check_card in CARD_LIST:
    if check_card in dic:
        print(dic[check_card], end=' ')
    else:
        print('0', end=' ')