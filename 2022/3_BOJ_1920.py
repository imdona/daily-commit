import sys
N = int(sys.stdin.readline())
targets = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
problems = list(map(int, sys.stdin.readline().split()))
# print(targets)
# print(problems)

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return 1
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return 0

for i in problems:
    print(binary_search(i, targets))