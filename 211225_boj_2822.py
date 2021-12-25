'''
백준 2822 [점수 계산]
상근이는 퀴즈쇼의 PD이다. 이 퀴즈쇼의 참가자는 총 8개 문제를 푼다.
참가자는 각 문제를 풀고, 그 문제를 풀었을 때 얻는 점수는 문제를 풀기 시작한 시간부터 경과한 시간과 난이도로 결정한다.
문제를 풀지 못한 경우에는 0점을 받는다. 참가자의 총 점수는 가장 높은 점수 5개의 합이다.
상근이는 잠시 여자친구와 전화 통화를 하느라 참가자의 점수를 계산하지 않고 있었다.
참가자의 8개 문제 점수가 주어졌을 때, 총 점수를 구하는 프로그램을 작성하시오

[입력]
8개 줄에 걸쳐서 각 문제에 대한 참가자의 점수가 주어진다. 점수는 0보다 크거나 같고, 150보다 작거나 같다. 모든 문제에 대한 점수는 서로 다르다.
입력으로 주어지는 순서대로 1번 문제, 2번 문제, ... 8번 문제이다.

[출력]
첫째 줄에 참가자의 총점을 출력한다. 둘째 줄에는 어떤 문제가 최종 점수에 포함되는지를 공백으로 구분하여 출력한다. 출력은 문제 번호가 증가하는 순서이어야 한다.
'''

'''
1. for문 8번 돌면서 점수 리스트 입력받기
2. 내림차순으로 정렬하는 새로운 리스트 만들고, 상위 5개 점수 뽑아서 sum함수로 합계 출력
3. 정렬된 리스트를 돌면서 기존 리스트의 해당 top5점수를 넣어 인덱스번호를 출력
    여기서 주의할 점은, 인덱스번호는 0~7번이지만 문제는 1~8번이므로 +1을 해준다.
4. 마지막으로 *을 이용하여 list를 unpacking하여 프린트해준다.
'''

score_list = [int(input()) for _ in range(8)]
score_sort = sorted(score_list, reverse=True)[:5]
# print(score_list)
# print(score_sort)
print(sum(score_sort))

index_list = []
for score in score_sort:
    index_list.append(score_list.index(score) + 1)
    # print(score_list)
    # print(score)
    # print(score_list.index(score))

index_list.sort()
print(* index_list)

################################# 정리
score_list = [int(input()) for _ in range(8)]
score_sort = sorted(score_list, reverse=True)[:5]
# print(score_sort)
print(sum(score_sort))

index_list = []
for score in score_sort:
    index_list.append(score_list.index(score) + 1)
index_list.sort()
print(* index_list)