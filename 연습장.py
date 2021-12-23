N = int(input())
A = list(map(int, list(input().split())))
B = list(map(int, list(input().split())))

result = 0
for _ in range(N):
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(result)