class Solution:
    def myAtoi(self, str: str) -> int:
        intMax = 2**31 - 1
        intMin = -2**31
        str = str.strip()
        if not str:
            return 0
        sign, i = 1, 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            num = num * 10 + ord(str[i]) - ord('0')
            if num > intMax:
                break
            i += 1
        return min(max(sign * num, intMin), intMax)
