from collections import deque

def computerNode(li):
    new_li = []
    for i in range(len(li)):
        tmp = []
        for j in range(len(li)):
            if (i != j) and (li[i][j] == 1):
                tmp.append(j)
        new_li.append(tmp)
    return new_li

def bfs(q,li,vi):
    while q:
        v = q.popleft()
        for i in li[v]:
            if not vi[i]:
                q.append(i)
                vi[i] = True
    



def solution(n, computers):
    
    node = computerNode(computers)
    visited = [False] * n
    queue = deque([])
    answer = 0
    
    for i in range(n):
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            bfs(queue,node,visited)
            answer += 1

    return answer