from collections import deque


class Solution():

    def __init__(self, capacity):
       self.capacity = capacity
       self.m = dict()
       self.deq = deque()

    def get(self, key):
        if key not in self.m:
            return -1
        else:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value

    def put(self, key, value):
        if key not in self.m:
            if len(self.deq) == self.capacity:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)

s = Solution(2)
s.put(1, 1)
s.put(2, 2)
print(s.get(1))
s.put(3, 3)
print(s.get(2))
s.put(4, 4)
print(s.get(1))
print(s.get(3))
print(s.get(4))
