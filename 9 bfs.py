import sys


graph = {
        1 : [],
        2 : [3, 4],
        3 : [1],
        4 : [3, 5],
        5 : [1]
        }

print graph



#
print '#comment'

def bfs(G,v):
    Q = []
    V = set([])
    V.add(v)
    print V
    Q.append(v)
    print Q
    while len(Q)>0:
        t = Q.pop(0)
        if(t==4):
            return t
        #print G[t]
        for i in G[t]:
            #print i
            if i not in V:
                V.add(i)
                Q.append(i)


    return None



ret = bfs(graph,3   )
print ret














