#! /usr/bin/env python
import click
from stacklang import commands, shuggar
from stacklang.environment import Environment

env_globals = {}

@click.command()
@click.argument('script')
@click.option('--verbose', default=False, help='Output interpreter debug information')
def runScript(script, verbose):
    env_globals['verbose'] = verbose
    try:
        with open(script, r) as inf:
            script = inf.read()
        debug("Script read in from file")
    except Exception as e:
        debug("Script read in as code, not file")
    finally:
        parseCode(script)


def debug(msg):
    if env_globals['verbose']:
        print(msg)


def parseCode(code):
    i = iter(code)
    for c in i:
        try:
            env_globals['env'].push(int(c))
        except:
            try:
                if commands.runCommand(env_globals['env'], c):
                    i.next()
            except KeyError as e:
                debug(e)
                shuggar.parseShuggar(env_globals['env'], c, i)
            except Exception as e:
                debug(e)

if __name__ == '__main__':
    env_globals['env'] = Environment()
    runScript()
