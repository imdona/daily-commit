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
#