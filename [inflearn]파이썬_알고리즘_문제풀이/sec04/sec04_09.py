import sys
# sys.stdin = open("input.txt","r")
'''
증가수열 만들기(그리디)
'''
n = int(input())
arr = list(map(int, input().split()))
left, right = 0, n-1
# cnt, last, result
result = [0, 0, []]
while right >= left:
    check_left = arr[left] > result[1]
    check_right = arr[right] > result[1]
    if not check_left and not check_right:
        break
    else:
        if check_left and not check_right:
            result[2].append('L')
        elif not check_left and check_right:
            result[2].append('R')
        else:
            if arr[left] <= arr[right]:
                result[2].append('L')
            else:
                result[2].append('R')

        result[0] += 1
        if result[2][-1] == 'L':
            result[1] = arr[left]
            left += 1
        else:
            result[1] = arr[right]
            right -= 1
print(result[0])
print(''.join(result[2]))

'''
solution
'''
n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n-1
last = 0
res = ''
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)