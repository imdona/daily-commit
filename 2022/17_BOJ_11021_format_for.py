'''
백준 11021 [A+B - 7]  : for반복문, 수학, 구현, 사칙연산
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

[출력]
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''
# case 1 : f string
import sys
N = int(sys.stdin.readline())
for i in range(1, N + 1):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {num1 + num2}")


# case 2 : range 범위를 N으로 하고, print 할 때 +1 해주기
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {num1 + num2}")


# case 3 : 다양한 formating 방법 - % 연산자
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" % (i + 1, num1 + num2))


# case 4 : 다양한 formating 방법 - format 메소드
import sys
N = int(sys.stdin.readline())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i + 1, num1 + num2))