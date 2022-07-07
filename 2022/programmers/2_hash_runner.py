# case 1
def solution(participant, completion):
	# 두 리스트 모두 정렬
    participant.sort()
    completion.sort()

    # 완료 리스트의 길이만큼 반복하여 확인
    for i in range(len(completion)):
        # 같은 원소가 아니면 출력
        if participant[i] != completion[i]:
            return participant[i]
    # 리스트를 다 돌아도 없으면 마지막 원소
    return participant[len(participant)-1]


# -------------------------------------------------------------
# case 2 : 해시
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        # 참가자를 해시에 넣어주기
        dic[hash(part)] = part
        temp += int(hash(part))  # 해시값 합계

    for com in completion:
        # 완주자의 해시값을 합계에서 빼주기
        temp -= hash(com)
    # 나머지 해시값이 미완주자
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))



# -------------------------------------------------------------
# case 3 : collections 활용(가장 간단!)
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]