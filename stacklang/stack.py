class Stack(object):

    def __init__(self, stack=None):
        self.stack = []
        self.size = 0
        if isinstance(stack, Stack):
           for e in Stack.stack:
               self.push(e)

    def __getitem__(self, key):
        return self.stack[key]

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp
        return None
