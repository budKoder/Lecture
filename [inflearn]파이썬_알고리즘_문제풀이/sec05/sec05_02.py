import sys
# sys.stdin = open("input.txt","r")
'''
쇠막대기
'''
arr = list(input())
st = []
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        st.append(arr[i])
    else:
        st.pop()
        if arr[i-1] == '(':
            cnt += len(st)
        else:
            cnt += 1
print(cnt)
