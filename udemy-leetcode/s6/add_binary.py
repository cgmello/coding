class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        final = ""
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            va = int(a[i]) if i >= 0 else 0
            vb = int(b[j]) if j >= 0 else 0

            s = va + vb + carry

            if s == 2:
                s = 0
                carry = 1
            elif s == 3:
                s = 1
                carry = 1
            else:
                carry = 0

            i -= 1
            j -= 1

            final = "{}{}".format(s, final)

        if carry == 1:
            final = "1{}".format(final)

        return final


s = Solution()
print(s.addBinary("1010", "1011"))
