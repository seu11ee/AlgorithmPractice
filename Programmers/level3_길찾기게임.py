import sys
sys.setrecursionlimit(1000000)
pre = []
post = []
def solution(nodeinfo):
    answer = []
    sorted_list = sorted(enumerate(nodeinfo),key=lambda x: (-x[1][1], x[1][0]))

    bst = BinarySearchTree(Node(sorted_list[0][0]+1,sorted_list[0][1][0]))
    for idx, point in sorted_list[1:]:
        bst.insert(idx+1,point[0])

    preorder_traverse(bst.root)
    postorder_traverse(bst.root)
    answer.append(pre)
    answer.append(post[::-1])
    return answer


# 노드 생성과 삽입
class Node:
    def __init__(self, data,x):
        self.left = None
        self.right = None
        self.data = data
        self.x = x
class BinarySearchTree(Node):
    def __init__(self,root):
        self.root = root
    def insert(self, data,x):
        self.root = self._insert_value(self.root, data,x)
        return self.root is not None

    def _insert_value(self, node, data,x):
        if node is None:
            node = Node(data,x)
        else:
            if x < node.x:
                if node.left:
                    self._insert_value(node.left,data,x)
                else:
                    node.left = Node(data,x)
            else:
                if node.right:
                    self._insert_value(node.right,data,x)
                else:
                    node.right = Node(data,x)
        return node
def preorder_traverse(node):
    if node == None:
        return
    pre.append(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)
def postorder_traverse(node):
    if node == None:
        return
    post.append(node.data)
    postorder_traverse(node.right)
    postorder_traverse(node.left)
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
#result [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]