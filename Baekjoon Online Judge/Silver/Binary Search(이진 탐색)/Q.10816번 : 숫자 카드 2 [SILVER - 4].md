# [BOJ 10816번: 숫자 카드 2](https://www.acmicpc.net/problem/10816)

## 문제 설명

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.  

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다  

## 출력

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

### 예제 입력 1

```
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
```

### 예제 출력 1

```
3 0 0 1 2 0 0 2
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

## ✅ First Code (Hash + Binary Search)

```python3
import sys
import bisect 
from collections import defaultdict
input = sys.stdin.readline

def binary_Search(array, value, start, end):
    
    if start > end: # 시작점이 끝점보다 커지면 0을 반환
        return 0
    
    middle_value = (start + end) // 2 # 시작점 + 끝점을 반으로 나눈 몫을 중간값을오 계산
    
    if array[middle_value] == value: # 중간 값과 찾을 값이 동일하다면 
        return result_dict.get(value) # 계산 된 hash에서 값을 꺼내 Return
        
    elif array[middle_value] < value: # 중간 값보다 작다면
        return binary_Search(array, value, middle_value +1, end) # 시작 점을 중간 값 + 1로 재귀 호출
    
    else: # 중간 값 보다 크다면 
        return binary_Search(array, value, start, middle_value - 1) # 끝점을 중간 값 -1로 재귀 호출
        
    
if __name__ == "__main__":
    
    N = int(input())
    N_cards = sorted(list(map(int, input().split())))

    M = int(input())
    M_cards = list(map(int, input().split()))

    
    result_dict = defaultdict(int) # 해시 값을 저장할 기본 해시 생성
    
    for value in N_cards:
        result_dict[value] += 1 # 해시에 값이 있으면 Value를 1씩 추가합니다.

    for item in M_cards:
        print(binary_Search(N_cards, item, 0, len(N_cards) - 1), end = ' ') # 이진 탐색 후, 결과 출력
```

## ✅ Discription

이전에 풀었던 [`BOJ 10815. 숫자 카드 [SILVER - 5]`](https://github.com/nasa1515/Learn_Algorithm-Python/blob/main/Baekjoon%20Online%20Judge/Silver/Binary%20Search(%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89)/Q.10815%EB%B2%88%20%3A%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C%20%5BSILVER%20-%205%5D.md)와 거의 동일한 유형의 문제입니다.  
해당 문제에서는 단순히 찾을 값의 존재 여부에 따라서, `0 or 1`로 나타내는 출력 형태 였다면, 이번 문제에서는 실제로 문자열 리스트안에서 해당 값의 `Count`를 세서 출력하는 문제입니다.  

* 결론적으로, 실제 이분 탐색 알고리즘에서 Return의 범위를 `True or False`에서 해당 인자의 갯수로 확장해야 합니다.  

### HASH 처리

* hash() - N_cards의 인자 별로 Value Count를 1씩 증가시켜 최종 인자 별 개수를 계산한 dict를 생성합니다.
* 이후 이분 탐색 함수에서 `array[middle_value] == value` 값을 찾았을 경우, 해당 Hash의 Key의 Value를 가져오는 방식입니다.


<br/>

## ✅ Second Code (Bisect Module 사용)

```python3
import sys
import bisect # Modeul import
input = sys.stdin.readline

def bisect_counter(array, value):
    
    left_index = bisect.bisect_left(array, value) # 해당 인덱스의 가장 왼쪽 위치 반환
    right_index = bisect.bisect_right(array, value) # 해당 인덱스의 가장 오른쪽 위치 반환
    
    return right_index - left_index # 오른쪽 - 왼쪽 = 해당 인자의 개수
    
if __name__ == "__main__":
    
    N = int(input())
    N_cards = sorted(list(map(int, input().split())))

    M = int(input())
    M_cards = list(map(int, input().split()))

    for item in M_cards:
        print(bisect_counter(N_cards, item), end=' ') # 개수 카운터 함수 호출
```

## ✅ Discription

Python 내장 모듈인 `Bisect`모듈을 사용해서 풀이해봤습니다. 
* [참고](https://docs.python.org/ko/3.7/library/bisect.html)

`Bisect` 모듈은 첫번째 인자로, Array를 받고, 두번째 인자로 목적 값을 받습니다.  
최종적으로 `bisect_right, bisect_left, bisect` 등의 내장함수로 해당 인자값이 정렬적으로 삽입 될 경우 몇번째 인덱스 위치에 있어야 하는지 인덱스 위치를 반환해줍니다.  
따라서 위의 경우, 만약 10이 3개가 있다면, 10이 삽입 될 수 있는 가장 왼쪽의 인덱스와 10이 삽입 될 수 있는 가장 오른쪽 인덱스의 차를 구하면, 현재 Array 안에 10이 몇개 있는디 인덱스의 차를 통해서 계산할 수 있게됩니다. 



<br/>

## ✅ Second Code (Counter 사용)

```python3
iimport sys
import bisect 
from collections import Counter # Counter 호출
input = sys.stdin.readline

    
if __name__ == "__main__":
    
    N = int(input())
    N_cards = list(map(int, input().split()))

    M = int(input())
    M_cards = list(map(int, input().split()))

    count_ = Counter(N_cards) # Counter Dict 생성
    
    for item in M_cards:
        if item in count_: # Counter Dict에서 값을 찾아서 출력
            print(count_.get(item), end = ' ')
        else:
            print(0 , end = ' ')

```

## ✅ Discription

Python 내장 모듈인 `collections 의 Counter`모듈을 사용해서 풀이해봤습니다. 
* [참고](https://docs.python.org/ko/3/library/collections.html)

`collections의 Counter` 모듈의 경우, Array를 집어 넣으면, 해당 Array의 인자 갯수를 자동으로 계산한 `Dict()`를 반환합니다.   
따라서 최종적으로, 해당 `Dict()`안에 검색할 인자가 포함되어 있는지만 확인하면 가장 쉽고 간단한 코드로 구현이 가능합니다.
