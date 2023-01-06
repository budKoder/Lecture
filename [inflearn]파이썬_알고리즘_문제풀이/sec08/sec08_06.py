import sys
sys.stdin = open("input.txt", "r")
'''
가장 높은 탑 쌓기
'''
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# a.sort(key=lambda x: (x[0], x[2]), reverse=True)
# h = []
# for width, height, weight in a:
#     h.append(height)
# for i in range(n):
#     for j in range(i):
#         if a[i][0] < a[j][0] and a[i][2] < a[j][2]:
#             h[i] = max(h[i], h[j] + a[i][1])
# print(max(h))
'''
solution
'''
if __name__ == "__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int ,input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dy = [0] * n
    dy[0] = bricks[0][1]
    res = bricks[0][1]
    for i in range(1, n):
        max_h = 0
        for j in range(i-1, -1, -1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)



