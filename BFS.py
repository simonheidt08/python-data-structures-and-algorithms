from collections import deque

def bst(graph, start):
    q = deque([start])
    vis = {start}

    while q:
        cur = q.popleft()
        print(cur)

        for nxt in graph(cur):
            if nxt not in vis:
                q.append(nxt)
                vis.add(nxt)