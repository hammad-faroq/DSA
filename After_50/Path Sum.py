def hasPathSum(root, targetSum):
    if root is None:
        return 0
    stack = [(root, root.val)]
    while stack != []:
        value, depth = stack.pop()
        if value.left is not None or value.right is not None:
            if value.left is not None:
                obj = value.left
                stack.append((obj, depth + value.left.val))
            if value.right is not None:
                obj = value.right
                stack.append((obj, depth + value.right.val))
        else:
            if depth==targetSum:
                return True
    return False