# [BOJ 2738번: 행렬 덧셈](https://www.acmicpc.net/problem/2738)

## 문제

N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

## 입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.


## 출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

### 예제 입력 1

```
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
```

### 예제 출력 1

```
4 4 4
6 6 6
5 6 100
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

N, M = map(int, input().split()) # N, M 입력값을 받습니다.  

A_array = [list(map(int, input().split())) for _ in range(N)] # 첫번째 행렬의 이차원 리스트를 생성합니다.
B_array = [list(map(int, input().split())) for _ in range(N)] # 두번째 행렬의 이차원 리스트를 생성합니다.

for x in range(N): # N개의 줄 만큼의 For loop
    sum_ = [] # 합 리스트 초기화
    for y in range(M):
        sum_.append(A_array[x][y] + B_array[x][y]) # 첫번째, 두번째 행렬의 동일한 index를 더한 값을 넣습니다. 
    print(*sum_)
```

## ✅ Discription  

2차원 리스트 구조의 두개의 행렬이 존재할 때 각각 동일한 위치를 가진 Index의 인자 값 끼리의 합을 구하는 문제였습니다.  
쉬운 문제였지만 이 문제의 중요 요점을 다음과 같이 정리할 수 있을 것 같습니다.  

* A, B 3x3의 이차원 리스트의 입력 값은 List Comprehension으로 받으면 될 것 같다!
* loop에서 두 행렬의 index를 비교한 뒤 최종적으로 하나의 행렬로 출력되어야 하니, y 좌표 loop가 끝날 때 마다 리스트를 초기화 시켜야 됩니다.

위의 두개 말고는 중요도가 높아보이는 부분은 문제 풀이에서 없었습니다.

* 코드의 시간 복잡도 -> O(n^2)
    * 리스트 컴프리헨션으로 입력 값 받기 = O(N) * O(N) = O(n^2)
    * 최대값을 찾는 For Loop = 0(N) -> O(9) 