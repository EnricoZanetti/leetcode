class Solution:
    def intToRoman(self, num: int) -> str:
        res = []

        thousands = num // 1000
        res.append("M" * thousands)
        num -= thousands * 1000

        hundreds = (num % 1000) // 100
        if hundreds in (1, 2, 3):
            res.append("C" * hundreds)
        elif hundreds == 4:
            res.append("CD")
        elif hundreds == 5:
            res.append("D")
        elif hundreds in (6, 7, 8):
            res.append("D" + "C" * (hundreds - 5))
        elif hundreds == 9:
            res.append("CM")
        num -= hundreds * 100

        tens = (num % 100) // 10
        if tens in (1, 2, 3):
            res.append("X" * tens)
        elif tens == 4:
            res.append("XL")
        elif tens == 5:
            res.append("L")
        elif tens in (6, 7, 8):
            res.append("L" + "X" * (tens - 5))
        elif tens == 9:
            res.append("XC")
        num -= tens * 10

        ones = num % 10
        if ones in (1, 2, 3):
            res.append("I" * ones)
        elif ones == 4:
            res.append("IV")
        elif ones == 5:
            res.append("V")
        elif ones in (6, 7, 8):
            res.append("V" + "I" * (ones - 5))
        elif ones == 9:
            res.append("IX")

        return "".join(res)
