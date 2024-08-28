# [BOJ 10814번: 나이순 정렬](https://www.acmicpc.net/problem/10814)

## 문제 설명

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.


## 입력

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)  

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.  

## 출력

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.


### 예제 입력 1

```
3
21 Junkyu
21 Dohyun
20 Sunyoung
```

### 예제 출력 1

```
20 Sunyoung
21 Junkyu
21 Dohyun
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

N = int(input())

# 입력 값을 이차원 리스트로 저장
array = [list(input().split()) for _ in range(N)]

# 정렬 후 개행문자를 포함해서 출력
print("\n".join(map(lambda x : f"{x[0]} {x[1]}", sorted(array, key= lambda x : int(x[0])))))
```

## ✅ Discription

`10650, 11651` 문제를 풀었다면, 쉽게 해결이 가능합니다.   
동일하게, 이차원 배열 형태로 저장된 데이터를 Index를 기준으로 정렬하고, 출력하는 형태입니다. (단순히 정렬 Key가 변경되었습니다. )  

우선 입력 값을 `List Comprehension`을 통해서 Array에 저장하면, 다음과 같은 이차원 배열이 저장되게 됩니다. 

```
array = [[21, "Junkyu"],[21, "Dohyun"],[20, "Sunyoung"]]
```

문제에서 요구하는 것은 각 이차원 배열의 Index[0] = `나이`를 기준으로 정렬하는 것 입니다.    
그래서 단순하게  `Lambda 함수`를 사용해서 Array 안의 Element 들을 뽑아서 정렬된 형태로 저장할 것 입니다.
`sorted()` 함수에는 정렬할 기준(Key)를 설정할 수 있는데, 여기에 Array의 정렬 할 기준 Index를 Lambda로 전달하면 쉽게 정렬이 가능합니다.

* sorted(array, key= lambda x : int(x[0]))

* array의 element 들을 기준으로, 나이 순으로 = index[0]을 기준으로 오름차순

이제 정렬된 Element를 출력해야하니, `MAP()` 함수를 사용해서, 출력에 맞는 Lambda 함수를 입혀줍니다.    

* map(lambda x : f"{x[0]} {x[1]}", sorted(array, key= lambda x : int(x[0])))

다음과 같이, x 값에, 문자열 f"{x[0]} {x[1]}" 을 대입해준 뒤, `'\n'`을 join 한 뒤 출력하면 됩니다.   