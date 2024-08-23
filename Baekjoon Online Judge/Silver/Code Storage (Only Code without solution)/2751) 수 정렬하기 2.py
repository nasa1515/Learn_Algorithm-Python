import sys

input = sys.stdin.readline


# get input using list Comprehension
array = [int(input().strip()) for _ in range(int(input()))]

# print arg in array 
print(*sorted(array), sep='\n')