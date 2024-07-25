
check_list = [8, 3, 5, 19, 23, 24]

def quick_sort(value: list[int]) -> list[int]:
    
    if len(value) <= 1:
        return value
    pivot = value[0]
    left = [x for x in value[1:] if x <= pivot]
    right = [x for x in value[1:] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(check_list))
