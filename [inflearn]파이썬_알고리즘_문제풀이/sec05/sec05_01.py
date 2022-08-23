import sys
# sys.stdin = open("input.txt","r")
'''
가장 큰 수
'''
n, m = map(int, input().split())
n = str(n)
cnt = 0
idx = 0
st = []
while cnt < m and idx < len(n):
    if len(st) == 0 or st[-1] >= n[idx]:
        st.append(n[idx])
        idx += 1
    else:
        st.pop()
        cnt += 1
if len(st) < len(n)-m:
    st.extend(n[idx:])
else:
    st = st[:len(n)-m]
print(''.join(st))
