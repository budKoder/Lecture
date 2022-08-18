import sys
# sys.stdin = open("input.txt","r")
'''
격자판 회문수
'''
n = 7
m = 5
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
# 가로
for row in range(n):
    for col in range(n-m+1):
        if arr[row][col:col+m] == list(reversed(arr[row][col:col+m])):
            cnt += 1
# 세로
for col in range(n):
    for row in range(n-m+1):
        nums = []
        for x in range(m):
            nums.append(arr[row+x][col])
        if nums == list(reversed(nums)):
            cnt += 1
print(cnt)
