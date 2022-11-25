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


# solution
def solution(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            solution(L+1, i+1, sum + a[i])


if __name__ == "__main__":
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # m = int(input())
    # cnt = 0
    # res = [0] * k
    # DFS(0)
    # print(cnt)

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    solution(0, 0, 0)
    print(cnt)
