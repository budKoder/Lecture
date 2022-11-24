import sys
sys.stdin = open("input.txt", "r")
'''
조합 구하기
'''
def DFS(x):
    global cnt
    if x > m:
        for x in res[1:]:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(res[x-1]+1, n+1):
            res[x] = i
            DFS(x+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (m+1)
    cnt = 0
    DFS(1)
    print(cnt)
