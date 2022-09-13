import sys
# sys.stdin = open("input.txt","r")
'''
대표값
'''
n = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr)/len(arr))
# index, score, diff
current = [-1, -1, avg]
for idx, value in enumerate(arr):
    if abs(value - avg) < current[2]:
        current = [idx+1, value, abs(value - avg)]
    elif abs(value - avg) == current[2]:
        if value > current[1]:
            current = [idx+1, value, abs(value-avg)]
        elif idx < current[0]:
            current = [idx+1, value, abs(value-avg)]
print(avg, current[0])

'''
선수지식 - 최소값 구하기
'''
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 파이썬에서 가장 큰 수
for i in range(len(arr)):
    if arrMin > arr[i]:
        arrMin = arr[i]
print(arrMin)


'''
solution
'''
'''
대표값 문제 오류 수정
round는 round_half_even 방식을 택한다.
정확하게 소수점이 half(0.5)일 때는 결과를 짝수로 만드는 쪽으로 계산
'''
n = int(input())
a = list(map(int, input()))
ave = int(sum(a)/n + 0.5)   # int형 변환 시 소수점 버림
min = 2147000000            # 정수형에서 표현 가능한 가장 큰 수
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
