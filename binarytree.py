class Node:
    def __init__(self, key=None, lT=None, rT=None):
        self.rT = rT
        self.lT = lT
        self.key = key


class BinaryTree:

    def __init__(self):
        self.rootNode = Node()

    def isLeaf(self, root):
        if (root.rT == None) and (root.lT == None):
            return True
        return False

    def insert(self, root, key):
        if root.key==key:
            print('[*] Key already exists!')
        elif key<root.key:
            if root.lT==None:
                newNode = Node(key)
                root.lT = newNode
            else:
                self.insert(root.lT, key)
        elif root.key<key:
            if root.rT==None:
                newNode = Node(key)
                root.rT = newNode
            else:
                self.insert(root.rT, key)

    def search(self, root, key):
        if self.isLeaf(root) and root.key!=key:
            print('[*] Key not found')
        else:
            if root.key == key:
                print('[*] Search successful - Key found! '.format(root.key))
                return 0
            elif root.key>key:
                self.search(root.lT, key)
            elif root.key<key:
                self.search(root.rT, key)
        


b = BinaryTree()
b.rootNode.key = 5
b.insert(b.rootNode, 1)
b.insert(b.rootNode, 10)
b.insert(b.rootNode, 14)
