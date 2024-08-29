# [BOJ 10989번: 수 정렬하기 3](https://www.acmicpc.net/problem/10989)

## 문제 설명

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


### 예제 입력 1

```
10
5
2
3
1
4
2
3
5
1
7
```

### 예제 출력 1

```
1
1
2
2
3
3
4
5
5
7
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


## ❌ Firsy incorrect Solution Code

```python3
import sys

input = sys.stdin.readline


N = int(input())

array = [int(input()) for _ in range(N)]

print(*sorted(array))
```

문제를 제대로 안읽고, Bronze 문제이길래, `Sorted` 함수로 구현했는데  
바로 메모리 초과 이슈로 실패... 다시 문제를 차근차근 읽어서, 아래와 같이 성공했습니다.  

<br/>

## ✅ Solution Code

```python3
import sys

input = sys.stdin.readline

# N의 입력 값 받기
N = int(input())

# 계수 정렬을 위한 가능 범위 만큼의 Empty Array 공간 생성 
array = [0] * (10000 + 1)

# 계수 정렬을 위해 array의 size 만큼의 Loop 실행
for _ in range(N):
    array[int(input())] += 1 # array의 입력값에 해당하는 index number에 +1 

# array에 저장되어 있는 value를 기반으로 출력
for index in range(len(array)):
    if array[index] != 0: # index가 0이 아닌 경우
        for _ in range(array[index]): # index의 value 만큼 loop로 출력
            print(index) 
```

## ✅ Discription

`계수 정렬` 알고리즘 방식을 안다면 쉽게 해결이 가능합니다.     
단순하게, Python으로 Array list에서 `sorted()` 함수로 시간초과, 메모리초과의 경우 선택, 버블, 퀵 정렬로도 해결이 불가능 한 경우 입니다.  
조금 더 구체적으로 지금 문제 같이 특정 숫자의 범위가 정해져 있는 경우, 계수 정렬 - `dict`로 해결하는 방식이 가장 빠릅니다.  

우선 계수 정렬 구현을 위해, 문제에서 주어진 숫자의 범위 = `10,000` 만큼의 bin array 공간을 생성합니다. 

```python3
array = [0] * (10000 + 1)
```
array [0 ,0, 0, 0,......] 10001개의 인덱스를 생성합니다.  

<br/>

입력 값 (input)을 받을 때 마다, 그에 해당하는 index에 +1을 추가합니다.  
```python3
for _ in range(N)
    array[int(input())] += 1    
```
1, 1, 2, 2, 3, 3, 1 을 차례로 입력 받았다고 가정하면, 1은 총 3개, 2는 2개, 3도 2개로 `array[0,3,2,2]` 가 저장됩니다.  

<br/>

입력 저장이 끝난 뒤, 저장된 index 중 0 = `입력이 없던 것`을 제외하고, value 만큼 출력해주면 됩니다.  

```python3
    if array[index] != 0: # index가 0이 아닌 경우
        for _ in range(array[index]): # index의 value 만큼 loop로 출력
            print(index) 
```
