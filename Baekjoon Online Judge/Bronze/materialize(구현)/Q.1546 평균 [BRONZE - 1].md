# [백준 1546번: 평균](https://www.acmicpc.net/problem/1546)

## 문제

세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 
일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.  

예를 들어, 세준이의 최고점이 70이고, 수학 점수가 50이었으면 수학 점수는 50/70*100이 되어 71.43점이 된다.  
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 시험 본 과목의 개수 N이 주어진다. (1 ≤ N ≤ 1000)  
둘째 줄에 세준이의 현재 성적이 주어진다. 이 성적은 모두 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

## 출력

첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 \(10^{-2}\) 이하이면 정답이다.

### 예제 입력 1

```
3
40 80 60
```

### 예제 출력 1 

```
75.0
```

### 예제 입력 2 

```
3
10 20 30
```

### 예제 출력 2 

```
66.666667

10-2 이하의 오차를 허용한다는 말은 정확히 소수 2번째 자리까지 출력하라는 뜻이 아니다.
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

#### 원본 코드

```pyhon3
word_count = int(input())
word_list = list(map(int, input().split()))

total_score = 0
max_value = max(word_list)

for score in word_list:
    total_score += score / max_value * 100
    
print(total_score / word_count)
```

#### 파이써닉한 코드

```python3
word_count = int(input())
word_list = list(map(int, input().split()))

total_score = 0

max_value = max(word_list)
sum_score = sum(word_list)/max_value*100
    
print(sum_score/word_count)
```

## ✅ Discription

너무 쉽습니다...BRONZE 1 수준은 아닌 것 같습니다.  
단순하게 리스트의 구조를 알면 쉽게 접근할 수 있는 영역인 것 같습니다.

1. 모든 점수에다가 문자열의 점수 중 가장 최고 점수를 가지고 추가적인 수식의 평균을 구하면 되는 문제 입니다.
2. 파이써닉하게 문자열을 분할해서 받고, `MAX()` 함수로 최고 값을 뽑아서, 수식을 구현하면 됩니다.  

<br/>