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

'''
출력 :
geeks
for
geeks
'''


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
import math
PI = math.pi
R = int(input())

print("{:.6f}".format(PI*R*R))
print("{:.6f}".format(2*R*R))



