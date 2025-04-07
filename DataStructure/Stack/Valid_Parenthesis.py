#Leetcode 
#Valid Parenthesis 
class Solution:
    def isValid(self, s: str) -> bool:
        mapper={')': '(', '}': '{', ']' : '['}
        stack=[]

        for c in s:
            #if opening bracket put in stack 

            #else for clsoing bracket if stack not empty then check the peek == vlaue of closing bracket 
                #pop if yes 
                #else 
                #return false 
        #if empty stack then true else False 
            if c in mapper.values():
                stack.append(c)
            elif stack and stack[-1]==mapper[c]:
                stack.pop()
            else:
                return False
        return True if not stack else False
        

        
