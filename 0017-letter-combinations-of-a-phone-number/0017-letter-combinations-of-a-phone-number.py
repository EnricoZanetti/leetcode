class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combinations = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        if len(digits) == 0:
            return []
        
        # iterative stack to simulate DFS
        stack = [("", 0)]  # (current_string, current_index)
        res = []
        
        while stack:
            current, index = stack.pop()
            
            if index == len(digits):
                res.append(current)
            else:
                for letter in combinations[digits[index]]:
                    stack.append((current + letter, index + 1))
        
        return res
