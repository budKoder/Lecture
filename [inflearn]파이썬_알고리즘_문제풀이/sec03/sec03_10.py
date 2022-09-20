import sys
# sys.stdin = open("input.txt","r")
'''
스도쿠 검사
'''
arr = [list(map(int,input().split())) for _ in range(9)]
result = True
# 가로
for i in range(9):
    if len(set(arr[i])) != 9:
        result = False
        break
else:
    # 세로
    for row in range(9):
        cols = set()
        for col in range(9):
            cols.add(arr[row][col])
        if len(cols) != 9:
            result = False
            break
    else:
        # box
        for row in range(0,9,3):
            for col in range(0,9,3):
                box = set()
                box.update([arr[row+0][col+0], arr[row+0][col+1], arr[row+0][col+2]])
                box.update([arr[row+1][col+0], arr[row+1][col+1], arr[row+1][col+2]])
                box.update([arr[row+2][col+0], arr[row+2][col+1], arr[row+2][col+2]])
                if len(box) != 9:
                    result = False
                    break

if not result:
    print("NO")
else:
    print('YES')

'''
solution
'''
def check(a):
    for i in range(9):
        ch1 = [0]*10    # 행
        ch2 = [0]*10    # 열
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")