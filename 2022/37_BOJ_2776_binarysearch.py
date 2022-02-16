'''
백준 2776 [암기왕]
문제 : https://www.acmicpc.net/problem/2776
연종이는 엄청난 기억력을 가지고 있다. 그래서 하루 동안 본 정수들을 모두 기억 할 수 있다.
하지만 이를 믿을 수 없는 동규는 그의 기억력을 시험해 보기로 한다. 동규는 연종을 따라 다니며, 연종이 하루 동안 본 정수들을 모두 ‘수첩1’에 적어 놓았다.
그것을 바탕으로 그가 진짜 암기왕인지 알아보기 위해, 동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다.
연종은 막힘없이 모두 대답을 했고, 동규는 연종이 봤다고 주장하는 수 들을 ‘수첩2’에 적어 두었다. 집에 돌아온 동규는 답이 맞는지 확인하려 하지만, 연종을 따라다니느라 너무 힘들어서 여러분에게 도움을 요청했다.
동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.

[입력]
첫째 줄에 테스트케이스의 개수 T가 들어온다.
다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다.
그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다.
모든 정수들의 범위는 int 로 한다.

[출력]
‘수첩2’에 적혀있는 M개의 숫자 순서대로, ‘수첩1’에 있으면 1을, 없으면 0을 출력한다.
'''
# case 1 : 재귀(시간 초과)
import sys
T = int(sys.stdin.readline())  # test case

# binary search
def binary_search(element, some_list, start = 0, end = None):
    # end index 따로 주어지지 않으면, 리스트의 마지막 인덱스로 정의
    if end == None: end = len(some_list) - 1

    # start > end 이면 some_list안에 element는 없다
    if start > end: return 0  # 없으면 0 리턴

    mid = (start + end) // 2

    # base case : mid 인덱스 값이 찾는 값(element)인지 확인
    if some_list[mid] == element: return 1  # 찾으면(있으면) 1출력

    # recursive case
    # 찾는 값 < 중간 값 -> 리스트 왼쪽 탐색
    if element < some_list[mid]: return binary_search(element, some_list, start, mid - 1)
    # 찾는 값 > 중간 값 -> 리스트 오른쪽 탐색
    else: return binary_search(element, some_list, mid + 1, end)


for _ in range(T):
    N = int(sys.stdin.readline())  # note 1
    note_1 = sorted(list(map(int, sys.stdin.readline().split())))  # 이진 탐색에서 탐색해야하는 리스트 정렬 꼭!

    M = int(sys.stdin.readline())  # note 2
    note_2 = list(map(int, sys.stdin.readline().split()))

    # print(note_1)
    # print(note_2)

    for element in note_2:
        print(binary_search(element, note_1))


# -------------------------------------------------------------------------------------------------
# case 2 : 메모리 186180KB / 시간 6792ms
import sys
T = int(sys.stdin.readline())  # test case

# binary search
def binary_search(element, some_list, start = 0, end = None):
    # end index 따로 주어지지 않으면, 리스트의 마지막 인덱스로 정의
    if end == None: end = len(some_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if some_list[mid] == element: return 1
        # 중간값 < 찾는 값 -> 리스트 오른쪽 탐색
        elif some_list[mid] < element: start = mid + 1
        # 중간값 > 찾는 값 -> 리스트 왼쪽 탐색
        else: end = mid - 1

    # while문 탈출하면 값이 없다는 의미이므로 0 출력
    return 0


for _ in range(T):
    N = int(sys.stdin.readline())  # note 1
    note_1 = sorted(list(map(int, sys.stdin.readline().split())))  # 이진 탐색에서 탐색해야하는 리스트 정렬 꼭!

    M = int(sys.stdin.readline())  # note 2
    note_2 = list(map(int, sys.stdin.readline().split()))

    for element in note_2:
        print(binary_search(element, note_1))


# -------------------------------------------------------------------------------------------------
# case 3 : 메모리 214708KB / 시간 852ms
import sys
for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline()
    note_1 = set(sys.stdin.readline().split())
    M = sys.stdin.readline()
    print('\n'.join('1' if i in note_1 else '0' for i in sys.stdin.readline().split()))