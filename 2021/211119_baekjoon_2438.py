'''
백준 2438 [별 찍기 -1]
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
'''
N = int(input()) # 반복 횟수 받기
for i in range(N):
    i += 1 # range의 시작은 0부터 N-1까지라서
    print('*' * i) # string type은 *로 반복 프린팅이 가능함