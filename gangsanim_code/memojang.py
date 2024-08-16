import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(y, x):
        queue = [(y,x)]
        depth = 0

        while queue:
            tempY, tempX = queue.pop(0)
            for i in range(4):
                nowX = dx[i] + tempX
                nowY = dy[i] + tempY
                if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] == arr[tempY][tempX]+1:
                    depth += 1
                    queue.append((nowY, nowX))
        return depth
    ans = 0
    tmpList = []
    for y in range(n):
        for x in range(n):
            res = bfs(y, x, arr[y][x])
            if res >= ans:
                ans = res
                tmpList.append((res, arr[y][x]))
    print(*tmpList)