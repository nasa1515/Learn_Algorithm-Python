# 2차원 배열 형태의 100x100 빈 리스트 생성
arr = [[0] * 101 for _ in range(101)]

count = int(input())

# 색종이 갯수 만큼 루프
for _ in range(count):
    # 위아래, 양옆의 인풋
    LR, UD = map(int, input().split())
    # 행,열 = 색종이의 시작점 ~ 색종이의 크기(10)
    for col in range(LR, LR+10):
        for row in range(UD, UD+10):
            # 1로 치환
            arr[col][row] = 1

result = sum([sum(x) for x in arr])
print(result)

