import sys
from antlr4 import *
from LilaLexer import LilaLexer
from LilaParser import LilaParser
from LilaLangListener import LilaLangListener
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):

    def _init_(self):
        super(CustomErrorListener, self)._init_()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = 'In line {0}, column {1}: {2}'.format(
            line, column, msg)
        raise SyntaxError(message)

def main():
    sys.tracebacklimit = 0
    input_stream = FileStream('ejemplo.txt')
    lexer = LilaLexer(input_stream)
    lexer._listeners = [CustomErrorListener()]
    stream = CommonTokenStream(lexer)
    parser = LilaParser(stream)
    parser._listeners = [CustomErrorListener()]
    tree = parser.programa()
    #printer = LilaLangListener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()