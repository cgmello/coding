class Stairs:
    ans = []

    def climbStairs(self, n):
        self.ans = []
        self.nextStep([], n)
        return self.ans

    def nextStep(self, cur, n):
        if sum(cur) == n:
            self.ans.append(cur[:])
            return

        if sum(cur) > n:
            return

        cur.append(1)
        self.nextStep(cur[:], n)
        cur.pop()
        cur.append(2)
        self.nextStep(cur[:], n)


s = Stairs()
print(s.climbStairs(35))
print(len(s.climbStairs(2)))
