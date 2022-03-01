'''
백준 단계별 문제 : 함수 3문제
* https://www.acmicpc.net/step/5
'''
# 15596 : 정수 N개의 합
# 함수 이용
def solve(a):
    return sum(a)

# for문 이용
def solve(a):
    total = 0
    for i in a: total += i
    return total


# -------------------------------------------------------------
# 4673 : 셀프 넘버
num = set(range(1, 10001))  # 1 ~ 10000까지의 숫자로 이루어진 set 객체
remove = set()

# 1 ~ 10000까지 반복문을 돌면서 각 자리의 수와 해당 수를 더해준다.(셀프넘버)
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove.add(i)

# 전체 - 셀프넘버 차집합
num = num - remove

# 셀프넘버 아닌 수들만 남기고, 이를 출력
for k in sorted(num):
    print(k)


# -------------------------------------------------------------
# 1065 : 한수
