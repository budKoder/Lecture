import sys
sys.stdin = open("input.txt", "r")
'''
인접행렬(가중치 방향그래프)
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    # a = [list(map(int, input().split())) for _ in range(m)]
    # arr = [[0 for i in range(n)] for j in range(n)]
    # for st, ed, val in a:
    #     arr[st-1][ed-1] = val
    # for x in arr:
    #     print(' '.join(list(map(str, x))))

    # solution(1) - 무방향그래프
    g = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
        g[b][a] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=' ')
        print()

    # solution(2) - 가중치방향그래프
    for i in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = c

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=' ')
        print()
