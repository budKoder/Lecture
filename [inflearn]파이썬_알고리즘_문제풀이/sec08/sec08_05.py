import sys
sys.stdin = open("input.txt", "r")
'''
최대 선 연결하기
'''
n = int(input())
a = list(map(int, input().split()))
f = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            f[i] = max(f[i], f[j]+1)
print(max(f))
