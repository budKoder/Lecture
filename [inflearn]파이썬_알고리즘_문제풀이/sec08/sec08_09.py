import sys
sys.stdin = open("input.txt", "r")
'''
가방문제(냅색 알고리즘)
'''
# n, limit = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# a.sort()
# v = [0] * (limit + 1)
# for i in range(n):
#     v[a[i][0]] = a[i][1]
# for i in range(limit+1):
#     mx = 0
#     for j in range(n):
#         if i - a[j][0] > 0 and v[i-a[j][0]] > mx:
#             mx = v[i-a[j][0]] + a[j][1]
#     v[i] = max(v[i], mx)
# print(v[limit])
'''
solution
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1)
    for i in range(n):
        w, b = map(int, input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j], dy[j-w]+b)
    print(dy[m])
