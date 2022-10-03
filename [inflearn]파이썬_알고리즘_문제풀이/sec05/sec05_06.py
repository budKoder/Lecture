import sys
from collections import deque
# sys.stdin = open("input.txt","r")
'''
응급실
'''
n,m = map(int, input().split())
risk = list(map(int, input().split()))
q = deque([i, risk[i]] for i in range(len(risk)))
seq = 0
while True:
    mx_item = max(q, key=lambda x:x[1])
    cur_item = q.popleft()

    if cur_item[1] == mx_item[1]:
        seq += 1
        if cur_item[0] == m:
            break
    else:
        q.append(cur_item)
print(seq)

'''
solution
'''
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
