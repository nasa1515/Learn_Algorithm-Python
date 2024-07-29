# [BOJ 9093번: 단어 뒤집기](https://www.acmicpc.net/problem/9093)

## 문제

문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

## 출력

각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

### 예제 입력 1

```
2
I am happy today
We want to win the first prize
```

### 예제 출력 1 

```
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
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

```python3
import sys 

input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수 T 입력 받기

for _ in range(T): # 테스트 케이스 개수 만큼
    sentence = input().split() # 문장 입력 받기
    reversed_word = [ words[::-1] for words in sentence] # 문장의 값을 반대로
    print(' '.join(reversed_word)) # 공백과 Join 한 문자열을 출력
```


## ✅ Discription

단순하게 리스트의 `slicing`을 사용하면 쉽게 해결할 수 있습니다.  
`input.split()`으로 문장의 공백을 기준으로 단어들만 문자열 안에 저장한 뒤.  
`리스트 컨프리헨션`으로 문장안의 내용들을 뒤집어서 다시 저장하는 로직을 실행합니다.  
이 후, 리스트에 저장되어 있는 인수들을 `' '.join`으로 공백을 포함하여 출력하면 정답입니다.  

* 이 list slicing의 동작은 총 세 개의 부분으로 나뉩니다 -> `[start:end:step]`
    * start : 시작 할 인덱스를 위치를 지정합니다.
    * end : 끝나는 인덱스의 위치를 지정합니다.
    * step : 증가나 감소의 값을 지정합니다.

* 위의 설명대로 `[::-1]`을 정의해보겠습니다.
    * start, end : `::`으로 start와 end 값을 생략하면 처음부터 끝까지를 의미합니다. `(모든)`
    * step : `-1`의 경우 x 좌표가 뒤로 간다는 의미로 뒤로 한칸씩 이동하면 요소를 지정합니다.  
    * 결과 : 문자열의 처음부터 끝까지를 뒤로 한칸씩 이동하며, 모든 요소를 뒤집습니다.  

<br/>