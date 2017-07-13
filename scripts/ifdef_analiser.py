#!/usr/bin/python
from __future__ import print_function 
import argparse

class bashcolors:
    BLUE = '\033[34m'
    RED = '\033[91m'
    GREEN = '\033[32m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class DefAnalyser(object):
    
    def __init__(self, filename):
        self.src = open(filename, "r")
        self.filename = filename
        self.lines = self.src.readlines()
        self.stripped_lines = [line.strip() for line in self.lines]
    
    def printSrc(self):
        for line_no, line in enumerate(self.lines):
            print ("%04d: %r"%(line_no, line))

    def printIf(self, auto_indent=False, print_path=False, print_filename=False):
        if_depth = 0
        if_path = []
        for line_no, line in enumerate(self.stripped_lines):
            if line.startswith("#if"):
                print(bashcolors.GREEN, end="")
            elif line.startswith("#endif"):
                if_depth -= 1
                if_path.pop()
                print(bashcolors.RED, end="")
            
            print ("%s%04d: (%d) %s - %s%r%s"%("%s:"%(self.filename)*print_filename, line_no+1, if_depth, " && ".join(if_path*print_path) ,"    "*auto_indent*if_depth, line, bashcolors.ENDC))

            if line.startswith("#if"):
                if_depth += 1
                if_path.append(line[3:].strip())
            elif line.startswith("#endif"):
                pass

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='Analyse c file #if and #endif')
    parser.add_argument('-i', '--indentation', action='store_true')
    parser.add_argument('-p', '--print-path', action='store_true')
    parser.add_argument('-f', '--print-filename', action='store_true')
    parser.add_argument('filenames', metavar='N', type=str, nargs='+',
                    help='Files that will be analysed')
    
    args = parser.parse_args()
    for filename in args.filenames:
        print ("")
        print (">>> Analysing %s..."%(filename))
        print ("")
        d = DefAnalyser(filename)
        d.printIf(args.indentation, args.print_path, args.print_filename)

