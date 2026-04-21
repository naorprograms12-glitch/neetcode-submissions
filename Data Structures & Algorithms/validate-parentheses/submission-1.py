class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        if n == 0:
            return True 
        for char in s:
            if char in ['{', '[', '(']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                    
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else: 
                        return False
                
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else: 
                        return False

                if char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else: 
                        return False

        if len(stack) == 0:
            return True
        return False
