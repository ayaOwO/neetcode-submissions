class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        valid = True
        # row
        # col
        dic = defaultdict(set)
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == ".":
                    continue

                if item in dic["r", i] or item in dic["c", j] or item in dic[i // 3, j // 3]:
                    valid = False
                    return False
                else:
                    dic["r", i].add(item)
                    dic["c",j].add(item)
                    dic[i // 3, j // 3].add(item)

        return valid
