# [BOJ 10815번: 숫자 카드](https://www.acmicpc.net/problem/10815)

## 문제 설명

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.  

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다  

## 출력

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.


### 예제 입력 1

```
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
```

### 예제 출력 1

```
1 0 0 1 1 0 0 1
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

## ✅ First Code (Hash - Dict())

```python3
import sys
from collections import defaultdict

input = sys.stdin.readline

first_num = int(input())
first_card = [item for item in map(int, input().split())] # 첫번째 검색할 숫자 입력 리스트 생성

second_num = int(input())
second_card = [item for item in map(int, input().split())] # 두번째 숫자 입력 리스트 생성

count_dict = defaultdict(int) 

for item in first_card: 
    count_dict[item] += 1 # 첫번째 숫자를 Key로 Default dict 생성

result_dict = defaultdict(int)

for item_2 in second_card: 
    result_dict[item_2] = count_dict[item_2] # 첫번째 숫자를 기록한 dict를 기준으로 최종 result dict의 key를 기록

print(*list(result_dict.values())) # result dict의 value만 출력
```

## ✅ Discription

문제의 로직은, 간단하게 처음 받은 문자의 집합이 두번 째 받은 문자의 집합안에 얼마나 포함되어 있는지를 합산하는 로직입니다.  
문제의 알고리즘을 구현하기 이전에 문제 속에서 아래와 같은 힌트를 얻을 수 있습니다. 

* 시간 제한 : 2초 
* N은 최대 500,000만, M은 -10,000,000 ~ 10,000,000 까지의 범위의 숫자일 수 있다.

위의 힌트들을 종합해보면, 결국 특정 문자들을 검색해야 하는 알고리즘을 구현해야합니다.  
그렇다면 검색 알고리즘 중 `해쉬 맵` 방식과 `순차 탐색`, `이진 탐색` 등 을 생각해볼 수 있습니다.  
하지만, `O(N)`의 시간복잡도를 가지고 있는 `순차 탐색`의 경우 `N = 100000`을 `M = 100000` 번 반복해서 찾아야 한다고 하면  
`O(N*M)`만큼의 시간 복잡도 즉 `O(100,000 * 100,000) = O(10,000,000,000)` 입니다.  
보통 평균적으로 Python에서 1억번의 수행마다 대략 1초 정도 걸린다고 예측하고 있으니, 단순히 계산해봐도 2초 안에는 불가능합니다.  

* 그래서 `HASH, Binary search` 두개로 구현해봤습니다. 

### dict 처리

* defaultdict() - 값이 없는 Key의 경우 기본 값으로 채워주는 함수입니다. int 형의 경우 기본 값은 0 입니다.  
* count_dict - 첫번재 문자열을 기준으로, Key - value에 1의 값을 넣어놓은 뒤  
* result_dict - 두번째 문자열을 기준으로 첫번째 dict에서 조회 후, Value 값을 넣어줍니다. 이때, 없다면 0이 들어가겠죠.

 

## ✅ Second Code (Binary Search)

```python3
import sys
from collections import defaultdict

input = sys.stdin.readline

def fun_binary_search(array, check, start, end):
    
    if start > end: # start 값이 end 보다 커지면 재귀 종료
        return False  # 값을 찾지 못했을 때 False 반환
    
    middle = (start + end) // 2 # 중간 값을 찾습니다. start = 1, end = 3, start + end = 4 // 2 = 2 
    
    if array[middle] == check: # 값을 찾았다면 = True 반환
        return True
    
    elif array[middle] < check: # check 값이 middle 보다 크다면
        return fun_binary_search(array, check, middle + 1, end) # 다음 재귀에서 검색 범위를 middle 보다 큰 값으로 이분
    
    else: # check 값이 middle 보다 작은 경우
        return fun_binary_search(array, check, start, middle - 1) # 다음 재귀에서 검색 범위를 middle 보다 작은 값으로 이분


if __name__ == "__main__":
    
    first_num = int(input())
    first_card = sorted([item for item in map(int, input().split())]) # 정렬 알고리즘 에서는 대상 수열은 항상 정렬되어야 합니다.

    second_num = int(input())
    second_card = [item for item in map(int, input().split())] # 두번째 검색 카드리스트르 입력값을 받습니다.

    for item in second_card: 
        if fun_binary_search(first_card, item, 0, len(first_card) - 1): # 각 검색 카드 항목마다 재귀 결과를 받아옵니다. 
            print(1, end = ' ')
        else: 
            print(0, end = ' ')
```

## ✅ Discription

이분 탐색의 경우 순차 탐색과는 다르게 O(log N)의 시간 복잡도를 가지기 때문에, 정상적으로 문제 해결이 가능합니다.  
간단한 로직 구현에는 `Check - 검색할 숫자, start - 시작점, end - 끝점` 세개의 변수가 필요합니다.   
탐색 알고리즘에는 무조건 적으로, 비교해야 할 인자가 정렬되어 있어야 하는 것이 기본 전제입니다. 
처음 `Binary search 함수에 인자는 초기 값을 기준으로 전달되고, 이후 재귀 호출이 되면서 값이 변하는 구조 입니다.`

* start - 시작 값이, end 값 보다 커지는 경우 -> 값을 찾기 못한 경우
* middle index의 값보다, middle(중간 값)이 크거나 작은 경우을 따져서, 검색 할 인덱스 범위를 이분하면서 좁혀가는 과정입니다.  
* 쉽게는 bisect() 모듈을 사용할 수도 있습니다.