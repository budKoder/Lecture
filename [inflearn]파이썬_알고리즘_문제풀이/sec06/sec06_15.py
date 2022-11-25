import sys
sys.stdin = open("input.txt", "r")
'''
경로 탐색(그래프 DFS)
'''
def DFS(node):
    global cnt
    if node == n-1:
        cnt += 1
        return
    else:
        for i in range(n):
            if arr[node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                DFS(i)
                visited[i] = 0


# solution
def solution(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                solution(i)
                ch[i] = 0
                path.pop()


if __name__ == "__main__":
    # n, m = map(int, input().split())
    # arr = [[0 for i in range(n)] for j in range(n)]
    # for _ in range(m):
    #     st, ed = map(int, input().split())
    #     arr[st-1][ed-1] = 1
    # visited = [0] * n
    # visited[0] = 1
    # cnt = 0
    # DFS(0)
    # print(cnt)

    n,m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = []
    path.append(1)
    ch[1] = 1
    solution(1)
