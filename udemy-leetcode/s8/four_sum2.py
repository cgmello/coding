class Solution():
    def fourSum2(self, A, B, C, D):
        m = {}
        ans = 0

        for i in range(len(A)):
            x = A[i]
            for j in range(len(B)):
                y = B[i]
                if x + y not in m:
                    m[x + y] = 0
                m[x + y] += 1

        for k in range(len(C)):
            x = C[k]
            for l in range(len(D)):
                y = D[l]
                target = -(x + y)
                if target in m:
                    ans += m[target]

        return ans
