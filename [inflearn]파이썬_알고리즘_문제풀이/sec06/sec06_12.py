import sys
import itertools as lt
sys.stdin = open("input.txt", "r")
"""
라이브러리를 이용한 순열(순열추측하기)
"""
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = (b[i-1] * (n-i)) // i
a = list(range(1, n+1))
# lt.permutations(x) : 리스트의 모든 순열
# lt.permutations(x, n) : 리스트 x에서 3개를 뽑아 만든 모든 수열
cnt = 0
for tmp in lt.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        # L : index 번호
        sum += x * b[L]
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break
