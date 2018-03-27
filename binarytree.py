class Node:
    def __init__(self, key=None, lT=None, rT=None):
        self.rT = rT
        self.lT = lT
        self.key = key
        self.parent = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.rootNode = Node()

    @staticmethod
    def isLeaf(root):
        if (root.rT is None) and (root.lT is None):
            return True
        return False

    def insert(self, key):
        self._insert(self.rootNode, key)

    def _insert(self, root, key):
        if root.key == key:
            print('[*] Key already exists!')
        elif key < root.key:
            if root.lT is None:
                newNode = Node(key)
                root.lT = newNode
                newNode.parent = root
                newNode.height = root.height + 1
            else:
                self._insert(root.lT, key)
        elif root.key < key:
            if root.rT is None:
                newNode = Node(key)
                root.rT = newNode
                newNode.parent = root
                newNode.height = root.height + 1
            else:
                self._insert(root.rT, key)

    def search(self, key):
        self._search(self.rootNode, key)

    def _search(self, root, key):
        if self.isLeaf(root) and root.key != key:
            print('[*] Key not found')
        else:
            if root.key == key:
                print('[*] Search successful - Key found! '.format(root.key))
                return 0
            elif root.key > key:
                self._search(root.lT, key)
            elif root.key < key:
                self._search(root.rT, key)

    def predecessor(self, node):
        if node.rT is None:
            return node
        else:
            n = self.predecessor(node.rT)
        return n

    def delete(self, key):
        self._delete(self.rootNode, key)

    def _delete(self, root, key):
        if root.key == key:
            if self.isLeaf(root):
                if root == self.rootNode:
                    root.key = None
                else:
                    if root.parent.lT is root:
                        root.parent.lT = None
                        root.parent = None
                    else:
                        root.parent.rT = None
                        root.parent = None
            elif root.rT is None:
                if root.parent.key > root.lT.key:
                    root.parent.lT = root.lT
                    root.lT.parent = root.parent
                    root.lT = None
                    root.parent = None
                elif root.parent.key < root.lT.key:
                    root.parent.rT = root.lT
                    root.lT.parent = root.parent
                    root.lT = None
                    root.parent = None
            elif root.lT is None:
                if root.parent.key > root.rT.key:
                    root.parent.lT = root.rT
                    root.rT.parent = root.parent
                    root.rT = None
                    root.parent = None
                elif root.parent.key < root.rT.key:
                    root.parent.rT = root.rT
                    root.rT.parent = root.parent
                    root.rT = None
                    root.parent = None
            elif root.lT is not None and root.rT is not None:
                node = self.predecessor(root.lT)
                self._delete(self.rootNode, node.key)
                root.key = node.key

        elif key < root.key and root.lT is not None:
            self._delete(root.lT, key)
        elif root.key < key and root.rT is not None:
            self._delete(root.rT, key)
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
            if root.lT is not None:
                self._preorder(root.lT)
            if root.rT is not None:
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


if __name__ == "__main__":
    b = BinaryTree()
    b.rootNode.key = 5
    b.insert(1)
    b.insert(10)
    b.insert(2)
    b.insert(4)
    b.insert(7)
    b.insert(18)
    b.insert(0)
    b.insert(14)
    b.insert(6)
    b.insert(3)
    b.delete(5)
    b.display(b.rootNode)
