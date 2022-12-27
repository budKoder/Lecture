import sys
# sys.stdin = open("input.txt", "r")
'''
동전 바꿔주기
'''
# def DFS(L, left):
#     global cnt
#     if left == 0:
#         cnt += 1
#         return
#     if L == k:
#         return
#     else:
#         for i in range(min(left//a[L][0], a[L][1]), -1, -1):
#             DFS(L+1, left - a[L][0] * i)
#
#
# if __name__ == "__main__":
#     t = int(input())
#     k = int(input())
#     a = [list(map(int, input().split())) for _ in range(k)]
#     a.sort(key=lambda x: x[0], reverse=True)
#     cnt = 0
#     DFS(0, t)
#     print(cnt)
'''
solution
'''
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for j in range(cn[L]+1):
            DFS(L+1, sum+(cv[L] * j))


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()     # 동전의 금액
    cn = list()     # 동전의 갯수
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)
