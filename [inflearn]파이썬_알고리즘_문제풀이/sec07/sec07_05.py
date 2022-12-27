import sys
# sys.stdin = open("input.txt", "r")
'''
동전 분배하기
'''
# def DFS(L):
#     global mi
#     if L == n:
#         if len(set(money)) < 3:
#             return
#         if max(money) - min(money) < mi:
#             mi = max(money) - min(money)
#         return
#     else:
#         for i in range(3):
#             money[i] += a[L]
#             DFS(L+1)
#             money[i] -= a[L]
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [int(input()) for _ in range(n)]
#     mi = 2147000000
#     money = [0] * 3
#     DFS(0)
#     print(mi)
'''
solution
'''
def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * n
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
