'''
백준 11022 [A+B - 8]  : for반복문, 수학, 구현, 사칙연산 / 11021이랑 거의 동일함
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

[출력]
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
'''
# case 1 : f string
import sys

from sympy import im
N = int(sys.stdin.readline())
for i in range(1, N + 1):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {num1} + {num2} = {num1 + num2}")

# case 2 : range 범위를 N으로 하고, print 할 때 +1 해주기
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {num1} + {num2} = {num1 + num2}")


# case 3 : 다양한 formating 방법 - % 연산자
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i + 1, num1, num2, num1 + num2))


# case 4 : 다양한 formating 방법 - format 메소드
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i + 1, num1, num2, num1 + num2))
