class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements
    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements
    def find_min(self):
        if self.left is None:
            return self.data 
        return self.left.find_min()
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
        
def build_tree(arr):
    root = BinaryTree(arr[0])
    for i in range(1, len(arr)):
        root.add_child(arr[i])
    return root
if __name__ == '__main__':
    arr = [17, 7, 2, 3, 7, 5, 6, 9, 10]
    tree = build_tree(arr)

    print("Inorder traversal:", tree.inorder())
    print("Postorder traversal:", tree.postorder())
    print("Preorder traversal:",tree.preorder())
    print('Max of Binary tree:',tree.find_max())
    print('Min of binary tree', tree.find_min())
