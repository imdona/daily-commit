'''
백준 단계별 문제 : 기본수학 1
* https://www.acmicpc.net/step/8
'''
# 1712 : 손익분기점 - 수학 & 사칙연산
# case 1 : 시간 초과
import sys
fix, var, cost = map(int, map(int, sys.stdin.readline().split()))

def solve(fix, var, cost):
    for num in range(1, 2100000000):
        total = fix + num * var
        income = num * cost

        if income > total:
            return num
            break

    return -1

if __name__ == '__main__':
    print(solve(fix, var, cost))


# case 2 : 가변비용 >= 노트북 가격보다 같거나 크면 손익분기점 존재 x
'''
손익분기점이 발생할 시점
fix + num * var = income = num * cost
fix = num(cost - var)
num = fix // (cost - var)  -> 판매량(몫)
보다 클 때!니까 + 1
'''
import sys
fix, var, cost = map(int, map(int, sys.stdin.readline().split()))

if var >= cost:
    # 가변비용 >= 노트북가격 이면 손익분기점이 존재하지 않음
    print(-1)
else:
    # 손익분기점이 최초로 발생하는 시점의 판매량(몫) + 1
    print(fix // (cost - var) + 1)

# -------------------------------------------------------------
# 1193 [분수찾기] - 수학 & 구현
'''
[의사코드]
결과
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> 1/4 -> 2/3 -> 3/2 -> 4/1 -> 5/1 -> ...
합
2 -> 3-> 3 -> 4 -> 4 -> 4-> 5 -> 5-> 5 -> 5 -> 6 -> ...

정수를 나눌 수 있는 정수의 경우의 수로 나누고,

2 = (1, 1) -> 1
3 = (1, 2), (2, 1)  # [0]이 작은 것 부터 -> 2, 3
4 = (3, 1), (2, 2), (1, 3)  # [0]이 큰 것 부터 -> 4, 5, 6
5 = (1, 4), (2, 3), (3, 2), (4, 1)  # [0]이 작은 것 부터 -> 7, 8, 9, 10
6 = (5, 1)  # [0]이 큰 것 부터 -> 11, 12, 13, 14, 15
...

입력값의 범위가 X(1 ≤ X ≤ 10,000,000) 이므로, 그때 그때 계산을 하자.
'''
import sys
X = int(sys.stdin.readline())





# -------------------------------------------------------------
# 10757 [큰 수 A+B] - 수학, 구현, 사칙연산, 임의 정밀도 / 큰 수 연산
# case 1 - 메모리 : 30864KB	/ 시간 : 76ms
import sys
A, B = map(int, sys.stdin.readline().split())
print(A+B)


# case 2: short - 메모리 : 29284KB	/ 시간 : 56ms
print(sum(map(int,input().split())))