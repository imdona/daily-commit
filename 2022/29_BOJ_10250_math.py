'''
백준 10250 [호텔] - 수학, 구현, 사칙연산
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 여러분은 지우를 도와 줄 프로그램을 작성하고자 한다. 즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.
문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자. 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99). 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고). 이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다.
또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.
방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다. 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.
손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다. 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.
여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

그림참고 : https://www.acmicpc.net/problem/10250

[입력]
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).

[출력]
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.
'''
'''
의사 코드 작성해보기
* 선호하는 방을 들어가는 순서 : 101호 -> 201호 -> 301호 -> ... -> x01호 (x : height) -> 102호 -> 202호 -> ... -> ... ->
* 규칙을 생각해보면 :
    1) 예 : height = 10이라하면,
        8번째는 801호, (8 % 10 = 나머지 8 -> 층, 8 // 10 = 몫 0 + 1 = 1 -> 방번호)
        9번째는 901호, (9 % 10 = 나머지 9 -> 층, 9 // 10 = 몫 0 + 1 = 1 -> 방번호)
        10번째는 1001호, (10 % 10 = 나머지 0 -> 나누어떨어지면 높이로 10 , 10 // 10 = 몫 1 + 1 = 2 - 1 = 1 -> 방번호)
        11번째가 102호, (11 % 10 = 나머지 1 -> 층, 11 // 10 = 몫 1 + 1 = 2 -> 방번호)
        12번째가 202호 (12 % 10 = 나머지 2 -> 층, 12 // 10 = 몫 1 + 1 = 2 -> 방번호)
    2) 손님이 들어가는 층 : 손님 순서 % 높이 (나머지)
    3) 손님이 들어가는 방 번호 : 손님 순서 // 높이 + 1 (몫+1)
    4) height와 동일한 손님 순서는 예외처리 해줄 것
'''
# case 1
import sys
T = int(sys.stdin.readline())  # test case

for _ in range(T):
    height, room, customer = map(int, sys.stdin.readline().split())
    # print(height, room, customer)

    floor = customer % height  # 층 번호
    room_number = customer // height + 1  # 방 번호

    # 예외처리 : 고객순서 % 높이가 0으로 나누어떨어질 때
    if floor == 0:
        room_number -= 1
        floor = height

    # print(floor, room_number)
    print(floor * 100 + room_number)


# -------------------------------------------------------------------------
# case 2
import sys
T = int(sys.stdin.readline())  # test case

for _ in range(T):
    height, room, customer = map(int, sys.stdin.readline().split())

    '''
    * 규칙 : 아예 손님순서 -1을 해주고 나머지, 몫을 구하고 +1 해주기(예외처리 할 것 없이)
        1) 예 : height = 10이라하면,
            8번째는 801호, ((8-1) % 10 = 나머지 7 + 1 -> 8층, (8-1) // 10 = 몫 0 + 1 = 1 -> 방번호)
            9번째는 901호, ((9-1) % 10 = 나머지 8 + 1 -> 9층, (9-1) // 10 = 몫 0 + 1 = 1 -> 방번호)
            10번째는 1001호, ((10-1) % 10 = 나머지 9 + 1 -> 10층, (10-1) // 10 = 몫 0 + 1 = 1 -> 방번호)
            11번째가 102호, ((11-1) % 10 = 나머지 0 + 1 -> 1층, (11-1) // 10 = 몫 1 + 1 = 2 -> 방번호)
            12번째가 202호 ((12-1) % 10 = 나머지 1 + 1 -> 2층, (12-1) // 10 = 몫 1 + 1 = 2 -> 방번호)
        2) 손님이 들어가는 층 : (손님 순서-1) % 높이 (나머지) + 1
        3) 손님이 들어가는 방 번호 : (손님 순서-1) // 높이 (몫) + 1

    * '방번호'.rjust(2, '0') : 방번호가 두자리이면 그대로, 두자리가 아니면 앞에 0을 채워준다 굿!'''
    # print(str((customer-1)%height + 1) + str((customer-1)//height + 1))  # 42, 123
    print(str((customer-1)%height + 1) + str((customer-1)//height + 1).rjust(2,'0'))  # 402, 1203