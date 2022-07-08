class Solution():
    def createKey(self, s):
        return "".join(sorted(s))

    def groupAnagrams(self, strs):
        m = {}
        arr = []

        for s in strs:
            key = self.createKey(s)
            if key not in m:
                m[key] = []
            m[key].append(s)

        for v in m.values():
            arr.append(v)

        return arr


s = Solution()
strs = [ "eat", "tea", "tan", "ate", "nat", "bat" ]
# strs = ["ddddddddddg", "dgggggggggg"]
print(s.groupAnagrams(strs))
