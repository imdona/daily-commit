'''
백준 1181 [단어정렬] silver 5
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
[입력]
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
주어지는 문자열의 길이는 50을 넘지 않는다
[출력]
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
'''
# word_list = []
# for i in range(N):
#     word_list.append(input())
'''3 lines -> line by list comprehension'''
word_list = [input() for _ in range(N)]

# str 길이 순으로 정렬
word_list.sort(key=len)

'''첫번째 방법
-> sort(key=len) : 길이 순으로 정렬
sort(key=func) : func는 하나의 값을 취하고 정렬을 안내하는 프록시 값을 반환하는 함수'''
N = int(input())
word_list = [input() for _ in range(N)]
word_list = sorted(list(set(word_list))) # 중복 제거
word_list.sort(key=len) # str 길이 순 정렬
for word in word_list:
    print(word)

'''두번째 방법
1. word, word의 길이인 튜플을 원소로 갖는 리스트로 만든다
2. 정렬 메소드인 sort에 key optional parameter 사용(길이(x[1]) -> 알파벳 순(x[0]) 정렬)'''
N = int(input())
word_list = []
for i in range(N):
    word = str(input())
    word_list.append((word, len(word))) # word, word의 길이인 튜플을 원소로 갖는 리스트로 만든다
word_list = list(set(word_list))
word_list.sort(key = lambda x: (x[1], x[0])) # 정렬 메소드인 sort에 key optional parameter 사용(길이(x[1]) -> 알파벳 순(x[0]) 정렬)
for i in word_list:
    print(i[0])

'''세번째 방법
-> 두번째 방법에서 튜플의 순서를 len, word 순으로 바꾸면 lambda 함수 사용하지 않고 바로 정렬 할 수 있다'''
N = int(input())
word_list = []
for i in range(N):
    word = str(input())
    word_list.append((len(word), word)) # len, word인 튜플을 원소로 갖는 리스트로 만든다
word_list = list(set(word_list))
word_list.sort() # 튜플의 첫번째 값인 len먼저 정렬 -> word 다음으로 알아서 정렬함!
for word_len, word in word_list:
    print(word)



