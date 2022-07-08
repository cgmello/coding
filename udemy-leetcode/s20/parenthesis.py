class ValidParenthesis:

    def __init__(self):
        self.st = []

    def push(self, symbol):
        self.st.append(symbol)

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1] if self.st else None

    def isValid(self, input):
        m = {}
        m['{'] = '}'
        m['['] = ']'
        m['('] = ')'
        rev_m = dict((v,k) for k,v in m.items())

        for i in range(len(input)):
            s = input[i]
            if s in m.keys():
                self.push(s)
            elif s in rev_m.keys():
                if rev_m[s] == self.top():
                    self.pop()
                else:
                    return False
        return True


v = ValidParenthesis()
print(v.isValid("{[hello my friend (mello)]}"))
