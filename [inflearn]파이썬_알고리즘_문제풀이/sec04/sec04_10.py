import sys
# sys.stdin = open("input.txt","r")
'''
역수열(그리디)
'''
n = int(input())
arr = list(map(int, input().split()))
result = [[n+1, False] for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and not result[j][1]:
            result[j][0] = i+1
            result[j][1] = True
            break

        if result[j][0] > i and not result[j][1]:
            cnt += 1
for i in range(n):
    print(result[i][0],end=' ')