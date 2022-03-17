'''
[하노이의 탑]
이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것입니다. 지켜야할 규칙은 두가지입니다:
    1. 한 번에 하나의 원판만 옮길 수 있다.
    2. 큰 원판이 작은 원판 위에 있어서는 안 된다.
하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요.
hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.
'''
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # num_disks : 원판 수, start_peg : 시작하는 기둥 번호, end_peg : 목표 기둥번호
    # base case : 원판이 하나도 없을 때 -> 부분 문제 나누지 않고, 함수를 끝낸다
    if num_disks == 0:
        return
    # recursive case
    else:
        # 기둥이 1, 2, 3 총 3개고 합이 6이므로 전체에서 두 기둥을 빼주면 남는 기둥!
        other_peg = 6 - start_peg - end_peg

        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)

        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)

        # 3. 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)

# 테스트 코드
hanoi(3, 1, 3)

################################################################
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):

    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)

    mid_peg = (6 - start_peg - end_peg)

    hanoi(num_disks-1, start_peg, mid_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, mid_peg, end_peg)
    print(num_disks, start_peg, mid_peg, end_peg)

# 테스트 코드
print('---다른방법---')
hanoi(3, 1, 3)