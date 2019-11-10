# Generated from Lila.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Operand, VirtualAddress
gen = IntermediateGenerator()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u01cb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\5\2\67\n\2\3\2\7\2:\n\2\f\2\16\2")
        buf.write("=\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3F\n\3\r\3\16\3G")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4S\n\4\f\4\16\4")
        buf.write("V\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6b\n")
        buf.write("\6\f\6\16\6e\13\6\3\7\3\7\3\7\5\7j\n\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7r\n\7\3\7\3\7\3\7\5\7w\n\7\3\7\6\7z\n\7\r")
        buf.write("\7\16\7{\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\b\u008b\n\b\f\b\16\b\u008e\13\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u0098\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00a1\n\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00a9")
        buf.write("\n\13\f\13\16\13\u00ac\13\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00b8\n\f\f\f\16\f\u00bb\13\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c6\n\r\f\r\16")
        buf.write("\r\u00c9\13\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d1\n\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7")
        buf.write("\17\u00de\n\17\f\17\16\17\u00e1\13\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\7\17\u00eb\n\17\f\17\16\17\u00ee")
        buf.write("\13\17\5\17\u00f0\n\17\3\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00f8\n\20\3\20\3\20\3\20\7\20\u00fd\n\20\f\20\16")
        buf.write("\20\u0100\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u010f\n\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u0115\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u011d\n\22\3\22\3\22\3\22\7\22\u0122\n\22\f\22\16")
        buf.write("\22\u0125\13\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u012d")
        buf.write("\n\23\3\23\3\23\3\23\7\23\u0132\n\23\f\23\16\23\u0135")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u013e\n")
        buf.write("\24\3\24\5\24\u0141\n\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u014f\n\25\f\25\16")
        buf.write("\25\u0152\13\25\5\25\u0154\n\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u0160\n\25\f\25\16\25")
        buf.write("\u0163\13\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u016d\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0182\n\27\f\27\16\27\u0185\13\27\5\27\u0187\n\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0194\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\5\31\u01a3\n\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u01c9\n\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\2\5\3\2\f\17\3\2\32\33")
        buf.write("\3\2+\65\2\u01ea\2\62\3\2\2\2\4C\3\2\2\2\6L\3\2\2\2\b")
        buf.write("Y\3\2\2\2\n]\3\2\2\2\ff\3\2\2\2\16\u0082\3\2\2\2\20\u0097")
        buf.write("\3\2\2\2\22\u0099\3\2\2\2\24\u00a5\3\2\2\2\26\u00af\3")
        buf.write("\2\2\2\30\u00bf\3\2\2\2\32\u00d4\3\2\2\2\34\u00ef\3\2")
        buf.write("\2\2\36\u00f1\3\2\2\2 \u0114\3\2\2\2\"\u0116\3\2\2\2$")
        buf.write("\u0126\3\2\2\2&\u0140\3\2\2\2(\u016c\3\2\2\2*\u016e\3")
        buf.write("\2\2\2,\u0175\3\2\2\2.\u018d\3\2\2\2\60\u01c8\3\2\2\2")
        buf.write("\62\63\7\4\2\2\63\64\7;\2\2\64\66\b\2\1\2\65\67\5\4\3")
        buf.write("\2\66\65\3\2\2\2\66\67\3\2\2\2\67;\3\2\2\28:\5\f\7\29")
        buf.write("8\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3")
        buf.write("\2\2\2>?\b\2\1\2?@\5\b\5\2@A\b\2\1\2AB\b\2\1\2B\3\3\2")
        buf.write("\2\2CE\7\t\2\2DF\5\6\4\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2")
        buf.write("GH\3\2\2\2HI\3\2\2\2IJ\b\3\1\2JK\b\3\1\2K\5\3\2\2\2LM")
        buf.write("\5\n\6\2MN\7;\2\2NT\b\4\1\2OP\7\30\2\2PQ\7;\2\2QS\b\4")
        buf.write("\1\2RO\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2")
        buf.write("VT\3\2\2\2WX\7\31\2\2X\7\3\2\2\2YZ\7\3\2\2Z[\b\5\1\2[")
        buf.write("\\\5\24\13\2\\\t\3\2\2\2]c\t\2\2\2^_\7\22\2\2_`\7\'\2")
        buf.write("\2`b\7\23\2\2a^\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2")
        buf.write("d\13\3\2\2\2ec\3\2\2\2fi\7\b\2\2gj\5\n\6\2hj\7\5\2\2i")
        buf.write("g\3\2\2\2ih\3\2\2\2jk\3\2\2\2kl\7;\2\2lm\b\7\1\2mn\b\7")
        buf.write("\1\2no\b\7\1\2oq\7\24\2\2pr\5\16\b\2qp\3\2\2\2qr\3\2\2")
        buf.write("\2rs\3\2\2\2st\7\25\2\2tv\7\26\2\2uw\5\4\3\2vu\3\2\2\2")
        buf.write("vw\3\2\2\2wy\3\2\2\2xz\5\20\t\2yx\3\2\2\2z{\3\2\2\2{y")
        buf.write("\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7\27\2\2~\177\b\7\1\2\177")
        buf.write("\u0080\b\7\1\2\u0080\u0081\b\7\1\2\u0081\r\3\2\2\2\u0082")
        buf.write("\u0083\5\n\6\2\u0083\u0084\7;\2\2\u0084\u008c\b\b\1\2")
        buf.write("\u0085\u0086\7\30\2\2\u0086\u0087\5\n\6\2\u0087\u0088")
        buf.write("\7;\2\2\u0088\u0089\b\b\1\2\u0089\u008b\3\2\2\2\u008a")
        buf.write("\u0085\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\17\3\2\2\2\u008e\u008c\3\2")
        buf.write("\2\2\u008f\u0098\5\30\r\2\u0090\u0098\5\22\n\2\u0091\u0098")
        buf.write("\5*\26\2\u0092\u0098\5\26\f\2\u0093\u0098\5.\30\2\u0094")
        buf.write("\u0098\5,\27\2\u0095\u0098\5\32\16\2\u0096\u0098\5\60")
        buf.write("\31\2\u0097\u008f\3\2\2\2\u0097\u0090\3\2\2\2\u0097\u0091")
        buf.write("\3\2\2\2\u0097\u0092\3\2\2\2\u0097\u0093\3\2\2\2\u0097")
        buf.write("\u0094\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2")
        buf.write("\u0098\21\3\2\2\2\u0099\u009a\7\13\2\2\u009a\u009b\5\36")
        buf.write("\20\2\u009b\u009c\b\n\1\2\u009c\u00a0\5\24\13\2\u009d")
        buf.write("\u009e\7\n\2\2\u009e\u009f\b\n\1\2\u009f\u00a1\5\24\13")
        buf.write("\2\u00a0\u009d\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\7\31\2\2\u00a3\u00a4\b\n\1\2\u00a4")
        buf.write("\23\3\2\2\2\u00a5\u00a6\7\26\2\2\u00a6\u00aa\5\20\t\2")
        buf.write("\u00a7\u00a9\5\20\t\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7\27\2")
        buf.write("\2\u00ae\25\3\2\2\2\u00af\u00b0\7\6\2\2\u00b0\u00b1\7")
        buf.write("\24\2\2\u00b1\u00b2\5\36\20\2\u00b2\u00b9\b\f\1\2\u00b3")
        buf.write("\u00b4\7\30\2\2\u00b4\u00b5\5\36\20\2\u00b5\u00b6\b\f")
        buf.write("\1\2\u00b6\u00b8\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b8\u00bb")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\7\25\2")
        buf.write("\2\u00bd\u00be\7\31\2\2\u00be\27\3\2\2\2\u00bf\u00c0\7")
        buf.write(";\2\2\u00c0\u00c7\b\r\1\2\u00c1\u00c2\7\22\2\2\u00c2\u00c3")
        buf.write("\5\"\22\2\u00c3\u00c4\7\23\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c1\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3")
        buf.write("\2\2\2\u00ca\u00cb\7\"\2\2\u00cb\u00d0\b\r\1\2\u00cc\u00cd")
        buf.write("\5\36\20\2\u00cd\u00ce\b\r\1\2\u00ce\u00d1\3\2\2\2\u00cf")
        buf.write("\u00d1\5\34\17\2\u00d0\u00cc\3\2\2\2\u00d0\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7\31\2\2\u00d3\31\3")
        buf.write("\2\2\2\u00d4\u00d5\7\20\2\2\u00d5\u00d6\5\36\20\2\u00d6")
        buf.write("\u00d7\b\16\1\2\u00d7\u00d8\b\16\1\2\u00d8\u00d9\7\31")
        buf.write("\2\2\u00d9\33\3\2\2\2\u00da\u00df\5(\25\2\u00db\u00dc")
        buf.write("\7\30\2\2\u00dc\u00de\5(\25\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00f0\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7")
        buf.write("\22\2\2\u00e3\u00e4\5\34\17\2\u00e4\u00ec\7\23\2\2\u00e5")
        buf.write("\u00e6\7\30\2\2\u00e6\u00e7\7\22\2\2\u00e7\u00e8\5\34")
        buf.write("\17\2\u00e8\u00e9\7\23\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e5")
        buf.write("\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ef\u00da\3\2\2\2\u00ef\u00e2\3\2\2\2\u00f0\35\3\2")
        buf.write("\2\2\u00f1\u00f2\5 \21\2\u00f2\u00fe\b\20\1\2\u00f3\u00f4")
        buf.write("\7%\2\2\u00f4\u00f8\b\20\1\2\u00f5\u00f6\7&\2\2\u00f6")
        buf.write("\u00f8\b\20\1\2\u00f7\u00f3\3\2\2\2\u00f7\u00f5\3\2\2")
        buf.write("\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\5 \21\2\u00fa\u00fb")
        buf.write("\b\20\1\2\u00fb\u00fd\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fd")
        buf.write("\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\37\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u010e\5\"")
        buf.write("\22\2\u0102\u0103\7\37\2\2\u0103\u010f\b\21\1\2\u0104")
        buf.write("\u0105\7\36\2\2\u0105\u010f\b\21\1\2\u0106\u0107\7 \2")
        buf.write("\2\u0107\u010f\b\21\1\2\u0108\u0109\7!\2\2\u0109\u010f")
        buf.write("\b\21\1\2\u010a\u010b\7$\2\2\u010b\u010f\b\21\1\2\u010c")
        buf.write("\u010d\7#\2\2\u010d\u010f\b\21\1\2\u010e\u0102\3\2\2\2")
        buf.write("\u010e\u0104\3\2\2\2\u010e\u0106\3\2\2\2\u010e\u0108\3")
        buf.write("\2\2\2\u010e\u010a\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0111\5\"\22\2\u0111\u0112\b\21\1\2\u0112")
        buf.write("\u0115\3\2\2\2\u0113\u0115\5\"\22\2\u0114\u0101\3\2\2")
        buf.write("\2\u0114\u0113\3\2\2\2\u0115!\3\2\2\2\u0116\u0117\5$\23")
        buf.write("\2\u0117\u0123\b\22\1\2\u0118\u0119\7\32\2\2\u0119\u011d")
        buf.write("\b\22\1\2\u011a\u011b\7\33\2\2\u011b\u011d\b\22\1\2\u011c")
        buf.write("\u0118\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011f\5$\23\2\u011f\u0120\b\22\1\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u011c\3\2\2\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124#\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0126\u0127\5&\24\2\u0127\u0133\b\23\1")
        buf.write("\2\u0128\u0129\7\34\2\2\u0129\u012d\b\23\1\2\u012a\u012b")
        buf.write("\7\35\2\2\u012b\u012d\b\23\1\2\u012c\u0128\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\5&\24\2")
        buf.write("\u012f\u0130\b\23\1\2\u0130\u0132\3\2\2\2\u0131\u012c")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134%\3\2\2\2\u0135\u0133\3\2\2\2\u0136")
        buf.write("\u0137\7\24\2\2\u0137\u0138\b\24\1\2\u0138\u0139\5\36")
        buf.write("\20\2\u0139\u013a\7\25\2\2\u013a\u013b\b\24\1\2\u013b")
        buf.write("\u0141\3\2\2\2\u013c\u013e\t\3\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\5")
        buf.write("(\25\2\u0140\u0136\3\2\2\2\u0140\u013d\3\2\2\2\u0141\'")
        buf.write("\3\2\2\2\u0142\u0143\7;\2\2\u0143\u0144\7\24\2\2\u0144")
        buf.write("\u0145\b\25\1\2\u0145\u0146\b\25\1\2\u0146\u0147\b\25")
        buf.write("\1\2\u0147\u0153\b\25\1\2\u0148\u0149\5\36\20\2\u0149")
        buf.write("\u0150\b\25\1\2\u014a\u014b\7\30\2\2\u014b\u014c\5\36")
        buf.write("\20\2\u014c\u014d\b\25\1\2\u014d\u014f\3\2\2\2\u014e\u014a")
        buf.write("\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0153\u0148\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3")
        buf.write("\2\2\2\u0155\u0156\b\25\1\2\u0156\u0157\7\25\2\2\u0157")
        buf.write("\u0158\b\25\1\2\u0158\u016d\b\25\1\2\u0159\u015a\7;\2")
        buf.write("\2\u015a\u0161\b\25\1\2\u015b\u015c\7\22\2\2\u015c\u015d")
        buf.write("\5\"\22\2\u015d\u015e\7\23\2\2\u015e\u0160\3\2\2\2\u015f")
        buf.write("\u015b\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u016d\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0164\u0165\7\'\2\2\u0165\u016d\b\25\1\2\u0166")
        buf.write("\u0167\7)\2\2\u0167\u016d\b\25\1\2\u0168\u0169\7(\2\2")
        buf.write("\u0169\u016d\b\25\1\2\u016a\u016b\7*\2\2\u016b\u016d\b")
        buf.write("\25\1\2\u016c\u0142\3\2\2\2\u016c\u0159\3\2\2\2\u016c")
        buf.write("\u0164\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0168\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016d)\3\2\2\2\u016e\u016f\7\7\2")
        buf.write("\2\u016f\u0170\b\26\1\2\u0170\u0171\5\36\20\2\u0171\u0172")
        buf.write("\b\26\1\2\u0172\u0173\5\24\13\2\u0173\u0174\b\26\1\2\u0174")
        buf.write("+\3\2\2\2\u0175\u0176\7;\2\2\u0176\u0177\7\24\2\2\u0177")
        buf.write("\u0178\b\27\1\2\u0178\u0179\b\27\1\2\u0179\u017a\b\27")
        buf.write("\1\2\u017a\u0186\b\27\1\2\u017b\u017c\5\36\20\2\u017c")
        buf.write("\u0183\b\27\1\2\u017d\u017e\7\30\2\2\u017e\u017f\5\36")
        buf.write("\20\2\u017f\u0180\b\27\1\2\u0180\u0182\3\2\2\2\u0181\u017d")
        buf.write("\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0186\u017b\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3")
        buf.write("\2\2\2\u0188\u0189\b\27\1\2\u0189\u018a\7\25\2\2\u018a")
        buf.write("\u018b\b\27\1\2\u018b\u018c\7\31\2\2\u018c-\3\2\2\2\u018d")
        buf.write("\u018e\7\21\2\2\u018e\u018f\7\24\2\2\u018f\u0190\7;\2")
        buf.write("\2\u0190\u0193\b\30\1\2\u0191\u0192\7\30\2\2\u0192\u0194")
        buf.write("\7(\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\7\25\2\2\u0196\u0197\7\31\2")
        buf.write("\2\u0197/\3\2\2\2\u0198\u0199\t\4\2\2\u0199\u019a\7\24")
        buf.write("\2\2\u019a\u019b\7;\2\2\u019b\u019c\7\25\2\2\u019c\u01c9")
        buf.write("\7\31\2\2\u019d\u019e\7\66\2\2\u019e\u019f\7\24\2\2\u019f")
        buf.write("\u01a2\7;\2\2\u01a0\u01a1\7\30\2\2\u01a1\u01a3\7;\2\2")
        buf.write("\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01a5\7\25\2\2\u01a5\u01c9\7\31\2\2\u01a6")
        buf.write("\u01a7\7\67\2\2\u01a7\u01a8\7\24\2\2\u01a8\u01a9\7;\2")
        buf.write("\2\u01a9\u01aa\7\30\2\2\u01aa\u01ab\7;\2\2\u01ab\u01ac")
        buf.write("\7\25\2\2\u01ac\u01c9\7\31\2\2\u01ad\u01ae\78\2\2\u01ae")
        buf.write("\u01af\7\24\2\2\u01af\u01b0\7)\2\2\u01b0\u01b1\7\30\2")
        buf.write("\2\u01b1\u01b2\7)\2\2\u01b2\u01b3\7\30\2\2\u01b3\u01b4")
        buf.write("\7\'\2\2\u01b4\u01b5\7\25\2\2\u01b5\u01c9\7\31\2\2\u01b6")
        buf.write("\u01b7\79\2\2\u01b7\u01b8\7\24\2\2\u01b8\u01b9\7;\2\2")
        buf.write("\u01b9\u01ba\7\30\2\2\u01ba\u01bb\5(\25\2\u01bb\u01bc")
        buf.write("\7\30\2\2\u01bc\u01bd\5(\25\2\u01bd\u01be\7\25\2\2\u01be")
        buf.write("\u01bf\7\31\2\2\u01bf\u01c9\3\2\2\2\u01c0\u01c1\7:\2\2")
        buf.write("\u01c1\u01c2\7\24\2\2\u01c2\u01c3\7;\2\2\u01c3\u01c4\7")
        buf.write("\30\2\2\u01c4\u01c5\5(\25\2\u01c5\u01c6\7\25\2\2\u01c6")
        buf.write("\u01c7\7\31\2\2\u01c7\u01c9\3\2\2\2\u01c8\u0198\3\2\2")
        buf.write("\2\u01c8\u019d\3\2\2\2\u01c8\u01a6\3\2\2\2\u01c8\u01ad")
        buf.write("\3\2\2\2\u01c8\u01b6\3\2\2\2\u01c8\u01c0\3\2\2\2\u01c9")
        buf.write("\61\3\2\2\2(\66;GTciqv{\u008c\u0097\u00a0\u00aa\u00b9")
        buf.write("\u00c7\u00d0\u00df\u00ec\u00ef\u00f7\u00fe\u010e\u0114")
        buf.write("\u011c\u0123\u012c\u0133\u013d\u0140\u0150\u0153\u0161")
        buf.write("\u016c\u0183\u0186\u0193\u01a2\u01c8")
        return buf.getvalue()


class LilaParser ( Parser ):

    grammarFileName = "Lila.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'lila'", "'void'", "'display'", 
                     "'while'", "'func'", "'var'", "'else'", "'if'", "'int'", 
                     "'num'", "'text'", "'bool'", "'return'", "'getinput'", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "','", "';'", 
                     "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!='", "'=='", 
                     "'='", "'<='", "'>='", "'AND'", "'OR'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'getOutliers'", 
                     "'removeOutliers'", "'tellMeWhatToUse'", "'printMeasures'", 
                     "'mean'", "'median'", "'mode'", "'range'", "'min'", 
                     "'max'", "'desEstandar'", "'quickShow'", "'pearsoneCorrelation'", 
                     "'normalDistribution'", "'fillValue'", "'removeValue'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "LILA", "VOID", "DISPLAY", "WHILE", 
                      "FUNC", "VAR", "ELSE", "IF", "INT", "NUM", "TEXT", 
                      "BOOL", "RETURN", "GETINPUT", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_CURLY", 
                      "CLOSE_CURLY", "COMMA", "SEMICOLON", "PLUS", "MINUS", 
                      "MULTIPLICATION", "DIVISION", "LESS_THAN", "GREATER_THAN", 
                      "NOTEQUAL", "EQUALITY", "EQUAL", "LESS_THAN_EQUAL", 
                      "GREATER_THAN_EQUAL", "AND", "OR", "CTE_INT", "CTE_STRING", 
                      "CTE_F", "CTE_BOOL", "GETOUTLIERS", "REMOVEOUTLIERS", 
                      "TELLMEWHATTOUSE", "PRINTMEASURES", "MEAN", "MEDIAN", 
                      "MODE", "RANGE", "MIN", "MAX", "DESESTANDAR", "QUICKSHOW", 
                      "PEARSONCORRELATION", "NORMALDISTRIBUTION", "FILLVALUE", 
                      "REMOVEVALUE", "ID", "WS", "Comment" ]

    RULE_programa = 0
    RULE_data = 1
    RULE_data2 = 2
    RULE_main = 3
    RULE_tipo = 4
    RULE_funciones = 5
    RULE_params = 6
    RULE_estatuto = 7
    RULE_condicion = 8
    RULE_bloque = 9
    RULE_display = 10
    RULE_asignacion = 11
    RULE_sreturn = 12
    RULE_arr = 13
    RULE_expresion = 14
    RULE_comparacion = 15
    RULE_exp = 16
    RULE_termino = 17
    RULE_factor = 18
    RULE_var_cte = 19
    RULE_swhile = 20
    RULE_invocacion = 21
    RULE_getinput = 22
    RULE_especiales = 23

    ruleNames =  [ "programa", "data", "data2", "main", "tipo", "funciones", 
                   "params", "estatuto", "condicion", "bloque", "display", 
                   "asignacion", "sreturn", "arr", "expresion", "comparacion", 
                   "exp", "termino", "factor", "var_cte", "swhile", "invocacion", 
                   "getinput", "especiales" ]

    EOF = Token.EOF
    MAIN=1
    LILA=2
    VOID=3
    DISPLAY=4
    WHILE=5
    FUNC=6
    VAR=7
    ELSE=8
    IF=9
    INT=10
    NUM=11
    TEXT=12
    BOOL=13
    RETURN=14
    GETINPUT=15
    OPEN_BRACKET=16
    CLOSE_BRACKET=17
    OPEN_PARENTHESIS=18
    CLOSE_PARENTHESIS=19
    OPEN_CURLY=20
    CLOSE_CURLY=21
    COMMA=22
    SEMICOLON=23
    PLUS=24
    MINUS=25
    MULTIPLICATION=26
    DIVISION=27
    LESS_THAN=28
    GREATER_THAN=29
    NOTEQUAL=30
    EQUALITY=31
    EQUAL=32
    LESS_THAN_EQUAL=33
    GREATER_THAN_EQUAL=34
    AND=35
    OR=36
    CTE_INT=37
    CTE_STRING=38
    CTE_F=39
    CTE_BOOL=40
    GETOUTLIERS=41
    REMOVEOUTLIERS=42
    TELLMEWHATTOUSE=43
    PRINTMEASURES=44
    MEAN=45
    MEDIAN=46
    MODE=47
    RANGE=48
    MIN=49
    MAX=50
    DESESTANDAR=51
    QUICKSHOW=52
    PEARSONCORRELATION=53
    NORMALDISTRIBUTION=54
    FILLVALUE=55
    REMOVEVALUE=56
    ID=57
    WS=58
    Comment=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LILA(self):
            return self.getToken(LilaParser.LILA, 0)

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def main(self):
            return self.getTypedRuleContext(LilaParser.MainContext,0)


        def data(self):
            return self.getTypedRuleContext(LilaParser.DataContext,0)


        def funciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.FuncionesContext)
            else:
                return self.getTypedRuleContext(LilaParser.FuncionesContext,i)


        def getRuleIndex(self):
            return LilaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LilaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(LilaParser.LILA)
            self.state = 49
            self.match(LilaParser.ID)
            gen.goTo()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 51
                self.data()


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.FUNC:
                self.state = 54
                self.funciones()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            gen.conditionEnd()
            self.state = 61
            self.main()
            gen.end()
            gen.test_final()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LilaParser.VAR, 0)

        def data2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.Data2Context)
            else:
                return self.getTypedRuleContext(LilaParser.Data2Context,i)


        def getRuleIndex(self):
            return LilaParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = LilaParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(LilaParser.VAR)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.data2()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                    break

            Semantic.isGlobal = False
            VirtualAddress.resetLocals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token

        def tipo(self):
            return self.getTypedRuleContext(LilaParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.ID)
            else:
                return self.getToken(LilaParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def getRuleIndex(self):
            return LilaParser.RULE_data2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData2" ):
                listener.enterData2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData2" ):
                listener.exitData2(self)




    def data2(self):

        localctx = LilaParser.Data2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            localctx._tipo = self.tipo()
            self.state = 75
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 77
                self.match(LilaParser.COMMA)
                self.state = 78
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(LilaParser.MAIN, 0)

        def bloque(self):
            return self.getTypedRuleContext(LilaParser.BloqueContext,0)


        def getRuleIndex(self):
            return LilaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = LilaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(LilaParser.MAIN)
            gen.contextChange()
            self.state = 89
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LilaParser.INT, 0)

        def NUM(self):
            return self.getToken(LilaParser.NUM, 0)

        def TEXT(self):
            return self.getToken(LilaParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(LilaParser.BOOL, 0)

        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OPEN_BRACKET)
            else:
                return self.getToken(LilaParser.OPEN_BRACKET, i)

        def CTE_INT(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CTE_INT)
            else:
                return self.getToken(LilaParser.CTE_INT, i)

        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CLOSE_BRACKET)
            else:
                return self.getToken(LilaParser.CLOSE_BRACKET, i)

        def getRuleIndex(self):
            return LilaParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LilaParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 92
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 93
                self.match(LilaParser.CTE_INT)
                self.state = 94
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._VOID = None # Token
            self._ID = None # Token

        def FUNC(self):
            return self.getToken(LilaParser.FUNC, 0)

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def OPEN_CURLY(self):
            return self.getToken(LilaParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(LilaParser.CLOSE_CURLY, 0)

        def tipo(self):
            return self.getTypedRuleContext(LilaParser.TipoContext,0)


        def VOID(self):
            return self.getToken(LilaParser.VOID, 0)

        def params(self):
            return self.getTypedRuleContext(LilaParser.ParamsContext,0)


        def data(self):
            return self.getTypedRuleContext(LilaParser.DataContext,0)


        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.EstatutoContext)
            else:
                return self.getTypedRuleContext(LilaParser.EstatutoContext,i)


        def getRuleIndex(self):
            return LilaParser.RULE_funciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunciones" ):
                listener.enterFunciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunciones" ):
                listener.exitFunciones(self)




    def funciones(self):

        localctx = LilaParser.FuncionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LilaParser.FUNC)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.INT, LilaParser.NUM, LilaParser.TEXT, LilaParser.BOOL]:
                self.state = 101
                localctx._tipo = self.tipo()
                pass
            elif token in [LilaParser.VOID]:
                self.state = 102
                localctx._VOID = self.match(LilaParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 105
            localctx._ID = self.match(LilaParser.ID)
            index = len(gen.Quadruples)
            Semantic.enterFunciones((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),(None if localctx._VOID is None else localctx._VOID.text),index)
            gen.contextChange()
            self.state = 109
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0):
                self.state = 110
                self.params()


            self.state = 113
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 114
            self.match(LilaParser.OPEN_CURLY)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 115
                self.data()


            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.estatuto()
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0)):
                    break

            self.state = 123
            self.match(LilaParser.CLOSE_CURLY)
            gen.endProc()
            Semantic.display_test()
            Semantic.dump_varFunt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.TipoContext)
            else:
                return self.getTypedRuleContext(LilaParser.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.ID)
            else:
                return self.getToken(LilaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def getRuleIndex(self):
            return LilaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = LilaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            localctx._tipo = self.tipo()
            self.state = 129
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 131
                self.match(LilaParser.COMMA)
                self.state = 132
                localctx._tipo = self.tipo()
                self.state = 133
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LilaParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(LilaParser.CondicionContext,0)


        def swhile(self):
            return self.getTypedRuleContext(LilaParser.SwhileContext,0)


        def display(self):
            return self.getTypedRuleContext(LilaParser.DisplayContext,0)


        def getinput(self):
            return self.getTypedRuleContext(LilaParser.GetinputContext,0)


        def invocacion(self):
            return self.getTypedRuleContext(LilaParser.InvocacionContext,0)


        def sreturn(self):
            return self.getTypedRuleContext(LilaParser.SreturnContext,0)


        def especiales(self):
            return self.getTypedRuleContext(LilaParser.EspecialesContext,0)


        def getRuleIndex(self):
            return LilaParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = LilaParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_estatuto)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.swhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.display()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.getinput()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.invocacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.sreturn()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.especiales()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LilaParser.IF, 0)

        def expresion(self):
            return self.getTypedRuleContext(LilaParser.ExpresionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(LilaParser.BloqueContext,i)


        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(LilaParser.ELSE, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = LilaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LilaParser.IF)
            self.state = 152
            self.expresion()
            gen.checkExpresion()
            self.state = 154
            self.bloque()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.ELSE:
                self.state = 155
                self.match(LilaParser.ELSE)
                gen.conditionElse()
                self.state = 157
                self.bloque()


            self.state = 160
            self.match(LilaParser.SEMICOLON)
            gen.conditionEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURLY(self):
            return self.getToken(LilaParser.OPEN_CURLY, 0)

        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.EstatutoContext)
            else:
                return self.getTypedRuleContext(LilaParser.EstatutoContext,i)


        def CLOSE_CURLY(self):
            return self.getToken(LilaParser.CLOSE_CURLY, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = LilaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LilaParser.OPEN_CURLY)
            self.state = 164
            self.estatuto()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0):
                self.state = 165
                self.estatuto()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(LilaParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(LilaParser.DISPLAY, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpresionContext,i)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def getRuleIndex(self):
            return LilaParser.RULE_display

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplay" ):
                listener.enterDisplay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplay" ):
                listener.exitDisplay(self)




    def display(self):

        localctx = LilaParser.DisplayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_display)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LilaParser.DISPLAY)
            self.state = 174
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 175
            self.expresion()
            gen.display()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 177
                self.match(LilaParser.COMMA)
                self.state = 178
                self.expresion()
                gen.display()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 187
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._EQUAL = None # Token

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def EQUAL(self):
            return self.getToken(LilaParser.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def expresion(self):
            return self.getTypedRuleContext(LilaParser.ExpresionContext,0)


        def arr(self):
            return self.getTypedRuleContext(LilaParser.ArrContext,0)


        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OPEN_BRACKET)
            else:
                return self.getToken(LilaParser.OPEN_BRACKET, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpContext,i)


        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CLOSE_BRACKET)
            else:
                return self.getToken(LilaParser.CLOSE_BRACKET, i)

        def getRuleIndex(self):
            return LilaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = LilaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            localctx._ID = self.match(LilaParser.ID)
            gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 191
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 192
                self.exp()
                self.state = 193
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            localctx._EQUAL = self.match(LilaParser.EQUAL)
            gen.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 202
                self.expresion()
                gen.assign()
                pass

            elif la_ == 2:
                self.state = 205
                self.arr()
                pass


            self.state = 208
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SreturnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LilaParser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LilaParser.ExpresionContext,0)


        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_sreturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSreturn" ):
                listener.enterSreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSreturn" ):
                listener.exitSreturn(self)




    def sreturn(self):

        localctx = LilaParser.SreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sreturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(LilaParser.RETURN)
            self.state = 211
            self.expresion()
            Semantic.checkReturn(gen.top_variables())
            gen.func_return()
            self.state = 214
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(LilaParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OPEN_BRACKET)
            else:
                return self.getToken(LilaParser.OPEN_BRACKET, i)

        def arr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ArrContext)
            else:
                return self.getTypedRuleContext(LilaParser.ArrContext,i)


        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CLOSE_BRACKET)
            else:
                return self.getToken(LilaParser.CLOSE_BRACKET, i)

        def getRuleIndex(self):
            return LilaParser.RULE_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr" ):
                listener.enterArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr" ):
                listener.exitArr(self)




    def arr(self):

        localctx = LilaParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.var_cte()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 217
                    self.match(LilaParser.COMMA)
                    self.state = 218
                    self.var_cte()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [LilaParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 225
                self.arr()
                self.state = 226
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 227
                    self.match(LilaParser.COMMA)
                    self.state = 228
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 229
                    self.arr()
                    self.state = 230
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ComparacionContext)
            else:
                return self.getTypedRuleContext(LilaParser.ComparacionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.AND)
            else:
                return self.getToken(LilaParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OR)
            else:
                return self.getToken(LilaParser.OR, i)

        def getRuleIndex(self):
            return LilaParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = LilaParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.comparacion()
            gen.exitExpresion()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.AND or _la==LilaParser.OR:
                self.state = 245
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.AND]:
                    self.state = 241
                    self.match(LilaParser.AND)
                    gen.addOperator('AND')
                    pass
                elif token in [LilaParser.OR]:
                    self.state = 243
                    self.match(LilaParser.OR)
                    gen.addOperator('OR')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 247
                self.comparacion()
                gen.exitExpresion()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpContext,i)


        def GREATER_THAN(self):
            return self.getToken(LilaParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(LilaParser.LESS_THAN, 0)

        def NOTEQUAL(self):
            return self.getToken(LilaParser.NOTEQUAL, 0)

        def EQUALITY(self):
            return self.getToken(LilaParser.EQUALITY, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(LilaParser.GREATER_THAN_EQUAL, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(LilaParser.LESS_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)




    def comparacion(self):

        localctx = LilaParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparacion)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.exp()
                self.state = 268
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.GREATER_THAN]:
                    self.state = 256
                    self.match(LilaParser.GREATER_THAN)
                    gen.addOperator('>')
                    pass
                elif token in [LilaParser.LESS_THAN]:
                    self.state = 258
                    self.match(LilaParser.LESS_THAN)
                    gen.addOperator('<')
                    pass
                elif token in [LilaParser.NOTEQUAL]:
                    self.state = 260
                    self.match(LilaParser.NOTEQUAL)
                    gen.addOperator('!=')
                    pass
                elif token in [LilaParser.EQUALITY]:
                    self.state = 262
                    self.match(LilaParser.EQUALITY)
                    gen.addOperator('==')
                    pass
                elif token in [LilaParser.GREATER_THAN_EQUAL]:
                    self.state = 264
                    self.match(LilaParser.GREATER_THAN_EQUAL)
                    gen.addOperator('>=')
                    pass
                elif token in [LilaParser.LESS_THAN_EQUAL]:
                    self.state = 266
                    self.match(LilaParser.LESS_THAN_EQUAL)
                    gen.addOperator('<=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 270
                self.exp()
                gen.exitComparacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.TerminoContext)
            else:
                return self.getTypedRuleContext(LilaParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.PLUS)
            else:
                return self.getToken(LilaParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.MINUS)
            else:
                return self.getToken(LilaParser.MINUS, i)

        def getRuleIndex(self):
            return LilaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = LilaParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.termino()
            gen.exitExp()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                self.state = 282
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.PLUS]:
                    self.state = 278
                    self.match(LilaParser.PLUS)
                    gen.addOperator('+')
                    pass
                elif token in [LilaParser.MINUS]:
                    self.state = 280
                    self.match(LilaParser.MINUS)
                    gen.addOperator('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 284
                self.termino()
                gen.exitExp()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.FactorContext)
            else:
                return self.getTypedRuleContext(LilaParser.FactorContext,i)


        def MULTIPLICATION(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.MULTIPLICATION)
            else:
                return self.getToken(LilaParser.MULTIPLICATION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.DIVISION)
            else:
                return self.getToken(LilaParser.DIVISION, i)

        def getRuleIndex(self):
            return LilaParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = LilaParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.factor()
            gen.exitTermino()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.MULTIPLICATION or _la==LilaParser.DIVISION:
                self.state = 298
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.MULTIPLICATION]:
                    self.state = 294
                    self.match(LilaParser.MULTIPLICATION)
                    gen.addOperator('*')
                    pass
                elif token in [LilaParser.DIVISION]:
                    self.state = 296
                    self.match(LilaParser.DIVISION)
                    gen.addOperator('/')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 300
                self.factor()
                gen.exitTermino()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LilaParser.ExpresionContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def var_cte(self):
            return self.getTypedRuleContext(LilaParser.Var_cteContext,0)


        def PLUS(self):
            return self.getToken(LilaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LilaParser.MINUS, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = LilaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.OPEN_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.addOperator('(')
                self.state = 310
                self.expresion()
                self.state = 311
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                pass
            elif token in [LilaParser.PLUS, LilaParser.MINUS, LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                    self.state = 314
                    _la = self._input.LA(1)
                    if not(_la==LilaParser.PLUS or _la==LilaParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 317
                self.var_cte()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._CTE_INT = None # Token
            self._CTE_F = None # Token
            self._CTE_STRING = None # Token
            self._CTE_BOOL = None # Token

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpresionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OPEN_BRACKET)
            else:
                return self.getToken(LilaParser.OPEN_BRACKET, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpContext,i)


        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CLOSE_BRACKET)
            else:
                return self.getToken(LilaParser.CLOSE_BRACKET, i)

        def CTE_INT(self):
            return self.getToken(LilaParser.CTE_INT, 0)

        def CTE_F(self):
            return self.getToken(LilaParser.CTE_F, 0)

        def CTE_STRING(self):
            return self.getToken(LilaParser.CTE_STRING, 0)

        def CTE_BOOL(self):
            return self.getToken(LilaParser.CTE_BOOL, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_var_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_cte" ):
                listener.enterVar_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_cte" ):
                listener.exitVar_cte(self)




    def var_cte(self):

        localctx = LilaParser.Var_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_cte)
        self._la = 0 # Token type
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                localctx._ID = self.match(LilaParser.ID)
                self.state = 321
                self.match(LilaParser.OPEN_PARENTHESIS)
                Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
                Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), False)
                gen.era((None if localctx._ID is None else localctx._ID.text))
                gen.addOperator('(')
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                    self.state = 326
                    self.expresion()
                    gen.params()
                    self.state = 334
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LilaParser.COMMA:
                        self.state = 328
                        self.match(LilaParser.COMMA)
                        self.state = 329
                        self.expresion()
                        gen.params()
                        self.state = 336
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                gen.goSub((None if localctx._ID is None else localctx._ID.text))
                self.state = 340
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                gen.addFunct(Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                localctx._ID = self.match(LilaParser.ID)
                gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.OPEN_BRACKET:
                    self.state = 345
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 346
                    self.exp()
                    self.state = 347
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 353
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                localctx._CTE_INT = self.match(LilaParser.CTE_INT)
                gen.addConst(Operand(None,'int',(None if localctx._CTE_INT is None else localctx._CTE_INT.text)))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                localctx._CTE_F = self.match(LilaParser.CTE_F)
                gen.addConst(Operand(None,'num',(None if localctx._CTE_F is None else localctx._CTE_F.text)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                localctx._CTE_STRING = self.match(LilaParser.CTE_STRING)
                gen.addConst(Operand(None,'text',(None if localctx._CTE_STRING is None else localctx._CTE_STRING.text)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 360
                localctx._CTE_BOOL = self.match(LilaParser.CTE_BOOL)
                gen.addConst(Operand(None,'bool',(None if localctx._CTE_BOOL is None else localctx._CTE_BOOL.text)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwhileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LilaParser.WHILE, 0)

        def expresion(self):
            return self.getTypedRuleContext(LilaParser.ExpresionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(LilaParser.BloqueContext,0)


        def getRuleIndex(self):
            return LilaParser.RULE_swhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwhile" ):
                listener.enterSwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwhile" ):
                listener.exitSwhile(self)




    def swhile(self):

        localctx = LilaParser.SwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_swhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(LilaParser.WHILE)
            gen.swhile()
            self.state = 366
            self.expresion()
            gen.checkExpresion()
            self.state = 368
            self.bloque()
            gen.whileEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpresionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def getRuleIndex(self):
            return LilaParser.RULE_invocacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvocacion" ):
                listener.enterInvocacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvocacion" ):
                listener.exitInvocacion(self)




    def invocacion(self):

        localctx = LilaParser.InvocacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_invocacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            localctx._ID = self.match(LilaParser.ID)
            self.state = 372
            self.match(LilaParser.OPEN_PARENTHESIS)
            Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
            Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), True)
            gen.era((None if localctx._ID is None else localctx._ID.text))
            gen.addOperator('(')
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                self.state = 377
                self.expresion()
                gen.params()
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 379
                    self.match(LilaParser.COMMA)
                    self.state = 380
                    self.expresion()
                    gen.params()
                    self.state = 387
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            gen.goSub((None if localctx._ID is None else localctx._ID.text))
            self.state = 391
            self.match(LilaParser.CLOSE_PARENTHESIS)
            gen.finParentesis()
            self.state = 393
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetinputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def GETINPUT(self):
            return self.getToken(LilaParser.GETINPUT, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def ID(self):
            return self.getToken(LilaParser.ID, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def COMMA(self):
            return self.getToken(LilaParser.COMMA, 0)

        def CTE_STRING(self):
            return self.getToken(LilaParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_getinput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetinput" ):
                listener.enterGetinput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetinput" ):
                listener.exitGetinput(self)




    def getinput(self):

        localctx = LilaParser.GetinputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_getinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(LilaParser.GETINPUT)
            self.state = 396
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 397
            localctx._ID = self.match(LilaParser.ID)
            gen.getinput(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.COMMA:
                self.state = 399
                self.match(LilaParser.COMMA)
                self.state = 400
                self.match(LilaParser.CTE_STRING)


            self.state = 403
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 404
            self.match(LilaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EspecialesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(LilaParser.OPEN_PARENTHESIS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.ID)
            else:
                return self.getToken(LilaParser.ID, i)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(LilaParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def GETOUTLIERS(self):
            return self.getToken(LilaParser.GETOUTLIERS, 0)

        def REMOVEOUTLIERS(self):
            return self.getToken(LilaParser.REMOVEOUTLIERS, 0)

        def TELLMEWHATTOUSE(self):
            return self.getToken(LilaParser.TELLMEWHATTOUSE, 0)

        def PRINTMEASURES(self):
            return self.getToken(LilaParser.PRINTMEASURES, 0)

        def MEAN(self):
            return self.getToken(LilaParser.MEAN, 0)

        def MEDIAN(self):
            return self.getToken(LilaParser.MEDIAN, 0)

        def MODE(self):
            return self.getToken(LilaParser.MODE, 0)

        def RANGE(self):
            return self.getToken(LilaParser.RANGE, 0)

        def MIN(self):
            return self.getToken(LilaParser.MIN, 0)

        def MAX(self):
            return self.getToken(LilaParser.MAX, 0)

        def DESESTANDAR(self):
            return self.getToken(LilaParser.DESESTANDAR, 0)

        def QUICKSHOW(self):
            return self.getToken(LilaParser.QUICKSHOW, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

        def PEARSONCORRELATION(self):
            return self.getToken(LilaParser.PEARSONCORRELATION, 0)

        def NORMALDISTRIBUTION(self):
            return self.getToken(LilaParser.NORMALDISTRIBUTION, 0)

        def CTE_F(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CTE_F)
            else:
                return self.getToken(LilaParser.CTE_F, i)

        def CTE_INT(self):
            return self.getToken(LilaParser.CTE_INT, 0)

        def FILLVALUE(self):
            return self.getToken(LilaParser.FILLVALUE, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(LilaParser.Var_cteContext,i)


        def REMOVEVALUE(self):
            return self.getToken(LilaParser.REMOVEVALUE, 0)

        def getRuleIndex(self):
            return LilaParser.RULE_especiales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEspeciales" ):
                listener.enterEspeciales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEspeciales" ):
                listener.exitEspeciales(self)




    def especiales(self):

        localctx = LilaParser.EspecialesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_especiales)
        self._la = 0 # Token type
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.GETOUTLIERS, LilaParser.REMOVEOUTLIERS, LilaParser.TELLMEWHATTOUSE, LilaParser.PRINTMEASURES, LilaParser.MEAN, LilaParser.MEDIAN, LilaParser.MODE, LilaParser.RANGE, LilaParser.MIN, LilaParser.MAX, LilaParser.DESESTANDAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 407
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 408
                self.match(LilaParser.ID)
                self.state = 409
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 410
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.QUICKSHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(LilaParser.QUICKSHOW)
                self.state = 412
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 413
                self.match(LilaParser.ID)
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.COMMA:
                    self.state = 414
                    self.match(LilaParser.COMMA)
                    self.state = 415
                    self.match(LilaParser.ID)


                self.state = 418
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 419
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.PEARSONCORRELATION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.match(LilaParser.PEARSONCORRELATION)
                self.state = 421
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 422
                self.match(LilaParser.ID)
                self.state = 423
                self.match(LilaParser.COMMA)
                self.state = 424
                self.match(LilaParser.ID)
                self.state = 425
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 426
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.NORMALDISTRIBUTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(LilaParser.NORMALDISTRIBUTION)
                self.state = 428
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 429
                self.match(LilaParser.CTE_F)
                self.state = 430
                self.match(LilaParser.COMMA)
                self.state = 431
                self.match(LilaParser.CTE_F)
                self.state = 432
                self.match(LilaParser.COMMA)
                self.state = 433
                self.match(LilaParser.CTE_INT)
                self.state = 434
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 435
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.FILLVALUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 436
                self.match(LilaParser.FILLVALUE)
                self.state = 437
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 438
                self.match(LilaParser.ID)
                self.state = 439
                self.match(LilaParser.COMMA)
                self.state = 440
                self.var_cte()
                self.state = 441
                self.match(LilaParser.COMMA)
                self.state = 442
                self.var_cte()
                self.state = 443
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 444
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.REMOVEVALUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 446
                self.match(LilaParser.REMOVEVALUE)
                self.state = 447
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 448
                self.match(LilaParser.ID)
                self.state = 449
                self.match(LilaParser.COMMA)
                self.state = 450
                self.var_cte()
                self.state = 451
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 452
                self.match(LilaParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





