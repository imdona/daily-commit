'''
백준 15792 [A/B - 2]  : for반복문, 수학, 구현, 사칙연산 / 서브테스크(절대/상대오차)에 따라 점수가 다름

두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 A와 B가 주어진다. (0 < A, B ≤ 10,000)

[출력]
첫째 줄에 A/B를 출력한다.
'''
# case 1 : 18점
import sys
num1, num2 = map(int, sys.stdin.readline().split())
print(num1 / num2)


# case 2 : 2000점
num1, num2 = map(int, input().split())
# print(f"num1: {num1}, num2: {num2}") # int

result = (str(num1 // num2)+".")
# print(f"결과 : {result}") # 몫 + .

num1 = (num1 % num2) * 10
# print(f"A를 B로 나눈 나머지(num1) : {num1}")

for _ in range(1000): #계속 10씩 곱해주면서 몫을 뒤에 붙여줌
    # result += str(num1 // num2)
    result = result + str(num1 // num2)
    num1 = (num1 % num2) * 10

print(result)
