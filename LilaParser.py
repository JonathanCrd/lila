# Generated from Lila.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Var
gen = IntermediateGenerator()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\5\2\67\n\2\3\2\7\2:\n\2\f\2\16\2")
        buf.write("=\13\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3E\n\3\r\3\16\3F\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4Q\n\4\f\4\16\4T\13\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6_\n\6\f\6\16\6b")
        buf.write("\13\6\3\7\3\7\3\7\5\7g\n\7\3\7\3\7\3\7\3\7\3\7\5\7n\n")
        buf.write("\7\3\7\3\7\3\7\5\7s\n\7\3\7\6\7v\n\7\r\7\16\7w\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0086\n\b")
        buf.write("\f\b\16\b\u0089\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u0093\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009c\n\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00a4\n\13\f\13\16\13")
        buf.write("\u00a7\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\7\f\u00b3\n\f\f\f\16\f\u00b6\13\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u00c1\n\r\f\r\16\r\u00c4\13\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\r\u00cc\n\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00d9\n\17\f\17")
        buf.write("\16\17\u00dc\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00e6\n\17\f\17\16\17\u00e9\13\17\5\17\u00eb")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f3\n\20\3")
        buf.write("\20\3\20\3\20\7\20\u00f8\n\20\f\20\16\20\u00fb\13\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u010a\n\21\3\21\3\21\3\21\3\21\5\21\u0110")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0118\n\22\3")
        buf.write("\22\3\22\3\22\7\22\u011d\n\22\f\22\16\22\u0120\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u0128\n\23\3\23\3\23")
        buf.write("\3\23\7\23\u012d\n\23\f\23\16\23\u0130\13\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u0139\n\24\3\24\5\24\u013c")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0143\n\25\3\25\3")
        buf.write("\25\7\25\u0147\n\25\f\25\16\25\u014a\13\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\7\25\u0153\n\25\f\25\16\25\u0156")
        buf.write("\13\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0160")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u016f\n\27\f\27\16\27\u0172\13\27")
        buf.write("\5\27\u0174\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u017f\n\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u018e\n\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u01b4\n\31\3\31\2\2\32\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\5\3\2\f\17")
        buf.write("\3\2\32\33\3\2+\65\2\u01d5\2\62\3\2\2\2\4B\3\2\2\2\6J")
        buf.write("\3\2\2\2\bW\3\2\2\2\nZ\3\2\2\2\fc\3\2\2\2\16}\3\2\2\2")
        buf.write("\20\u0092\3\2\2\2\22\u0094\3\2\2\2\24\u00a0\3\2\2\2\26")
        buf.write("\u00aa\3\2\2\2\30\u00ba\3\2\2\2\32\u00cf\3\2\2\2\34\u00ea")
        buf.write("\3\2\2\2\36\u00ec\3\2\2\2 \u010f\3\2\2\2\"\u0111\3\2\2")
        buf.write("\2$\u0121\3\2\2\2&\u013b\3\2\2\2(\u015f\3\2\2\2*\u0161")
        buf.write("\3\2\2\2,\u0168\3\2\2\2.\u0178\3\2\2\2\60\u01b3\3\2\2")
        buf.write("\2\62\63\7\4\2\2\63\64\7;\2\2\64\66\b\2\1\2\65\67\5\4")
        buf.write("\3\2\66\65\3\2\2\2\66\67\3\2\2\2\67;\3\2\2\28:\5\f\7\2")
        buf.write("98\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3")
        buf.write("\2\2\2>?\b\2\1\2?@\5\b\5\2@A\b\2\1\2A\3\3\2\2\2BD\7\t")
        buf.write("\2\2CE\5\6\4\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("GH\3\2\2\2HI\b\3\1\2I\5\3\2\2\2JK\5\n\6\2KL\7;\2\2LR\b")
        buf.write("\4\1\2MN\7\30\2\2NO\7;\2\2OQ\b\4\1\2PM\3\2\2\2QT\3\2\2")
        buf.write("\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7\31\2\2")
        buf.write("V\7\3\2\2\2WX\7\3\2\2XY\5\24\13\2Y\t\3\2\2\2Z`\t\2\2\2")
        buf.write("[\\\7\22\2\2\\]\7\'\2\2]_\7\23\2\2^[\3\2\2\2_b\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2a\13\3\2\2\2b`\3\2\2\2cf\7\b\2\2d")
        buf.write("g\5\n\6\2eg\7\5\2\2fd\3\2\2\2fe\3\2\2\2gh\3\2\2\2hi\7")
        buf.write(";\2\2ij\b\7\1\2jk\b\7\1\2km\7\24\2\2ln\5\16\b\2ml\3\2")
        buf.write("\2\2mn\3\2\2\2no\3\2\2\2op\7\25\2\2pr\7\26\2\2qs\5\4\3")
        buf.write("\2rq\3\2\2\2rs\3\2\2\2su\3\2\2\2tv\5\20\t\2ut\3\2\2\2")
        buf.write("vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\27\2\2z{")
        buf.write("\b\7\1\2{|\b\7\1\2|\r\3\2\2\2}~\5\n\6\2~\177\7;\2\2\177")
        buf.write("\u0087\b\b\1\2\u0080\u0081\7\30\2\2\u0081\u0082\5\n\6")
        buf.write("\2\u0082\u0083\7;\2\2\u0083\u0084\b\b\1\2\u0084\u0086")
        buf.write("\3\2\2\2\u0085\u0080\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\17\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u0093\5\30\r\2\u008b\u0093\5\22\n")
        buf.write("\2\u008c\u0093\5*\26\2\u008d\u0093\5\26\f\2\u008e\u0093")
        buf.write("\5.\30\2\u008f\u0093\5,\27\2\u0090\u0093\5\32\16\2\u0091")
        buf.write("\u0093\5\60\31\2\u0092\u008a\3\2\2\2\u0092\u008b\3\2\2")
        buf.write("\2\u0092\u008c\3\2\2\2\u0092\u008d\3\2\2\2\u0092\u008e")
        buf.write("\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\21\3\2\2\2\u0094\u0095\7\13\2\2\u0095")
        buf.write("\u0096\5\36\20\2\u0096\u0097\b\n\1\2\u0097\u009b\5\24")
        buf.write("\13\2\u0098\u0099\7\n\2\2\u0099\u009a\b\n\1\2\u009a\u009c")
        buf.write("\5\24\13\2\u009b\u0098\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009e\7\31\2\2\u009e\u009f\b\n\1")
        buf.write("\2\u009f\23\3\2\2\2\u00a0\u00a1\7\26\2\2\u00a1\u00a5\5")
        buf.write("\20\t\2\u00a2\u00a4\5\20\t\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7")
        buf.write("\27\2\2\u00a9\25\3\2\2\2\u00aa\u00ab\7\6\2\2\u00ab\u00ac")
        buf.write("\7\24\2\2\u00ac\u00ad\5\36\20\2\u00ad\u00b4\b\f\1\2\u00ae")
        buf.write("\u00af\7\30\2\2\u00af\u00b0\5\36\20\2\u00b0\u00b1\b\f")
        buf.write("\1\2\u00b1\u00b3\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b3\u00b6")
        buf.write("\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\7\25\2")
        buf.write("\2\u00b8\u00b9\7\31\2\2\u00b9\27\3\2\2\2\u00ba\u00bb\7")
        buf.write(";\2\2\u00bb\u00c2\b\r\1\2\u00bc\u00bd\7\22\2\2\u00bd\u00be")
        buf.write("\5\"\22\2\u00be\u00bf\7\23\2\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00bc\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c6\7\"\2\2\u00c6\u00cb\b\r\1\2\u00c7\u00c8")
        buf.write("\5\36\20\2\u00c8\u00c9\b\r\1\2\u00c9\u00cc\3\2\2\2\u00ca")
        buf.write("\u00cc\5\34\17\2\u00cb\u00c7\3\2\2\2\u00cb\u00ca\3\2\2")
        buf.write("\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7\31\2\2\u00ce\31\3")
        buf.write("\2\2\2\u00cf\u00d0\7\20\2\2\u00d0\u00d1\5\36\20\2\u00d1")
        buf.write("\u00d2\b\16\1\2\u00d2\u00d3\b\16\1\2\u00d3\u00d4\7\31")
        buf.write("\2\2\u00d4\33\3\2\2\2\u00d5\u00da\5(\25\2\u00d6\u00d7")
        buf.write("\7\30\2\2\u00d7\u00d9\5(\25\2\u00d8\u00d6\3\2\2\2\u00d9")
        buf.write("\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00eb\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\7")
        buf.write("\22\2\2\u00de\u00df\5\34\17\2\u00df\u00e7\7\23\2\2\u00e0")
        buf.write("\u00e1\7\30\2\2\u00e1\u00e2\7\22\2\2\u00e2\u00e3\5\34")
        buf.write("\17\2\u00e3\u00e4\7\23\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e0")
        buf.write("\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00ea\u00d5\3\2\2\2\u00ea\u00dd\3\2\2\2\u00eb\35\3\2")
        buf.write("\2\2\u00ec\u00ed\5 \21\2\u00ed\u00f9\b\20\1\2\u00ee\u00ef")
        buf.write("\7%\2\2\u00ef\u00f3\b\20\1\2\u00f0\u00f1\7&\2\2\u00f1")
        buf.write("\u00f3\b\20\1\2\u00f2\u00ee\3\2\2\2\u00f2\u00f0\3\2\2")
        buf.write("\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\5 \21\2\u00f5\u00f6")
        buf.write("\b\20\1\2\u00f6\u00f8\3\2\2\2\u00f7\u00f2\3\2\2\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00fa\37\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u0109\5\"")
        buf.write("\22\2\u00fd\u00fe\7\37\2\2\u00fe\u010a\b\21\1\2\u00ff")
        buf.write("\u0100\7\36\2\2\u0100\u010a\b\21\1\2\u0101\u0102\7 \2")
        buf.write("\2\u0102\u010a\b\21\1\2\u0103\u0104\7!\2\2\u0104\u010a")
        buf.write("\b\21\1\2\u0105\u0106\7$\2\2\u0106\u010a\b\21\1\2\u0107")
        buf.write("\u0108\7#\2\2\u0108\u010a\b\21\1\2\u0109\u00fd\3\2\2\2")
        buf.write("\u0109\u00ff\3\2\2\2\u0109\u0101\3\2\2\2\u0109\u0103\3")
        buf.write("\2\2\2\u0109\u0105\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u010c\5\"\22\2\u010c\u010d\b\21\1\2\u010d")
        buf.write("\u0110\3\2\2\2\u010e\u0110\5\"\22\2\u010f\u00fc\3\2\2")
        buf.write("\2\u010f\u010e\3\2\2\2\u0110!\3\2\2\2\u0111\u0112\5$\23")
        buf.write("\2\u0112\u011e\b\22\1\2\u0113\u0114\7\32\2\2\u0114\u0118")
        buf.write("\b\22\1\2\u0115\u0116\7\33\2\2\u0116\u0118\b\22\1\2\u0117")
        buf.write("\u0113\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011a\5$\23\2\u011a\u011b\b\22\1\2\u011b\u011d")
        buf.write("\3\2\2\2\u011c\u0117\3\2\2\2\u011d\u0120\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f#\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0121\u0122\5&\24\2\u0122\u012e\b\23\1")
        buf.write("\2\u0123\u0124\7\34\2\2\u0124\u0128\b\23\1\2\u0125\u0126")
        buf.write("\7\35\2\2\u0126\u0128\b\23\1\2\u0127\u0123\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\5&\24\2")
        buf.write("\u012a\u012b\b\23\1\2\u012b\u012d\3\2\2\2\u012c\u0127")
        buf.write("\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f%\3\2\2\2\u0130\u012e\3\2\2\2\u0131")
        buf.write("\u0132\7\24\2\2\u0132\u0133\b\24\1\2\u0133\u0134\5\36")
        buf.write("\20\2\u0134\u0135\7\25\2\2\u0135\u0136\b\24\1\2\u0136")
        buf.write("\u013c\3\2\2\2\u0137\u0139\t\3\2\2\u0138\u0137\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\5")
        buf.write("(\25\2\u013b\u0131\3\2\2\2\u013b\u0138\3\2\2\2\u013c\'")
        buf.write("\3\2\2\2\u013d\u013e\7;\2\2\u013e\u013f\7\24\2\2\u013f")
        buf.write("\u0140\b\25\1\2\u0140\u0142\b\25\1\2\u0141\u0143\5\"\22")
        buf.write("\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0148")
        buf.write("\3\2\2\2\u0144\u0145\7\30\2\2\u0145\u0147\5\"\22\2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\u0160\7\25\2\2\u014c\u014d\7;\2\2\u014d\u0154")
        buf.write("\b\25\1\2\u014e\u014f\7\22\2\2\u014f\u0150\5\"\22\2\u0150")
        buf.write("\u0151\7\23\2\2\u0151\u0153\3\2\2\2\u0152\u014e\3\2\2")
        buf.write("\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0160\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u0158\7\'\2\2\u0158\u0160\b\25\1\2\u0159\u015a\7)\2\2")
        buf.write("\u015a\u0160\b\25\1\2\u015b\u015c\7(\2\2\u015c\u0160\b")
        buf.write("\25\1\2\u015d\u015e\7*\2\2\u015e\u0160\b\25\1\2\u015f")
        buf.write("\u013d\3\2\2\2\u015f\u014c\3\2\2\2\u015f\u0157\3\2\2\2")
        buf.write("\u015f\u0159\3\2\2\2\u015f\u015b\3\2\2\2\u015f\u015d\3")
        buf.write("\2\2\2\u0160)\3\2\2\2\u0161\u0162\7\7\2\2\u0162\u0163")
        buf.write("\b\26\1\2\u0163\u0164\5\36\20\2\u0164\u0165\b\26\1\2\u0165")
        buf.write("\u0166\5\24\13\2\u0166\u0167\b\26\1\2\u0167+\3\2\2\2\u0168")
        buf.write("\u0169\7;\2\2\u0169\u016a\b\27\1\2\u016a\u0173\7\24\2")
        buf.write("\2\u016b\u0170\5\36\20\2\u016c\u016d\7\30\2\2\u016d\u016f")
        buf.write("\5\36\20\2\u016e\u016c\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0174\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0173\u016b\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\7\25\2\2\u0176")
        buf.write("\u0177\7\31\2\2\u0177-\3\2\2\2\u0178\u0179\7\21\2\2\u0179")
        buf.write("\u017a\7\24\2\2\u017a\u017b\7;\2\2\u017b\u017e\b\30\1")
        buf.write("\2\u017c\u017d\7\30\2\2\u017d\u017f\7(\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\7\25\2\2\u0181\u0182\7\31\2\2\u0182/\3\2\2\2\u0183")
        buf.write("\u0184\t\4\2\2\u0184\u0185\7\24\2\2\u0185\u0186\7;\2\2")
        buf.write("\u0186\u0187\7\25\2\2\u0187\u01b4\7\31\2\2\u0188\u0189")
        buf.write("\7\66\2\2\u0189\u018a\7\24\2\2\u018a\u018d\7;\2\2\u018b")
        buf.write("\u018c\7\30\2\2\u018c\u018e\7;\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7")
        buf.write("\25\2\2\u0190\u01b4\7\31\2\2\u0191\u0192\7\67\2\2\u0192")
        buf.write("\u0193\7\24\2\2\u0193\u0194\7;\2\2\u0194\u0195\7\30\2")
        buf.write("\2\u0195\u0196\7;\2\2\u0196\u0197\7\25\2\2\u0197\u01b4")
        buf.write("\7\31\2\2\u0198\u0199\78\2\2\u0199\u019a\7\24\2\2\u019a")
        buf.write("\u019b\7)\2\2\u019b\u019c\7\30\2\2\u019c\u019d\7)\2\2")
        buf.write("\u019d\u019e\7\30\2\2\u019e\u019f\7\'\2\2\u019f\u01a0")
        buf.write("\7\25\2\2\u01a0\u01b4\7\31\2\2\u01a1\u01a2\79\2\2\u01a2")
        buf.write("\u01a3\7\24\2\2\u01a3\u01a4\7;\2\2\u01a4\u01a5\7\30\2")
        buf.write("\2\u01a5\u01a6\5(\25\2\u01a6\u01a7\7\30\2\2\u01a7\u01a8")
        buf.write("\5(\25\2\u01a8\u01a9\7\25\2\2\u01a9\u01aa\7\31\2\2\u01aa")
        buf.write("\u01b4\3\2\2\2\u01ab\u01ac\7:\2\2\u01ac\u01ad\7\24\2\2")
        buf.write("\u01ad\u01ae\7;\2\2\u01ae\u01af\7\30\2\2\u01af\u01b0\5")
        buf.write("(\25\2\u01b0\u01b1\7\25\2\2\u01b1\u01b2\7\31\2\2\u01b2")
        buf.write("\u01b4\3\2\2\2\u01b3\u0183\3\2\2\2\u01b3\u0188\3\2\2\2")
        buf.write("\u01b3\u0191\3\2\2\2\u01b3\u0198\3\2\2\2\u01b3\u01a1\3")
        buf.write("\2\2\2\u01b3\u01ab\3\2\2\2\u01b4\61\3\2\2\2(\66;FR`fm")
        buf.write("rw\u0087\u0092\u009b\u00a5\u00b4\u00c2\u00cb\u00da\u00e7")
        buf.write("\u00ea\u00f2\u00f9\u0109\u010f\u0117\u011e\u0127\u012e")
        buf.write("\u0138\u013b\u0142\u0148\u0154\u015f\u0170\u0173\u017e")
        buf.write("\u018d\u01b3")
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
            self.state = 64
            self.match(LilaParser.VAR)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.data2()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                    break

            Semantic.isGlobal = False
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
            self.state = 72
            localctx._tipo = self.tipo()
            self.state = 73
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_var(Var((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 75
                self.match(LilaParser.COMMA)
                self.state = 76
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_var(Var((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
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
            self.state = 85
            self.match(LilaParser.MAIN)
            self.state = 86
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
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 89
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 90
                self.match(LilaParser.CTE_INT)
                self.state = 91
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 96
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
            self.state = 97
            self.match(LilaParser.FUNC)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.INT, LilaParser.NUM, LilaParser.TEXT, LilaParser.BOOL]:
                self.state = 98
                localctx._tipo = self.tipo()
                pass
            elif token in [LilaParser.VOID]:
                self.state = 99
                localctx._VOID = self.match(LilaParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 102
            localctx._ID = self.match(LilaParser.ID)
            index = len(gen.Quadruples)
            Semantic.enterFunciones((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),(None if localctx._VOID is None else localctx._VOID.text),index)
            self.state = 105
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0):
                self.state = 106
                self.params()


            self.state = 109
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 110
            self.match(LilaParser.OPEN_CURLY)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 111
                self.data()


            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.estatuto()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0)):
                    break

            self.state = 119
            self.match(LilaParser.CLOSE_CURLY)
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
            self.state = 123
            localctx._tipo = self.tipo()
            self.state = 124
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_param(Var((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),''))
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 126
                self.match(LilaParser.COMMA)
                self.state = 127
                localctx._tipo = self.tipo()
                self.state = 128
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_param(Var((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),''))
                self.state = 135
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.swhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.display()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.getinput()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.invocacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.sreturn()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 143
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
            self.state = 146
            self.match(LilaParser.IF)
            self.state = 147
            self.expresion()
            gen.checkExpresion()
            self.state = 149
            self.bloque()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.ELSE:
                self.state = 150
                self.match(LilaParser.ELSE)
                gen.conditionElse()
                self.state = 152
                self.bloque()


            self.state = 155
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
            self.state = 158
            self.match(LilaParser.OPEN_CURLY)
            self.state = 159
            self.estatuto()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0):
                self.state = 160
                self.estatuto()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
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
            self.state = 168
            self.match(LilaParser.DISPLAY)
            self.state = 169
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 170
            self.expresion()
            gen.display()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 172
                self.match(LilaParser.COMMA)
                self.state = 173
                self.expresion()
                gen.display()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 182
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
            self.state = 184
            localctx._ID = self.match(LilaParser.ID)
            gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 186
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 187
                self.exp()
                self.state = 188
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            localctx._EQUAL = self.match(LilaParser.EQUAL)
            gen.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 197
                self.expresion()
                gen.assign()
                pass

            elif la_ == 2:
                self.state = 200
                self.arr()
                pass


            self.state = 203
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
            self.state = 205
            self.match(LilaParser.RETURN)
            self.state = 206
            self.expresion()
            Semantic.checkReturn(gen.top_variables())
            gen.func_return()
            self.state = 209
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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.var_cte()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 212
                    self.match(LilaParser.COMMA)
                    self.state = 213
                    self.var_cte()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [LilaParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 220
                self.arr()
                self.state = 221
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 222
                    self.match(LilaParser.COMMA)
                    self.state = 223
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 224
                    self.arr()
                    self.state = 225
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 231
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
            self.state = 234
            self.comparacion()
            gen.exitExpresion()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.AND or _la==LilaParser.OR:
                self.state = 240
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.AND]:
                    self.state = 236
                    self.match(LilaParser.AND)
                    gen.addOperator('AND')
                    pass
                elif token in [LilaParser.OR]:
                    self.state = 238
                    self.match(LilaParser.OR)
                    gen.addOperator('OR')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 242
                self.comparacion()
                gen.exitExpresion()
                self.state = 249
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
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.exp()
                self.state = 263
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.GREATER_THAN]:
                    self.state = 251
                    self.match(LilaParser.GREATER_THAN)
                    gen.addOperator('>')
                    pass
                elif token in [LilaParser.LESS_THAN]:
                    self.state = 253
                    self.match(LilaParser.LESS_THAN)
                    gen.addOperator('<')
                    pass
                elif token in [LilaParser.NOTEQUAL]:
                    self.state = 255
                    self.match(LilaParser.NOTEQUAL)
                    gen.addOperator('!=')
                    pass
                elif token in [LilaParser.EQUALITY]:
                    self.state = 257
                    self.match(LilaParser.EQUALITY)
                    gen.addOperator('==')
                    pass
                elif token in [LilaParser.GREATER_THAN_EQUAL]:
                    self.state = 259
                    self.match(LilaParser.GREATER_THAN_EQUAL)
                    gen.addOperator('>=')
                    pass
                elif token in [LilaParser.LESS_THAN_EQUAL]:
                    self.state = 261
                    self.match(LilaParser.LESS_THAN_EQUAL)
                    gen.addOperator('<=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 265
                self.exp()
                gen.exitComparacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
            self.state = 271
            self.termino()
            gen.exitExp()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                self.state = 277
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.PLUS]:
                    self.state = 273
                    self.match(LilaParser.PLUS)
                    gen.addOperator('+')
                    pass
                elif token in [LilaParser.MINUS]:
                    self.state = 275
                    self.match(LilaParser.MINUS)
                    gen.addOperator('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 279
                self.termino()
                gen.exitExp()
                self.state = 286
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
            self.state = 287
            self.factor()
            gen.exitTermino()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.MULTIPLICATION or _la==LilaParser.DIVISION:
                self.state = 293
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.MULTIPLICATION]:
                    self.state = 289
                    self.match(LilaParser.MULTIPLICATION)
                    gen.addOperator('*')
                    pass
                elif token in [LilaParser.DIVISION]:
                    self.state = 291
                    self.match(LilaParser.DIVISION)
                    gen.addOperator('/')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 295
                self.factor()
                gen.exitTermino()
                self.state = 302
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
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.OPEN_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.addOperator('(')
                self.state = 305
                self.expresion()
                self.state = 306
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                pass
            elif token in [LilaParser.PLUS, LilaParser.MINUS, LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==LilaParser.PLUS or _la==LilaParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 312
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LilaParser.ExpContext,i)


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
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                localctx._ID = self.match(LilaParser.ID)
                self.state = 316
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.addFunct(Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text)))
                gen.goSub((None if localctx._ID is None else localctx._ID.text))
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                    self.state = 319
                    self.exp()


                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 322
                    self.match(LilaParser.COMMA)
                    self.state = 323
                    self.exp()
                    self.state = 328
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 329
                self.match(LilaParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                localctx._ID = self.match(LilaParser.ID)
                gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.OPEN_BRACKET:
                    self.state = 332
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 333
                    self.exp()
                    self.state = 334
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 340
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                localctx._CTE_INT = self.match(LilaParser.CTE_INT)
                gen.addVar(Var(None,'int',(None if localctx._CTE_INT is None else localctx._CTE_INT.text)))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 343
                localctx._CTE_F = self.match(LilaParser.CTE_F)
                gen.addVar(Var(None,'num',(None if localctx._CTE_F is None else localctx._CTE_F.text)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                localctx._CTE_STRING = self.match(LilaParser.CTE_STRING)
                gen.addVar(Var(None,'text',(None if localctx._CTE_STRING is None else localctx._CTE_STRING.text)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 347
                localctx._CTE_BOOL = self.match(LilaParser.CTE_BOOL)
                gen.addVar(Var(None,'bool',(None if localctx._CTE_BOOL is None else localctx._CTE_BOOL.text)))
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
            self.state = 351
            self.match(LilaParser.WHILE)
            gen.swhile()
            self.state = 353
            self.expresion()
            gen.checkExpresion()
            self.state = 355
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
            self.state = 358
            localctx._ID = self.match(LilaParser.ID)
            gen.goSub((None if localctx._ID is None else localctx._ID.text))
            self.state = 360
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                self.state = 361
                self.expresion()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 362
                    self.match(LilaParser.COMMA)
                    self.state = 363
                    self.expresion()
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 371
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 372
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
            self.state = 374
            self.match(LilaParser.GETINPUT)
            self.state = 375
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 376
            localctx._ID = self.match(LilaParser.ID)
            gen.getinput(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.COMMA:
                self.state = 378
                self.match(LilaParser.COMMA)
                self.state = 379
                self.match(LilaParser.CTE_STRING)


            self.state = 382
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 383
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
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.GETOUTLIERS, LilaParser.REMOVEOUTLIERS, LilaParser.TELLMEWHATTOUSE, LilaParser.PRINTMEASURES, LilaParser.MEAN, LilaParser.MEDIAN, LilaParser.MODE, LilaParser.RANGE, LilaParser.MIN, LilaParser.MAX, LilaParser.DESESTANDAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 386
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 387
                self.match(LilaParser.ID)
                self.state = 388
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 389
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.QUICKSHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(LilaParser.QUICKSHOW)
                self.state = 391
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 392
                self.match(LilaParser.ID)
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.COMMA:
                    self.state = 393
                    self.match(LilaParser.COMMA)
                    self.state = 394
                    self.match(LilaParser.ID)


                self.state = 397
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 398
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.PEARSONCORRELATION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(LilaParser.PEARSONCORRELATION)
                self.state = 400
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 401
                self.match(LilaParser.ID)
                self.state = 402
                self.match(LilaParser.COMMA)
                self.state = 403
                self.match(LilaParser.ID)
                self.state = 404
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 405
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.NORMALDISTRIBUTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.match(LilaParser.NORMALDISTRIBUTION)
                self.state = 407
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 408
                self.match(LilaParser.CTE_F)
                self.state = 409
                self.match(LilaParser.COMMA)
                self.state = 410
                self.match(LilaParser.CTE_F)
                self.state = 411
                self.match(LilaParser.COMMA)
                self.state = 412
                self.match(LilaParser.CTE_INT)
                self.state = 413
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 414
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.FILLVALUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 415
                self.match(LilaParser.FILLVALUE)
                self.state = 416
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 417
                self.match(LilaParser.ID)
                self.state = 418
                self.match(LilaParser.COMMA)
                self.state = 419
                self.var_cte()
                self.state = 420
                self.match(LilaParser.COMMA)
                self.state = 421
                self.var_cte()
                self.state = 422
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 423
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.REMOVEVALUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 425
                self.match(LilaParser.REMOVEVALUE)
                self.state = 426
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 427
                self.match(LilaParser.ID)
                self.state = 428
                self.match(LilaParser.COMMA)
                self.state = 429
                self.var_cte()
                self.state = 430
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 431
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





