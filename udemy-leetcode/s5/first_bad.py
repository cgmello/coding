class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            bad = isBadVersion(mid)
            if not bad:
                l = mid + 1
            elif bad:
                if mid == 0 or not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1
            else:
                r = mid - 1
        return -1

def isBadVersion(n):
    first_bad_version = 4
    return n == first_bad_version

s = Solution()
print (s.firstBadVersion(5))
