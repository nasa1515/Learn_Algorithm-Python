
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]


def search_fun(arr, target):
    
    start = 0
    end = len(arr) - 1
    
    while (start<=end):
        
        mid_idx = (start+end)//2
    
        if arr[mid_idx] == target:
            return arr[mid_idx]
        elif arr[mid_idx] > target:
            end = mid_idx - 1
        elif arr[mid_idx] < target:
            start = mid_idx + 1
        
    return print("수 없음")
    
    
    

print(search_fun(m_list, 30))