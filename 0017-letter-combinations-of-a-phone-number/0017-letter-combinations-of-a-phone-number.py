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

        if len(digits) == 0:
            return []
        
        res = [""]   # start with an empty combination
        
        for digit in digits:
            letters = combinations[digit]
            temp = []
            for prefix in res:
                for letter in letters:
                    temp.append(prefix + letter)
            res = temp   # update
        return res
