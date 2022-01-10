'''[팩토리얼]'''
# 재귀적 풀이
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(4))

# 반복문 풀이
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        # print(i) # 1, 2, 3, 4
        result *= i
    return result

print(factorial_loop(4))

########################################################################
'''
[숫자 합]
n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다.
파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요.
n은 11 이상의 자연수라고 가정합시다. 함수 안에 반복문은 쓰면 안됩니다!
'''
# 재귀적 풀이
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # recursive case
    if n == 1:
        return 1
    # recursive case
    return triangle_number(n-1) + n

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))


# 반복문 풀이
def sum_generator(N):
    return sum(n for n in range(1, N+1))

for i in range(1, 11):
    print(sum_generator(i))

########################################################################
'''
[자릿수 합]
파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요.
반복문을 쓰지 말고, 재귀(recursion)의 개념을 활용해주세요!
'''
# 재귀적 풀이
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# 반복문 풀이
print("----for문----")
def sum_digits_loop(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

# 테스트
print(sum_digits_loop(22541))
print(sum_digits_loop(92130))
print(sum_digits_loop(12634))
print(sum_digits_loop(704))
print(sum_digits_loop(3755))

########################################################################
'''
[리스트 뒤집기]
파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해 주는 재귀 함수 flip을 쓰세요.
'''
# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    n = len(some_list)
    # base case
    if n == 1:
        return some_list
    # recursive case
    return some_list[-1:] + flip(some_list[:-1])

'''
list 설명
some_list[-1:] : 맨 마지막 원소만
some_list[:-1] : 맨 마지막 원소 빼고 전체 다
'''
# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 반복문 풀이
def flip_loop(some_list):
    new_list = []
    for i in some_list:
        # insert(위치, '값') : 원하는 인덱스에 원소 삽입
        new_list.insert(0, i)
    return new_list

# 테스트
print('---반복문---')
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flip_loop(some_list))

########################################################################
'''
[이진 탐색 재귀로 구현해보기]
'''
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스로 정의
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None

    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2

    # base case : 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    # recursive case
    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))