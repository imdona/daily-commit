'''
백준 11050 [이항계수] - bronze1
자연수 N과 정수 K가 주어졌을 때 이항계수를 구하는 프로그램을 작성하시오.
첫째 줄에 N과 K가 주어진다.(1<=N<=10, 0<=K<=N)

nCk = n! / ((n-k)! * k!)
'''

# math의 factorial import해서 구하기
from math import factorial
N, K = map(int, input().split())
result = factorial(N) // (factorial(K) * factorial(N-K))
print(result)

# factorial 함수 직접 만들어보기
N, K = map(int, input().split())

def facto(x):
    if x == 0:
        result 1
    elif x == 1:
        return 1
    else:
        return x * facto(x-1) # x=0이 될 때까지 루프 돌기

result = facto(N) // (facto(K) * facto(N-K))
print(result)