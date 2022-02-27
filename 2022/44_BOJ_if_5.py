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

if M < 45 :
    if H == 0 :
        H = 23
        M += 60
    else :
        H -= 1
        M += 60

print(H, M-45)


# case 2
time = H*60 + M - 45  # 전체시간을 분으로 계산하기(-45분)
print(time//60 % 24, time % 60)


# -------------------------------------------------------------
# 2525 : 오븐 시계
import sys
H, M = map(int, sys.stdin.readline().split())
cook = int(sys.stdin.readline())

time = H*60 + M + cook
print(str(time//60 % 24), str(time%60))


# -------------------------------------------------------------
# 2480 : 주사위 세개
import sys
dice = list(map(int, sys.stdin.readline().split()))

if dice[0] == dice[1] == dice[2]: print(10000 + dice[0]*1000)
elif dice[0] == dice[1] and dice[1] != dice[2]: print(1000 + dice[0]*100)
elif dice[1] == dice[2] and dice[1] != dice[0]: print(1000 + dice[1]*100)
elif dice[0] == dice[2] and dice[1] != dice[0]: print(1000 + dice[0]*100)
else: print(max(dice)*100)


# case 2: dice
A, B, C = map(int, sys.stdin.readline().split())
print(10000 + A*1000 if A == B and A == C else 1000 + A*100 if A==B or A==C
    else 1000 + C*100 if B == C else max(A, B, C)*100)

# 같은 표현
if A == B == C: print(10000 + A*1000)
elif A == B or A == C: print(1000 + A*100)
elif B == C: print(1000 + B*100)
else: print(max(A, B, C) * 100)