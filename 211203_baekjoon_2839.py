'''
백준 2839 [설탕배달]
고민의 흔적 211129 ~ 211203 solve!
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''
# surger = 6
# if surger // 5 > 0:
#     five = surger // 5
#     print(f"five:{five}")
#     surger -= 5* five
#     print(surger)
#     if surger % 3 == 0:
#         three = surger // 3
#         print(f"three:{three}")
#         print(five + three)
#     else:
#         print(-1)
# else:
#     if surger == 3:
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
# surger = int(input())

# # case1
# surger % 3 == 0
# result = surger//3

# # case2
# # surger - (5로 나눈 몫 * 5) = surger
# five = surger//5
# surger -= (five)*5
# three = surger//3
# result = five + three

# # case3
# result = 0

# if surger % 3 == 0: result_1 = surger//3
# if surger //5 > 0:
#     five = surger//5
#     surger -= (five)*5
#     if surger % 3 == 0:
#         three = surger//3
#         result_2 = five + three
#     else:
#         result_2 = five
# print(min(result_1, result_2))


#####################################################
'''
3차시도
1. 결국 5를 먼저 체크해야한다.
2. if문을 나오면 5로 나누어떨어지지 않는 경우 -> 3을 빼고, 봉지수 1증가
3. 2번을 반복하다가 5의 배수가 되면 다시 1번 if문으로
4. 그리고 3보다 작아지면 -1
'''
surger = int(input())

result = 0
while surger >= 0:
    if surger % 5 == 0:
        result += (surger // 5)
        print(result)
        break

    surger -= 3
    result += 1

else:
    print(-1)