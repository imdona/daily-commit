# 10870 [피보나치 수 5] : https://www.acmicpc.net/problem/10870
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