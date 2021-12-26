'''
백준 1755 [숫자놀이] - silver 4 & 문자열
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다.
79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

[입력]
첫째 줄에 M과 N이 주어진다.

[출력]
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
'''
# M , N = map(int, input().split())
# num_list = [str(i) for i in range(M, N + 1)]
# print(num_list)
# ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

# alphabet = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# print(sorted(alphabet))

# test용
num_list = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

# 숫자 -> 알파벳로 만들어주는 사전 만들기
def convert_to_str(txt):
    dictionary = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    transTable = txt.maketrans(dictionary)
    txt = txt.translate(transTable)
    return txt

# print(convert_to_str('1'))

# 숫자, 알파벳을 포함한 튜플을 원소로하는 알파벳리스트 만들기
# alphabet_list = []
# for num in num_list:
#     if len(num) == 1:
#         alphabet_list.append((num, convert_to_str(num)))
#     else:
#         alphabet_list.append((num, convert_to_str(num[0]), convert_to_str(num[1])))
# # print(alphabet_list)

# # 첫째 자리수 -> 둘째 자리수로 정렬하기
# alphabet_list.sort(key = lambda x : (x[1], x[2]))
# 인덱스 에러


## 다시 풀어보기 - 'two', 'seven'을 'twoseven'으로 아예 합쳐서 하나의 문자로 만들기!

alphabet_list = []
for num in num_list:
    if len(num) == 1:
        alphabet_list.append((num, convert_to_str(num)))
    else:
        alphabet_list.append((num, convert_to_str(num[0]) + " " + convert_to_str(num[1])))

# print(alphabet_list)

# 정렬하기
alphabet_list.sort(key = lambda x : (x[1]))

# print(alphabet_list)

for i in range(len(alphabet_list)):
    if i % 10 == 0 and i!=0:
        print(sep = '\n')
    print(alphabet_list[i][0], end=" ")


################################################################
'''최종 제출 코드'''
M , N = map(int, input().split())
num_list = [str(i) for i in range(M, N + 1)]

def convert_to_str(txt):
    dictionary = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    transTable = txt.maketrans(dictionary)
    txt = txt.translate(transTable)
    return txt

alphabet_list = []
for num in num_list:
    if len(num) == 1:
        alphabet_list.append((num, convert_to_str(num)))
    else:
        alphabet_list.append((num, convert_to_str(num[0]) + " " + convert_to_str(num[1])))

# 정렬하기
alphabet_list.sort(key = lambda x : (x[1]))

for i in range(len(alphabet_list)):
    if i % 10 == 0 and i!=0:
        print(sep = '\n')
    print(alphabet_list[i][0], end=" ")




################################################################
'''dict와 join을 사용해 더 간단하게 푼 코드'''
M, N = map(int, input().split())
dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
alphabet_list = []
for i in range(M, N + 1):
    alphabet = ' '.join([dict[j] for j in str(i)])
    alphabet_list.append([i, alphabet])

alphabet_list.sort(key = lambda x : x[1])

for i in range(len(alphabet_list)):
    if i % 10 == 0 and i != 0:
        print(sep = '\n')
    print(alphabet_list[i][0], end = " ")

# 블로그 정리까지 완료!

