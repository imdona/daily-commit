'''
백준 2747~8 [피보나치 수]
문제 - https://www.acmicpc.net/problem/2747
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 n번째 피보나치 수를 출력한다.
'''
# case 1: 피보나치 수를 저장시켜 놓을 표(table) 만들기 -  메모리 30860KB/ 시간 80ms
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


# ----------------------------------------------------------------
# case 2: dict로 정의하는 방법
import sys
n = int(sys.stdin.readline())

def fib_tab(n):
    fib_table = {}
    fib_table[1] = 1
    fib_table[2] = 1

    for i in range(3, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

print(fib_tab(n))


# ----------------------------------------------------------------
# case 3: 다른 사람 풀이 공부하기 - 메모리 29288KB/ 시간 52ms
# 피보나치 함수 정의
def recursive(fn1, fn2):
    return fn1 + fn2

import sys
number = int(sys.stdin.readline())

count = 0
array =[]  # 피보나치 수를 담을 array

for i in range(number+1):
    if count >= 2:
        array.append(recursive(array[count-1], array[count-2]))
    elif count == 0:
        array.append(0)
    elif count == 1:
        array.append(1)

    count += 1

print(array[number])
