# 1541 [잃어버린 괄호] : https://www.acmicpc.net/problem/1541
# case 1 : 메모리 30840KB / 시간 72ms
'''-나오면 뒤에 괄호쳐서 빼는 수를 크게 하여 최솟값 만들기!'''
nums = input().split('-')
result = 0

# - 앞에 숫자들 결과에 더해주기
for i in nums[0].split('+'):
    result += int(i)

# - 뒤의 숫자들 : 결과에서 빼주기
for i in nums[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 64ms
# -를 기준으로 나눠서 두 부분의 합계를 각각 구함
nums = [sum(map(int, x.split('+'))) for x in input().split('-')]
# print(nums) : 55-50+40 -> [55, 90]
print(nums[0]-sum(nums[1:]))