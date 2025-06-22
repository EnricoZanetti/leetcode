class Solution:
    def myAtoi(self, s: str) -> int:

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        is_positive = True
        res = []

        s = s.lstrip()
        if not s:
            return 0

        if s[0] == '-':
            is_positive = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for char in s:
            if char.isdigit():
                res.append(char)
            else:
                break
                
        if not res:
            return 0

        final_number = int(''.join(res))

        if not is_positive:
            final_number = -final_number

        if final_number > MAX_INT:
            return MAX_INT
        elif final_number < MIN_INT:
            return MIN_INT
        
        return final_number

