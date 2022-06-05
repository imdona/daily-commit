'''
백준 단계별 문제 : 정렬
* https://www.acmicpc.net/step/9
'''
# 1427 [소트인사이드] - 문자열 & 정렬
# case 1 - 메모리 30864KB / 시간 72ms
N = list(input())
result = sorted(N, reverse=True)
print(*result, sep='')  # unpacking & sep


# case 2: short code - 메모리 29284KB / 시간 52ms
print(''.join(sorted(input())[::-1]))


# case 3 -  메모리 29284KB / 시간 52ms
print("".join(sorted(input(), reverse=True)))


# -------------------------------------------------------------
# 11650 [좌표 정렬하기] - 정렬
N = int(input())
coordinate_list = []

for i in range(N):
    x, y = map(int, input().split())
    coordinate_list.append((x, y))

coordinate_list.sort()

for i in coordinate_list:
    print(i[0], i[1])


# -------------------------------------------------------------
# 11651 [좌표 정렬하기 2] - 정렬
N = int(input())
coordinate_list = []

for i in range(N):
    x, y = map(int, input().split())
    coordinate_list.append((x, y))

# y좌표 먼저 -> x좌표 정렬
coordinate_list.sort(key = lambda x: (x[1], x[0]))

for i in coordinate_list:
    print(i[0], i[1])


# -------------------------------------------------------------
# 1181 [단어 정렬] - 정렬 & 문자열
# case 1
N = int(input())
word_list = [input() for _ in range(N)]
word_list = sorted(list(set(word_list)))  # 중복 제거
word_list.sort(key=len)  # 길이순 정렬

for word in word_list:
    print(word)


# case 2
import sys
word = set()  # 입력받을 때부터 중복 제거
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word = list(word)  # 리스트로 바꿔준다
word.sort()  # 이름 순 정렬
word.sort(key = lambda x:len(x))  # 길이 짧은 순 정렬
print("\n".join(word))


# -------------------------------------------------------------
# 10814 [나이순 정렬] - 정렬
# case 1 - 메모리 45876KB / 시간 272ms
# 입력받기
import sys
N = int(sys.stdin.readline())
member_list = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member_list.append([age, name])

# 정렬
member_list.sort(key = lambda x : x[0])

# 출력
for member in member_list:
    print(*member)


# case 2 - 메모리 61632KB / 시간 292ms
# join & 코드 줄이기
import sys

N = int(sys.stdin.readline())
member_list = [sys.stdin.readline().split() for _ in range(N)]

member_list = sorted(member_list, key=lambda x: int(x[0]))
for member in member_list:
    print(' '.join(member))


# -------------------------------------------------------------
# 18870 [좌표 압축] - 정렬 & 값 / 좌표 압축
'''cf) list.index() 메소드를 사용하면, 시간복잡도가 O(N)임
dict[key] 형태로 출력하면 시간복잡도가 O(1)이라 훨씬 빠름'''
# case 1 - 메모리 148208KB / 시간 2116ms
N = int(input())  # 개수
cord = list(map(int, input().split()))  # 좌표 입력받기

# 중복 제거 후 정렬
new_cord = sorted(list(set(cord)))

# 정렬 값 key - index 번호 값인 dict 만들기
result = {}
for i in range(len(new_cord)):
    result[new_cord[i]] = i

for i in cord:
    print(result[i], end = ' ')


# case 2 - 메모리 200468KB / 시간 1504ms
N = input()
nums = list(map(int, input().split(" ")))

arr = sorted(set((nums)))
num_dict = {n: i for i, n in enumerate(arr)}  # dict comprehension

print(" ".join([str(num_dict[num]) for num in nums]))