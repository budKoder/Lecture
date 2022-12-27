import sys
from collections import deque
sys.stdin = open("input.txt", "r")
'''
송아지 찾기
'''
# if __name__ == "__main__":
#     s, e = map(int, input().split())
#     ch = [0] * (max(s, e) + 2)
#     d = [0] * (max(s, e) + 2)
#     q = [s]
#     direction = [-1, 1, 5]
#     while True:
#         item = q.pop()
#         if item == e:
#             break
#         else:
#             for di in direction:
#                 if item+di < len(d) and ch[item+di] == 0:
#                     q.append(item+di)
#                     ch[item+di] = 1
#                     d[item+di] = d[item] + 1
#     print(d[e])

'''
solution
'''
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for nxt in (now-1, now+1, now+5):
        if 0 < nxt <= MAX:
            if ch[nxt] == 0:
                dQ.append(nxt)
                ch[nxt] = 1
                dis[nxt] = dis[now] + 1
print(dis[m])
