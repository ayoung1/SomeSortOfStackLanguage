def runCommand(env, command):
    return commands[command](env)

def createStack(env):
    env.addStack()

def jumpStack(env):
    env.jumpStack(env.pop())

def stackShiftLeft(env):
    env.changeStack(-1)

def stackShiftRight(env):
    env.changeStack(1)

def multiply(env):
    a = env.pop()
    b = env.pop()
    env.push(a * b)

def divide(env):
    a = env.pop()
    b = env.pop()
    env.push(a / b)

def subtract(env):
    a = env.pop()
    b = env.pop()
    env.push(a - b)

def add(env):
    a = env.pop()
    b = env.pop()
    env.push(a + b)

def collapse(env):
    tens = env.pop()
    temp = ""
    for _ in xrange(0, tens):
        temp += str(env.pop())
    env.push(int(temp))

def boolean(env):
    check = env.pop()
    try:
        check = int(check)
    finally:
        if not check:
            return True

def reverse(env):
    t = []
    for x in env.stacks[env.stackIndex]:
        t.append(x)
    for x in t:
        env.push(x)

def charPrint(env):
    print(chr(env.pop()))

def peek(env):
    print(env.stacks[env.stackIndex][-1])

def string(env):
    print(env.pop())

commands = {
  'r': reverse,
  '?': boolean,
  '$': createStack,
  '^': jumpStack,
  '<': stackShiftLeft,
  '>': stackShiftRight,
  '+': add,
  '*': multiply,
  '/': divide,
  'P': string,
  'p': peek,
  'v': collapse,
  'c': charPrint
}
