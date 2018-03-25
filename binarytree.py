class Node:
    def __init__(self, key=None, lT=None, rT=None):
        self.rT = rT
        self.lT = lT
        self.key = key
        self.parent = None


class BinaryTree:

    def __init__(self):
        self.rootNode = Node()

    def isLeaf(self, root):
        if (root.rT is None) and (root.lT is None):
            return True
        return False

    def insert(self, root, key):
        if root.key==key:
            print('[*] Key already exists!')
        elif key<root.key:
            if root.lT==None:
                newNode = Node(key)
                root.lT = newNode
                newNode.parent = root
            else:
                self.insert(root.lT, key)
        elif root.key<key:
            if root.rT==None:
                newNode = Node(key)
                root.rT = newNode
                newNode.parent = root
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

    def predecessor(self, node):
        if self.isLeaf(node):
            return node
        else:
            self.predecessor(node.rT)


    def delete(self, root, key):
        if root.key==key:
            if self.isLeaf(root):
                if root.parent!=None:
                    if root.parent.lT!=None:
                        if root.parent.lT.key==key:
                            root.parent.lT=None
                    elif root.parent.rT!=None:
                        if root.parent.rT.key==key:
                            root.parent.rT=None
                else:
                    root.key=0
                    print('[*][*] BinaryTree is empty!')
            elif root.rT==None:
                root.parent.lT = root.lT
                root.lT.parent = root.parent
                root.parent = None
            elif root.lT is None:
                root.parent.rT = root.rT
                root.rT.parent = root.parent
                root.parent = None
            else:
                node = self.predecessor(root.lT)
                node.parent = None

        elif key < root.key and root.lT!=None:
            self.delete(root.lT, key)
        elif root.key < key and root.rT!=None:
            self.delete(root.rT, key)

        else:
            print('[*] Delete operation halted! key not found')

    def display(self, root):
        print('[*][*] Displaying the tree: ', end=' ')
        self._display(root)

    def _display(self, root):
        if root.lT is not None:
            print("[", end='')
            self._display(root.lT)
            print("]", end='')
        print(root.key, end='')
        if root.rT is not None:
            print("[", end='')
            self._display(root.rT)
            print("]", end='')

    def preorder(self, root):
        print('[*][*] Pre-order traversal begins: ', end='')
        self._preorder(root)

    def _preorder(self, root):
        if root is not None:
            print(root.key, end=' ')
            if root.lT!=None:
                self._preorder(root.lT)
            if root.rT!=None:
                self._preorder(root.rT)

    def postorder(self, root):
        print('[*][*] Post-order traversal begins: ', end='')
        self._postorder(root)

    def _postorder(self, root):
        if root.key is not None:
            if root.lT is not None:
                self._postorder(root.lT)
            if root.rT is not None:
                self._postorder(root.rT)
            print(root.key, end=' ')

    def inorder(self, root):
        print('[*][*] In-order traversal begins: ', end=' ')
        self._inorder(root)

    def _inorder(self, root):
        if root.key is not None:
            if root.lT is not None:
                self._inorder(root.lT)
            print(root.key, end=' ')
            if root.rT is not None:
                self._inorder(root.rT)


if __name__=="__main__":

    b = BinaryTree()
    b.rootNode.key = 5
    b.insert(b.rootNode, 1)
    b.insert(b.rootNode, 10)
    b.insert(b.rootNode, 2)
    b.insert(b.rootNode, 4)
    b.insert(b.rootNode, 7)
    b.insert(b.rootNode, 18)
    b.display(b.rootNode)