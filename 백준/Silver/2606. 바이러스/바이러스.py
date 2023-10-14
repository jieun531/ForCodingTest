from collections import deque

num_com = int(input())

#컴퓨터 연결 상태 나타내는 2차원 리스트 제작
graph = [[False] * (num_com + 1) for _ in range(num_com + 1)]

#감염된 컴퓨터 개수 저장
virused = 0

#연결된 컴퓨터 간선 생성
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#중복 확인 방지용 체크 리스트
visited = [False] * (num_com + 1)

#덱 시작점 지정
q = deque([1])
visited[1] = True

#연결된 컴퓨터는 전부 탐색할 수 있도록 bfs 돌리기
while q:
    cur = q.popleft()
    for i in range(1, num_com+1):
        if not visited[i] and graph[cur][i]:
            q.append(i)
            visited[i] =True

print(visited.count(True) - 1)