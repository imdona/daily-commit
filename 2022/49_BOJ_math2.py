'''
백준 단계별 문제 : 기본수학 2
* https://www.acmicpc.net/step/10
'''
# 2581 : 소수 - 수학, 정수론, 소수판정
# case 1 - 메모리 30864KB / 시간 76ms
M = int(input())
N = int(input())
primes = []  # 소수 모으는 리스트

def check_prime(num):
    '''소수인지 확인하고, 소수이면 True, 아니면 False 리턴'''
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(M, N + 1):
    # 소수이면 리스트에 추가
    if check_prime(i) == True:
        primes.append(i)

# 소수들이 존재하면 print, 존재하지않으면 -1
if primes: print(sum(primes), min(primes), sep = "\n")
else: print(-1)


# case 2 - 메모리 29056KB / 시간 60ms
'''
M과 N은 10,000이하의 자연수이므로 10000개의 소수 확인 리스트를 만들어준다.
0, 1는 소수가 아니므로 False, 3이상은 True(임시 정의)로 만들어준다.
'''
arr = [False, False] + [True] * 9999
for i in range(2, 101):
    # arr[i]가 True일때만 즉, 소수가 아니라고 임시 정의된 수만 검사한다
    if arr[i]:
        # i*2부터 10000까지 보폭 i씩(배수이므로 소수가 아니다) -> False로 바꿔준다
        for j in range(i * 2, len(arr), i):
            arr[j] = False

m = int(input())
n = int(input())
nums = [i for i in range(m, n+1) if arr[i]]  # 소수 리스트에서 True인 수만(즉, 소수인 수만) 담은 리스트 생성
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')


# -------------------------------------------------------------
# 11653 : 소인수분해 - 수학, 정수론, 소수판정
# case 1 - 메모리 30864KB / 시간 1464ms (시간 짱 오래걸림)
N = int(input())
i = 2  # 2부터 시작(1, 2는 소수 아니므로)

# 수가 1이 될 때까지(더이상 안나누어 질 때까지)
while N != 1:
    if N % i == 0:
        N = N // i  # 수는 소수로 나누어진 몫으로 바꿔준다
        print(i)
    # 안나누어지면 i를 1씩 올려준다.
    else: i += 1


# case 2 - 메모리 29056KB / 시간 56ms (반복문의 범위를 줄여서 시간을 줄이기)
N = int(input())  # 72
i = 2
r = int(N ** 0.5)  # 8

# 반복문의 범위를 r을 이용해 줄여주기
while i <= r:
    # N % i가 0(True)일때만
    while not N % i:
        print(i)
        N //= i
    # 해당 수로 안나눠질때까지 나누고, + 1
    i += 1

# 반복문 탈출 -> N 자기 자신이 소수일 때
if N > 1:
    print(N)


# -------------------------------------------------------------
# 4948 : 베르트랑 공준 - 수학 & 정수론 & 소수판정 & 에라토스테네스의 체
'''
베르트랑 공준 : 임의의 자연수 n에 대하여, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
예) 10보다 크고 20보다 작은 소수는 4개 있다. (11, 13, 17, 19)
n이 주어졌을 때 n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램(1 ≤ n ≤ 123,456)
'''
# case 1 : 시간초과
while True:
    n = int(input())

    # 0 입력하면 break
    if n == 0: break

    # n ~ 2n 사이의 소수의 개수 출력
    count = 0

    def check_prime(num):
        '''소수인지 확인하고, 소수이면 True, 아니면 False 리턴'''
        if num == 1: return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

    for i in range(n + 1, 2*n + 1):
        # 소수이면 리스트에 추가
        if check_prime(i) == True:
            count += 1

    # 소수개수 프린트
    print(count)


# case 2 : 에라토스테네스의 체 공식을 이용하여, 미리 소수 테이블 구하기 - 메모리 34720KB / 시간 728ms
# 소수 테이블 미리 만들기
prime_arr = [False, False] + [True] * (2*123456 - 1)  # n의 최대값인 12345*2

for i in range(2, int((2*123456)**0.5 + 1)):
    if prime_arr[i]:  # 소수일때만 확인
        j = 2  # i에 곱하는 초기값 정의
        # 범위 줄이기 : 전체가 아니라, i*j가 전체 범위보다 작을 때까지만 반복
        while i*j <= 2*123456:
            prime_arr[i*j] = False  # i에 j를 곱한 값은 소수x
            j += 1

while True:
    n = int(input())
    count = 0

    # 0 입력하면 break
    if n == 0: break

    # n ~ 2n 사이의 소수의 개수 출력
    for k in range(n+1, 2*n + 1):
        if prime_arr[k]: count += 1

    print(count)


# -------------------------------------------------------------
# 9020 : 골드바흐의 추측 - 수학 & 정수론 & 소수판정 & 에라토스테네스의 체
'''
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다.
또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
'''
# case 1 - 메모리 30860KB / 시간 2136ms -> 시간이 너무 오래걸림
# 소수 테이블 미리 만들기
prime_arr = [False, False] + [True]*9999  # n의 최대값인 10000

for i in range(2, int(9999**0.5 + 1)):
    if prime_arr[i]:  # 소수일때만 확인
        j = 2  # i에 곱하는 초기값 정의
        # 범위 줄이기 : 전체가 아니라, i*j가 전체 범위보다 작을 때까지만 반복
        while i*j <= 9999:
            prime_arr[i*j] = False  # i에 j를 곱한 값은 소수x
            j += 1

T = int(input())  # test case
for _ in range(T):
    n = int(input())  # 짝수 입력 : 4 ≤ n ≤ 10,000
    partition = []

    # 2부터 n/2까지 확인
    for i in range(2, n//2 + 1):
        # 짝수 - 소수 = 소수 일때 partition 리스트에 넣기
        if prime_arr[i] == True and prime_arr[n-i] == True:
            partition.append([i, n-i])
        else:
            continue
    # print(partition)  # [[3, 7], [5, 5]]

    # 파티션이 2개 이상일 때 비교
    if len(partition) >= 2:
        abs_value = abs(partition[0][0] - partition[0][1])  # 초기값 정의
        result = 0  # 결과

        # abs가 더 작으면 값 바꿔준다
        for j in partition:
            if abs_value > abs(j[0] - j[1]):
                abs_value = abs(j[0] - j[1])
                result = j

        print(*result)  # unpacking하여 print

    else: print(partition[0][0], partition[0][1])


# case 2 - 메모리 82776KB / 시간 76ms
T = int(input())  # test case
answer = ""

# 소수테이블 만들기
result = [False, False, True] + [True, False] * 5000  # 소수테이블 만들 때 처음부터 짝수는 False로 만들고 시작
# 3부터 확인, 짝수는 건너뛰고 보폭 2씩 확인
for number in range(3, 101, 2):
    # 소수가 아니면
    if result[number]:
        # 수*2를 해당 수의 보폭만큼 False로 바꿔준다
        result[number*2::number] = [False] * len(result[number*2::number])

for _ in range(T):
    N = int(input())  # 짝수 입력

    # 4일 때 결과는 2+2
    if N == 4:
        answer += "2 2\n"
        continue

    # 2로 나누어준다(범위 줄임)
    harf_N = N//2
    # 나머지가 0이면(not 0 == not False == True) -> + 1
    if not harf_N % 2:
        harf_N += 1

    for i in range(harf_N, N, 2):
        if result[i] and result[N-i]:
            answer += f"{N - i} {i}" + "\n"
            break

print(answer, end="")


# -------------------------------------------------------------
# 3009 : 네 번째 점 - 구현 & 기하학
'''세 점 중에 겹치지않는 점이 네번째 점의 좌표이다'''
# case 1 - 메모리 30864KB / 시간 68ms
dots_x = []
dots_y = []

for _ in range(3):
    x, y = input().split()
    dots_x.append(x)
    dots_y.append(y)

# 결과가 1개 인것을 새서 저장한다.
for i in range(3):
    if dots_x.count(dots_x[i]) == 1: result_x = dots_x[i]
    if dots_y.count(dots_y[i]) == 1: result_y = dots_y[i]

print(result_x, result_y)


# case 2 - 메모리 9284KB / 시간 52ms -> 변수를 만들지 않고, 바로 print하니까 메모리가 확실히 절약된다
x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

# 다르면 해당 좌표를 결과좌표로, 같으면 나머지 좌표를 결과좌표로
print(x[0] if x[0] != x[1] else x[2], y[0] if y[0] != y[1] else y[2])