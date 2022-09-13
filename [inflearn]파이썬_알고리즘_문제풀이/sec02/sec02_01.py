import sys
# sys.stdin = open("input.txt","r")
'''
K번째 약수
'''
def get_divisor(n):
    result = []
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)
    return result


n, k = map(int, input().split())
divisor = get_divisor(n)
if len(divisor) < k:
    print(-1)
else:
    print(divisor[k-1])


'''
solution
'''
# for~else : 중간에 break하지 않고 정상적으로 for문이 끝난 경우 else문 실행
n, k = map(int, input().split())
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
