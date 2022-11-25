import sys
sys.stdin = open("input.txt", "r")
'''
부분집합 구하기(DFS)
'''
def DFS(x):
    if x > n:
        for i in range(1, n+1):
            if res[i] == 1:
                print(i, end=' ')
        print()
    else:
        res[x] = 1
        DFS(x+1)
        res[x] = 0
        DFS(x+1)


# solution
def solution(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        solution(v+1)
        ch[v] = 0
        solution(v+1)


if __name__ == "__main__":
    n = int(input())
    res = [0] * (n+1)
    DFS(1)

    ch = [0] * (n+1)
    solution(1)
