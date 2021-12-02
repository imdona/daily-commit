'''
백준 4153 [직각삼각형] - bronze 3
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
'''

while True:
    # nums = list(map(int, input().split()))
    # nums.sort()
    # a, b, c = nums[0], nums[1], nums[2]
    '''위의 세줄과 아래의 한줄의 코드는 같은 의미!
    list.sort() => 기존 list를 정렬(default : 오름차순)
    sorted => 기존 list는 보존, 정렬된 새 list를 리턴 or
            + 현재 예시처럼 int들의 크기를 비교해서 바로 정렬도 가능!'''
    a, b, c = sorted(map(int, input().split()))
    if a + b + c == 0: break
    print("right" if a**2 + b**2 == c**2 else "wrong")


