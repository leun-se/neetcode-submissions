# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Check if the tree is balanced at each node
        # use a tuple [balanced, height] to calculate that
        def dfs(root):
            # base case, root is None
            if not root: return [True, 0]

            # call dfs on left and right children
            left, right = dfs(root.left), dfs(root.right)

            # check if both of them are balanced and their parent is balanced
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1],right[1])]
        
        return dfs(root)[0]