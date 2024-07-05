
N = []
max_value = 0

# 한 행 별로 리스트를 받아서 값 리스트의 MAX값을 저장
for i in range(9):
    new_list = list(map(int, input().split()))
    new_max = max(new_list)
    # 매 리스트의 MAX값과 기존 MAX 값을 비교해서 row, col 위치를 지정
    if new_max >= max_value:
        max_value = new_max
        max_row = i+1 
        max_col = new_list.index(max_value)+1
        
print(max_value)
print(max_row, max_col)
        