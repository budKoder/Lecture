import sys
sys.stdin = open("input.txt", "r")
'''
동전교환
'''
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# cnt = [2147000000] * (m+1)
# for x in a:
#     cnt[x] = 1
# for i in range(m+1):
#     for j in range(n):
#         if i - a[j] > 0:
#             cnt[i] = min(cnt[i-a[j]] + 1, cnt[i])
# print(cnt[m])
'''
solution
'''
if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dy = [1000]*(m+1)
    dy[0] = 0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])
