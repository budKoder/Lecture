import sys
# sys.stdin = open("input.txt","r")
'''
후위식 연산
'''
arr = list(input().strip())
st = []
for x in arr:
    if x.isdigit():
        st.append(int(x))
    else:
        n2 = st.pop()
        n1 = st.pop()
        if x == '+':
            st.append(n1+n2)
        elif x == '-':
            st.append(n1-n2)
        elif x == '*':
            st.append(n1*n2)
        elif x == '/':
            st.append(n1/n2)
print(st[0])