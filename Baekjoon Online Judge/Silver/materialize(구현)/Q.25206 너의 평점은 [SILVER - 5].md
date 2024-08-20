# [BOJ 25206번: 너의 평점은](https://www.acmicpc.net/problem/25206)

## 문제


인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!  

치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.  

전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.  

인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.  

| 등급 | 과목평점 |
|------|----------|
| A+   | 4.5      |
| A0   | 4.0      |
| B+   | 3.5      |
| B0   | 3.0      |
| C+   | 2.5      |
| C0   | 2.0      |
| D+   | 1.5      |
| D0   | 1.0      |
| F    | 0.0      |

P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.  

과연 치훈이는 무사히 졸업할 수 있을까?  

## 입력

20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.  

## 출력

치훈이의 전공평점을 출력한다.  

정답과의 절대오차 또는 상대오차가   
\(10^{-4}\) 이하이면 정답으로 인정한다.  

## 제한

* 1 ≤ 과목명의 길이 ≤ 50
* 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
* 학점은 1.0,2.0,3.0,4.0중 하나이다.
* 등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
* 적어도 한 과목은 등급이 P가 아님이 보장된다.

## 예제 입력 1

```
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P
```

## 예제 출력 1
```
3.284483
```

## 예제 입력 2
```
BruteForce 3.0 F
Greedy 1.0 F
DivideandConquer 2.0 F
DynamicProgramming 3.0 F
DepthFirstSearch 4.0 F
BreadthFirstSearch 3.0 F
ShortestPath 4.0 F
DisjointSet 2.0 F
MinimumSpanningTree 2.0 F
TopologicalSorting 1.0 F
LeastCommonAncestor 2.0 F
SegmentTree 4.0 F
EulerTourTechnique 3.0 F
StronglyConnectedComponent 2.0 F
BipartiteMatching 2.0 F
MaximumFlowProblem 3.0 F
SuffixArray 1.0 F
HeavyLightDecomposition 4.0 F
CentroidDecomposition 3.0 F
SplayTree 1.0 F
```

## 예제 출력 2
```
0.000000
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

if __name__ == "__main__":
    
    _total_sum = 0
    _grade_sum = 0

    grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
    }
    
    for _ in range(20): # 20줄에 걸쳐 입력을 받는 loop
        major_name, score, grade = input().split()   # 각 전공과목 명, 점수, 등급을 변수로 받기.  
        
        if grade != 'P':
            
            _total_sum += float(score) # 전체 학점을 구하기 위한 단순 합
            _grade_sum += float(score) * grades[grade] # 기본 학점 * 과목 평점의 합을 구하기 위한 값
            
    print(round(_grade_sum/_total_sum, 6)) # 기본 학점 * 과목 평점 합 /전체 학점 합 and ROUND 소수점
```

## ✅ Discription

1. 결과론적으로, 출력되어야 하는 로직은 20줄에서의 `score`의 총합으로 `score`* `grade`에 해당하는 전공 평점의 합을 소수점 6자리까지 출력하는 것입니다.   
2. 따라서, 각각 grade에 맞는 Dict를 선언해서, `grades[grade]`로 전공 평점 값을 가져와서 계산하는 로직으로 구현했습니다.  
3. 또한 `Float`로 소수점 계산을 해야, 3.0 , 2.5 등 소수점에 대한 정수 계산이 가능합니다.  
4. `if grade != 'P':` 조건의 경우 문제의 제한에 `적어도 한 과목은 등급이 P가 아님이 보장된다.`라는 문구로, `F`는 열어두고 진행했습니다.

<br/>
<br/>

