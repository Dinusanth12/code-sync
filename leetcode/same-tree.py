class Solution:
    def isSameTree(self, p, q):
        # Both nodes are None
        if not p and not q:
            return True
        # One node is None and the other isn't
        if not p or not q:
            return False
        # Compare current values and recurse on left and right
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )