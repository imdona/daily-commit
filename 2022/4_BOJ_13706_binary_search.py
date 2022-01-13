'''
백준 13706 [제곱근]
* 수학, 이분 탐색, 임의 정밀도 / 큰 수 연산

정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.

[출력]
첫째 줄에 정수 N의 제곱근을 출력한다.
'''
# 이진 탐색을 이용한 풀이 방법
import sys
N = int(sys.stdin.readline())

start = 1
end = N

while True:
    midpoint = (start + end) // 2
    if (midpoint)**2 == N:
        print(midpoint)
        break
    elif (midpoint)**2 > N:
        end = midpoint - 1
    else:
        start = midpoint + 1

# math의 isqrt 메소드를 이용한 간단한 풀이방법
import sys
from math import isqrt
N = int(sys.stdin.readline())
print(isqrt(N))

'''
🔍 python math - sqrt & isqrt
1. math.sqrt(n) : n의 제곱근 반환
2. math.isqrt(n) : 음이 아닌 정수 n의 정수 제곱근 반환
'''
import math
n = 36
math.sqrt(n) # 6.0
math.isqrt(n) # 6