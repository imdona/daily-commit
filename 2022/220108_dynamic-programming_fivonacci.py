'''
Dynamic Programming - 1. Memoization 방식
해당 방식은 재귀 함수를 사용한다!
재귀 함수를 작성할 때에는 base case와 recursive case에 대해 생각해야 함
    - Recursive case: 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우
    - Base case: 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우
'''
def fib_memo(n, cache):
    # cache[n]이 존재하면 cache[n]을 리턴하고, 아니면 cache[n]값을 구하고 cache[n]을 리턴
    # base case
    if n < 3:
        return 1

    # recursive case
    # 이미 n번째 피보나치를 계산했으면: 저장된 값을 바로 리턴
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면: 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n -1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

'''
Dynamic Programming - 2. Tabulation 방식
해당 방식은 반복문을 사용해 Table 방식으로 정리하여 접근한다!
    - 1번 피보나치 수는 1, 2번 피보나치 수는 2, 0번 피보나치 수는 임의로 0이라고 지정
    - 최초 피보나치 테이블 리스트 정의
    - 3부터 n까지 Table을 리스트 인덱스에 맞추어 채우고 n번째 항목 리턴
'''
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))