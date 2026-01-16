def solution(n, computers):
    visited = [False] * n
    network_count = 0

    def dfs(node):
        visited[node] = True

        for other in range(n):
            if computers[node][other] == 1 and not visited[other]:
                dfs(other)

    for i in range(n):
          if not visited[i]:
                dfs(i)
                network_count += 1

    return network_count