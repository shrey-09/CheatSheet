# Left View and Right View of a Binary Tree

class Node:
    def __init__(self,v):
        self.val=v
        self.left=None
        self.right=None

def createTree():
    root=Node(45)
    root.left=Node(15)
    root.left.left=Node(30)
    root.left.left.left=Node(30)
    root.left.left.right=Node(40)
    root.left.right=Node(45)
    root.right=Node(60)
    root.right.left=Node(57)
    root.right.right=Node(69)
    return root

class LeftView:
    def helper(self,root,level):
        if not root:
            return
        if self.maxLevel<level:
            self.maxLevel=level
            self.ans.append(root.val)
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)
        return 
    
    def leftView(self,root):
        self.ans=[]
        self.maxLevel=-1
        self.helper(root,0)
        return self.ans

class RightView:
    def helper(self,root,level):
        if not root:
            return
        if self.maxLevel<level:
            self.maxLevel=level
            self.ans.append(root.val)
        self.helper(root.right,level+1)
        self.helper(root.left,level+1)
        return
    def rightView(self,root):
        self.ans=[]
        self.maxLevel=-1
        self.helper(root,0)
        return self.ans

object_Right=RightView()
object_Left=LeftView()
print(object_Left.leftView(createTree()))
print(object_Right.rightView(createTree()))