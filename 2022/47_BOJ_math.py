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