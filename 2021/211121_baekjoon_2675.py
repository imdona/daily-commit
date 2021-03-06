'''
백준 2575 [문자열 반복]
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
'''

T = int(input()) # 테스트 케이스 개수

for i in range(T):
    R, S = input().split() # 각각 반복횟수, 문자열 - 테스트 케이스 개수만큼 반복해야하므로 for문 안으로!
    for j in S:
        print(j * int(R), end='')
    print() # 줄 바꾸기
