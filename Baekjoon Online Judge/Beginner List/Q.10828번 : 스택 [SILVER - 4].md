# [BOJ 10828번: 스택](https://www.acmicpc.net/problem/10828)

## 문제 설명

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.  

명령은 총 다섯 가지이다.  

push X: 정수 X를 스택에 넣는 연산이다.  
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
size: 스택에 들어있는 정수의 개수를 출력한다.  
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.  
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.  

## 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.  
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.  

## 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

### 예제 입력 1

```
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```

### 예제 출력 1

```
2
2
0
2
1
-1
0
1
-1
0
3
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

def fun_10828_stack(*command : str) -> str:
    
    if command[0] == "push": # push 일 경우
        Stack_list.append(command[1])
    
    elif command[0] == "pop": # pop 일 경우
        if len(Stack_list) == 0: # 리스트가 비었을 경우
            print("-1") 
        else:
            print(Stack_list.pop())       
    
    elif command[0] == "size": # size 일 경우
        return print(len(Stack_list))
    
    elif command[0] == "empty": # empty 일 경우
        if len(Stack_list) == 0:
            print("1")
        else:
            print("0")
            
    elif command[0] == "top": # top 일 경우
        if len(Stack_list) == 0:
            print("-1")
        else:
            print(Stack_list[-1])
        
if __name__ == "__main__":
    
    Stack_list = [] # 빈 리스트 생성
    N = int(input().strip())

    for _ in range(N):
        command = input().split() # 문자를 split 해서 저장
        fun_10828_stack(*command) # 함수에 문자열을 풀어서 전달
```

## ✅ Discription

문제의 구현 로직은 `N` 값의 Loop 만큼, `Stack`의 명령 인자를 받아서, 그에 맞는 기능을 구현하는 문제입니다.      
* 시간복잡도는 0.5초이지만, N의 Max 허용값이 100,000 까지라 for loop도 문제 없습니다.

파이썬에서는 따로 JAVA 같이 Stack 구조를 지원하지 않습니다. 
그보다 더 편한 `LIST`가 있기 때문입니다. 보통 Stack, Queue 두개의 구조를 구현하려면 List를 사용하시면 됩니다.     

* 문제의 Key는 Push 1, pop 이런식으로 공백을 기준으로 Split 할 수 있는 것, 없는 것 두가지 종류의 문자가 들어오게 되는데, 이를 어떤 방식으로 구분해서 저장한 뒤 인자로 쓸 것인지 입니다.  
-> 저의 경우는, 하나의 문자열로 받은 뒤에, 함수에 *(asterisk)로 풀어서 전달했습니다.