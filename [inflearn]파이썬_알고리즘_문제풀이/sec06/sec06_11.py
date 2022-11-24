import sys
sys.stdin = open("input.txt", "r")
'''
수들의 조합
'''
def DFS(x):
    global cnt
    if x >= k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        st = -1 if x == 0 else a.index(res[x-1])
        for i in range(st+1, n):
            res[x] = a[i]
            DFS(x+1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = [0] * k
    DFS(0)
    print(cnt)
