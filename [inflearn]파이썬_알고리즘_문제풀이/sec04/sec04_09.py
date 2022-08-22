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

