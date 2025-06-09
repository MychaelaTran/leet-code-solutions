class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        paint = {}  #{ball : col}
        col_count = defaultdict(int)  #{col : num_balls}
        result = []

        for ball, col in queries:
            if ball in paint:
                old_col = paint[ball]
                col_count[old_col] -= 1
                if col_count[old_col] == 0:
                    del col_count[old_col]  # remove color if no ball has it

            paint[ball] = col
            col_count[col] += 1
            result.append(len(col_count))

        return result
