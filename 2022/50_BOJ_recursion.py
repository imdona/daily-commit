'''
백준 단계별 문제 : 재귀
* https://www.acmicpc.net/step/19
'''
# 10872 [팩토리얼]
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


# -------------------------------------------------------------
# 10870 [피보나치수 5]
# case 1: 메모리 30860KB/ 시간 80ms
# 피보나치 수를 저장시켜 놓을 표(table) 만들기(BOJ_2309와 동일하게 풀이) - 재귀
import sys
n = int(sys.stdin.readline())

def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

print(fib_tab(n))


# -------------------------------------------------------------
# case 2 : 메모리 29056KB / 시간 52ms
# 간단하게 피보나치 함수 구현
def fib(num):
    x = 0
    y = 1
    for i in range(num):
        x, y = y, x + y;
    return x

n = int(input())
print(fib(n))


# -------------------------------------------------------------
# case 3 : 메모리 29056KB / 시간 52ms
# 재귀함수로 간단하게 구현
def fib(num):
    if num <= 1: return num
    return fib(num - 1) + fib(num - 2)

n = int(input())
print(fib(n))


# -------------------------------------------------------------
# 17478 [재귀함수가 뭔가요?] - 구현 & 재귀
# case 1 : 재귀 함수 활용
n = int(input())

def chatbot(m):
    print("_" * (4 * (n - m)) + '"재귀함수가 뭔가요?"')

    # 종료 조건 : m이 0이 될 때까지
    if not m:
        print("_" * (4 * (n - m)) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print("_" * (4 * (n - m)) + "라고 답변하였지.")
        return  # None 반환하고 종료

    print("_" * (4 * (n - m)) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("_" * (4 * (n - m)) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("_" * (4 * (n - m)) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    chatbot(m - 1)  # 자기 자신 호출
    print("_" * (4 * (n - m)) + "라고 답변하였지.")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(n)

# case 2 : for 반복문 활용(재귀x)
n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

for i in range(n):
    print("____"*i, "\"재귀함수가 뭔가요?\"", sep="")
    print("____"*i, "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.", sep = "")
    print("____"*i, "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.", sep="")
    print("____"*i, "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"", sep="")
print("____"*n, "\"재귀함수가 뭔가요?\"", sep="")
print("____"*n, "\"재귀함수는 자기 자신을 호출하는 함수라네\"", sep="")

for i in range(n):
    print("____"*(n-i),"라고 답변하였지.",sep="")
print("라고 답변하였지.")


# -------------------------------------------------------------
# 2447 [별찍기 - 10] - 분할 정복 & 재귀
# case 1 : 메모리 35192KB / 시간 108ms
def star(n, first = ['***', '* *', '***']):
    out = []
    if n == 3:
        return first
    else:
        for i in first:
            out.append(i*3)
        for i in first:
            out.append(i + ' '*len(first) + i)
        for i in first:
            out.append(i*3)
        return star(n//3, out)

N = int(input())
for i in star(N):
    print(i)

# -------------------------------------------------------------
# case 2 : 메모리 40188KB / 시간 76ms
N = int(input())

def star(n) :
    if n ==3 :
        return ['***','* *', '***']
    temp = star(n//3)
    stars = []

    for i in temp:
        stars.append(i*3)

    for i in temp:
        stars.append(i+' '*(n//3)+i)

    for i in temp:
        stars.append(i*3)

    return stars

print('\n'.join(star(N)))


# -------------------------------------------------------------
# 11729 [하노이 탑  이동 순서]
