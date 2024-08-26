# [BOJ 11651번: 좌표 정렬하기 2](https://www.acmicpc.net/problem/11651)

## 문제 설명

2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

## 출력

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

### 예제 입력 1

```
5
0 4
1 2
1 -1
2 2
3 3
```

### 예제 출력 1

```
1 -1
1 2
2 2
3 3
0 4
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

if __name__ == "__main__":
    
    array = [ list(map(int, input().split())) for _ in range(int(input().strip()))]
    
    print("\n".join(map(lambda x: f"{x[0]} {x[1]}", sorted(array, key=lambda x: (x[1], x[0])))))
```

## ✅ Discription

11651을 풀었다면, 쉽게 해결이 가능합니다.   
동일하게, 이차원 배열 형태로 저장된 데이터를 Index를 기준으로 정렬하고, 출력하는 형태입니다. (단순히 정렬 Key가 변경되었습니다. )  


우선 입력 값을 `List Comprehension`을 통해서 Array에 저장하면, 다음과 같은 이차원 배열이 저장되게 됩니다. 

```
array = [[0, 4],[1, 2],[1, -1],[2, 2],[3, 3]]
```

문제에서 요구하는 것은 각 이차원 배열의 Index[1] = Y 좌표를 기준으로 정렬하는 것 입니다.    
그래서 단순하게  `Lambda 함수`를 사용해서 Array 안의 Element 들을 뽑아서 정렬된 형태로 저장할 것 입니다.
`sorted()` 함수에는 정렬할 기준(Key)를 설정할 수 있는데, 여기에 Array의 정렬 할 기준 Index를 Lambda로 전달하면 쉽게 정렬이 가능합니다.

* sorted(array, key= lambda x: (x[1], x[0]))

* array의 element 들을 기준으로, Y좌표가 증가하는 순으로 = index[1] 을 기준으로 오름차순, 만약 동일하다면, X좌표 (index[0]) 가 증가하는 순서로 정렬 
    * 문제를 보면 음수~양수까지니, SET으로 묶어서 절대값 (Y, X) 로 정렬이 가능합니다.   

이제 정렬된 Element를 출력해야하니, `MAP()` 함수를 사용해서, 출력에 맞는 Lambda 함수를 입혀줍니다.    

* map(lambda x: f"{x[0]} {x[1]}", sorted(array, key=lambda x: (x[1], x[0])))

다음과 같이, x 값에, 문자열 f"{x[0]} {x[1]}" 을 대입해준 뒤, `'\n'`을 join 한 뒤 출력하면 됩니다.   