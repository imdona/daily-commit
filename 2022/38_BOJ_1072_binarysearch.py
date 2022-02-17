'''
백준 1072 [게임] - 수학 & 이분 탐색
문제 : https://www.acmicpc.net/problem/1072
김형택은 지금 몰래 Spider Solitaire(스파이더 카드놀이)를 하고 있다. 형택이는 이 게임을 이길 때도 있었지만, 질 때도 있었다.
누군가의 시선이 느껴진 형택이는 게임을 중단하고 코딩을 하기 시작했다. 의심을 피했다고 생각한 형택이는 다시 게임을 켰다. 그 때 형택이는 잠시 코딩을 하는 사이에 자신의 게임 실력이 눈에 띄게 향상된 것을 알았다.
이제 형택이는 앞으로의 모든 게임에서 지지 않는다. 하지만, 형택이는 게임 기록을 삭제 할 수 없기 때문에, 자신의 못하던 예전 기록이 현재 자신의 엄청난 실력을 증명하지 못한다고 생각했다.

게임 기록은 다음과 같이 생겼다.
    - 게임 횟수 : X
    - 이긴 게임 : Y (Z%)
    - Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

[입력]
각 줄에 정수 X와 Y가 주어진다.

[출력]
첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.
'''
# case 1 : 시간 초과, 확인하는 add_game의 값이 너무 커서 이진 분류로 바꿔보자
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = int(Y/X*100)  # round 사용하면 반올림이 되어서 int로 형변환
# print(Z)

add_game = 0  # 추가로 실시한 게임
win_rate = 1  # 승률 : 임시로 1로 정의
while win_rate <= Z:
    if add_game == 1000000000:
        print(-1)
        break

    add_game += 1
    win_rate = int((Y+add_game) / (X+add_game) * 100)
print(add_game)


# ----------------------------------------------------------------
# case 2 : binary search(메모리 30864KB, 시간 80ms)
'''
1. 부동소수점 및 소수점 버리기 주의(반올림x)
    * 참고 블로그
        - https://ahn3330.tistory.com/110
        - https://steemit.com/kr/@modolee/floating-point
2. 이진탐색 end index 범위 주의 : 이미 진 이력이 있어서 승률은 최대 99%까지 올릴 수 있으므로, 99가 승률이 변할 수 있는 최대값임을 이용
'''
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100 // X  # round 사용하면 반올림되고, int 사용시 부동소수점 주의 필요
# Z = int(Y*100 / X)  # 가능
# print(Z)

start, end, answer = 0, X, X  # 시작, 끝 인덱스, 정답(최소 게임 수)

# 이미 진 이력이 있어서 승률은 최대 99%까지 올릴 수 있으므로, 99가 승률이 변할 수 있는 최대값
if Z >= 99: print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        if ((Y + mid)*100) // (X + mid) > Z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)


# ----------------------------------------------------------------
# case 3 : binary search(메모리 30864KB, 시간 76ms)
'''start가 승률을 바꾸는 최소 게임 수!'''
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = int(Y*100 / X) #기존 승률

if Z >= 99: print(-1)
else:
    start, end = 0, 1000000000
    while start <= end:
        mid = (start + end) // 2
        if Z < int((Y + mid)*100 / (X + mid)): end = mid - 1
        else: start = mid + 1
    print(start)


# ----------------------------------------------------------------
# case 4 : binary search(메모리 29056KB, 시간 56ms)
'''divmod 함수 = (몫, 나머지)
a, b 임의의 정수에 대하여 아래 1)과 2)는 같은 값이 return된다
    1) print(a//b, a%b) : 작은 숫자를 다룰 때 빠름
    2) print(*divmod(a, b)) : 큰 숫자를 다룰 때 빠름
* 참고 : https://programmers.co.kr/learn/courses/4008/lessons/12732
'''
import sys

def solve() :
    Z = int(Y*100 / X)  # 기존 승률

    if Z >= 99 : return -1
    else:
        # {게임횟수*(기존 승률 + 1) - 100*이긴게임 / (99 - 기존승률)}
        add_game, res = divmod((X*(Z + 1) - 100*Y), (99 - Z))
        # 나머지가 0이 아니면 게임 횟수 + 1
        if res != 0:
            add_game += 1

        return add_game  # 추가로 해야하는 최소 게임 횟수

X, Y = map(int, sys.stdin.readline().split())
print(solve())