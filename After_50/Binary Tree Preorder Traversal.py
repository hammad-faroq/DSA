def preorderTraversal(self, root,l=None):
    if l is None:
        l = []
    if root is None:
        return l

    l.append(root.val)
    self.preorderTraversal(root.left, l)  # Step 1: Visit left subtree
    self.preorderTraversal(root.right, l)
    return l