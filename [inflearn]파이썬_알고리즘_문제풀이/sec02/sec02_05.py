import sys
# sys.stdin = open("input.txt","r")
'''
정다면체
'''
n, m = map(int, input().split())
prob = [0] * (n+m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        prob[i+j] += 1
mx = max(prob)
for idx,val in enumerate(prob):
    if val == mx:
        print(idx, end=' ')
