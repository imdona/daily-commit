'''
백준 11050 [이항계수]
자연수 N과 정수 K가 주어졌을 때 이항계수를 구하는 프로그램을 작성하시오.
첫째 줄에 N과 K가 주어진다.(1<=N<=10, 0<=K<=N)
'''

from math import factorial
N, K = map(int, input().split())
result = factorial(N) // (factorial(K) * factorial(N - K))
print(result)

