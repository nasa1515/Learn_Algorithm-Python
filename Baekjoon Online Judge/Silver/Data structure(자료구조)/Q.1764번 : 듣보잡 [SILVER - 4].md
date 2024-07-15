# [백준 1764번: 듣보잡](https://www.acmicpc.net/problem/1764)

## 문제 설명

김진영은 듣도 못한 사람의 명단과 보도 못한 사람의 명단을 가지고 있다.  
이 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.  

## 입력

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. (1 ≤ N, M ≤ 500,000)  

둘째 줄부터 N개의 줄에는 듣도 못한 사람의 이름이 주어지고,  
그 다음 M개의 줄에는 보도 못한 사람의 이름이 주어진다.  
이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 최대 20이다.  

## 출력

듣도 보도 못한 사람의 수와 그 명단을 사전순으로 출력한다.  

### 예제 입력 1

```
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
```

### 예제 출력 1

```
2
baesangwook
ohhenrie
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

## ❌ First Code

```python3
import sys

input = sys.stdin.readline


def fun_1764():
    
    N, M = map(int, input().split())
    do_not_listen = [input().strip() for _ in range(N)]
    result = []
    for _ in range(M):
        do_not_see = input().strip()
        if do_not_see in do_not_listen:
            result.append(do_not_see)
    
    print(len(result))
    for i in sorted(result):
        print(i)
    
    
if __name__ == "__main__":
    fun_1764()
```
처음에는 막연히, 듣보잡의 리스트를 받고, `LIST in LIST` 검색으로 찾을 수 있다고 생각 했습니다.  
결과는 `시간 초과` 였습니다. -> 이유는, `N,M`의 경우 N, M은 `500,000 이하의 자연수` 범위 까지 허용하기에,  
LIST 속에서 문자열을 일일히 비교하기 위해선 시간 복잡도 O(N)만큼에 저는 추가적으로 O(N)이 한번 더 일어나기 때문이었습니다.  
-> `그래서 아래와 같이 HASH로 풀어 정답이 되었습니다.`

## ✅ Solution Code

```python3

import sys

input = sys.stdin.readline


def fun_1764():
    
    (1)
    N, M = map(int, input().split())
    do_not_listen = set(input().strip() for _ in range(N))
    do_not_see = set(input().strip() for _ in range(M))
    
    (2)
    result = list(do_not_see & do_not_listen)
    result.sort()
    
    (3)
    print(len(result))
    print(*result, sep='\n')

    
if __name__ == "__main__":
    fun_1764()
    
```

## ✅ Discription

문제의 구현 로직은 `set() 컴프리헨션으로, N,M에 해당하는 문자열들을 set()으로 받은 뒤 교집합을 출력`하는 간단한 로직입니다.    
다만, 이 문제를 푸는데 가장 중요한 요건은 위에서 한번 실패가 일어난 시간 복잡도 입니다.  
LIST 와는 다르게, SET()의 교집합을 구하는 시간 복잡도의 경우 `O(1)`이기 때문에, 위와 같이 시간 복잡도를 해결하였습니다.  
 

1. `input()`으로 저장할 문자의 개수와, 검색할 문자 개수, 문자열의 표준 입력을 받습니다.
2. 저장된 SET의 문자열의 교집합을 LIST로 생성합니다. 이후 출력을 위해 `SORT()`로 문자열의 정렬을 진행합니다.   
3. `len()`으로 리스트의 갯수를 출력하고, `*`으로 리스트 안의 원소를 모두 출력하되, `'\n'` 줄바꿈을 포함해서 출력합니다.
