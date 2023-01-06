import sys
sys.stdin = open("input.txt", "r")
'''
플로이드 워샬 알고리즘
'''
# n, m = map(int, input().split())
# INF = 2147000000
# graph = [[INF] * n for _ in range(n)]
# for _ in range(m):
#     s, e, w = map(int, input().split())
#     graph[s-1][e-1] = w
#
# for i in range(n):
#     graph[i][i] = 0
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == INF:
#             print("M", end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
'''
solution
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
