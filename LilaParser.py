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
        buf.write("\u01e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\5\29\n\2\3\2\7\2<\n\2")
        buf.write("\f\2\16\2?\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\6")
        buf.write("\3J\n\3\r\3\16\3K\3\3\3\3\3\4\3\4\3\4\3\4\5\4T\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\7\4[\n\4\f\4\16\4^\13\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6m\n\6\f\6\16")
        buf.write("\6p\13\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\by\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0081\n\b\3\b\3\b\3\b\5\b\u0086\n")
        buf.write("\b\3\b\6\b\u0089\n\b\r\b\16\b\u008a\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0099\n\t\f\t\16\t")
        buf.write("\u009c\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a6")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00af\n\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b7\n\f\f\f\16\f\u00ba")
        buf.write("\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c6")
        buf.write("\n\r\f\r\16\r\u00c9\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u00d4\n\16\f\16\16\16\u00d7\13\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\5\16\u00df\n\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\7\20")
        buf.write("\u00ed\n\20\f\20\16\20\u00f0\13\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u00f8\n\20\f\20\16\20\u00fb\13\20\3\20")
        buf.write("\3\20\7\20\u00ff\n\20\f\20\16\20\u0102\13\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u010a\n\21\3\21\3\21\3\21\7")
        buf.write("\21\u010f\n\21\f\21\16\21\u0112\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0121\n\22\3\22\3\22\3\22\3\22\5\22\u0127\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u012f\n\23\3\23\3\23\3\23")
        buf.write("\7\23\u0134\n\23\f\23\16\23\u0137\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u013f\n\24\3\24\3\24\3\24\7\24\u0144")
        buf.write("\n\24\f\24\16\24\u0147\13\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0152\n\25\3\25\3\25\3\25\5")
        buf.write("\25\u0157\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0166\n\26\f\26\16\26\u0169")
        buf.write("\13\26\5\26\u016b\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u0178\n\26\f\26\16\26\u017b")
        buf.write("\13\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0185")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u019b\n\30\f\30\16\30\u019e\13\30\5\30\u01a0\n\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u01ad\n\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u01bd\n\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u01e3\n\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\2\4\3\2\f\17\3\2+\65")
        buf.write("\2\u0205\2\64\3\2\2\2\4G\3\2\2\2\6S\3\2\2\2\bb\3\2\2\2")
        buf.write("\nf\3\2\2\2\fs\3\2\2\2\16u\3\2\2\2\20\u0090\3\2\2\2\22")
        buf.write("\u00a5\3\2\2\2\24\u00a7\3\2\2\2\26\u00b3\3\2\2\2\30\u00bd")
        buf.write("\3\2\2\2\32\u00cd\3\2\2\2\34\u00e2\3\2\2\2\36\u00e8\3")
        buf.write("\2\2\2 \u0103\3\2\2\2\"\u0126\3\2\2\2$\u0128\3\2\2\2&")
        buf.write("\u0138\3\2\2\2(\u0156\3\2\2\2*\u0184\3\2\2\2,\u0186\3")
        buf.write("\2\2\2.\u018d\3\2\2\2\60\u01a7\3\2\2\2\62\u01e2\3\2\2")
        buf.write("\2\64\65\7\4\2\2\65\66\7;\2\2\668\b\2\1\2\679\5\4\3\2")
        buf.write("8\67\3\2\2\289\3\2\2\29=\3\2\2\2:<\5\16\b\2;:\3\2\2\2")
        buf.write("<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\b")
        buf.write("\2\1\2AB\5\b\5\2BC\b\2\1\2CD\b\2\1\2DE\b\2\1\2EF\b\2\1")
        buf.write("\2F\3\3\2\2\2GI\7\t\2\2HJ\5\6\4\2IH\3\2\2\2JK\3\2\2\2")
        buf.write("KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\3\1\2N\5\3\2\2\2OT")
        buf.write("\5\f\7\2PQ\5\f\7\2QR\5\n\6\2RT\3\2\2\2SO\3\2\2\2SP\3\2")
        buf.write("\2\2TU\3\2\2\2UV\7;\2\2V\\\b\4\1\2WX\7\30\2\2XY\7;\2\2")
        buf.write("Y[\b\4\1\2ZW\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]")
        buf.write("_\3\2\2\2^\\\3\2\2\2_`\b\4\1\2`a\7\31\2\2a\7\3\2\2\2b")
        buf.write("c\7\3\2\2cd\b\5\1\2de\5\26\f\2e\t\3\2\2\2fn\b\6\1\2gh")
        buf.write("\7\22\2\2hi\7\'\2\2ij\b\6\1\2jk\7\23\2\2km\b\6\1\2lg\3")
        buf.write("\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2\2pn\3\2\2")
        buf.write("\2qr\b\6\1\2r\13\3\2\2\2st\t\2\2\2t\r\3\2\2\2ux\7\b\2")
        buf.write("\2vy\5\f\7\2wy\7\5\2\2xv\3\2\2\2xw\3\2\2\2yz\3\2\2\2z")
        buf.write("{\7;\2\2{|\b\b\1\2|}\b\b\1\2}~\b\b\1\2~\u0080\7\24\2\2")
        buf.write("\177\u0081\5\20\t\2\u0080\177\3\2\2\2\u0080\u0081\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7\25\2\2\u0083\u0085")
        buf.write("\7\26\2\2\u0084\u0086\5\4\3\2\u0085\u0084\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0089\5\22\n")
        buf.write("\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008d\7\27\2\2\u008d\u008e\b\b\1\2\u008e\u008f\b\b\1")
        buf.write("\2\u008f\17\3\2\2\2\u0090\u0091\5\f\7\2\u0091\u0092\7")
        buf.write(";\2\2\u0092\u009a\b\t\1\2\u0093\u0094\7\30\2\2\u0094\u0095")
        buf.write("\5\f\7\2\u0095\u0096\7;\2\2\u0096\u0097\b\t\1\2\u0097")
        buf.write("\u0099\3\2\2\2\u0098\u0093\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\21\3\2")
        buf.write("\2\2\u009c\u009a\3\2\2\2\u009d\u00a6\5\32\16\2\u009e\u00a6")
        buf.write("\5\24\13\2\u009f\u00a6\5,\27\2\u00a0\u00a6\5\30\r\2\u00a1")
        buf.write("\u00a6\5\60\31\2\u00a2\u00a6\5.\30\2\u00a3\u00a6\5\34")
        buf.write("\17\2\u00a4\u00a6\5\62\32\2\u00a5\u009d\3\2\2\2\u00a5")
        buf.write("\u009e\3\2\2\2\u00a5\u009f\3\2\2\2\u00a5\u00a0\3\2\2\2")
        buf.write("\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\23\3\2\2\2\u00a7\u00a8")
        buf.write("\7\13\2\2\u00a8\u00a9\5 \21\2\u00a9\u00aa\b\13\1\2\u00aa")
        buf.write("\u00ae\5\26\f\2\u00ab\u00ac\7\n\2\2\u00ac\u00ad\b\13\1")
        buf.write("\2\u00ad\u00af\5\26\f\2\u00ae\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7\31\2\2\u00b1")
        buf.write("\u00b2\b\13\1\2\u00b2\25\3\2\2\2\u00b3\u00b4\7\26\2\2")
        buf.write("\u00b4\u00b8\5\22\n\2\u00b5\u00b7\5\22\n\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00bb\u00bc\7\27\2\2\u00bc\27\3\2\2\2\u00bd\u00be\7\6")
        buf.write("\2\2\u00be\u00bf\7\24\2\2\u00bf\u00c0\5 \21\2\u00c0\u00c7")
        buf.write("\b\r\1\2\u00c1\u00c2\7\30\2\2\u00c2\u00c3\5 \21\2\u00c3")
        buf.write("\u00c4\b\r\1\2\u00c4\u00c6\3\2\2\2\u00c5\u00c1\3\2\2\2")
        buf.write("\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb")
        buf.write("\7\25\2\2\u00cb\u00cc\7\31\2\2\u00cc\31\3\2\2\2\u00cd")
        buf.write("\u00ce\7;\2\2\u00ce\u00d5\b\16\1\2\u00cf\u00d0\7\22\2")
        buf.write("\2\u00d0\u00d1\5$\23\2\u00d1\u00d2\7\23\2\2\u00d2\u00d4")
        buf.write("\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7\"\2\2\u00d9\u00de\b")
        buf.write("\16\1\2\u00da\u00db\5 \21\2\u00db\u00dc\b\16\1\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00df\5\36\20\2\u00de\u00da\3\2\2")
        buf.write("\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1")
        buf.write("\7\31\2\2\u00e1\33\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3")
        buf.write("\u00e4\5 \21\2\u00e4\u00e5\b\17\1\2\u00e5\u00e6\b\17\1")
        buf.write("\2\u00e6\u00e7\7\31\2\2\u00e7\35\3\2\2\2\u00e8\u00e9\7")
        buf.write("\22\2\2\u00e9\u00ee\5*\26\2\u00ea\u00eb\7\30\2\2\u00eb")
        buf.write("\u00ed\5*\26\2\u00ec\u00ea\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u0100\7\23\2\2\u00f2")
        buf.write("\u00f3\7\30\2\2\u00f3\u00f4\7\22\2\2\u00f4\u00f9\5*\26")
        buf.write("\2\u00f5\u00f6\7\30\2\2\u00f6\u00f8\5*\26\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fc\u00fd\7\23\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f2")
        buf.write("\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\37\3\2\2\2\u0102\u0100\3\2\2\2\u0103")
        buf.write("\u0104\5\"\22\2\u0104\u0110\b\21\1\2\u0105\u0106\7%\2")
        buf.write("\2\u0106\u010a\b\21\1\2\u0107\u0108\7&\2\2\u0108\u010a")
        buf.write("\b\21\1\2\u0109\u0105\3\2\2\2\u0109\u0107\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010c\5\"\22\2\u010c\u010d\b\21\1")
        buf.write("\2\u010d\u010f\3\2\2\2\u010e\u0109\3\2\2\2\u010f\u0112")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("!\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0120\5$\23\2\u0114")
        buf.write("\u0115\7\37\2\2\u0115\u0121\b\22\1\2\u0116\u0117\7\36")
        buf.write("\2\2\u0117\u0121\b\22\1\2\u0118\u0119\7 \2\2\u0119\u0121")
        buf.write("\b\22\1\2\u011a\u011b\7!\2\2\u011b\u0121\b\22\1\2\u011c")
        buf.write("\u011d\7$\2\2\u011d\u0121\b\22\1\2\u011e\u011f\7#\2\2")
        buf.write("\u011f\u0121\b\22\1\2\u0120\u0114\3\2\2\2\u0120\u0116")
        buf.write("\3\2\2\2\u0120\u0118\3\2\2\2\u0120\u011a\3\2\2\2\u0120")
        buf.write("\u011c\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\5$\23\2\u0123\u0124\b\22\1\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0127\5$\23\2\u0126\u0113\3\2\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127#\3\2\2\2\u0128\u0129\5&\24\2\u0129")
        buf.write("\u0135\b\23\1\2\u012a\u012b\7\32\2\2\u012b\u012f\b\23")
        buf.write("\1\2\u012c\u012d\7\33\2\2\u012d\u012f\b\23\1\2\u012e\u012a")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\5&\24\2\u0131\u0132\b\23\1\2\u0132\u0134\3\2\2")
        buf.write("\2\u0133\u012e\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136%\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u0139\5(\25\2\u0139\u0145\b\24\1\2\u013a")
        buf.write("\u013b\7\34\2\2\u013b\u013f\b\24\1\2\u013c\u013d\7\35")
        buf.write("\2\2\u013d\u013f\b\24\1\2\u013e\u013a\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\5(\25\2\u0141")
        buf.write("\u0142\b\24\1\2\u0142\u0144\3\2\2\2\u0143\u013e\3\2\2")
        buf.write("\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\'\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149")
        buf.write("\7\24\2\2\u0149\u014a\b\25\1\2\u014a\u014b\5 \21\2\u014b")
        buf.write("\u014c\7\25\2\2\u014c\u014d\b\25\1\2\u014d\u0157\3\2\2")
        buf.write("\2\u014e\u0152\7\32\2\2\u014f\u0150\7\33\2\2\u0150\u0152")
        buf.write("\b\25\1\2\u0151\u014e\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\5*\26\2")
        buf.write("\u0154\u0155\b\25\1\2\u0155\u0157\3\2\2\2\u0156\u0148")
        buf.write("\3\2\2\2\u0156\u0151\3\2\2\2\u0157)\3\2\2\2\u0158\u0159")
        buf.write("\7;\2\2\u0159\u015a\7\24\2\2\u015a\u015b\b\26\1\2\u015b")
        buf.write("\u015c\b\26\1\2\u015c\u015d\b\26\1\2\u015d\u015e\b\26")
        buf.write("\1\2\u015e\u016a\b\26\1\2\u015f\u0160\5 \21\2\u0160\u0167")
        buf.write("\b\26\1\2\u0161\u0162\7\30\2\2\u0162\u0163\5 \21\2\u0163")
        buf.write("\u0164\b\26\1\2\u0164\u0166\3\2\2\2\u0165\u0161\3\2\2")
        buf.write("\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u016a")
        buf.write("\u015f\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\b\26\1\2\u016d\u016e\7\25\2\2\u016e\u016f")
        buf.write("\b\26\1\2\u016f\u0170\b\26\1\2\u0170\u0185\b\26\1\2\u0171")
        buf.write("\u0172\7;\2\2\u0172\u0179\b\26\1\2\u0173\u0174\7\22\2")
        buf.write("\2\u0174\u0175\5$\23\2\u0175\u0176\7\23\2\2\u0176\u0178")
        buf.write("\3\2\2\2\u0177\u0173\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0185\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017c\u017d\7\'\2\2\u017d\u0185\b")
        buf.write("\26\1\2\u017e\u017f\7)\2\2\u017f\u0185\b\26\1\2\u0180")
        buf.write("\u0181\7(\2\2\u0181\u0185\b\26\1\2\u0182\u0183\7*\2\2")
        buf.write("\u0183\u0185\b\26\1\2\u0184\u0158\3\2\2\2\u0184\u0171")
        buf.write("\3\2\2\2\u0184\u017c\3\2\2\2\u0184\u017e\3\2\2\2\u0184")
        buf.write("\u0180\3\2\2\2\u0184\u0182\3\2\2\2\u0185+\3\2\2\2\u0186")
        buf.write("\u0187\7\7\2\2\u0187\u0188\b\27\1\2\u0188\u0189\5 \21")
        buf.write("\2\u0189\u018a\b\27\1\2\u018a\u018b\5\26\f\2\u018b\u018c")
        buf.write("\b\27\1\2\u018c-\3\2\2\2\u018d\u018e\7;\2\2\u018e\u018f")
        buf.write("\7\24\2\2\u018f\u0190\b\30\1\2\u0190\u0191\b\30\1\2\u0191")
        buf.write("\u0192\b\30\1\2\u0192\u0193\b\30\1\2\u0193\u019f\b\30")
        buf.write("\1\2\u0194\u0195\5 \21\2\u0195\u019c\b\30\1\2\u0196\u0197")
        buf.write("\7\30\2\2\u0197\u0198\5 \21\2\u0198\u0199\b\30\1\2\u0199")
        buf.write("\u019b\3\2\2\2\u019a\u0196\3\2\2\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a0\3")
        buf.write("\2\2\2\u019e\u019c\3\2\2\2\u019f\u0194\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b\30\1\2\u01a2")
        buf.write("\u01a3\7\25\2\2\u01a3\u01a4\b\30\1\2\u01a4\u01a5\b\30")
        buf.write("\1\2\u01a5\u01a6\7\31\2\2\u01a6/\3\2\2\2\u01a7\u01a8\7")
        buf.write("\21\2\2\u01a8\u01a9\7\24\2\2\u01a9\u01ac\7;\2\2\u01aa")
        buf.write("\u01ab\7\30\2\2\u01ab\u01ad\7(\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\b")
        buf.write("\31\1\2\u01af\u01b0\7\25\2\2\u01b0\u01b1\7\31\2\2\u01b1")
        buf.write("\61\3\2\2\2\u01b2\u01b3\t\3\2\2\u01b3\u01b4\7\24\2\2\u01b4")
        buf.write("\u01b5\7;\2\2\u01b5\u01b6\7\25\2\2\u01b6\u01e3\7\31\2")
        buf.write("\2\u01b7\u01b8\7\66\2\2\u01b8\u01b9\7\24\2\2\u01b9\u01bc")
        buf.write("\7;\2\2\u01ba\u01bb\7\30\2\2\u01bb\u01bd\7;\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\7\25\2\2\u01bf\u01e3\7\31\2\2\u01c0\u01c1")
        buf.write("\7\67\2\2\u01c1\u01c2\7\24\2\2\u01c2\u01c3\7;\2\2\u01c3")
        buf.write("\u01c4\7\30\2\2\u01c4\u01c5\7;\2\2\u01c5\u01c6\7\25\2")
        buf.write("\2\u01c6\u01e3\7\31\2\2\u01c7\u01c8\78\2\2\u01c8\u01c9")
        buf.write("\7\24\2\2\u01c9\u01ca\7)\2\2\u01ca\u01cb\7\30\2\2\u01cb")
        buf.write("\u01cc\7)\2\2\u01cc\u01cd\7\30\2\2\u01cd\u01ce\7\'\2\2")
        buf.write("\u01ce\u01cf\7\25\2\2\u01cf\u01e3\7\31\2\2\u01d0\u01d1")
        buf.write("\79\2\2\u01d1\u01d2\7\24\2\2\u01d2\u01d3\7;\2\2\u01d3")
        buf.write("\u01d4\7\30\2\2\u01d4\u01d5\5*\26\2\u01d5\u01d6\7\30\2")
        buf.write("\2\u01d6\u01d7\5*\26\2\u01d7\u01d8\7\25\2\2\u01d8\u01d9")
        buf.write("\7\31\2\2\u01d9\u01e3\3\2\2\2\u01da\u01db\7:\2\2\u01db")
        buf.write("\u01dc\7\24\2\2\u01dc\u01dd\7;\2\2\u01dd\u01de\7\30\2")
        buf.write("\2\u01de\u01df\5*\26\2\u01df\u01e0\7\25\2\2\u01e0\u01e1")
        buf.write("\7\31\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01b2\3\2\2\2\u01e2")
        buf.write("\u01b7\3\2\2\2\u01e2\u01c0\3\2\2\2\u01e2\u01c7\3\2\2\2")
        buf.write("\u01e2\u01d0\3\2\2\2\u01e2\u01da\3\2\2\2\u01e3\63\3\2")
        buf.write("\2\2)8=KS\\nx\u0080\u0085\u008a\u009a\u00a5\u00ae\u00b8")
        buf.write("\u00c7\u00d5\u00de\u00ee\u00f9\u0100\u0109\u0110\u0120")
        buf.write("\u0126\u012e\u0135\u013e\u0145\u0151\u0156\u0167\u016a")
        buf.write("\u0179\u0184\u019c\u019f\u01ac\u01bc\u01e2")
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
    RULE_array = 4
    RULE_tipo = 5
    RULE_funciones = 6
    RULE_params = 7
    RULE_estatuto = 8
    RULE_condicion = 9
    RULE_bloque = 10
    RULE_display = 11
    RULE_asignacion = 12
    RULE_sreturn = 13
    RULE_arr = 14
    RULE_expresion = 15
    RULE_comparacion = 16
    RULE_exp = 17
    RULE_termino = 18
    RULE_factor = 19
    RULE_var_cte = 20
    RULE_swhile = 21
    RULE_invocacion = 22
    RULE_getinput = 23
    RULE_especiales = 24

    ruleNames =  [ "programa", "data", "data2", "main", "array", "tipo", 
                   "funciones", "params", "estatuto", "condicion", "bloque", 
                   "display", "asignacion", "sreturn", "arr", "expresion", 
                   "comparacion", "exp", "termino", "factor", "var_cte", 
                   "swhile", "invocacion", "getinput", "especiales" ]

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
            self.state = 50
            self.match(LilaParser.LILA)
            self.state = 51
            self.match(LilaParser.ID)
            gen.goTo()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 53
                self.data()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.FUNC:
                self.state = 56
                self.funciones()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            gen.conditionEnd()
            self.state = 63
            self.main()
            gen.end()
            Semantic.display_test()
            gen.test_final()
            return gen.getObj()
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
            self.state = 69
            self.match(LilaParser.VAR)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.data2()
                self.state = 73 
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.ID)
            else:
                return self.getToken(LilaParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(LilaParser.SEMICOLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(LilaParser.TipoContext,0)


        def array(self):
            return self.getTypedRuleContext(LilaParser.ArrayContext,0)


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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 77
                localctx._tipo = self.tipo()
                pass

            elif la_ == 2:
                self.state = 78
                localctx._tipo = self.tipo()
                self.state = 79
                self.array()
                pass


            self.state = 83
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 85
                self.match(LilaParser.COMMA)
                self.state = 86
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            Semantic.reset_array_setup()
            self.state = 94
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
            self.state = 96
            self.match(LilaParser.MAIN)
            gen.contextChange()
            self.state = 98
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_INT = None # Token

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
            return LilaParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = LilaParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            Semantic.array_declaration()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 101
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 102
                localctx._CTE_INT = self.match(LilaParser.CTE_INT)
                Semantic.array_dimension((None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                self.state = 104
                self.match(LilaParser.CLOSE_BRACKET)
                Semantic.array_next_dim()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            Semantic.arr_second_round()
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
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 12, self.RULE_funciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(LilaParser.FUNC)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.INT, LilaParser.NUM, LilaParser.TEXT, LilaParser.BOOL]:
                self.state = 116
                localctx._tipo = self.tipo()
                pass
            elif token in [LilaParser.VOID]:
                self.state = 117
                localctx._VOID = self.match(LilaParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 120
            localctx._ID = self.match(LilaParser.ID)
            index = len(gen.Quadruples)
            Semantic.enterFunciones((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),(None if localctx._VOID is None else localctx._VOID.text),index)
            gen.contextChange()
            self.state = 124
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0):
                self.state = 125
                self.params()


            self.state = 128
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 129
            self.match(LilaParser.OPEN_CURLY)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 130
                self.data()


            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.estatuto()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0)):
                    break

            self.state = 138
            self.match(LilaParser.CLOSE_CURLY)
            gen.endProc()
            Semantic.end_function()
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
        self.enterRule(localctx, 14, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            localctx._tipo = self.tipo()
            self.state = 143
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 145
                self.match(LilaParser.COMMA)
                self.state = 146
                localctx._tipo = self.tipo()
                self.state = 147
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 154
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
        self.enterRule(localctx, 16, self.RULE_estatuto)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.swhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.display()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.getinput()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.invocacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.sreturn()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 162
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
        self.enterRule(localctx, 18, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(LilaParser.IF)
            self.state = 166
            self.expresion()
            gen.checkExpresion()
            self.state = 168
            self.bloque()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.ELSE:
                self.state = 169
                self.match(LilaParser.ELSE)
                gen.conditionElse()
                self.state = 171
                self.bloque()


            self.state = 174
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
        self.enterRule(localctx, 20, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(LilaParser.OPEN_CURLY)
            self.state = 178
            self.estatuto()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0):
                self.state = 179
                self.estatuto()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
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
        self.enterRule(localctx, 22, self.RULE_display)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(LilaParser.DISPLAY)
            self.state = 188
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 189
            self.expresion()
            gen.display()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 191
                self.match(LilaParser.COMMA)
                self.state = 192
                self.expresion()
                gen.display()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 201
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
        self.enterRule(localctx, 24, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx._ID = self.match(LilaParser.ID)
            gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 205
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 206
                self.exp()
                self.state = 207
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            localctx._EQUAL = self.match(LilaParser.EQUAL)
            gen.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.OPEN_PARENTHESIS, LilaParser.PLUS, LilaParser.MINUS, LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.state = 216
                self.expresion()
                gen.assign()
                pass
            elif token in [LilaParser.OPEN_BRACKET]:
                self.state = 219
                self.arr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 222
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
        self.enterRule(localctx, 26, self.RULE_sreturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(LilaParser.RETURN)
            self.state = 225
            self.expresion()
            Semantic.checkReturn(gen.top_variables())
            gen.func_return()
            self.state = 228
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

        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.OPEN_BRACKET)
            else:
                return self.getToken(LilaParser.OPEN_BRACKET, i)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LilaParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(LilaParser.Var_cteContext,i)


        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.CLOSE_BRACKET)
            else:
                return self.getToken(LilaParser.CLOSE_BRACKET, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LilaParser.COMMA)
            else:
                return self.getToken(LilaParser.COMMA, i)

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
        self.enterRule(localctx, 28, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(LilaParser.OPEN_BRACKET)
            self.state = 231
            self.var_cte()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 232
                self.match(LilaParser.COMMA)
                self.state = 233
                self.var_cte()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(LilaParser.CLOSE_BRACKET)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 240
                self.match(LilaParser.COMMA)
                self.state = 241
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 242
                self.var_cte()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 243
                    self.match(LilaParser.COMMA)
                    self.state = 244
                    self.var_cte()
                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 250
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 30, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.comparacion()
            gen.exitExpresion()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.AND or _la==LilaParser.OR:
                self.state = 263
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.AND]:
                    self.state = 259
                    self.match(LilaParser.AND)
                    gen.addOperator('AND')
                    pass
                elif token in [LilaParser.OR]:
                    self.state = 261
                    self.match(LilaParser.OR)
                    gen.addOperator('OR')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 265
                self.comparacion()
                gen.exitExpresion()
                self.state = 272
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
        self.enterRule(localctx, 32, self.RULE_comparacion)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.exp()
                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.GREATER_THAN]:
                    self.state = 274
                    self.match(LilaParser.GREATER_THAN)
                    gen.addOperator('>')
                    pass
                elif token in [LilaParser.LESS_THAN]:
                    self.state = 276
                    self.match(LilaParser.LESS_THAN)
                    gen.addOperator('<')
                    pass
                elif token in [LilaParser.NOTEQUAL]:
                    self.state = 278
                    self.match(LilaParser.NOTEQUAL)
                    gen.addOperator('!=')
                    pass
                elif token in [LilaParser.EQUALITY]:
                    self.state = 280
                    self.match(LilaParser.EQUALITY)
                    gen.addOperator('==')
                    pass
                elif token in [LilaParser.GREATER_THAN_EQUAL]:
                    self.state = 282
                    self.match(LilaParser.GREATER_THAN_EQUAL)
                    gen.addOperator('>=')
                    pass
                elif token in [LilaParser.LESS_THAN_EQUAL]:
                    self.state = 284
                    self.match(LilaParser.LESS_THAN_EQUAL)
                    gen.addOperator('<=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 288
                self.exp()
                gen.exitComparacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
        self.enterRule(localctx, 34, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.termino()
            gen.exitExp()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                self.state = 300
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.PLUS]:
                    self.state = 296
                    self.match(LilaParser.PLUS)
                    gen.addOperator('+')
                    pass
                elif token in [LilaParser.MINUS]:
                    self.state = 298
                    self.match(LilaParser.MINUS)
                    gen.addOperator('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 302
                self.termino()
                gen.exitExp()
                self.state = 309
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
        self.enterRule(localctx, 36, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.factor()
            gen.exitTermino()
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.MULTIPLICATION or _la==LilaParser.DIVISION:
                self.state = 316
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.MULTIPLICATION]:
                    self.state = 312
                    self.match(LilaParser.MULTIPLICATION)
                    gen.addOperator('*')
                    pass
                elif token in [LilaParser.DIVISION]:
                    self.state = 314
                    self.match(LilaParser.DIVISION)
                    gen.addOperator('/')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 318
                self.factor()
                gen.exitTermino()
                self.state = 325
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
            self._MINUS = None # Token

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
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.OPEN_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.addOperator('(')
                self.state = 328
                self.expresion()
                self.state = 329
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                pass
            elif token in [LilaParser.PLUS, LilaParser.MINUS, LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.PLUS]:
                    self.state = 332
                    self.match(LilaParser.PLUS)
                    pass
                elif token in [LilaParser.MINUS]:
                    self.state = 333
                    localctx._MINUS = self.match(LilaParser.MINUS)
                    gen.isNegative()
                    pass
                elif token in [LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                    pass
                else:
                    pass
                self.state = 337
                self.var_cte()
                gen.makeNegative((None if localctx._MINUS is None else localctx._MINUS.text))
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
        self.enterRule(localctx, 40, self.RULE_var_cte)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                localctx._ID = self.match(LilaParser.ID)
                self.state = 343
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.incoming_Params()
                Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
                Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), False)
                gen.era((None if localctx._ID is None else localctx._ID.text))
                gen.addOperator('(')
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                    self.state = 349
                    self.expresion()
                    gen.params()
                    self.state = 357
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LilaParser.COMMA:
                        self.state = 351
                        self.match(LilaParser.COMMA)
                        self.state = 352
                        self.expresion()
                        gen.params()
                        self.state = 359
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                gen.goSub((None if localctx._ID is None else localctx._ID.text))
                self.state = 363
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.check_params((None if localctx._ID is None else localctx._ID.text))
                gen.finParentesis()
                gen.addFunct(Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                localctx._ID = self.match(LilaParser.ID)
                gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.OPEN_BRACKET:
                    self.state = 369
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 370
                    self.exp()
                    self.state = 371
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                localctx._CTE_INT = self.match(LilaParser.CTE_INT)
                gen.addConst(Operand(None,'int',(None if localctx._CTE_INT is None else localctx._CTE_INT.text)))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                localctx._CTE_F = self.match(LilaParser.CTE_F)
                gen.addConst(Operand(None,'num',(None if localctx._CTE_F is None else localctx._CTE_F.text)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 382
                localctx._CTE_STRING = self.match(LilaParser.CTE_STRING)
                gen.addConst(Operand(None,'text',(None if localctx._CTE_STRING is None else localctx._CTE_STRING.text)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
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
        self.enterRule(localctx, 42, self.RULE_swhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(LilaParser.WHILE)
            gen.swhile()
            self.state = 390
            self.expresion()
            gen.checkExpresion()
            self.state = 392
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
        self.enterRule(localctx, 44, self.RULE_invocacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            localctx._ID = self.match(LilaParser.ID)
            self.state = 396
            self.match(LilaParser.OPEN_PARENTHESIS)
            gen.incoming_Params()
            Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
            Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), True)
            gen.era((None if localctx._ID is None else localctx._ID.text))
            gen.addOperator('(')
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                self.state = 402
                self.expresion()
                gen.params()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 404
                    self.match(LilaParser.COMMA)
                    self.state = 405
                    self.expresion()
                    gen.params()
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            gen.goSub((None if localctx._ID is None else localctx._ID.text))
            self.state = 416
            self.match(LilaParser.CLOSE_PARENTHESIS)
            gen.check_params((None if localctx._ID is None else localctx._ID.text))
            gen.finParentesis()
            self.state = 419
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
            self._CTE_STRING = None # Token

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
        self.enterRule(localctx, 46, self.RULE_getinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(LilaParser.GETINPUT)
            self.state = 422
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 423
            localctx._ID = self.match(LilaParser.ID)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.COMMA:
                self.state = 424
                self.match(LilaParser.COMMA)
                self.state = 425
                localctx._CTE_STRING = self.match(LilaParser.CTE_STRING)


            gen.getinput(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)), (None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
            self.state = 429
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 430
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
        self.enterRule(localctx, 48, self.RULE_especiales)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.GETOUTLIERS, LilaParser.REMOVEOUTLIERS, LilaParser.TELLMEWHATTOUSE, LilaParser.PRINTMEASURES, LilaParser.MEAN, LilaParser.MEDIAN, LilaParser.MODE, LilaParser.RANGE, LilaParser.MIN, LilaParser.MAX, LilaParser.DESESTANDAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 433
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 434
                self.match(LilaParser.ID)
                self.state = 435
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 436
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.QUICKSHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(LilaParser.QUICKSHOW)
                self.state = 438
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 439
                self.match(LilaParser.ID)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.COMMA:
                    self.state = 440
                    self.match(LilaParser.COMMA)
                    self.state = 441
                    self.match(LilaParser.ID)


                self.state = 444
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 445
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.PEARSONCORRELATION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.match(LilaParser.PEARSONCORRELATION)
                self.state = 447
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 448
                self.match(LilaParser.ID)
                self.state = 449
                self.match(LilaParser.COMMA)
                self.state = 450
                self.match(LilaParser.ID)
                self.state = 451
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 452
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.NORMALDISTRIBUTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.match(LilaParser.NORMALDISTRIBUTION)
                self.state = 454
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 455
                self.match(LilaParser.CTE_F)
                self.state = 456
                self.match(LilaParser.COMMA)
                self.state = 457
                self.match(LilaParser.CTE_F)
                self.state = 458
                self.match(LilaParser.COMMA)
                self.state = 459
                self.match(LilaParser.CTE_INT)
                self.state = 460
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 461
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.FILLVALUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 462
                self.match(LilaParser.FILLVALUE)
                self.state = 463
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 464
                self.match(LilaParser.ID)
                self.state = 465
                self.match(LilaParser.COMMA)
                self.state = 466
                self.var_cte()
                self.state = 467
                self.match(LilaParser.COMMA)
                self.state = 468
                self.var_cte()
                self.state = 469
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 470
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.REMOVEVALUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
                self.match(LilaParser.REMOVEVALUE)
                self.state = 473
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 474
                self.match(LilaParser.ID)
                self.state = 475
                self.match(LilaParser.COMMA)
                self.state = 476
                self.var_cte()
                self.state = 477
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 478
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





