from collections import deque

#노드 개수, 간선개수, 탐색 시작할 정점 번호 입력
N,M,V = map(int, input().split())

#그래프를 2차원 리스트로 구현 후 연결되어있는 노드들끼리 True로 표현
graph = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#dfs와 bfs에서 방문한 노드 체크용 리스트
visitedD = [False] * (N+1)
visitedB = [False] * (N+1)

def dfs(V):
    visitedD[V] =True
    print(V, end=' ')
    for i in range(1, N+1):
        if not visitedD[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    q = deque([V])                  #노드 방문할 순서 저장할 큐 생성
    visitedB[V] = True              #첫 노드 방문 처리 먼저 해주기
    while q:
        V = q.popleft()             #큐의 맨 앞에 들어있는 노드를 기준잡기
        print(V, end=' ')           #방문한 노드 출력
        for i in range(1, N+1):
            if not visitedB[i] and graph[V][i]:
                q.append(i)         #큐에 아직 방문안한 노드 i 추가
                visitedB[i] = True  #노드 i 방문 처리하기

dfs(V)
print()
bfs(V)