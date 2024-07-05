import sys

# N 카드 입력
N = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

# M 카드 입력
M = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

arr = {}

# 시간 복잡도 O(n)
for n_words in n_list:
    if n_words in arr:
        arr[n_words] += 1
    else:
        arr[n_words] = 1

for m_words in m_list:
    if m_words in arr:
        print(arr[m_words], end=" ")
    else:
        print('0', end=" ")

