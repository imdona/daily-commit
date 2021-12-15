'''
백준 2750 [수 정렬하기]
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

[출력]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

'''
1. chance 횟수 input으로 받기
2. 숫자들은 횟수만큼 for문으로 리스트로 받기
3. sort로 정렬 - 오름차순
4. 정렬된 리스트 하나씩 print
'''
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
for i in nums:
    print(i)


'''
다른 풀이 방법 : 버블 정렬(bubble sort)
🧼 버블정렬이란?
서로 인접한 두 원소를 검사하여 정렬하는 알고리즘 -> 인접한 2개의 레코드를 비교해서 크기 순서대로 되어있지 않으면 서로 교환한다.
'''
N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(len(nums)) :
    for j in range(len(nums)) :
        if nums[i] < nums[j] :
            nums[i], nums[j] = nums[j], nums[i]

for i in nums:
    print(i)


'''
다른 풀이 방법 : 삽입 정렬(insert sort)
🤔 삽입 정렬이란?
자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
매 순서마다 해당 원소를 삽입할 수 있는 위치를 찾아 해당 위치에 넣는다.
두번째 자료부터 시작하여 끝까지 회전한다.
'''
N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        i -= 1

for i in nums:
    print(i)