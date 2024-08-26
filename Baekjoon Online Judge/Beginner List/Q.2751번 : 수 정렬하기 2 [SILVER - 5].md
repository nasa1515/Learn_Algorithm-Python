# [BOJ 2751번: 수 정렬하기 2](https://www.acmicpc.net/problem/2751)

## 문제 설명

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.  


## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.  


## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.  

### 예제 입력 1

```
5
5
4
3
2
1
```

### 예제 출력 1

```
1
2
3
4
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

```python3
import sys

input = sys.stdin.readline


# get input using list Comprehension
array = [int(input().strip()) for _ in range(int(input()))]

# print arg in array 
print(*sorted(array), sep='\n')
```

## ✅ Discription

문제의 풀이 방법은, 간단하게 `N` 개 만큼의 들어온 문자열을 저장해서, 오름차순으로 하나씩 출력하기만 하면 됩니다.  

* list Comprehension 으로 N값 만큼의 입력 값을 받은 Array를 생성 합니다.  
* sorted() 함수로 리스트 안에 있는 Element 들을 , Seprate를 `'\n'`을 추가해서 하나씩 출력합니다. 

### 정렬에서의 Sort(), Sorted()의 차이

* 두 함수 모두 오름차순을 기본으로 Array 안의 Element 들을 정렬해주는 것은 동일합니다.  
* 다만 Sort()는 원본 Array의 Element 들을 직접적으로 정렬하는 것이고, Sorted()는 새로운 메모리 주소에 정렬된 새로운 List를 생성해, 원본은 정렬되지 않습니다.  