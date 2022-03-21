import sys

N = int(sys.stdin.readline())
member_list = [sys.stdin.readline().split() for _ in range(N)]

member_list = sorted(member_list, key=lambda x: int(x[0]))
for member in member_list:
    print(' '.join(member))