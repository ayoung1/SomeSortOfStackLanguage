from stack import Stack

class Environment(object):
    def __init__(self, env=None):
        self.parent = env
        self.stacks = [Stack()]
        self.stackIndex = 0
        self.__mergeEnvs(env)

    def changeStack(self, direction):
        if direction > 0:
            self.stackIndex += 1
        elif direction < 0:
            self.stackIndex -= 1
        self.__clamp()

    def push(self, ele):
        self.stacks[self.stackIndex].push(ele)

    def pop(self):
        return self.stacks[self.stackIndex].pop()

    def addStack(self, copy=0, retain=False):
        temp = Stack()
        for _ in xrange(0, copy):
            temp.push(self.pop())
        self.stacks.append(temp)

    def removeStack(self, retain=False):
        del self.stacks[self.stackIndex]
        self.__clamp()

    def __mergeEnvs(self, env):
        if env is not None:
            for stack in env.stacks:
                self.stacks.append(stack)

    def __clamp(self):
        self.stackIndex = max(0, min(self.stackIndex, len(self.stacks)-1))
