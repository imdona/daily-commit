'''
백준 1978 [소수 찾기] - silver 4
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

[입력]
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
[출력]
주어진 수들 중 소수의 개수를 출력한다.
'''

'''
소수 : 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수 (1은 포함하지않음)
약수 : 어떤 수나 식을 나누어 나머지가 없이 떨어지는 수

1. 횟수는 정수로, 확인해야할 숫자는 리스트로 받기
2. for문을 돌면서 약수 리스트를 return 해주는 함수 만들기
3. 확인해야할 리스트를 map으로 2번에서 만든 함수로 적용해주기
4. 원소 중 길이가 2인(즉 1과 자기자신인) 리스트가 있으면, 소수 count += 1
5. 소수 print!
'''
N = int(input())
numbers = map(int, list(input().split()))
# numbers = list(map(int, list(input().split())))
# print(numbers) # <map object at 0x1044b2260>
# print(list(numbers)) # [1, 3, 5, 7]

def get_divisor(num):
    divisor_list = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list

divisor_list = map(get_divisor, numbers)
# divisor_list = list(map(get_divisor, numbers))
# print(divisor_list) # [[1], [1, 3], [1, 5], [1, 7]]

prime_num = 0
for i in divisor_list:
    if len(i) == 2:
        prime_num += 1
print(prime_num)

'''
다른 풀이방법
1. 아예 range(2, num)으로 두어 1을 제외하고 시작한다
2. num이 0으로 나누어떨어진다 -> 1외에 나누어지는 수가 있다 -> 소수가 아니다.
3. 2번 상황이면 False 상황으로 두고 소수 카운트를 +=1 해준다!
'''
N = int(input())
numbers = map(int, list(input().split()))

prime_num = 0
for num in numbers:
    condition = True
    if num <= 1:continue
    for i in range(2, num):
        if num % i == 0:
            condition = False
            break
    if condition:
        prime_num += 1

print(prime_num)

'''추가개념 - map에 대한 이해
1. map으로 함수를 적용한 결과를 보고싶을 때는 list로 데이터 타입을 변형하여 print
2. for문을 돌때는 list로 변형하지않아도 괜찮다 -> 그 이유는 map object에서 하나씩 꺼내서 보여주기때문에'''