class Solution:
    ans = -float("inf")

    def solution(self, node):
        if node is None:
            return 0

        left = self.solution(node.left)
        right = self.solution(node.rigth)

        # max value that this path can contribute
        mxSide = max(node.val, max(left, right) + node.val)

        # node is top (center) of the answer ?
        mxTop = max(mxSide, left + right + node.val)

        self.ans = max(self.ans, mxTop)

        return mxSide

    def maxPathSum(self, root):
        self.solution(root)
        return self.ans

