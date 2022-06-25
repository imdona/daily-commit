# 10872 [팩토리얼] : https://www.acmicpc.net/problem/10872
# case 1 : 메모리 32952KB / 시간 68ms
# math 모듈 활용
import math
N = int(input())
print(math.factorial(N))

# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 72ms
# 단순 반복문 활용
def facto(n):
    # 1부터 n까지 곱함
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

N = int(input())
print(facto(N))


# -------------------------------------------------------------
# case 3 : 메모리 30840KB / 시간 68ms
# 재귀함수 활용
def facto_recursive(n):
    return n * facto(n - 1) if n > 1 else 1

N = int(input())
print(facto_recursive(N))


# -------------------------------------------------------------
# case 4 : 런타임 에러
# reduce 활용
from functools import reduce

def facto_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

N = int(input())
print(facto_reduce(N))


# -------------------------------------------------------------
# case 5 : 메모리 30840KB / 시간 72ms
# cache 사용
def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper

@in_cache
def facto_recursive(n):
    return n * facto_recursive(n-1) if n > 1 else 1


N = int(input())
print(facto_recursive(N))