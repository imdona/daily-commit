def consecutive_sum(start, end):
    # base case : start와 end가 같을 때 예를 들어, 1에서 1까지의 합이라면 1을 리턴!
    if end == start:
        return start

    # Divide : 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine)
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))  # 55
print(consecutive_sum(1, 100))  # 5050
print(consecutive_sum(1, 253))  # 32131
print(consecutive_sum(1, 388))  #75466


# case 2: 분할 정복을 사용하지 않는 just 재귀적 풀이
'''
분할정복은 보통 재귀함수로 구현합니다.
분할정복은 어떤 문제를 나눌 수 없을 때까지 나누어서 각각을 풀어서 다시 합병하여 문제의 답을 얻는 알고리즘이고
재귀는 단순히 함수가 자신을 참조하는 것을 뜻합니다.
consecutive_sum은 분할정복을 사용하는 재귀함수이고 recursive_sum은  분할정복을 사용하지 않는 재귀함수 입니다.
'''
def recursive_sum(start, end):
    if end == start + 1:
        return end + start
    else:
        return end + recursive_sum(start, end - 1)

##############################################################
'''
합병 정렬 알고리즘 중 사용되는 merge 함수 구현하기
정렬된 두 리스트 list1과 list2를 받아서, 하나의 정렬된 리스트를 리턴합니다.
'''
def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    ## 두 리스트 중 소진된 리스트와 소진되지 않은 리스트가 있는지 각각 확인
    # list1은 다 소진 (len(list1)) == i) -> list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list2은 다 소진 (len(list2)) == j) -> list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


# case 2
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # 원소가 남은 리스트가 있으면 뒤에 붙여준다(리스트의 + : 원소 추가)
    merged_list = merged_list + list1[i:] + list2[j:]

    return merged_list


# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))


##############################################################
'''합병 정렬 구현하기 - 위에서 구현한 merge 함수 사용!'''

# 합병 정렬
def merge_sort(my_list):
    # base case : 이미 정렬된 리스트가 있으면 바로 리턴(즉 리스트의 길이가 0 또는 1인 경우)
    if len(my_list) < 2:
        return my_list

    # my_list를 반씩 나눈다(divide)
    left_half = my_list[:len(my_list)//2]    # 왼쪽 반
    right_half = my_list[len(my_list)//2:]   # 오른쪽 반

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left_half), merge_sort(right_half))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


##############################################################
'''
퀵 정렬 구현하기
Divide and Conquer 방식으로 quicksort 함수를 써 보세요.
quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 범위를 나타내는 인덱스 start와 인덱스 end를 받습니다.
merge_sort 함수와 달리 quicksort 함수는 정렬된 새로운 리스트를 리턴하는 게 아니라, 파라미터로 받는 리스트 자체를 정렬시키는 것입니다.

[Divide and Conquer]
- Divide: partition 과정을 통해, pivot을 기준으로 리스트를 나눈다.
- Conquer: pivot 왼쪽 부분과 pivot 오른쪽 부분을 각각 quicksort 함수로 정렬한다.
- Combine: 따로 할 게 없다!
'''
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    #pivot의 최종 인덱스를 리턴해 준다
    return p


# 퀵 정렬
def quicksort(my_list, start = 0, end = None):
    if end == None:
        end = len(my_list) - 1

    # base case
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고, partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)


# ---------------------------------------------------------------
# case 2 : 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p = end
    i = b = start

    while True:
        # i가 p보다 크면 i만 다음칸으로 이동
        if my_list[i] > my_list[p]:
            i += 1
            continue
        # i가 p보다 작으면 i <-> b 자리 바꾸고 둘 다 다음칸으로 이동
        if my_list[i] < my_list[p]:
            swap_elements(my_list, i, b)
            i += 1
            b += 1
            continue
        # i가 pivot이 되면, b <-> p 자리바꾸고 break!
        if my_list[i] == my_list[p]:
            swap_elements(my_list, b, p)
            break

    return my_list.index(p) - 1