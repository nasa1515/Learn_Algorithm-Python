import sys

input = sys.stdin.readline

# Array 받기
array = [list(map(int, input().split())) for _ in range(int(input()))]

# x[0] index , [1] 인덱스 오름차순 정렬
sorted_array = sorted(array, key= lambda x: (x[0], x[1]))

# 이차원 배열 출력
print("\n".join(map(lambda x: f"{x[0]} {x[1]}", sorted_array)))