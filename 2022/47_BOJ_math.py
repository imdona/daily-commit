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

[그룹]
1. 2 = (1, 1) -> 1
2. 3 = (1, 2), (2, 1) -> 2, 3
3. 4 = (3, 1), (2, 2), (1, 3) -> 4, 5, 6
4. 5 = (1, 4), (2, 3), (3, 2), (4, 1)  -> 7, 8, 9, 10
5. 6 = (5, 1), (4, 2), (3, 3), (2, 4), (1, 5) -> 11, 12, 13, 14, 15

=>  * 홀수 그룹
        - top : [1] -> [3, 2, 1] -> [5, 4, 3, 2, 1] -> ...
        - bottom : [1] -> [1, 2, 3] -> [1, 2, 3, 4, 5] -> ...
    * 짝수 그룹
        - top : [1, 2] -> [1, 2, 3, 4] -> ...
        - bottom : [2, 1] -> [4, 3, 2, 1] -> ...
...

입력값의 범위가 X(1 ≤ X ≤ 10,000,000) 이므로, 그때 그때 계산을 하자.
'''
# case 1 : 메모리 30864KB / 시간 68ms
import sys
X = int(sys.stdin.readline())  # X = 14(홀수 예) // 10(짝수 예)
group = 1

# 입력된 수  X가 속하는 [그룹] 구하기
while X > group:
    '''각 그룹은 그룹 번호의 수만큼의 개수를 가지고 있다.
        입력값 = 입력값 - 그룹의 갯수
        그룹의수 += 1 : 1씩 카운트 하면서 올린다.
        => 그룹의 수만큼 뺀 (X =< 그룹) 일때까지 반복
        => X는 그룹에서 몇번째 수인지'''
    X -= group  # 14 -> 13, 11, 8, 4 // 10 -> 9, 7, 4
    group += 1  # 1 -> 2, 3, 4, 5 //  1 -> 2, 3, 4

# print(group)  # X가 14일 때, 그룹5 (6의 합들로 이루어짐)에 속함 // 10일 때, 그룹 4


if group % 2 == 0:
    # 짝수번 그룹
    top = X  # 4
    bottom = group - X + 1  # 4 - 4 + 1

else:
    # 홀수번 그룹
    top = group - X + 1  # 5 - 4 + 1
    bottom = X  # 5

print(f"{top}/{bottom}")


# case 2 : 메모리 29200KB / 시간 64ms
X = int(input())
group = 1

while X > group:
    X, group = X - group, group + 1

top, bottom = X, group - X + 1  # 짝수면 그대로

# 홀수면 방향 바꿔주기
if group % 2 == 1:
    top, bottom = bottom, top

print(str(top)+"/"+str(bottom))

# -------------------------------------------------------------
# 10757 [큰 수 A+B] - 수학, 구현, 사칙연산, 임의 정밀도 / 큰 수 연산
# case 1 - 메모리 : 30864KB	/ 시간 : 76ms
import sys
A, B = map(int, sys.stdin.readline().split())
print(A+B)


# case 2: short - 메모리 : 29284KB	/ 시간 : 56ms
print(sum(map(int,input().split())))