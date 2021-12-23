'''
백준 2609 [최대공약수와 최소공배수]
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

[출력]
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''
'''
* 공약수 : 두 수 사이에서 공통으로 존재하는 약수
* 최대공약수 : 공약수 중에 가장 큰 공약수
* 공배수 : 두 수의 공통적인 배수
* 최소공배수 : 공배수 중에 제일 작은 공배수

🥕 최대공약수(GCD(Great Common Divisor))
1. num1과 num2 중 작은 수부터 1까지 거꾸로 for문을 돈다
2. 1번 for문의 값을 num1과 num2로 둘 다 나누어지는 수를 gcd라고 한다.
3. gcd가 생기면 for문을 num2reak한다(이유 : 더 돌면 최대공약수보다 작은 약수가 gcd 변수에 들어갈 수 있음)

🥕 최소공배수(LCM(Least Common Multiple))
1. num1과 num2 중 큰 수부터 num1*num2(두 수의 곱)까지 for문을 돈다.
    (최소공배수는 어차피 두 수의 배수들의 공통값이기때문에 큰 수부터 시작하자!)
    (범위는 입력값에서 10000이 최대라고해서 최대값까지 했다. 어차피 최소공배수가 나오면 num2reak된다.)
2. 1번 for문의 값으로 num1과 num2를 나누어서 0이 되는 수를 lcm이라고 한다.
'''
# 풀이1) 그런데 런타임 에러가 났다.
num1, num2 = map(int, map(int, input().split()))
for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break
for j in range(max(num1, num2), 10000):
    if j % num1 == 0 and j % num2 == 0:
        lcm = j
        break
print(gcd)
print(lcm)

### 풀이2) 이미 구현이 되어있는 math 모듈을 임포트해서 사용할 수 있다.
import math

num1, num2 = map(int, input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))

### 풀이3) 유클리드 호재법
'''
🥕🥕유클리드 호재법 : 두 수의 최대공약수를 구하는 알고리즘
호재법 : 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘
MOD연산 : 두 값을 나눈 나머지를 구하는 연산
=> 유클리드 호재법 사용하기
    1. 큰 수를 작은 수로 나눈 나머지를 구한다.( = MOD연산)
    2. 작은 수와 1번의 연산에서 나온 나머지로 또 MOD연산을 한다.
    3. 반복한다.
    4. 나머지가 0이 되었을 때, 마지막 계산에서 나누는 수로 사용된 숫자가 최초 두 수의 최대공약수가 된다.
    예제)   1112 mod 695 = 417
            695 mod 417 = 278
            417 mod 278 = 139
            278 mod 139 = 0
            => 139는 1112와 695의 최대공약수!
* 유클리드 호제법은 나눗셈만 반복해서 최대공약수(GCD)를 구할 수 있다.
* 두 개의 수가 아무리 커도 정해진 순서로 계산하면 효율적으로 최대공약수를 구할 수 있다.
'''
'''
💻 code
1. gcd(a, b)
    계속해서 a를 b로 나누어서 b를 a에 나눈 나머지 b를 대입시켜서 b가 0이 될때까지 반복하면
    남는 a의 값이 최대공약수가 된다

def gcd(a, b):
    while b > 0:
    a, b = b, a % b
return a


2. lcm(a, b)
    a, b의 곱을 a, b의 최대공약수로 나눈 값이다.(몫 : //)

* gcd * lcm= num1 * num2


def lcm(a, b):
    return a * b // gcd(a, b)
'''

### 유클리드 호재법으로 풀기

num1, num2 = map(int, input().split())

def gcd(num1, num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

print(gcd(num1, num2))
print(lcm(num1, num2))