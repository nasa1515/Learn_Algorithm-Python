# 그룹 단어 체커

## 문제

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.  
예를 들면, `ccazzzzbb`는 `c`, `a`, `z`, `b`가 모두 연속해서 나타나고, `kin`은 `k`, `i`, `n`이 연속해서 나타나기 때문에 그룹 단어이지만,  
`aabbbccb`는 `b`가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

`단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.`

## 입력

첫째 줄에 단어의 개수 N이 들어온다. (1 ≤ N ≤ 100)  
둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 길이는 최대 100이다.  

## 출력

첫째 줄에 그룹 단어의 개수를 출력한다.

## 예제 입력 1

```
3
happy
new
year
```

## 예제 출력 1
```
1
```

## 예제 입력 2
```
4
aba
abab
abcabc
a
```

## 예제 출력 2
```
1
```

## 예제 입력 3
```
5
aa
aaa
aaaa
aaaaa
aaaaaa
```

## 예제 출력 3

```
5
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

```pyhon3

import sys

loop_count = int(sys.stdin.readline()) #주어지는 그룹 단어의 LOOP 횟수 값 입력
word_count = loop_count

for _ in range(loop_count):
    group_word = sys.stdin.readline().strip() # 그룹 단어를 검사할 단어 입력
    for i in range(len(group_word) - 1): 
        if group_word[i] == group_word[i + 1]: # 문자열의 앞과 뒤를 비교해서 같으면 Pass
            pass
        elif group_word[i] in group_word[i+1:]: # 문자열의 i와 지금까지 봤던 문자열 중 i를 포함하면 중복으로 Break
            word_count -= 1
            break

print(word_count)
```

## ✅ Discription

1. 그룹 단어라는 것은 결국 한번 나온 단어가 뒤에서 또 나온다면, 연속성을 잃기 때문에 그룹 단어가 아니게 됩니다.
2. 그래서 `리스트 슬라이싱`으로, 현재 위치의 알파벳이 이전에 검사한 리스트에 포함된다면, 중복에 해당, 그룹 단어에서 제외하는 알고리즘으로 해결했습니다. 

<br/>
<br/>


## ✅ + Solution Code

```python
group_cnt = 0
group_word = sys.stdin.readline().strip()
group_cnt += list(group_word) == sorted(group_word, key=group_word.find)  
```

1. 결국 `그룹 단어`의 의미는, 연속성이 아닌 문자 중복의 필터링이 좀 더 쉬운 해결 방법 입니다. (따라서 위와 같은 코드로도 해결이 가능합니다.)
2. `list()`로 단어를 분할하고, `sorted(group_word, key=group_word.find)`로 가장 처음에 문자 기준으로 정렬한 뒤 비교 후 수를 셉니다.  

* 예를 들면 `happy` 의 경우 [h,a,p,p,y] == [h,a,p,p,y]로 True 값이 나오니 `1` 값이 추가될 것이고  
    `happyah`의 경우 [h,a,p,p,y,a,h] == [h,h,a,a,p,p,y]가 나올테니, False 값으로 0이 추가 되는 알고리즘도 가능합니다.