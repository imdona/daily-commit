'''
백준 13777 [Hunt The Rabbit]
문제 : https://www.acmicpc.net/problem/13777
Mr Farkle was brought up on a farm and spent quite a bit of time in his youth hunting rabbits! He now teaches maths and computing, and came up with a hunting game to help his students learn about the binary search.
He put 50 envelopes at the front of the room, numbered sequentially from 1 to 50. Inside one he hid a rabbit – not a real one, of course, just a card with a rabbit picture on it! He then put cards in all the other envelopes so that if an envelope was chosen with a number lower than the one holding the rabbit, the card would read “Try a higher number”, otherwise the card would read “Try a lower number”.
Students have to find the rabbit using a binary search, and write down the numbers of all the envelopes they open (in order) during their search. Remember, in a binary search you have to pick the middle envelope in the range you are searching. This is easy to find if there is an odd number of envelopes, but with an even number, you have to choose the lower numbered of the two middle envelopes. That means 25 will always be the first envelope checked.

[입력]
Each line of input will be a single number in the range 1 to 50 inclusive, it being the number of the envelope in which Mr Farkle has hidden the rabbit. The final input will be 0 which should not be processed.

[출력]
For each line of input, output the numbers of all envelopes opened, in the order they were opened, until the rabbit is found. Each number must be on the same line separated by a space from the previous number.
'''
# case 1
# 메모리 : 30870KB, 시간 : 68ms
import sys

while True:
    num = int(sys.stdin.readline())
    # input 0이 들어오면 반복문 break!!
    if num == 0: break

    start, end = 1, 50  # 범위 1 ~ 50
    while start <= end:
        mid = (start + end) // 2
        print(mid, end = " ")

        if mid == num: break
        elif mid < num: start = mid + 1
        else: end = mid - 1
    print()


# --------------------------------------------------------------
# case 2 : result 리스트 만들고 unpacking하기
# 메모리 : 30864KB, 시간 : 64ms
import sys
num = int(sys.stdin.readline())

while num:
    start, end, result = 1, 50, []
    while 1:  # while True와 같음
        mid = (end + start) // 2; result += [mid]  # ;은 다음줄
        if mid == num: break
        elif mid < num: start = mid + 1
        else: end = mid - 1
    print(*result); num = int(sys.stdin.readline())