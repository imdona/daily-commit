'''
백준 1316 [그룹 단어 체커]
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

[출력]
첫째 줄에 그룹 단어의 개수를 출력한다.
'''
## test
# N = int(input())
# words = [input() for _ in range(N)]
# print(words)

## case 1
import sys
N = int(sys.stdin.readline())
# words = [sys.stdin.readline().strip() for _ in range(N)]
# print(words)

count = N  # 처음에 입력된 단어의 갯수

# N만큼 반복해서 단어 하나씩 input받고, 확인
for _ in range(0, N):
    word = sys.stdin.readline()

    # 단어의 길이 -1 만큼 확인
    for i in range(0, len(word) - 1):
        # 다음 알파벳과 같으면 패스
        if word[i] == word[i+1]:
            pass
        # 다음 알파벳과 같지않고, 문장 안에 있으면 count에서 빼준다.
        elif word[i] in word[i+1:]:
            count -= 1
            break
print(count)

# ----------------------------------------------------------------
## case 2 : while 문으로 풀어보기
import sys
N = int(sys.stdin.readline())

count = 0
for _ in range(0, N):
    word = list(sys.stdin.readline())
    index = 0

    # case1과 마찬가지로 단어의 길이 -1보다 커지면 break
    while index < len(word) - 1:
        # 다음 알파벳과 같으면 다음 알파벳 삭제(중복 제거)
        if word[index] == word[index+1]:
            word.pop(index+1)
        # 다음 알파벳과 같지 않으면 index 하나씩 올려주기
        else:
            index += 1
    # 중복을 제거한 길이와 같으면 count + 1
    if len(word) == len(set(word)):
        count += 1

print(count)

# ----------------------------------------------------------------
## case 3 : key = str.find로 sort 하기
count = 0
for i in range(int(input())):
    word = input()
    # key=word.find를 key로 넣어주면 기존 순서를 유지한채로 정렬 : 예를 들어 a, b, c 순으로
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)