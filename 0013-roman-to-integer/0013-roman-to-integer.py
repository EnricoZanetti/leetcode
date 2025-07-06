class Solution:
    def romanToInt(self, s: str) -> int:

        res = 0
        n = len(s)
        
        for i in range(n):

            if s[i] == 'I':
                if i+1 < n and s[i+1] == 'V':
                    res += 4
                elif i+1 < n and s[i+1] == 'X':
                    res += 9
                else:
                    res += 1

            elif s[i] == 'V':
                if i > 0 and s[i-1] == 'I':
                    continue
                res += 5

            elif s[i] == 'X':
                if i > 0 and s[i-1] == 'I':
                    continue
                if i+1 < n and s[i+1] == 'L':
                    res += 40
                elif i+1 < n and s[i+1] == 'C':
                    res += 90
                else:
                    res += 10

            elif s[i] == 'L':
                if i > 0 and s[i-1] == 'X':
                    continue
                res += 50

            elif s[i] == 'C':
                if i > 0 and s[i-1] == 'X':
                    continue
                if i+1 < n and s[i+1] == 'D':
                    res += 400
                elif i+1 < n and s[i+1] == 'M':
                    res += 900
                else:
                    res += 100

            elif s[i] == 'D':
                if i > 0 and s[i-1] == 'C':
                    continue
                res += 500

            elif s[i] == 'M':
                if i > 0 and s[i-1] == 'C':
                    continue
                res += 1000

        return res