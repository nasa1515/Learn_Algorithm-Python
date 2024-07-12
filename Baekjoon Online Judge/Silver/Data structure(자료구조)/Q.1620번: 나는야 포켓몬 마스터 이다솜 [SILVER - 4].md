# [백준 1620번: 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)

## 입력
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.  N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.  

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

## 출력

첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 출력합니다.  
입력으로 숫자가 들어오면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어오면 그 포켓몬의 번호를 출력합니다.

### 예제 입력 1

```
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
```

### 예지 출력 1

```
Pikachu
26
Venusaur
16
14
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

def fun_start():
    
    (1)
    input_poketmon_count, search_poketmon_count = map(int, input().split())
    
    (2)
    poketmon_dict = {}

    
    for i in range(input_poketmon_count):
        poketmon_name = input().strip()
        poketmon_dict[i+1] = poketmon_name
        poketmon_dict[poketmon_name] = int(i+1)
    
    (3)
    for _ in range(search_poketmon_count):
        search_poketmon_name = input().strip()
        if search_poketmon_name.isdigit():
            print(poketmon_dict[int(search_poketmon_name)])
        else:
            print(poketmon_dict[search_poketmon_name])

if __name__ == "__main__":
    fun_start()
```

## ✅ Discription

문제의 구현 로직은 `input() 값이 숫자면 = 문자`, `input() 값이 문자면 = 숫자`를 출력하는 간단한 로직입니다.  
다만, 이 문제를 푸는데 가장 중요한 요건은 시간 복잡도 입니다. 조건 자체가 `100,000`개 까지의 범위 만큼의 문자가 존재할 수 있는데   
`LIST`를 이용한다고 단순히 숫자,문자를 조회해서 출력하는데 `O(N) = 10만의 경우 0(100000)` 만큼의 시간 복잡도가 발생합니다.    
따라서 갯수와 상관없이 `key-value` 형태의 출력이 가능한 `HASH - DICT`으로 풀어야 합니다.  

1. `map(int, input().split())`으로 저장할 문자의 개수와, 검색할 문자 개수의 표준 입력을 받습니다.
2. 비어있는 dict을 선언하고, for 문으로 입력 받은 인수만큼의 문자를 `dict`에 `key, value`로 번갈아가면서 넣어줍니다.  
-> `"Bulbasaur","Ivysaur","Venusaur"` 세개를 넣는다면  
`{1:Bulbasaur, Bulbasaur:1, 2:Ivysaur, Ivysaur:2, 3:Venusaur, Venusaur:3}`이 들어간 dict이 만들어지겠죠.  
3. `isdigit()`으로 검색할 문자가 숫자인지 확인 후에, `dict`에 저장된 문자를 꺼내 옵니다.