num = int(input())
grades_int = list(map(int, input().split()))

max_grade = max(grades_int)
new_grade = [i / max_grade * 100 for i in grades_int]

print(sum(new_grade) / num)
