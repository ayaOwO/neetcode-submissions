class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        valid = True
        # row
        # col
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == ".":
                    continue

                if item in rows[i] or item in cols[j] or item in square[i // 3, j // 3]:
                    valid = False
                    return False
                else:
                    rows[i].add(item)
                    cols[j].add(item)
                    square[i // 3, j // 3].add(item)

        return valid
