# 2309 [일곱 난쟁이] : https://www.acmicpc.net/problem/2309
# case 1 : 메모리 30840KB / 시간 68ms
dwarf = [int(input()) for _ in range(9)]  # 난쟁이들의 키를 담은 리스트

total = sum(dwarf)  # 키 합계

for i in range(9):
    for j in range(i+1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            dwarf.pop(j)  # 뒤에서 부터 삭제(인덱스 번호 바뀔 수 있으니까)
            dwarf.pop(i)
            break
    if len(dwarf) == 7: break

# 정렬해서 리스트 순서대로 출력
for d in sorted(dwarf):
    print(d)


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 80ms
# enumerate 활용
dwarf = [int(input()) for _ in range(9)]  # 난쟁이들의 키를 담은 리스트
dwarf.sort()  # 미리 정렬
total = sum(dwarf)  # 키 합계

for i in range(9):
    for j in range(9):
        # 같은 인덱스 고를 때는 pass
        if i == j:
            continue
        else:
            if total - dwarf[i] - dwarf[j] == 100:
                c = i; d = j
                break
    # 이중 for문 break
    if i != j and total - dwarf[i] - dwarf[j] == 100:
        break

for x, y in enumerate(dwarf):
    if x == c or x == d:
        continue
    else:
        print(y)