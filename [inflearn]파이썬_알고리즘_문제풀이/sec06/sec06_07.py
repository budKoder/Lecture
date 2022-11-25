import sys
sys.stdin = open("input.txt", "r")
'''
동전교환
'''
def DFS(x, cnt, money):
    global mi
    if money == 0:
        if cnt < mi:
            mi = cnt
    elif x >= n or cnt + money//s[x] > mi:
        return
    else:
        for i in range(money//s[x]+1, -1, -1):
            DFS(x+1, cnt + i, money-s[x]*i)


def solution(L, sum):
    global res
    # L : 동전의 사용 개수
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            solution(L+1, sum + a[i])


if __name__ == "__main__":
    n = int(input())
    # s = list(map(int, input().split()))
    # s.sort(reverse=True)
    # m = int(input())
    # mi = 2147000000
    # DFS(0, 0, m)
    # print(mi)

    res = 2147000000
    a = list(map(int, input().split()))
    m = int(input())
    a.sort(reverse=True)
    solution(0, 0)
    print(res)
