# 프로그래머스 스택/큐 [기능개발]
# case 1
def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0

    # 모든 작업이 완료될때까지
    while len(progresses) > 0:
        # 100%와 같거나 커지면 없애고 카운트 +1
        if (progresses[0] + day*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # 100%보다 작으면
        else:
            # count가 0보다크면 추가하고 초기화
            if count > 0:
                answer.append(count)
                count = 0
            day += 1

    answer.append(count)
    return answer


# -------------------------------------------------------------
# case 2
# best 풀이법
def solution(progresses, speeds):
    Q=[]
    # zip을 활용해서 기능의 작업률과 속도를 합쳐서 게산이 쉽게 작성
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]