#! /usr/bin/env python
import click
import commands
from environment import Environment

env_globals = {}

@click.command()
@click.option('--script', help='The Script to interpret')
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
    for c in code:
        try:
            env_globals['env'].push(int(c))
        except:
            commands.runCommand(env_globals['env'], c)

if __name__ == '__main__':
    env_globals['env'] = Environment()
    runScript()
