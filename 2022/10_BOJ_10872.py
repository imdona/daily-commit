'''
백준 10872 [백준]
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

[출력]
첫째 줄에 N!을 출력한다.
'''
# 반복문 풀이
N = int(input())
result = 1
for i in range(1, N + 1):
    result *= i

print(result)

########################################################################
# 재귀적 풀이
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(int(input())))

########################################################################
# math 라이브러리를 사용한 풀이
import math
print(math.factorial(int(input())))