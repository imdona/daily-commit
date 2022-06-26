# 2447 [별찍기 - 10] : https://www.acmicpc.net/problem/2447
# case 1 : 메모리 35192KB / 시간 108ms
def star(n, first = ['***', '* *', '***']):
    out = []
    if n == 3:
        return first
    else:
        for i in first:
            out.append(i*3)
        for i in first:
            out.append(i + ' '*len(first) + i)
        for i in first:
            out.append(i*3)
        return star(n//3, out)

N = int(input())
for i in star(N):
    print(i)

# -------------------------------------------------------------
# case 2 : 메모리 KB / 시간 ms