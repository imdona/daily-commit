# 오늘의 목표는 level up!
'''
백준 2753 [윤년] - bronze 4
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
'''

# 첫번째 방법
year = int(input())
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400) == 0:
    print('1')
else:
    print('0')

# 두번째 방법 : 삼항연산자
year = int(input())
print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')


################################################################

'''
백준 9498 [시험성적] - bronze 4
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

'''
첫번째 방법 : 조건에 90 < score < 100 이런식으로 안해준 이유는
아래 코드에서 if -> 첫번째 elif -> 두번째 elif -> ... -> else 순으로 실행되기 때문!
'''
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 두번째 방법(숏코딩) : 삼항 연산자 연속으로 사용하고 리스트 인덱스 번호에 맞게 프린트하기!
score = int(input())
print(('A','B','C','D','F')[0 if score>=90 else 1 if score>=80 else 2 if score>=70 else 3 if score>=60 else 4 ])


################################################################
'''
백준 2739 [구구단] - bronze 3
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
'''

N =int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")

# 참고 방법 : 아래처럼 : 뒤에 이어서 작성하여도 된다
N =int(input())
for i in range(1,10):print(f"{N} * {i} = {N*i}")


################################################################
'''
백준 2741 [N 찍기] - bronze 3
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

N =int(input())
for i in range(1, N+1):print(i)

# 숏코딩 방법
print(*range(1,int(input())+1))


################################################################
'''
백준 2742 [기찍 N] - bronze 3
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

N =int(input())

for i in range(N, 0, -1):
    print(i)

# 숏코딩 방법
print(*range(int(input()), 0, -1))


################################################################
'''
백준 2884 [알람시계] - bronze 3
현재 설정한 알람 시각이 주어졌을 때, 이를 45분 앞서게 하기 위해
언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
'''

H, M = map(int, input().split())

if M < 45 : # 분이 45분 보다 작아 음수가 나오는 상황
    if H == 0 : # 시간이 0일때 H -1 +24이므로 H =23
        H = 23
        M += 60
    else :
        H -= 1
        M += 60

print(H, M-45)


################################################################
'''
백준 10818 [최대, 최소] - bronze 3
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
'''

N = int(input())
nums = list(map(int, input().split())) # 입력값들을 map 함수로 int로 바꿔주고 list에 담는다
print(min(nums), max(nums)) #list의 최대 최소값을 구한다


################################################################
'''
백준 10871 [X보다 작은 수] - bronze 3
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
'''

N, X = map(int, input().split())
nums = list(map(int, input().split()))
print(*[num for num in nums if num<X])
# 어제 배운 컨테이너 타입 unpacking하는 방법인 * 사용!


################################################################
'''
백준 10951 [A+B - 4] - bronze 3
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
(테스트 케이스의 개수가 주어지지 않음)
'''

while True:
    try:
        print(sum(map(int, input().split())))
    except:
        break


################################################################
'''
백준 10952 [A+B - 5] - bronze 3
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력의 마지막에는 0 두 개가 들어온다.
'''

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)


################################################################
'''
백준 11720 [숫자의 합] - bronze 2
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
'''

N = int(input())
nums = str(input())
total = 0
for i in nums:
    total += int(i)
print(total)

# 숏코딩 방법
input() # 개수
print(sum(map(int,input()))) #int로만 받아서 바로 sum함수를 이용하기


################################################################
'''
백준 1546 [평균] - bronze 1
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다.
일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다.
그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
'''

N = int(input())
scores = list(map(int, input().split()))
new_scores = [i/max(scores)*100 for i in scores]
print(sum(new_scores)/N)


