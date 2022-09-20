import sys
# sys.stdin = open('input.txt',"r")
'''
격자판 최대합
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sums = []
# 행의 합
for i in range(n):
    sums.append(sum(arr[i]))
# 열의 합
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j][i]
    sums.append(sum)
# 대각선의 합
cross1, cross2 = 0, 0
for i in range(n):
    cross1 += arr[i][i]
    cross2 += arr[i][n-1-i]
sums.extend([cross1, cross2])
print(max(sums))

'''
solution
'''
n = list(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 행의 합
        sum2 += a[j][i] # 열의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]     # 대각선 1
    sum2 += a[i][n-i-1] # 대각선 2
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
