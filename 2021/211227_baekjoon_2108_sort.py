'''
백준 2108 [통계학] - silver 4 & 구현, 정렬
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

[출력]
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''

'''
첫번째 풀이방법 : 런타임 에러가 난다.
답은 맞는데, 아무래도 mode를 4000개로 이루어진 행렬로 만들어서 일일이 확인하다보니 그런 것 같다.
'''

# 최종 제출코드(1)
import sys
from collections import Counter
N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술평균
print(round(sum(numbers) / N))

# 중앙값
print(numbers[N // 2])

# 최빈값
count_list = sorted(Counter(numbers).items(), key = lambda x : (-x[1], x[0]))
if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

# 범위 : 최댓값 - 최솟값
print(max(numbers) - min(numbers))

## 풀이 방법 설명
# readline 까먹지않게 사용하면서 친해지기!
import sys
from collections import Counter
N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술평균 : 합계 / 갯수
# print("----------------")
# print(f"산술평균 : {round(sum(numbers) / N)}")
print(round(sum(numbers) / N))

# 중앙값 : 정렬해서 중간위치 - 인덱스는 몫으로
print(numbers[N // 2])

# 최빈값 : 가장 많이 나타나는 값
'''
1. Counter를 이용해서 갯수를 센다
2. 1번의 값은 딕셔너리이므로, items 메소드를 이용해서 (key, value) 튜플을 뽑는다.
3. 문제에 정의된 조건에 따라, value(카운팅 갯수) - key(숫자 자체) 순으로 정렬한다.
4. 인덱스 범위 초과 문제를 해결하기 위해서,
    N = 1일때는 자기자신이 최빈값으로
    N > 1일때는 최빈값이 한 개일 때(= 정렬한 리스트의 첫번째와 두번째 값이 다를 때)는 해당 값을
                최빈값이 두 개 이상일 때는 더 두번째 값(인덱스번호는 1번)을 프린트하는 if문으로 구성하였다.
'''
count_list = sorted(Counter(numbers).items(), key = lambda x : (-x[1], x[0]))
# print(count_list)
if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

# 범위 : 최댓값 - 최솟값
print(max(numbers) - min(numbers))

############################################################################################
# 최종 제출코드(2)
import sys
import statistics as st
from collections import Counter
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

print(round(st.mean(numbers)))
print(st.median(numbers))
count_list = sorted(Counter(numbers).most_common(), key = lambda x : (-x[1], x[0]))

if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

print(max(numbers)-min(numbers))

## 풀이 방법 설명
'''statistics 라이브러리 import해서 풀기 - 산술평균, 중앙값, 범위'''
import sys
import statistics as st
from collections import Counter
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

print(f"산술평균 : {round(st.mean(numbers))}")
print(f"중앙값 : {st.median(numbers)}")
print(f"범위 : {max(numbers)-min(numbers)}")

'''
[mod 최빈값 새로운 method 사용해보기]

Counter에 🔍most_common()이라는 메소드 덕분에 간단한 코드 변경
    - 위에서 작성한 코드와 똑같이 (숫자, 카운팅) 튜플형태로 return된다.

🔍 collections.Counter(a).most_common(n)   : a의 요소를 세어, 리스트에 담긴 튜플형태로 최빈값 n개를 반환하는 메소드
-> documentation을 보면 동일한 갯수의 요소는 처음 발생한 순서대로 정렬이 되어서, 정렬 및 if문으로 확인해주는 절차는 똑같이 해야함!

* collections documentation : https://docs.python.org/3/library/collections.html
'''
count_list = sorted(Counter(numbers).most_common(), key = lambda x : (-x[1], x[0]))

if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

############################################################################################
"""2022.1.1(sat) 새로운 풀이방법으로 풀어보기 도전!
문제 풀면서 입력값이 정수 절대값 4000을 넘지 않는다. 즉 -4000 ~ 4000의 범위 밖에 되지않아서
for문으로 풀어도 가능할 것 같아서 시도해보고싶었다.
풀고 보니 count함수를 쓴것과 비슷했다. 그래도 직접해보니 속이 후련했다.
오늘의 경험 블로깅까지 완료! ➡️ https://imdona.tistory.com/24
"""
# 최종 제출코드(3)
import sys
N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술평균
print(round(sum(numbers) / N))

# 중앙값
print(numbers[N // 2])

# 최빈값
# 숫자, count로 리스트 만들기
count = []
for i in range(-4000, 4001):
    count.append([i, 0])
# num을 돌면서 해당 숫자를 표현하는 인덱스번호에 1을 추가해준다
for num in numbers:
    count[num + 4000][1] += 1
# 갯수 기준으로 정렬
count.sort(key = lambda x: (-x[1], x[0]))
# 출력
if N == 1:
    print(numbers[0])
else:
    if count[0][1] != count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])

# 범위 : 최댓값 - 최솟값
print(max(numbers) - min(numbers))


