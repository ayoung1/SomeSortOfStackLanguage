def runCommand(env, command):
    commands[command](env)

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

def toNumber(env):
    tens = env.pop()
    temp = ""
    for _ in xrange(0, tens):
        temp += str(env.pop())
    env.push(int(temp))

def charPrint(env):
    print(chr(env.pop()))

def peek(env):
    print env.stacks[env.stackIndex][-1]

def string(env):
    print env.pop()

commands = {
  '+': add,
  '*': multiply,
  '/': divide,
  'P': string,
  'p': peek,
  'n': toNumber,
  'c': charPrint
}
