# Detect Cycle in directed graph

def isCyclic(self, V, adj):
    def cycle(src,visited,recurseStack):
        visited[src]=True
        recurseStack[src]=True
        for x in range(len(adj[src])):
            if visited[adj[src][x]]==False:
                if cycle(adj[src][x],visited,recurseStack):
                    return True
            elif recurseStack[adj[src][x]]:
                return True
        recurseStack[src]=False
        return False
    recurseStack=[False for x in range(V)]
    visited=[False for x in range(V)]
    for x in range(V):
        if visited[x]==False:
            if cycle(x,visited,recurseStack):
                return True
    return False