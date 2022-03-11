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
# 4948 : 베르트랑 공준






