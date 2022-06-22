# 2609 [최대공약수와 최소공배수] : https://www.acmicpc.net/problem/2609
# case 1 : 메모리 32952KB / 시간 68ms (제일 빠르다)
import math
n, m = map(int, input().split())

print(math.gcd(n, m))
print(math.lcm(n, m))

# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 88ms
# 유클리드 호제법 활용
n, m = map(int, input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    # (최소공배수 * 최대공약수) = A*B 활용
    return n * m // gcd(n, m)

print(gcd(n, m))
print(lcm(n, m))


# -------------------------------------------------------------
# case 3 : 메모리 28776KB / 시간 60ms
# 재귀 함수 & 유클리드 호제법 활용
def GCD(m, n):
    # 최대공약수 구하는 함수 정의
    if n == 0:
        return m
    return GCD(n, m % n)

m, n = map(int, input().split())

print(GCD(m, n))
print(int(m * n / GCD(m, n)))  # (최소공배수 * 최대공약수) = A*B 활용