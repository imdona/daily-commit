'''
백준 2839 [설탕배달]
고민의 흔적
'''
N = 6
if N // 5 > 0 and N%:
    five = N // 5
    print(f"five:{five}")
    N -= 5* five
    print(N)
    if N % 3 == 0:
        three = N // 3
        print(f"three:{three}")
        print(five + three)
    else:
        print(-1)
else:
    if N == 3:
        print(1)
    else:
        print(-1)