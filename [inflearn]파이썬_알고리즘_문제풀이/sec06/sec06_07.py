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


if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    m = int(input())
    mi = 2147000
    DFS(0, 0, m)
    print(mi)
