# N = int(input())
# A = list(map(int, list(input().split())))
# B = list(map(int, list(input().split())))

# result = 0
# for _ in range(N):
#     result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
# print(result)


# txt = "Hi I am Dona!"
# x = "I"
# y = "i"
# mytable = txt.maketrans(x, y)
# print(txt.translate(mytable)) # Hi i am Dona!


import sys

# stdout assigned to a variable
var = sys.stdout
arr = ['geeks', 'for', 'geeks']

# printing everything in the same line
for i in arr:
    var.write(i)
# 출력 : geeksforgeeks

# printing everything in a new line
for j in arr:
    var.write('\n'+j)

'''
출력 :
geeks
for
geeks
'''







