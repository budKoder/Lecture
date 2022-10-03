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

'''
solution
'''
from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
