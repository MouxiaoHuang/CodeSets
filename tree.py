# ref: https://www.jianshu.com/p/9503238394df & 
# https://blog.csdn.net/zzfightingy/article/details/86742755?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control
# https://www.cnblogs.com/anzhengyu/p/11083568.html

from operator import indexOf
from platform import node
import queue
from tkinter.messagebox import NO


class Node():
    def __init__(self, item, lchild=None, rchild=None) -> None:
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    def __init__(self, root=None) -> None:
        self.root = root
    
    def add(self, item):
        node = Node(item=item)
        if (self.root==None):
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while (queue):
                cur = queue.pop(0)
                if (cur.lchild==None):
                    cur.lchild = node
                    return
                elif (cur.rchild==None):
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, node):
        if (node==None):
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def bfs(self, node):
        if (node==None):
            return
        else:
            queue = []
            queue.append(node)
            while (queue):
                cur = queue.pop(0)
                print(cur.item, end=" ")
                if (cur.lchild is not None):
                    queue.append(cur.lchild)
                if (cur.rchild is not None):
                    queue.append(cur.rchild)
    
    def dfs(self, node):
        if node is None:
            return
        print(node.item)
        self.dfs(node.lchild)
        self.dfs(node.rchild)

    def maxdepth(self, root):
        if root==None:
            return 0
        else:
            return 1 + max(self.maxdepth(root.lchild), self.maxdepth(root.rchild))


if __name__ == '__main__':
    t = Tree()
    nums = [1,2,4,6,8,9]
    for num in nums:
        t.add(num)
    t.preorder(t.root)
    print("")
    t.bfs(t.root)
    print("")
    print(t.maxdepth(t.root))
    t.dfs(t.root)


def preorder(root):
    if root is None:
        return
    print(root.item)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.item)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.item)

def bfs(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        print(cur.item)
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)

def add(root, item):
    node = Node(item=item)
    if root is None:
        root = node
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        if cur.left is None:
            cur.left = node
            return
        elif cur.right is None:
            cur.right = node
        else:
            queue.append(cur.left)
            queue.append(cur.right)
    
def mindepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1 + mindepth(root.right)
    if root.right is None:
        return 1 + mindepth(root.left)
    return 1 + min(mindepth(root.left), mindepth(root.right))