# [BOJ 2309번: 일곱 난쟁이](https://www.acmicpc.net/problem/2309)


## 문제 설명

동혁이는 자신의 집에서 난쟁이 일곱 명과 함께 크리스마스를 축하할 예정이다. 그런데 난쟁이들이 크리스마스 선물로 각자의 키를 잊어버렸고, 동혁이는 난쟁이 일곱 명의 키의 합이 100이 되어야 한다고 한다. 동혁이는 자신이 키를 재서 그 값들을 알고 있다.

주어진 9명의 난쟁이 키 중 7명의 키를 선택하여 그 합이 100이 되도록 하여, 선택된 7명의 난쟁이의 키를 오름차순으로 출력하는 프로그램을 작성하시오.

## 입력

- 입력은 9개의 정수로 이루어진다. 각 정수는 난쟁이의 키를 나타내며, 각 정수는 1,000보다 작거나 같고, 1보다 크거나 같다.

## 출력

- 7명의 난쟁이의 키를 오름차순으로 출력한다. 각 키는 한 줄에 하나씩 출력되어야 한다.

## 예제

### 입력

```
20
7
23
19
10
15
25
8
13
```

### 출력

```
7
8
10
13
19
20
23
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


## ✅ Solution Code + itertools LIB의 combinations 사용

```python3
# use lib
import sys, itertools
input = sys.stdin.readline

# 리스트로 입력 값을 받습니다.
human_list = [int(input()) for _ in range(9)]

# Combinations 이터레이너로 7개의 값을 뽑는 순열 모음 리스트를 생성해서 출력합니다.
for item in itertools.combinations(human_list, 7):
    if sum(item) == 100: //7개의 반환 순열의 합이 100이면
        print("\n".join(map(str, sorted(item)))) // 해당 리스트의 값을 출력한다.
        break
```

## ✅ Discription  

저는 문제 해결을 위한 조건들을 다음과 같이 정의했습니다.  

1. **입력 받기:** 총 9개의 난쟁이 키 인자를 입력받는다.
2. **조합 확인:** 9개의 난쟁이 키 중 7명을 선택하여 그 합이 100이 되는 조합을 찾는다. -> combination()
3. **출력:** 조건을 만족하는 7명의 키를 오름차순으로 출력한다.

<br/>

## ✅ Solution Code_2 + Brute Force FOR_LOOP 사용

```python3
# use lib
import sys, itertools
input = sys.stdin.readline

human_list = [int(input()) for _ in range(9)] // # 리스트로 입력 값을 받습니다.
human_list.sort() // # 완전 탐색 구현을 위해서, 리스트 안의 인자를 오름차순으로 정렬합니다.

sum_ = sum(human_list) // # 총 합과의 비교를 위한 sum() 값을 구했습니다.

for i in range(len(human_list)): // human_list index search를 위한 완전 탐색 For loop
    for j in range(i+1, len(human_list)):
        if sum_ - human_list[i]-human_list[j] == 100: // # human_list 최종 합에서 2개의 Index를 제거 한 값 = 100 = 완전한 수열
            for item in human_list: 
                if item != human_list[i] and item != human_list[j]: // # i index, j index 값이 아닌 인자값을 출력합니다.
                    print(item, sep="\n")
            sys.exit()
```

## ✅ FOR_LOOP Discription  

첫번째 combination의 풀이와는 다르게, `Brute Force` 방식의 `For Loop`으로도 풀이 해봤습니다.  
Combination에서는 해당 리스트의 숫자 인자를 가지고, 가능한 모든 수열을 만들어주는 이터레이터 방식이라면  
이 방식에서는, 전체 리스트의 합을 계산한 뒤에, 2개의 `index` 리스트를 빼가면서, 총합이 `100`이 되는 경우의 수를 구하는 방식으로 풀이했습니다.  

<br/>

## ✅ Solution Code_3 + DFS 사용

```python3

def dfs_2309(depth, start): //DFS 함수 구현
    
    if depth == 7: // # 리스트 안에 들어있는 난쟁이 수가 7이 될 경우를 구분하는 종료 구문.
        if sum(SUM_100_LIST) == 100: // # 난쟁이 수가 7인데, 리스트의 합이 100인 경우 리스트 인자 값 출력
            print(*sorted(SUM_100_LIST), sep="\n")
            exit()
        else:
            return // # 합이 100이 아닌 경우 그대로 재귀를 종료.
   
    for i in range(start, len(P_list)): // # 재귀의 계산 구문, Start 인자 ~ 난쟁이의 원본 리스트 만큼의 FORLOOP
        SUM_100_LIST.append(P_list[i]) // # 리스트에 i 인덱스의 값을 삽입
        dfs_2309(depth + 1, i + 1) // # 삽입 한 리스트를 가지고, 재귀 depth는 1씩 증가하고, 다음 인덱스 검색을 위한 i 값도 하나 증가
        SUM_100_LIST.pop() // # 리스트에 7이상의 값이 담겼으나, 합이 100이 아닌 경우, 마지막 인덱스의 값을 pop()


if __name__ == "__main__":
    
    P_list = [int(input()) for _ in range(9)]
    SUM_100_LIST = []
    dfs_2309(0,0) // # 0번 인덱스 부터 DFS 실행
```

## ✅ DFS  Discription  

`Brute Force`의 경우 For문을 7번 이상 돌아야 하기 때문에, 가장 효율적인? 방식이라고 하면 효율적인 방식입니다.  
-> (사실 파이써닉한 건 Combination을 사용하는 것이긴 합니다.)  
단순히, Depth를 늘려가면서, 모든 인덱스를 `Stack` 방식으로 하나씩 넣었다가, 빼는 방식으로 재귀를 호출하는 방식입니다.  

<br/>

`itertools의 가이드는 아래 사이트를 참조하면 좋습니다.`

## (PYTHON itertools Guide)[https://docs.python.org/ko/3/library/itertools.html]