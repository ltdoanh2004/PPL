import sys, os
import subprocess
import unittest
import shutil
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
print(DIR)
ANTLR_JAR = '/Users/doa_ai/Developer/Poem_PPL/antlr-4.10.1-complete.jar' # your location is going here
CPL_Dest = os.path.join(DIR, 'CompiledFiles_poem_ppl')  # Use absolute path
SRC = os.path.join(DIR, 'PoemDSL.g4')  # Use absolute path
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')    
    print('python run.py test')
    print('python run.py dsl "<command>"')  # New command for DSL

def generateAntlr2Python():
    print('Antlr4 is running...')
    
    # Clean up existing generated files
    if os.path.exists(CPL_Dest):
        shutil.rmtree(CPL_Dest)
    
    # Create output directory
    os.makedirs(CPL_Dest, exist_ok=True)
    
    # Generate ANTLR files with visitor
    cmd = [
        'java', '-jar', ANTLR_JAR,
        '-o', CPL_Dest,
        '-Dlanguage=Python3',
        '-visitor',  # Generate visitor
        SRC
    ]
    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    
    # Create __init__.py to make it a proper Python package
    with open(os.path.join(CPL_Dest, '__init__.py'), 'w') as f:
        f.write('# Generated ANTLR files\n')
    
    print('Generate successfully')

def runTest():
    print('Running testcases...')
    sys.path.append(CPL_Dest)  # Add the generated files directory to Python path
    from PoemDSLLexer import PoemDSLLexer
    from PoemDSLParser import PoemDSLParser
    from poem_dsl_parser import parse_poem_command

    test_commands = [
        'GENERATE POEM MODEL 0 CONTEXT "ai ơi" STANZAS 2',
        'GEN POEM M 0 C "ai ơi" S 2',
        'GENERATE CONTROLLED POEM CONTEXT "cha mẹ một nắng hai sương" TOPIC 3',
        'GEN CONTROLLED POEM C "cha mẹ một nắng hai sương" T 3'
    ]

    for cmd in test_commands:
        print(f'\nTesting command: {cmd}')
        success, result = parse_poem_command(cmd)
        if success:
            print("Success!")
            print(result)
        else:
            print(result)

def runDSL(command):
    print('Running DSL command...')
    sys.path.append(CPL_Dest)  # Add the generated files directory to Python path
    from poem_dsl_parser import parse_poem_command
    
    success, result = parse_poem_command(command)
    if success:
        print("Success!")
        print(result)
    else:
        print(result)

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
       
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':                    
        runTest()
    elif argv[0] == 'dsl':
        if len(argv) < 2:
            print("Error: Please provide a DSL command")
            printUsage()
        else:
            runDSL(argv[1])
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])     
    