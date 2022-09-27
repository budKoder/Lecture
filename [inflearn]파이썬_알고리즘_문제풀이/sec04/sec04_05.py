import sys
# sys.stdin = open("input.txt","r")
'''
회의실 배정(그리디)
'''
n = int(input())
rooms = []
for _ in range(n):
    st,ed = map(int, input().split())
    rooms.append([st,ed])
rooms.sort(key=lambda x:x[1])
st = rooms[0][0]
ed = rooms[0][1]
cnt = 1
for i in range(1,len(rooms)):
    stm = rooms[i][0]
    etm = rooms[i][1]
    if stm >= ed:
        st = stm
        ed = etm
        cnt += 1
print(cnt)

'''
solution
'''
n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1], x[0]))
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        cnt += 1
        et = e

