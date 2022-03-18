'''
백준 단계별 문제 : 정렬
* https://www.acmicpc.net/step/9
'''
# 1427 [소트인사이드] - 문자열 & 정렬
# case 1 - 메모리 30864KB / 시간 72ms
N = list(input())
result = sorted(N, reverse=True)
print(*result, sep='')  # unpacking & sep


# case 2: short code - 메모리 29284KB / 시간 52ms
print(''.join(sorted(input())[::-1]))


# case 3 -  메모리 29284KB / 시간 52ms
print("".join(sorted(input(), reverse=True)))