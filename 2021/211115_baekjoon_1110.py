'''
백준 1110 [더하기 사이클]
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
'''

num = int(input())

# 일의 자리 수가 입력될 경우, 0 붙여주기
if num < 10:
    num = num * 10

def change_num(num):
    ''' 더하기 사이클 함수'''
    ''' 십의 자리수와 일의 자리수를 더해준다'''
    add_num = (num // 10) + (num % 10)
    ''' 주어진 수의 일의 자리수는 새로운 수의 십의 자리 수
        더한 수의 일의 자리수는 새로운 수의 일의 자리 수 '''
    new_num = (num % 10)* 10 + add_num % 10
    return new_num

new_num = change_num(num)
count = 1
while num != new_num:
    new_num = change_num(new_num)
    count += 1

print(count)