'''
백준 2775 [부녀회장이 될테야] - 수학
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

[입력]
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

[출력]
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
'''
# 최종 제출 코드(1)
import sys
T = int(sys.stdin.readline())
case = []
for i in range(T):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    people = [k for k in range(1, room+1)]

    for _ in range(floor):
        for k in range(1, room):
            people[k] += people[k-1]
    print(people[-1])

# 해설
import sys
T = int(sys.stdin.readline())
case = []
for i in range(T):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    # 최초 people은 1층 호수별 사람 수 리스트
    people = [k for k in range(1, room+1)]

    # for 문을 돌면서 floor-1층의 호수별 사람 리스트로 업데이트
    for _ in range(floor):
        for k in range(1, room):
            people[k] += people[k-1]
    # 제일 마지막 사람 수 프린트
    print(people[-1])

################################################################

# 최종 제출 코드(2)
from math import comb
T = int(sys.stdin.readline())
for _ in range(T):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    print(comb(room + floor, floor + 1))

# 해설
'''
🔍 조합
조합이란 서로 다른 n개 중에서 r개(n≥r) 취하여 조를 만들 때, 이 하나하나의 조를 n개 중에서 r개 취한 조합이라고 한다.
조합은 순서를 고려하지 않기 때문에 [A, B, C]의 리스트에서 2개의 원소를 골라 나열하면
[(A, B), (A, C), (B, C)] 가 나오게 된다. 조합은 (A, B)와 (B, A)는 같은 것으로 취급한다.

🔍 math.comb(n,k)
    - 반복과 순서 없이 n 개의 항목에서 k 개의 항목을 선택하는 방법의 수를 반환
    - k <= n이면 n! / (k! * (n - k)!)로 평가되고, k > n이면 0으로 평가
    - 식 (1 + x) ** n의 다항식 전개에서 k 번째 항의 계수와 같기 때문에 이항 계수(binomial coefficient)라고도 한다
    * python documentation : https://docs.python.org/ko/3/library/math.html
'''