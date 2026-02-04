class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in ['[','{','(']:
                stack.append(item)
            elif item == ')' and stack[-1] == '(':
                stack.remove(stack[-1])
            elif item == ']' and stack[-1] == '[':
                stack.remove(stack[-1]) 
            elif item == '}' and stack[-1] == '{':
                stack.remove(stack[-1])
        if stack:
            return False
        else:
            return True    