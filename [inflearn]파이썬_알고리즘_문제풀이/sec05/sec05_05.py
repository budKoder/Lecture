import sys
from collections import deque
# sys.stdin = open("input.txt","r")
'''
공주 구하기(큐)
'''
n, k = map(int, input().split())
q = deque(range(1,n+1))
while len(q) > 1:
    for _ in range(k-1):
        q.append(q.popleft())
    q.popleft()
print(q[0])
