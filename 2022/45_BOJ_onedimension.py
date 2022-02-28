'''
백준 단계별 문제 : 1차원 배열 7문제
* https://www.acmicpc.net/step/6
'''
# 4344: 평균은 넘겠지
import sys
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    grades = list(map(int, sys.stdin.readline().split()))
    mean = sum(grades[1:]) / grades[0]  # 평균 = 합계 + 갯수
    count = 0

    for i in grades[1:]:
        if i > mean: count += 1

    # print(f"{round(count / grades[0] * 100, 3)}%")
    print(f"{format(count / grades[0] * 100, '.3f')}%")


    # 같은 표현
    print("{:.3f}%".format(count / grades[0] * 100))

'''소수점 n번째 자리까지 0으로 채우는 방법 : format 함수
1. round 함수 : 반올림함수로, 소수점 3자리까지 표시하라고 설정을 해도 끝자리가 0이면 그 이상 출력하지 않음.
2. format 함수 : 출력되는 소수점의 개수에 대한 서식을 지정할 수 있음
    [example]
    1) format(count / grades[0] * 100, '.3f')
    2) "{:.3f}".format(count / grades[0] * 100)
    유용한 표현이니 기억하자!
'''