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
# case 1 : 한수가 아닌 수 카운트해서 전체에서 빼기 - 메모리 30864KB / 시간 68ms
import sys
num = int(sys.stdin.readline())
count = 0  # 한수가 아닌 수 카운트

for i in range(1, num + 1):
    # 길이가 3자리이거나 4자리일때만 확인(1자리 또는 2자리일때는 무조건 한수임)
    if len(str(i)) == 3 and (int(str(i)[2]) - int(str(i)[1])) != (int(str(i)[1]) - int(str(i)[0])): count += 1
    elif len(str(i)) == 4: count += 1

print(num - count)

# case 1 : (함수로 만들기) 한수가 아닌 수 카운트해서 전체에서 빼기 - 메모리 30864KB / 시간 72ms
import sys
num = int(sys.stdin.readline())

def solve(num):
    count = 0  # 한수가 아닌 수 카운트

    for i in range(1, num + 1):
        # 길이가 3자리이거나 4자리일때만 확인(1자리 또는 2자리일때는 무조건 한수임)
        if len(str(i)) == 3 and (int(str(i)[2]) - int(str(i)[1])) != (int(str(i)[1]) - int(str(i)[0])): count += 1
        elif len(str(i)) == 4: count += 1

    return num - count

print(solve(num))


# case 2 : 한수인 수 카운트 정리
import sys
num = int(sys.stdin.readline())

if num <= 99: sum = num  # 3자리 수 이하일 때는 입력한 수 = 한 수
else:
    sum = 99  # 3자리 수 이상일 때는, 두자리 수까지는 한 수로 카운트하고 시작
    for i in range(100, num + 1):
        if i//100 + i%10 == ((i%100) // 10) * 2: sum += 1

print(sum)

# case 2 : 한수인 수 카운트 이해하기
import sys
num = int(sys.stdin.readline())

if num <= 99: sum = num  # 3자리 수 이하일 때는 입력한 수 = 한 수
else:
    sum = 99  # 3자리 수 이상일 때는, 두자리 수까지는 한 수로 카운트하고 시작
    for i in range(100, num + 1):
        # 첫번째 수 + 세번째 수(2a+2b) == 두번째수(a+b) * 2
        if i//100 + i%10 == ((i%100) // 10) * 2:
            print(i)  # 한수인 수
            print(f"1 : {i//100}")  # 100으로 나눈 몫 : 첫번째 자리 수(a)
            print(f"2 : {i%10}")  # 10으로 나눈 나머지 : 세번째 자리 수(a+2b)
            print(f"3 : {(i%100 // 10) * 2}")  # 두번째 자리 수(a+b) * 2
            sum += 1

print(sum)