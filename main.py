import sys
from antlr4 import *
from LilaLexer import LilaLexer
from LilaParser import LilaParser
from LilaLangListener import LilaLangListener

def main():
    input_stream = FileStream('/Users/lizzie/Documents/GitHub/lila/ejemplo.txt')
    lexer = LilaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LilaParser(stream)
    tree = parser.programa()
    printer = LilaLangListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()