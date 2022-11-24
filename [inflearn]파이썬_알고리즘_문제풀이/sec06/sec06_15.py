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


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0 for i in range(n)] for j in range(n)]
    for _ in range(m):
        st, ed = map(int, input().split())
        arr[st-1][ed-1] = 1
    visited = [0] * n
    visited[0] = 1
    cnt = 0
    DFS(0)
    print(cnt)
