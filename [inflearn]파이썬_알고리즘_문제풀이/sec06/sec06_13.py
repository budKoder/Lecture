import sys
import itertools as lt
sys.stdin = open("input.txt", "r")
'''
라이브러리를 이용한 조합(수들의 조합)
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
# lt.combinations(x) : 리스트 x의 모든 조합
# lt.combinations(x, n) : 리스트 x의 n개로 이루어진 모든 조합
for tmp in lt.combinations(a, k):
    if sum(tmp) % m == 0:
        cnt += 1
print(cnt)
