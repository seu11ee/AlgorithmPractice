import sys
from collections import defaultdict
n = int(sys.stdin.readline())
def getParent(x):
    if parent[x]==x:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(x,y):
    a = getParent(x)
    b = getParent(y)
    if a != b:
        parent[b] = a
        children[a]+=(children[b])
    return a

for _ in range(n):
    m = int(sys.stdin.readline())
    parent = dict()
    children = defaultdict(int)
    for _ in range(m):
        f1,f2 = sys.stdin.readline().split()
        if f1 not in parent:
            parent[f1] = f1
            children[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            children[f2] = 1
        p = unionParent(f1,f2)
        print(children[p])



# import sys
# from collections import defaultdict
#
# n = int(sys.stdin.readline())
# def getParent(parent,x):
#     if x not in parent:
#         parent[x] = x
#         children[x] = 1
#     elif parent[x]==x:
#         return x
#     return getParent(parent,parent[x])
# def unionParent(parent,x,y):
#     a = getParent(parent,x)
#     b = getParent(parent,y)
#     if a < b:
#         parent[y] = a
#         children[a] += children[y]
#         return a
#     else:
#         parent[x] = b
#         children[b] += children[x]
#         return b
#
# def countChildren(children,p):
#     return children[p]
#
# for _ in range(n):
#     m = int(sys.stdin.readline())
#     parent = dict()
#     children = defaultdict(int)
#     for _ in range(m):
#         f1,f2 = sys.stdin.readline().split()
#         p = unionParent(parent,f1,f2)
#         print(countChildren(children,p))


