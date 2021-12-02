'''
백준 2839 [설탕배달]
고민의 흔적 211129 ~
'''
# N = 6
# if N // 5 > 0:
#     five = N // 5
#     print(f"five:{five}")
#     N -= 5* five
#     print(N)
#     if N % 3 == 0:
#         three = N // 3
#         print(f"three:{three}")
#         print(five + three)
#     else:
#         print(-1)
# else:
#     if N == 3:
#         print(1)
#     else:
#         print(-1)

'''
2차시도
정확하게 킬로그램에 맞추어 배달 => 맞지않으면 -1 출력
1. 3키로만으로 나누어 떨이진다
2. 5킬로 먼저 + 남은거 3키로 나누어 떨어진다
두 가지 상황을 각각 변수로 지정하고 최소값을 출력
이때 나머지가 0이 아니면 -1 출력
'''
surger = int(input())

# case1
surger % 3 == 0
result = surger//3

# case2
# surger - (5로 나눈 몫 * 5) = surger
five = surger//5
surger -= (five)*5
three = surger//3
result = five + three

# case3
result = 0

if surger % 3 == 0: result_1 = surger//3
if surger //5 > 0:
    five = surger//5
    surger -= (five)*5
    if surger % 3 == 0:
        three = surger//3
        result_2 = five + three
    else:
        result_2 = five
print(min(result_1, result_2))
