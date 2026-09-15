#solution...
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                # int(a / b) truncates toward zero for both positive and negative results
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

#my code...
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for i in tokens:
            if i.isdigit():
                res.append(i)
            elif i=="+":
                res.append(int(res.pop(-2))+int(res.pop(-1)))
            elif i=="-":
                res.append(int(res.pop(-2))-int(res.pop(-1)))
            elif i=="*":
              res.append(int(res.pop(-2))*int(res.pop(-1)))
            elif i=="/":
                res.append(int(res.pop(-2))/int(res.pop(-1)))
        if len(res)==1:
            return res[0]