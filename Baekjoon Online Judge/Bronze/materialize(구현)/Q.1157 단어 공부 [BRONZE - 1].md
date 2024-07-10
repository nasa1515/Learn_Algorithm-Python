# 1157번: 단어공부

## 문제 설명

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.  
단, 대문자와 소문자를 구분하지 않는다.

---

## 입력

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

---

## 출력

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.  
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

---

## 예제

### 입력 1

```
Mississipi
```

### 출력 1

```
?
```

### 입력 2

```
zZa
```

### 출력 2

```
Z
```

### 입력 3

```
z
```

### 출력 3

```
Z
```

### 입력 4

```
baaa
```

### 출력 4

```
A
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

word = sys.stdin.readline().upper().strip() # 문자 입력 + 대문자 변형
word_dict = {} # dict 초기화

for char in word:
    if char in word_dict: # dict 안에 문자가 있으면 Value 값을 증가
        word_dict[char] += 1
    else: # dict 안에 문자가 없으면 Value 값 선언 
        word_dict[char] = 1
    
max_value_word = [key for key, value in word_dict.items() if value == max(word_dict.values())] # 리스트 컴프리 헨션으로 MAX Value의 key만 저장. //

print('?' if len(max_value_word) > 1 else max_value_word[0]) # key index 갯수가 1개 이상이면 ?, 아닐 경우 인덱스를 그대로 출력.
```

## ✅ Discription  

저는 문제 해결을 위한 조건들을 다음과 같이 정의했습니다.  

1. 입력된 단어는 출력 시 대문자로 출력되기에, 입력부터 대문자로 처리 해야한다.  
2. 가장 많이 사용된 단어를 체크하기 위해선, 결국 `For loop` 보다는 `hash` 형태의 알고리즘이 더 적합하다고 생각했습니다.  
3. 문자열을 for 문으로 분할해, `dict hash` 형태로 각 문자별 `count value`를 가진 Dict를 생성합니다.
4. 이후 `(List Comprehension)`으로 `word_dict` 안에 있는 `KEY, VALUE`를 꺼내, 가장 높은 `Value`를 가진 `Key` 값을 뽑아냅니다.  
5. 출력 시에, 문제의 조건에 맞게, `INDEX`의 갯수에 따라 다른 출력을 제어합니다.  

% 근데 DICT으로 풀려니까, 결국 `for loop`을 2번 이상 돌아야 해서, `LIST` 형태로도 풀어봤습니다. 

## ✅ Solution Code.2

```python3
import sys

line = sys.stdin.readline().upper().strip() # 입력
line_u = list(set(line)) # 여러 중복 알파벳의 유니크 값을 저장
cnt = [] # 리스트 초기화
for x in line_u: # 유니크 알파벳 분기
    cnt.append(line.count(x)) # 원본 문자열에서 각 알파벳의 갯수를 세서, 새 리스트에 저장

if cnt.count(max(cnt)) > 2: # 새 리스트에 동일한 count의 알파벳이 있으면 바로 ? 출력
    print("?")
else:
    print(line_u[cnt.index(max(cnt))]) # 다른 출력
```

1. 리스트로 풀 경우, `set()`을 이용해서, 문자열의 유니크 값을 정의하고 해당 값으로 `For loop`을 돌려 갯수를 구했습니다.  
2. 이후, `Value count`가 저장된 리스트의 갯수를 기준으로 출력을 정합니다.  
3. 만약 리스트 갯수가 1개 일 경우, 알파벳의 숫자를 저장하고 있는 `cnt` 리스트의 max 값의 index 위치를 기준으로 유니크 알파벳을 가지고 있는 `line_u`에서 알파벳을 꺼내 옵니다.  


<br/>

#### 제출 후 속도 비교 결과 : 리스트로 푼게 : 76ms , HASH로 푼게 184ms로 for loop 두번의 결과 차이가 심한 것 같습니다...
![스크린샷 2024-07-10 오후 3 42 49](https://github.com/nasa1515/Learn_Algorithm-Python/assets/69498804/b8631671-c612-47be-9eb6-fcb3bb078d2a)





