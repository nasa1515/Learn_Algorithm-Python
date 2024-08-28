# [BOJ 10825번: 국영수](https://www.acmicpc.net/problem/10825)

## 문제 설명


도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.  

1. 국어 점수가 감소하는 순서로  
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로  
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로  
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)  

## 입력  

첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다. 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다. 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

## 출력

문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.

### 예제 입력 1

```
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
```

### 예제 출력 1

```
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
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

# N 입력 값 저장
N = int(input())

# 입력 값 Array 저장
array = [list(input().split()) for _ in range(N)]

# 정렬 후 개행 문자를 포함해서 출력
print('\n'.join(map(lambda x: x[0] ,(sorted(array, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )))))
```

## ✅ Discription

`10650, 11651, 11814` 문제를 풀었다면, 쉽게 해결이 가능합니다.   
동일하게, 이차원 배열 형태로 저장된 데이터를 Index를 기준으로 정렬하고, 출력하는 형태입니다. (단순히 정렬 Key가 변경되었습니다. )  

우선 입력 값을 `List Comprehension`을 통해서 Array에 저장하면, 다음과 같은 이차원 배열이 저장되게 됩니다. 

```
array = [
    ["Junkyu", 50, 60, 100],
    ["Sangkeun", 80, 60, 50],
    ["Sunyoung", 80, 70, 100],
    ["Soong", 50, 60, 90],
    ["Haebin", 50, 60, 100],
    ["Kangsoo", 60, 80, 100],
    ["Donghyuk", 80, 60, 100],
    ["Sei", 70, 70, 70],
    ["Wonseob", 70, 70, 90],
    ["Sanghyun", 70, 70, 80],
    ["nsj", 80, 80, 80],
    ["Taewhan", 50, 60, 90]
]
```

문제에서 요구하는 정렬 조건은 총 4개인데 아래와 같습니다. 

1. 국어 점수가 감소하는 순서로 -> `index[1] 을 내림차순으로`
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로 -> `index[2]을 오름차순으로`
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 -> `index[3]을 내림차순으로`
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 -> `index[0]을 오름차순으로`

그래서 단순하게  `Lambda 함수`를 사용해서 Array 안의 Element 들을 뽑아서 정렬된 형태로 저장할 것 입니다.
`sorted()` 함수에는 정렬할 기준(Key)를 설정할 수 있는데, 여기에 Array의 정렬 할 기준 Index를 Lambda로 전달하면 쉽게 정렬이 가능합니다.

* (sorted(array, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) ))  
    * array의 element를 기준, 각 index의 오름차순, 내림차순에 맞게 정렬
    * `sorted의 기본 정렬은 오름차순이기에, key에 -를 붙이면 Reverse  처리되어, 내림차순으로 적용됩니다.`

이제 정렬된 Element를 출력해야하니, `MAP()` 함수를 사용해서, 출력에 맞는 Lambda 함수를 입혀줍니다.    

* map(lambda x: x[0] , ....

다음과 같이, x 값에, index[0]" 을 대입 합니다. (정답 출력에, 이름만 출력하므로..), `'\n'`을 join 한 뒤 출력하면 됩니다.   