'''
백준 1018 [체스판 다시 칠하기] - silver 5
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

➡️ 입력예시
    8 8
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBBBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW

[출력]
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''

'''
오답이 나온다 다시 풀기
1. 횟수는 int로, 체스판은 list로 받는다
2. M×N 보드판 전체를 조사한다.
3. 8x8 크기로 잘라내는 경우의 수는 (N-7)x(M-7) -> N-7, M-7 범위 내에서 이중for문을 돌린다.
'''
N, M = map(int, input().split())
chess_list = [input() for j in range(N)]
# print(chess_list)

for j in range(N-7):
    for k in range(M-7):
        w_start = 0
        b_start = 0
        for k in range(j, j+8):
            for board in range(k, k+8):
                if (k+board) % 2 == 0:
                    if chess_list[k][board] != 'W':
                        w_start += 1
                    if chess_list[k][board] != 'B':
                        b_start += 1
                else:
                    if chess_list[k][board] != 'B':
                        w_start += 1
                    if chess_list[k][board] != 'W':
                        b_start += 1

print(min(w_start, b_start))


################################################################
'''min을 구할 때, 그냥 비교하면 안되고, list를 만들어주어야 성공한다'''
N, M = map(int, input().split())
board = [input() for _ in range(N)]
mini_board = []

for i in range(N - 7):
    for j in range(M - 7):
        w_start = 0
        b_start = 0
        for l in range(i, i + 8):
            for k in range(j, j + 8):
                if (k + l)%2 == 0:
                    if board[l][k] != 'W': w_start += 1
                    if board[l][k] != 'B': b_start += 1
                else :
                    if board[l][k] != 'B': w_start += 1
                    if board[l][k] != 'W': b_start += 1
        mini_board.append(w_start)
        mini_board.append(b_start)

print(min(mini_board))