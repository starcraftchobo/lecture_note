import sys
from pprint import pprint

sys.stdin = open('input.txt')

# def fibo1(n):
#     if n>=2 and memo[n] == 0:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo
# n = 10
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
#
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return  fibo(n-1) + fibo(n-2)
#
# print(fibo1(n))


# 모든 곳 들르기
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''



# def DFS(s, V):                  # s는 시작정점, V는 정점개수
#     visited = [0]*(V+1)         # 방문한 정점을 표시
#     stack = []                  # 스택 생성
#     print(s)
#     visited[s] = 1              # 시작정점 방문 표시
#     v =s
#     while True:
#         for w in adjL[V]:       # v에 인접하고 방문 안한 w가 있으면
#             if visited[w] == 0:
#                 stack.append(v) # 현재 정점 push하고
#                 v = w           # 방문표시
#                 print(v)
#                 visited[w] = 1  # w에 방문
#                 break           # v부터 다시 탐색
#         else:                   # 남은 인접정점이 없어서 break가 걸리지않음
#             if stack:           # 스택이 남아있으면
#                 v = stack.pop() # 되돌아갓!
#             else:               # 되돌아갈 곳이 없으면 탐색 종료
#                 break
#
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     adjL = [[] for _ in range(V + 1)]
#     arr = list(map(int, input().split()))
#     for i in range(E):
#         v1, v2 = arr[i * 2], arr[i * 2 + 1]
#         adjL[v1].append(v2)
#         adjL[v2].append(v1)
#     print(adjL)
#
#     DFS(1, V)



# another DFS
'''
인접행렬 
n x n 크기의 정사각형 행렬
노드들 간의 연결 관계를 행렬로 표현한것
무방향 그래프에서는
    정점 i와 j 사이에 간선이 있다면 matrix[i][j] = matrix[j][i] = 1
'''

node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
# 교재 연습문제
#       A  B  C  D  E  F  G
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   # A
    [0, 1, 0, 0, 1, 1, 0, 0],   # B
    [0, 1, 0, 0, 0, 1, 0, 0],   # C
    [0, 0, 1, 0, 0, 0, 1, 0],   # D
    [0, 0, 1, 1, 0, 0, 1, 0],   # E
    [0, 0, 0, 0, 1, 1, 0, 1],   # F
    [0, 0, 0, 0, 0, 0, 1, 0],   # G
]

def DFS(s, V):                  # 시작정점, 정점개수
    # stack에 시작정점 push
    stack = [s]
    # 방문 여부 체크 리스트
    visited = [0] * (V + 1)

    # 스택이 빌 때까지 DFS 진행 (스택에 값이 있는 동안 진행)
    while stack:
        # 현재 조사할 노드
        current = stack.pop()

        # 방문하지 않은 노드라면
        if visited[current] == 0:
            # 방문 표시
            visited[current] = 1
            # 방문한 노드 출력
            print(node[current])

            # 현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가
            # V부터 1까지 역순으로 확인(작은 번호의 노드가 스택의 위쪽으로 위치)
            for next in range(V, 0, -1):
            # 큰번호 우선 탐색
            # for next in range(V, 0, -1):
                # 다음 노드가 간선이 연결이 되어있고 + 방문한 적이 없다면
                if matrix[current][next] == 1 and visited[next] == 0:
                    # stack에 push
                    stack.append(next)


# 인접행렬 만들기
T = int(input())
# V = 노드의 개수, E = 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
# 노드별 간선 정보
data = list(map(int, input().split()))
# 간선 정보 넣기
# 간선의 개수만큼 반복하며 넣기
for i in range(E):
    n1 = data[i*2]
    n2 = data[i*2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

pprint(adj_matrix)

DFS(1,7)