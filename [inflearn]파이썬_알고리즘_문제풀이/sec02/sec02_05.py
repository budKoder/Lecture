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

'''
solution
'''
n,m = map(int, input().split())
cnt = [0] * (n+m+3) # +3은 의미 없음. 그냥 여유롭게 결과 테이블 선언
max = -2147000000   # python 정수형 중 가장 작은 값
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
