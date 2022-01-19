adj_list = [[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [False] * N

def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for w in adj_list[v]:
        if not visited[w]:      # false일 경우
            dfs(w)

print('DFS 방문순서')
for i in range(N):
    if not visited[i]태:
        dfs(i)

# DFS 방문순서
# 0  2  3  9  8  1  4  5  7  6

# 노드 연결 상
# 0 - 2 - 3 - 9
#   - 1     - 8
#
# 4 - 5 - 6
#     |   |
#       7