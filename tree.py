# ref: https://www.jianshu.com/p/9503238394df & 
# https://blog.csdn.net/zzfightingy/article/details/86742755?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control
# https://www.cnblogs.com/anzhengyu/p/11083568.html

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


if __name__ == '__main__':
    t = Tree()
    nums = [1,2,4,6,8,9]
    for num in nums:
        t.add(num)
    t.preorder(t.root)
    print("")
    t.bfs(t.root)
    print("")