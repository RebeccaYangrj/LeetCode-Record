class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: return False
        stack =[]
        dic = {")":"(","]":"[","}":"{"} #key point, check value
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif c in dic.keys():
                if stack == [] or stack.pop()!=dic[c]:
                    return False
            else:
                return False
        return stack == []
# Parentheses: stack
# char ==? stack.pop() stack ?== []
