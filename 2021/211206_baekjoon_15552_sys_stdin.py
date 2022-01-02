'''
백준 15552 [빠른 A+B] -
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
[출력]
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
'''

'''
rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다.
즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다.
참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.'''

## 이해하기 쉬운 코드
import sys
data = []
T = int(sys.stdin.readline())
for i in range(T):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data) # [[1, 1], [12, 34], [5, 500], [40, 60], [1000, 1000]]
for i in data:
    print(sum(i))

## 조금 더 간단하게 쓴 코드
import sys

T = int(sys.stdin.readline())
for i in range(T):
    a, b = (map(int,sys.stdin.readline().split()))
    print(a+b)

'''
[sys.stdin.readline() 배우기]
1. 한 개의 문자열 또는 정수를 입력 받을 때 :
import sys
# 문자열 한 개
str_1 = sys.stdin.readline()
# 정수 한 개
num_1 = int(sys.stdin.readline())

2. 여러 개 정수
ex) 2개
import sys
a, b = map(int, sys.stdin.readline().split())

3. 문자열 N개 입력받아 리스트로 저장
import sys
N = int(sys.stdin.readline())
list_1 = [sys.stdin.readline().strip() for i in range(N)]

[input과 sys.stdin.readline()차이]
 * input() : 입력으로부터 한 줄을 읽은 뒤, 그 때 발생한 개행문자(\n)을 없애고 문자열로 변환한 후 return
 * sys.stdin.readline() : sys라는 모듈의 파일 객체 stdin의 메소드 중 readline()을 사용!
    -> readline()은 입력을 읽을 때 한 번에 한 줄씩 읽는데, 이 말은 여러 줄의 입력이 있을 때 한 줄을 읽고 나면 그 다음 줄을 가리킨다는 뜻이다.
'''