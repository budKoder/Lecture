import sys
sys.stdin = open("input.txt", "r")
'''
피자 배달 거리
'''
'''
solution
'''
def DFS(L, s):
    global res
    if L == m:
        sum = 0     # 도시의 피자거리
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            # 선택된 피자집의 인덱스 번호
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0]*m              # 조합의 경우의 수
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)
