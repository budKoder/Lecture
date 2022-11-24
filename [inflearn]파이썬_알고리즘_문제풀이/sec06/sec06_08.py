import sys
sys.stdin = open("input.txt", "r")
'''
순열 구하기
'''
def DFS(x):
    global cnt
    if x >= m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if i not in res:
                res[x] = i
                DFS(x+1)
                res[x] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    DFS(0)
    print(cnt)
