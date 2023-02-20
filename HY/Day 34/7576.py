"""
토마토 골드 5
"""
import sys
from collections import deque ##bfs를 사용할 땐 deque를 사용하자
input = sys.stdin.readline

m,n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

#상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

""" 큐에 1인 토마토값을 초기화
🌟🌟🌟출발점이 여러개인 경우 출발점을 모~두 Queue에 미리 넣어야 한다.🌟🌟🌟
시작점 익은 토마토(1)인 토마토 위치 큐에 append
 1 -1 0 0 0 0
 0 -1 0 0 0 0
 0 0 0 0 -1 0     큐에 1인 토마토들의 위치가 입력된다
 0 0 0 0 -1 1      deque([(0, 0), (3, 5)])
"""
q = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1: #1인 값들이 q에 들어감
            q.append([i, j])

def bfs():
     while q:
         x, y = q.popleft() #익은 토마토들의 위치를 꺼냄
         for i in range(4):  # 현재 위치에서 상하좌우 확인
             nextX = x + dx[i]  # 새로 이동할 위치
             nextY = y + dy[i]
             # 범위 확인: 범위 안에 있고, 토마토 상태가 0인 경우
             if 0 <= nextX < n and 0 <= nextY < m and box[nextX][nextY] == 0:
                box[nextX][nextY] = box[x][y] + 1 #기존 토마토값 +1 박스에 넣음
                q.append([nextX, nextY]) #q에 토마토 위치를 넣어줌
bfs()
answer = 0
# for문으로 박스 안에 토마토들을 확인한다. 
#box = [[1, -1, 7, 6, 5, 4], 
#       [2, -1, 6, 5, 4, 3],  
#       [3, 4, 5, 6, -1, 2], 
#       [4, 5, 6, 7, -1, 1]]  
# 만약 0인 값이 있다면 익히지 못하는 토마토이므로 -1를 출력한 후 종료한다.
for line in box:
     for tomato in line:
         if tomato == 0:# 안익은 토마토(0)이 있으면 -1 출력 후바로 종료
             print(-1)
             exit(0)
     answer = max(answer, max(line)) #박스 안에서 다 익었으면 최댓값이 정답
print(answer-1) #처음 익은 토마토 1에서 시작했기 때문에 -1