# 문자 받기
words = [input().rstrip() for i in range(5)]

# 세로 읽기 문자를 저장 할 빈 리스트
new = []

max_len = max(len(word) for word in words)
# words 문자열 리스트 중 가장 길이가 긴 리스트 만큼
for i in range(max_len):
    # 읽을 Col
    for j in range(5):
        # 조건 : 0번 부터 읽는데 만약, j의 인덱스에 값이 없으면 0
        if i < len(words[j]):
            new.append(words[j][i])
            
print(''.join(new))

