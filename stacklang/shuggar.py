import commands

def parseShuggar(env, c, i):
    shuggar[c](env, i)

def fancyStrings(env, i):
    string = ""
    for c in i:
        if ord(c) is not ord('"'):
            string += str(c)
        else:
            break
    string = string[::-1]
    for c in string:
        env.push(ord(c))
    env.push(len(string))

def setFunction(env, i):
    function = ""
    commands.runCommand(env, '$')
    for c in i:
        if ord(c) is not ord('}'):
            function += c
        else:
            break
    for c in function[::-1]:
        env.push(ord(c))
    env.push(len(function))
    commands.runCommand(env, '>')

def runFunction(env, i):
    index = env.stackIndex
    commands.runCommand(env, '^')
    length = env.pop()
    function = ""
    for _ in xrange(0, length):
        function += chr(env.pop())
    for c in function[::-1]:
        env.push(ord(c))
    env.push(len(function))
    env.push(index)
    commands.runCommand(env, '^')
    for c in function:
        try:
            if commands.runCommand(env, c):
                i.next()
        except:
            parseShuggar(env, c, i)

def printString(env, i):
    length = env.pop()
    string = ""
    for _ in xrange(0, length):
        commands.runCommand(env, 'c')

shuggar = {
  "~": runFunction,
  "{": setFunction,
  "\"": fancyStrings,
  "&": printString
}
