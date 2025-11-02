def inorder(self, root, l=[]):
    if root is None:
        return

    self.inorder(root.left, l)  # Step 1: Visit left subtree
    print(root.val, end=" ")
    l.append(root.val)  # Step 2: Visit current node (root)
    self.inorder(root.right, l)
