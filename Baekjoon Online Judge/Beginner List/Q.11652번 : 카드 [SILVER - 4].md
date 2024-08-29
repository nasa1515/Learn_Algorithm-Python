# [BOJ 11652번: 카드](https://www.acmicpc.net/problem/11652)

## 문제 설명

준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.  

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.  

## 입력

첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.


## 출력

첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.



### 예제 입력 1

```
5
1
2
1
2
1
```

### 예제 출력 1

```
1
```

### 예제 입력 2

```
6
1
2
1
2
1
2
```

### 예제 출력 2

```
1
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
from collections import defaultdict

input = sys.stdin.readline

N = int(input())  

# Key의 기본 값을 0으로 설정하는 dict 생성
array = defaultdict(int)

# 각 index가 발견되면, +1 
for _ in range(N):
    array[int(input())] += 1

# 문제의 조건에 맞게, 정렬 및 출력
print(sorted(array.items(), key=lambda x: (-x[1], x[0]))[0][0])
```

## ✅ Discription

처음에는 `계수 정렬` 알고리즘 방식을 생각했지만, 문제의 조건에 `음수 ~ 양수` 까지의 카드 숫자가 존재, 양수만 가능한 `계수 정렬은 제외`
문제에서 아래와 같은 조건을 토대로, dict로 단순 구현아면 될 것이라고 생각해서 구현했습니다.  

* 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다. -> 단순 loop로는 시간 제한, 메모리에 맞출 수 없으므로, `HASH` 구현이 필요.
* 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다. -> dict의 items 혹은 value의 비교 후, key 값을 오름차순으로 정렬해야한다.  

```python3
array = defaultdict(int)
```
defaultdict로 0의 기본 값을 가진 array list를 생성합니다.   

<br/>

입력 값 (input)을 받을 때 마다, 그에 해당하는 index에 +1을 추가합니다.  
```python3
for _ in range(N)
    array[int(input())] += 1    
```
1, 1, 2, 2, 3, 3, 1 을 차례로 입력 받았다고 가정하면, 1은 총 3개, 2는 2개, 3도 2개로 `array[0,3,2,2]` 가 저장됩니다.  

<br/>

입력이 끝난 뒤, 출력 조건에 맞춰 정렬합니다. `lambda 식을 사용`

```python3
print(sorted(array.items(), key=lambda x: (-x[1], x[0]))[0][0])
```

* array.items() : array의 key:value 형태의 데이터를 꺼내 올 수 있습니다. 
* key=lambda x: (-x[1], x[0]) : x 값을 뒤의 수식에 맞게 x[1] : value 로 내림차순, x[0]: key로 오름차순 정렬
* [0][0] : 정렬이 끝난 뒤, 튜플의 가장 맨 앞 데이터를 출력합니다. 