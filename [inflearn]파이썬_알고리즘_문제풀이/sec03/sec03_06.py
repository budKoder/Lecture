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