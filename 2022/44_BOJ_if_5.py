'''
백준 단계별 문제 : if문 7문제
* https://www.acmicpc.net/step/4
'''
# 1330 : 두 수 비교하기
import sys
A, B = map(int, sys.stdin.readline().split())

if A > B: print(">")
elif A < B: print("<")
elif A == B: print("==")

# shot coding
print(">" if A > B else ("<" if A < B else "=="))


# -------------------------------------------------------------
# 9498 : 시험 성적
import sys
grade = int(sys.stdin.readline())

if grade >= 90: print("A")
elif grade >= 80: print("B")
elif grade >= 70: print("C")
elif grade >= 60: print("D")
else: print("F")


# -------------------------------------------------------------
# 2753 : 윤년
import sys
year = int(sys.stdin.readline())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print(1)
else: print(0)


# -------------------------------------------------------------
# 14681 : 사분면 구하기
import sys
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x > 0 and y > 0: print(1)
elif x < 0 and y > 0: print(2)
elif x < 0 and y < 0: print(3)
else: print(4)

# 조금 더 짧게 표현하기
if x > 0: print(1 if y < 0 else 4)
elif x < 0: print(2 if y < 0 else 3)


# -------------------------------------------------------------
# 2884 : 알람 시계
import sys
H, M = map(int, sys.stdin.readline().split())  # 0 ≤ H ≤ 23, 0 ≤ M ≤ 59

