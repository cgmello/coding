class Solution():
    def wordSearch(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                # find the first letter
                if word[0] == board[i][j] and \
                        self.solution(board, word, i, j, ""):
                    return True

    def solution(self, board, word, x, y, cur):
        # out of the limits or a cell visited before
        if x < 0 or x >= len(board) or \
            y < 0 or y >= len(board[x]) or \
                board[x][y] == "":
            return False

        # keep track of the search
        cur += board[x][y]

        # bigger than word, no
        if len(cur) > len(word):
            return False

        # different letter, no
        index = len(cur) - 1
        if cur[index] != word[index]:
            return False

        # match!
        if cur == word:
            return True

        # navigate through the board, mark visited letter
        temp = board[x][y]
        board[x][y] = ""
        pos = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        for i in range(len(pos)):
            if self.solution(board, word, x + pos[i][0], y + pos[i][1], cur):
                return True

        board[x][y] = temp

        return False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]
word = "ABCCED"
print(s.wordSearch(board, word))
