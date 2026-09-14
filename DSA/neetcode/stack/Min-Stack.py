#solution by ai...
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            # self.min_stack[-1] gives you the current minimum (the top of min_stack)
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        # Removes the top item from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Returns the top item of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Returns the top item of the min stack
        return self.min_stack[-1]

#i asked ai first pseudocode and tried also i didn't know how to access last element...
class MinStack:

    def __init__(self):
        Stack=[]
        MinStack=[]

    def push(self, val: int) -> None:
        Stack.append(val)
        if len(MinStack)==0:
            MinStack.append(val)
        else:
            currentmin=min(val,...)
            Minstack.append(currentmin)

    def pop(self) -> None:
        ...

    def top(self) -> int:
        ...

    def getMin(self) -> int:
        ...
