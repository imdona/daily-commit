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

################################################################################################
'''
Dynamic Programming - 2. Tabulation 방식
해당 방식은 반복문을 사용해 Table 방식으로 정리하여 접근한다!
    - 1번 피보나치 수는 1, 2번 피보나치 수는 2, 0번 피보나치 수는 임의로 0이라고 지정
    - 최초 피보나치 테이블 리스트 정의
    - 3부터 n까지 Table을 리스트 인덱스에 맞추어 채우고 n번째 항목 리턴
'''
# case 1 : list로 정의하는 방법
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

# ------------------------------------------------------------------------------------------------
# case 2 : dict로 정의하는 방법
'''
* 리스트 - 오브젝트를 순서대로 저장하는 자료구조이고 (e.g. ['Alice', 'Bob']) 데이터 접근은 인덱스로 합니다 (O(1) 연산입니다).

* 사전 - key-value pair들을 저장하는 자료구조이고 (e.g. {'Alice':'01012345678', 'Bob':'01087654321'}) 데이터 접근은 key로 합니다 (O(1) 연산입니다).

따라서 쓰이는 용도가 약간 다릅니다.
만약 전화번호부를 구현하려면 위와 같이 사전으로는 쉽지만 리스트로는 어렵습니다.
쓰이는 용도가 다르기 때문에 두 자료구조를 비교하기는 어렵지만 장점을 몇가지 알려드린다면:

* 리스트 - 리스트 끝에 데이터를 append하는것이 빠르고 인덱스로 데이터 접근도 빠릅니다. 사전에 비해 메모리를 덜 차지합니다.

* 사전 - 탐색 (lookup)이 빠릅니다: 리스트에 'Alice'가 있는지 확인하는것은 O(n) 이지만 사전에 'Alice'가 있는지 확인하는것은 O(1)입니다.

마지막으로 피보나치 수열 문제의 경우 리스트, 사전 둘 다 적합하다고 생각합니다 (굳이 따지자면 리스트가 메모리를 덜 차지할 것 같네요).
'''
def fib_tab(n):
    fib_table = {}
    fib_table[1] = 1
    fib_table[2] = 1

    for i in range(3, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]


################################################################################################
'''
[n번째 피보나치 수를 찾아주는 함수 구현] - 공간 복잡도 O(1)로 구현하기
n번째 피보나치 수를 계산하기 위해서는 가장 최근에 계산한 두 값만 알면 됩니다.
'''
def fib_optimized(n):
    # 1, 2일때로 변수 지정
    previous = 1
    current = 1

    if n < 3: return current

    # 반복문 : 변수 2개에 재할당하여 공간 복잡도 최적화
    for _ in range(3, n + 1):
        previous, current = current, previous + current

    # 피보나치 n번째 수인 current를 리턴한다
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

print(fib_optimized(1))    # 1을 출력
print(fib_optimized(2))    # 1을 출력
print(fib_optimized(3))    # 2을 출력
print(fib_optimized(4))    # 3을 출력
print(fib_optimized(5))    # 5을 출력