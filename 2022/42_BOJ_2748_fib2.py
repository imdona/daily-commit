'''
백준 2749 [피보나치 수 3] - 수학 & 분할 정복을 이용한 거듭제곱
    * 앞서 풀었던 피보나치 수  1, 2보다 입력값이 크다. 기존의 방식으로 풀면 메모리 초과!!
    기존의 방식의 시간 복잡도는 O(N)으로, N의 값이 커진 해당 문제에서는 시간복잡도가 매우 높아 적절한 방법이 아니다.
    여기서 사용하는 개념이 '피사노 주기'인데, 피보나치 수를 k로 나눈 나머지는 항상 주기를 갖게된다는 원리이다.
    * 피사노 주기 : N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.

문제 - https://www.acmicpc.net/problem/2749
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 n번째 피보나치 수를 1,000,000으로 나눈 나머지를 출력한다.
'''
# case 1
import sys
n = int(sys.stdin.readline())

def fib_table_tab(n):
    mod = 1000000
    p = mod // 10*15
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다(p까지)
    for i in range(3, p):
        fib_table_table.append(fib_table_table[i - 1] + fib_table_table[i - 2])
        fib_table_table[i] %= mod

    # 피사노 주기 : N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
    return fib_table_table[n%p]

print(fib_table_tab(n))
