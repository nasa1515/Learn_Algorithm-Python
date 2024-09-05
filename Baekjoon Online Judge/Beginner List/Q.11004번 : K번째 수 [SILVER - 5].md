# [BOJ 11004번: K번째 수](https://www.acmicpc.net/problem/11004)

## 문제 설명


수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

## 입력  

첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

## 출력

A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.


### 예제 입력 1

```
5 2
4 1 2 3 5
```

### 예제 출력 1

```
2
```



---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## ✅ Solution Code

```python3
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

array = sorted(list(map(int, input().split())))

print(array[K-1])
```

## ✅ [내부 함수 sort(), sorted() 를 사용] Discription

가장 첫번째 풀이로는 Python 내부 함수에 존재하는 `sort`, `sorted`를 사용한 풀이입니다.  
굉장히 간단하게 풀이가 가능하고, 따로 sorted의 로직을 알지 못해도, 구현이 가능한 python의 장점이 담겨있습니다.  

<div align="center">

  ### [문제를 풀기위한 요구조건은 무엇일까?]

</div>

<br/>
<br/>

알고리즘 풀이를 위해서 필수적으로 완수해야 할 요건을 아래와 같습니다. 

1. 시간 제한, 메모리 제한이 존재하는데, N의 최대 범위 즉 array 안에 존재하는 element의 범위가 5,000,000 까지이다.
    *  알고리즘의 시간복잡도가 `O(n2)`이 되는 순간, 곧바로 1억 이상의 동작이 필요해집니다. 

2. 즉 (1)의 시간복잡도를 계산했을 때, `O(n log n)`에 해당하는 정렬 알고리즘만 사용이 가능합니다.  
    * python의 sort, sorted는 모두 `O(n log n)`을 지원합니다.  

<br/>

그럼 이제 근본적인 알고리즘으로 넘어가서, 실제 정렬 알고리즘 중 현재 문제에 가장 알맞는 형태가 어떤 것인지 확인해봐야 합니다.   
최악의 경우에도 `O(n log n)`의 시간복잡도는 지원하는 경우는 `MERGE SORT, Heap Sort` 두개 밖에 없습니다.  
Quick_sort의 경우 최악의 경우 `O(n2)`가 가능하기에 정렬로서는 제외해야합니다. (실제로 시간초과...)  


<br/>

## ✅ [Quick-Select] Solution Code

```python3
import sys

def quick_select(arr, start, end, K):
    if start <= end:
        pivot_index = partition(arr, start, end)
        if K == pivot_index:
            return arr[K]
        elif K < pivot_index:
            return quick_select(arr, start, pivot_index - 1, K)
        else: 
            return quick_select(arr, pivot_index + 1, end, K)
        
def partition(arr, start, end):
    pivot_index = (start + end) // 2
    pivot_value = arr[pivot_index]
    _swap(arr, start, pivot_index)
    left = start + 1
    right = end
    
    while left <= right:
        while left <= right and arr[left] < pivot_value:
            left += 1
        while left <= right and arr[right] > pivot_value:
            right -= 1
            
        if left <= right:
            _swap(arr, left, right)
            left += 1
            right -= 1

    _swap(arr, start, right)
    return right

def _swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

if __name__ == "__main__":

    inputs = sys.stdin.readline
    n, k = map(int, inputs().split())
    arr = list(map(int, inputs().split())) 
    result = quick_select(arr, 0, len(arr)-1, k-1)
    print(result)
```


## ✅ [Quick-Select] Discription

위에서 말한 `Quick-sort`의 변형 알고리즘 입니다. 어찌보면 지금의 문제와 가장 적합한 형태의 알고리즘이라고 할 수 있습니다.  
간단하게 요약하자면, 중간 `pivot` 값을 구한 뒤, 해당 `pivot` 값보다 작은 값은 `left` 영역에, 큰 값은 `right` 영역으로 `swap`해서  
최종적으로 찾아야 할 index의 위치와 `pivot`의 위치를 비교해서, 전체 arr를 확인하는 것이 아닌, 반씩 쪼갠 Index에서만 찾는 방식입니다.  

<div align="center">

![image](https://github.com/user-attachments/assets/2c9b22e6-0848-4a1d-9856-791fd7416c28)  

</div>

위의 그림을 보면 이해가 쉬운데, pivot 값을 기준으로 정렬한 뒤, pivot 위치를 기준으로 다시 확인 할 array index range를 정하게 됩니다.  

추가적 자세한 로직의 설명은 제 블로그 글을 참고 부탁드립니다.

<br/>
<br/>
<br/>
<br/>
<br/>


## ✅ [Quick-Select] Pythonic Solution Code

```python3
import sys
import random

def q_select(arr:list[int], K:int):
    
    if len(arr) == 1:
        return arr[0]
        
    pivot = random.choice(arr)
    left =  [x for x in nums if x > pivot]
    mid  =  [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]
        
    if K <= len(left):
        return q_select(left, K)
    elif K <= len(left) + len(middle):
        return pivot
    else: 
        return q_select(right, k - len(left) - len(middle))        


if __name__ == "__main__":

    inputs = sys.stdin.readline
    n, k = map(int, inputs().split())
    arr = list(map(int, inputs().split())) 
    result = q_select(arr, k)
    print(result)
``` 

## ✅ [Quick-Select] Discription

위와 로직은 동일합니다. 다만 arr안에 담겨있는 element들을 비교하는 `partions` 함수에 대한 부분을 list comprehension 으로 구현했습니다.
결론적으로 가장 중요한 부분은, K 라는 index의 위치와 array list의 len = element 갯수를 이용해서 targer index를 구하는 로직입니다.  

* 먼저 숫자의 피벗 및 분할요소를 피벗보다 작거나, 같거나, 큰 세부분으로 선택합니다. (이분되서 종료가 가능)
* 다음으로는 각 그룹 (list) 별로 몇개의 원소가 존재하는지 살펴봅니다 (len)
* 가장 작은 것, 작은것 + 같은것 / 두가지 조건으로 찾아야 하는 인덱스와 비교해보면, 그 길이보다 작으면 왼쪽, 크면 오른족에 해당 인덱스가 존재합니다.  

<br/>
<br/>
<br/>
<br/>
<br/>


## ✅ [Merge-Sort] Solution Code

```python3
import sys

def merge_sort(arr:list[int]) -> None:
    
    if len(arr) <= 1: # 배열의 크기가 1이 될 경우 재귀 종료
        return
    
    L_ARR = arr[:len(arr)//2] # 왼쪽 배열은 중간 값 이전 값
    R_ARR = arr[len(arr)//2:] # 오른쪽 배열은 중간 값 이후 값
    
    merge_sort(L_ARR) # 재귀를 실행시켜 각 인자가 1개씩으로 분할
    merge_sort(R_ARR) # 재귀를 실행시켜 각 인자가 1개씩으로 분할
    
    L_index, R_index, merge_index = 0, 0, 0
    
    while L_index < len(L_ARR) and R_index < len(R_ARR):
    
        if L_ARR[L_index] < R_ARR[R_index]:
            arr[merge_index] = L_ARR[L_index]
            L_index += 1
        else:
            arr[merge_index] = R_ARR[R_index]
            R_index += 1
            
        merge_index += 1

    while L_index < len(L_ARR):
        arr[merge_index] = L_ARR[L_index]
        L_index += 1
        merge_index += 1
    
    while R_index < len(R_ARR):
        arr[merge_index] = R_ARR[R_index]
        R_index += 1
        merge_index += 1
        
if __name__ == "__main__":
    
    input = sys.stdin.readline
    
    N, K = map(int, input().split()) ## N , K 에 해당하는 입력 값 받기
    arr = list(map(int, input().split())) # arr 받기
    
    merge_sort(arr) # arr를 merge sort
    print(arr[K-1])
```

## ✅ [Merge-Sort] Discription

두번째의 정답인 `Quick-select`로 구현한 정확한 이유는 `Quick-Sort`로는 시간초과가 발생했기 때문입니다.  
그럴수 밖에 없는게, `Quick-sort`의 최악의 시간 복잡도는 `O(n2)`이기 때문에, 단순히 `Quick-select`로 구현해 `O(nlogk)`로 그 시간복잡도를 줄였을 뿐입니다.  
`Merge-sort`의 경우, Array안의 정렬 상태가 어떻든, 최악의 경우에도 `O(nlogn)`의 시간 복잡도를 지원하기 때문에, 이번 문제에서는 `Merge sort`가 더 적합합니다.      

따로 블로그에, 병합 정렬에 대해서 자세하게 로직 설명을 할 예정이라 문제 풀이에서는 간단하게 설명하겠습니다.  

간단하게 병합 정렬은 각 리스트의 인자들의 크기가 1이 될때 까지 분할한 뒤에, 1로 나뉘어진 인자들 끼리 비교해서 정렬하는 로직입니다.  

* 먼저 `merge_sort()` 함수에 전달된 리스트를 기준으로 `left, right` 리스트 반씩 분할해, 1개의 인자가 남을 때 까지 `Recursive` 합니다.  
* 1개의 인자가 남은 리스트 (left, right)는 아래 while의 조건에 따라서 병합됩니다. 
    * Pointer 2개로 left, right의 index를 비교해가면서 더 작은 value를 우선적으로 삽입하며 정렬합니다.  
    * 최종적으로는 ex) 4 1 2 3 5 의 경우 [1 2 4] [3 5] 두개가 pointer로 비교되면서 [1 2 3 4 5]로 정렬됩니다.

