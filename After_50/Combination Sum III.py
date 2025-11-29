class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start, k, target):
            # If we picked k numbers and sum reached target → valid combo
            if k == 0 and target == 0:
                result.append(path.copy())
                return
            # If impossible (too many picks or sum too large/small)
            if k < 0 or target < 0:
                return
            # Try all numbers from 'start' to 9
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, k - 1, target - num)
                path.pop()  # undo
        backtrack(1, k, n)
        return result
