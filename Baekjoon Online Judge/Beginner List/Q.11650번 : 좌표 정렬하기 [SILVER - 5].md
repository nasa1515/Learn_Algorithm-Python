# [BOJ 11650번: 좌표 정렬하기 ](https://www.acmicpc.net/problem/11650)

## 문제 설명

2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

## 출력

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

### 예제 입력 1

```
5
3 4
1 1
1 -1
2 2
3 3
```

### 예제 출력 1

```
1 -1
1 1
2 2
3 3
3 4
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

# Array 받기
array = [list(map(int, input().split())) for _ in range(int(input()))]

# x[0] index , [1] Index 오름차순 정렬
sorted_array = sorted(array, key= lambda x: (x[0], x[1]))

# 이차원 배열 출력
print("\n".join(map(lambda x: f"{x[0]} {x[1]}", sorted_array)))
```

## ✅ Discription

문제 풀이를 위한 요점, 이차원 Array 형태의 데이터의 입력을 받고, 각 이차원 Array의 특정 Index를 기준으로 정렬의 여부를 설정하는것 입니다.  
저는 간단하게, 정렬 및 출력을 `lambda`로 구현했습니다.  

우선 입력 값을 `List Comprehension`을 통해서 Array에 저장하면, 다음과 같은 이차원 배열이 저장되게 됩니다. 

```
array = [[1, 1],[1, -1],[2, 2],[3, 3],[3, 4]]
```

문제에서 요구하는 것은 우선적으로 각 이차원 배열의 Index[0] = X 좌표를 기준으로 정렬하는 것 입니다.    
그래서 단순하게 array[0][0] 이런식으로 하나씩 뽑아내서 정렬하는 것 보다는 `Lambda 함수`를 사용해서 Array 안의 Element 들을 뽑아서 정렬된 형태로 저장할 것 입니다.
`sorted()` 함수에는 정렬할 기준(Key)를 설정할 수 있는데, 여기에 Array의 정렬 할 기준 Index를 Lambda로 전달하면 쉽게 정렬이 가능합니다.

* sorted_array = sorted(array, key= lambda x: (x[0], x[1]))

* array의 element 들을 기준으로, X좌표가 증가하는 순으로 = index[0] 을 기준으로 오름차순, 만약 동일하다면, Y좌표 (index[1]) 가 증가하는 순서로 정렬 
    * 문제를 보면 음수~양수까지니, SET으로 묶어서 절대값 (X, Y) 로 정렬이 가능합니다.   

이제 `sorted_array` 에는 문제의 요구사항에 맞게 정렬된 Element들이 저장되었읜, 문제의 출력에 맞게 출력해야합니다.  

* print("\n".join(map(lambda x: f"{x[0]} {x[1]}", sorted_array)))

다음과 같이, map() 함수를 사용해서, sorted_array 안에 있는 index 들을, lambda 함수의 계산식에 맞는 형태로 뽑아낸 뒤, `'\n'` 줄 바꿈 문자와 `join`해서 출력합니다. 


