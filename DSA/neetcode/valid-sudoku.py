#code by ai i failed in these type of question...
#pattern: hashmap

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a collection of sets for rows, cols, and 3x3 boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 1. Skip empty spaces
                if val == ".":
                    continue
                
                # 2. Check if we have seen this number in row r, col c, or the 3x3 box
                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False
                
                # 3. Mark the number as seen in all three scopes
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
                
        return True


#most optimize according to ai... O(1)

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # Map '1'-'9' to bit position 0-8
                bit = 1 << (int(val) - 1)
                box_idx = (r // 3) * 3 + (c // 3)

                # Check if bit is already set in row, col, or box
                if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
                    return False

                # Set the bit
                rows[r] |= bit
                cols[c] |= bit
                boxes[box_idx] |= bit

        return True