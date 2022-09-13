import sys
# sys.stdin = open("input.txt","r")
'''
소수(에라토스테네스 체)
'''
n = int(input())
cnt = 0
nums = [1] * (n+1)
nums[0],nums[1] = 0, 0
for i in range(2, n+1):
    if nums[i] == 1:
        for j in range(i+i, n+1, i):
            nums[j] = 0
print(sum(nums))

'''
solution
'''
n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)