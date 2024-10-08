# 리스트에서 두 수의 합이 Target 값인 수

check_list = [1, 2, 3, 4, 5]
target = 4

def target_search(check: list[int], target) -> list[int]:
    # hash 검색 할 딕셔너리 생성
    hash_dict = {}
    for i in range(len(check)):
        if target - check[i] not in hash_dict:
            hash_dict[check[i]] = i
        else:
            return [check[hash_dict[target - check[i]]], check[i]]


print(target_search(check_list, target))