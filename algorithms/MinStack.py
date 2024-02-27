from typing import NamedTuple
"""
Min Stack

difficulty: medium
date: 2024.02.27
link: https://leetcode.com/problems/min-stack/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/8Agz4Ql7OCm
"""

class MinStack:
    """
    Two Stacks

    - Runtime: beats 62%
    - Memory: beats 59%
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        is_min_stack_empty = len(self.min_stack) == 0
        min_val = min(val, self.min_stack[-1] if not is_min_stack_empty else val)
        self.min_stack.append(min_val)
    
    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

"""
    Combined Stack
    - Runtime: beats 44%
    - Memory; beats 21


    StackNode = NamedTuple("StackNode", [("value", int), ("min", int)])

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        curr_min_val = min(val, self.stack[-1].min if len(self.stack) > 0 else val)
        self.stack.append(StackNode(val, curr_min_val))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min
"""     

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()