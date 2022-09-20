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

'''
solution
'''
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
