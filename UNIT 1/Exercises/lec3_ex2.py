for i in nodes:
    iname = i.getName()
    for j in range(len(iname) - 1):
        perm = iname[:j] + iname[j + 1] + iname[j] + iname[j + 2:]
        permnode = g.getNode(perm)
        if not permnode in g.childrenOf(i):
            g.addEdge(Edge(src=i, dest=permnode))
           
