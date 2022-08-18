import sys
# sys.stdin = open("input.txt","r")
'''
수들의 합
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

if sum(a) < m:
    cnt = 0
elif sum(a) == m:
    cnt = 1
else:
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += a[j]
            if sum == m:
                cnt += 1
            if sum > m:
                break
print(cnt)