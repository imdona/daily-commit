# N = int(input())
# A = list(map(int, list(input().split())))
# B = list(map(int, list(input().split())))

# result = 0
# for _ in range(N):
#     result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
# print(result)


# txt = "Hi I am Dona!"
# x = "I"
# y = "i"
# mytable = txt.maketrans(x, y)
# print(txt.translate(mytable)) # Hi i am Dona!


# import sys

# # stdout assigned to a variable
# var = sys.stdout
# arr = ['geeks', 'for', 'geeks']

# # printing everything in the same line
# for i in arr:
#     var.write(i)
# # 출력 : geeksforgeeks

# # printing everything in a new line
# for j in arr:
#     var.write('\n'+j)

# '''
# 출력 :
# geeks
# for
# geeks
# '''


# # 소수 테이블 미리 만들기
# prime_arr = [False, False] + [True]*9999  # n의 최대값인 10000

# for i in range(2, int(9999**0.5 + 1)):
#     if prime_arr[i]:  # 소수일때만 확인
#         j = 2  # i에 곱하는 초기값 정의
#         # 범위 줄이기 : 전체가 아니라, i*j가 전체 범위보다 작을 때까지만 반복
#         while i*j <= 9999:
#             prime_arr[i*j] = False  # i에 j를 곱한 값은 소수x
#             j += 1

# T = int(input())  # test case
# for _ in range(T):
#     n = int(input())  # 짝수 입력 : 4 ≤ n ≤ 10,000
#     partition = []

#     # 2부터 n/2까지 확인
#     for i in range(2, n//2 + 1):
#         # 짝수 - 소수 = 소수 일때 partition 리스트에 넣기
#         if prime_arr[i] == True and prime_arr[n-i] == True:
#             partition.append([i, n-i])
#         else:
#             continue
#     # print(partition)  # [[3, 7], [5, 5]]

#     # 파티션이 2개 이상일 때 비교
#     if len(partition) >= 2:
#         abs_value = abs(partition[0][0] - partition[0][1])  # 초기값 정의
#         result = 0  # 결과

#         # abs가 더 작으면 값 바꿔준다
#         for j in partition:
#             if abs_value > abs(j[0] - j[1]):
#                 abs_value = abs(j[0] - j[1])
#                 result = j

#         print(*result)  # unpacking하여 print

#     else: print(partition[0][0], partition[0][1])

# dot1 = list(map(int, input().split()))
# dot2 = list(map(int, input().split()))
# dot3 = list(map(int, input().split()))

# dots = [input().split() for _ in range(3)]
# # print(dots)  # [['5', '5'], ['5', '7'], ['7', '5']]

# dots_x = []
# dots_y = []

# for _ in range(3):
#     x, y = input().split()
#     dots_x.append(x)
#     dots_y.append(y)

# # 결과가 1개 인것을 새서 저장한다.
# for i in range(3):
#     if dots_x.count(dots_x[i]) == 1: result_x = dots_x[i]
#     if dots_y.count(dots_y[i]) == 1: result_y = dots_y[i]

# print(result_x, result_y)

# case 1
# import math
# PI = math.pi
# R = int(input())

# print("{:.6f}".format(PI*R*R))
# print("{:.6f}".format(2*R*R))

# '''
# - 두 원이 일치하는 경우 : d == 0 and r1 == r2 => -1
# - 두 원이 한점에서 만나는 경우(외접, 내접) : d == r1 + r2 or r2 == r1 + d => 1
# - 두 원이 만나지 않는 경우 : r, r1, r2 중 가장 긴 값이 나머지 두 값의 합보다 큼 => 0
# - 두 원이 두 점에서 만나는 경우 : else  => 2
# '''
# T = int(input())  # test case

# for _ in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # 두 원 사이의 거리
#     radius_list = [r1, r2, d]
#     m = max(radius_list)  # 최대값
#     radius_list.remove(m)  # 최대값 제거

#     if d == 0 and r1 == r2: print(-1)
#     elif d == r1 + r2 or m == sum(radius_list): print(1)
#     elif m > sum(radius_list): print(0)
#     else: print(2)


# import sys
# member_list = sys.stdin.read().splitlines()[1:]
# member_list.sort(key = lambda x: int(x.split()[0]))
# sys.stdout.write('\n'.join(member_list))

# def getBinaryNum(num, result = []):
#     a = num // 2
#     b = num % 2
#     result.append(b)
#     if a == 0: return result[::-1]
#     else: return getBinaryNum(a, result)

# n = int(input())
# print(f'{n:2b}')
# # print(*getBinaryNum(n))
# result = getBinaryNum(n)
# for i in result:
#     print(i, end='')

# def getBinaryNum(num, result = []):
#     a = num // 2
#     b = num % 2
#     result.append(b)
#     if a == 0: return result[::-1]
#     else: return getBinaryNum(a, result)

# T = int(input())
# for _ in range(T):
#     bnum = getBinaryNum(int(input()))[::-1]
#     # print(bnum)
#     for i in range(len(bnum)):
#         if bnum[i] == 1:
#             print(i, end = ' ')


n, m = map(int, input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    # (최소공배수 * 최대공약수) = A*B 활용
    return n * m // gcd(n, m)

print(gcd(n, m))
print(lcm(n, m))