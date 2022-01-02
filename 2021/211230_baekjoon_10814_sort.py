'''
백준 10814 [나이순 정렬] - silver 5 & 정렬
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

[출력]
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''
# 최종 제출 코드
import sys
N = int(sys.stdin.readline())
member_list = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member_list.append([age, name])

member_list.sort(key = lambda x : x[0])

for member in member_list:
    print(*member)

# 해설
# 입력받기 : sys와 제법 친해졌다
# age만 int로 바꿔준다
import sys
N = int(sys.stdin.readline())
member_list = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member_list.append([age, name])
print(member_list) # [[21, 'Junkyu'], [21, 'Dohyun'], [20, 'Sunyoung']]

# 정렬 : 나이 기준으로 정해주면, 나이가 같으면 자동으로 가입한 순으로 정렬된다.
member_list.sort(key = lambda x : x[0])
print(member_list) # [[20, 'Sunyoung'], [21, 'Junkyu'], [21, 'Dohyun']]

# 출력 : list unpacking 이용(*)
for member in member_list:
    print(*member)




