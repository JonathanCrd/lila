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
        buf.write("\u01c9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\5\2\67\n\2\3\2\7\2:\n\2\f\2\16\2")
        buf.write("=\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3F\n\3\r\3\16\3G")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4R\n\4\f\4\16\4U\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6a\n\6\f")
        buf.write("\6\16\6d\13\6\3\7\3\7\3\7\5\7i\n\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7q\n\7\3\7\3\7\3\7\5\7v\n\7\3\7\6\7y\n\7\r\7\16")
        buf.write("\7z\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7")
        buf.write("\b\u0089\n\b\f\b\16\b\u008c\13\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u0096\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u009f\n\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00a7\n\13")
        buf.write("\f\13\16\13\u00aa\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\7\f\u00b6\n\f\f\f\16\f\u00b9\13\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c4\n\r\f\r\16\r\u00c7")
        buf.write("\13\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00cf\n\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00dc")
        buf.write("\n\17\f\17\16\17\u00df\13\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00e9\n\17\f\17\16\17\u00ec\13\17")
        buf.write("\5\17\u00ee\n\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f6")
        buf.write("\n\20\3\20\3\20\3\20\7\20\u00fb\n\20\f\20\16\20\u00fe")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u010d\n\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u0113\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u011b")
        buf.write("\n\22\3\22\3\22\3\22\7\22\u0120\n\22\f\22\16\22\u0123")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u012b\n\23\3")
        buf.write("\23\3\23\3\23\7\23\u0130\n\23\f\23\16\23\u0133\13\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u013c\n\24\3\24")
        buf.write("\5\24\u013f\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\7\25\u014d\n\25\f\25\16\25\u0150")
        buf.write("\13\25\5\25\u0152\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u015e\n\25\f\25\16\25\u0161\13")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u016b")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0180")
        buf.write("\n\27\f\27\16\27\u0183\13\27\5\27\u0185\n\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0192")
        buf.write("\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u01a1\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u01c7\n\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\2\5\3\2\f\17\3\2\32\33\3\2+\65\2")
        buf.write("\u01e8\2\62\3\2\2\2\4C\3\2\2\2\6K\3\2\2\2\bX\3\2\2\2\n")
        buf.write("\\\3\2\2\2\fe\3\2\2\2\16\u0080\3\2\2\2\20\u0095\3\2\2")
        buf.write("\2\22\u0097\3\2\2\2\24\u00a3\3\2\2\2\26\u00ad\3\2\2\2")
        buf.write("\30\u00bd\3\2\2\2\32\u00d2\3\2\2\2\34\u00ed\3\2\2\2\36")
        buf.write("\u00ef\3\2\2\2 \u0112\3\2\2\2\"\u0114\3\2\2\2$\u0124\3")
        buf.write("\2\2\2&\u013e\3\2\2\2(\u016a\3\2\2\2*\u016c\3\2\2\2,\u0173")
        buf.write("\3\2\2\2.\u018b\3\2\2\2\60\u01c6\3\2\2\2\62\63\7\4\2\2")
        buf.write("\63\64\7;\2\2\64\66\b\2\1\2\65\67\5\4\3\2\66\65\3\2\2")
        buf.write("\2\66\67\3\2\2\2\67;\3\2\2\28:\5\f\7\298\3\2\2\2:=\3\2")
        buf.write("\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\b\2\1\2")
        buf.write("?@\5\b\5\2@A\b\2\1\2AB\b\2\1\2B\3\3\2\2\2CE\7\t\2\2DF")
        buf.write("\5\6\4\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2")
        buf.write("\2\2IJ\b\3\1\2J\5\3\2\2\2KL\5\n\6\2LM\7;\2\2MS\b\4\1\2")
        buf.write("NO\7\30\2\2OP\7;\2\2PR\b\4\1\2QN\3\2\2\2RU\3\2\2\2SQ\3")
        buf.write("\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\31\2\2W\7\3\2")
        buf.write("\2\2XY\7\3\2\2YZ\b\5\1\2Z[\5\24\13\2[\t\3\2\2\2\\b\t\2")
        buf.write("\2\2]^\7\22\2\2^_\7\'\2\2_a\7\23\2\2`]\3\2\2\2ad\3\2\2")
        buf.write("\2b`\3\2\2\2bc\3\2\2\2c\13\3\2\2\2db\3\2\2\2eh\7\b\2\2")
        buf.write("fi\5\n\6\2gi\7\5\2\2hf\3\2\2\2hg\3\2\2\2ij\3\2\2\2jk\7")
        buf.write(";\2\2kl\b\7\1\2lm\b\7\1\2mn\b\7\1\2np\7\24\2\2oq\5\16")
        buf.write("\b\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\25\2\2su\7\26\2")
        buf.write("\2tv\5\4\3\2ut\3\2\2\2uv\3\2\2\2vx\3\2\2\2wy\5\20\t\2")
        buf.write("xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{|\3\2\2\2|}\7")
        buf.write("\27\2\2}~\b\7\1\2~\177\b\7\1\2\177\r\3\2\2\2\u0080\u0081")
        buf.write("\5\n\6\2\u0081\u0082\7;\2\2\u0082\u008a\b\b\1\2\u0083")
        buf.write("\u0084\7\30\2\2\u0084\u0085\5\n\6\2\u0085\u0086\7;\2\2")
        buf.write("\u0086\u0087\b\b\1\2\u0087\u0089\3\2\2\2\u0088\u0083\3")
        buf.write("\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\17\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u0096")
        buf.write("\5\30\r\2\u008e\u0096\5\22\n\2\u008f\u0096\5*\26\2\u0090")
        buf.write("\u0096\5\26\f\2\u0091\u0096\5.\30\2\u0092\u0096\5,\27")
        buf.write("\2\u0093\u0096\5\32\16\2\u0094\u0096\5\60\31\2\u0095\u008d")
        buf.write("\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3\2\2\2\u0095")
        buf.write("\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\21\3\2")
        buf.write("\2\2\u0097\u0098\7\13\2\2\u0098\u0099\5\36\20\2\u0099")
        buf.write("\u009a\b\n\1\2\u009a\u009e\5\24\13\2\u009b\u009c\7\n\2")
        buf.write("\2\u009c\u009d\b\n\1\2\u009d\u009f\5\24\13\2\u009e\u009b")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\7\31\2\2\u00a1\u00a2\b\n\1\2\u00a2\23\3\2\2\2\u00a3")
        buf.write("\u00a4\7\26\2\2\u00a4\u00a8\5\20\t\2\u00a5\u00a7\5\20")
        buf.write("\t\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00ac\7\27\2\2\u00ac\25\3\2\2\2\u00ad")
        buf.write("\u00ae\7\6\2\2\u00ae\u00af\7\24\2\2\u00af\u00b0\5\36\20")
        buf.write("\2\u00b0\u00b7\b\f\1\2\u00b1\u00b2\7\30\2\2\u00b2\u00b3")
        buf.write("\5\36\20\2\u00b3\u00b4\b\f\1\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b1\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00ba\u00bb\7\25\2\2\u00bb\u00bc\7\31\2\2\u00bc")
        buf.write("\27\3\2\2\2\u00bd\u00be\7;\2\2\u00be\u00c5\b\r\1\2\u00bf")
        buf.write("\u00c0\7\22\2\2\u00c0\u00c1\5\"\22\2\u00c1\u00c2\7\23")
        buf.write("\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c4\u00c7")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\"\2\2")
        buf.write("\u00c9\u00ce\b\r\1\2\u00ca\u00cb\5\36\20\2\u00cb\u00cc")
        buf.write("\b\r\1\2\u00cc\u00cf\3\2\2\2\u00cd\u00cf\5\34\17\2\u00ce")
        buf.write("\u00ca\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d1\7\31\2\2\u00d1\31\3\2\2\2\u00d2\u00d3\7\20")
        buf.write("\2\2\u00d3\u00d4\5\36\20\2\u00d4\u00d5\b\16\1\2\u00d5")
        buf.write("\u00d6\b\16\1\2\u00d6\u00d7\7\31\2\2\u00d7\33\3\2\2\2")
        buf.write("\u00d8\u00dd\5(\25\2\u00d9\u00da\7\30\2\2\u00da\u00dc")
        buf.write("\5(\25\2\u00db\u00d9\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00ee\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00e0\u00e1\7\22\2\2\u00e1\u00e2")
        buf.write("\5\34\17\2\u00e2\u00ea\7\23\2\2\u00e3\u00e4\7\30\2\2\u00e4")
        buf.write("\u00e5\7\22\2\2\u00e5\u00e6\5\34\17\2\u00e6\u00e7\7\23")
        buf.write("\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e9\u00ec")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00d8\3\2\2\2")
        buf.write("\u00ed\u00e0\3\2\2\2\u00ee\35\3\2\2\2\u00ef\u00f0\5 \21")
        buf.write("\2\u00f0\u00fc\b\20\1\2\u00f1\u00f2\7%\2\2\u00f2\u00f6")
        buf.write("\b\20\1\2\u00f3\u00f4\7&\2\2\u00f4\u00f6\b\20\1\2\u00f5")
        buf.write("\u00f1\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f8\5 \21\2\u00f8\u00f9\b\20\1\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f5\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\37\3\2\2\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00ff\u010c\5\"\22\2\u0100\u0101\7\37\2")
        buf.write("\2\u0101\u010d\b\21\1\2\u0102\u0103\7\36\2\2\u0103\u010d")
        buf.write("\b\21\1\2\u0104\u0105\7 \2\2\u0105\u010d\b\21\1\2\u0106")
        buf.write("\u0107\7!\2\2\u0107\u010d\b\21\1\2\u0108\u0109\7$\2\2")
        buf.write("\u0109\u010d\b\21\1\2\u010a\u010b\7#\2\2\u010b\u010d\b")
        buf.write("\21\1\2\u010c\u0100\3\2\2\2\u010c\u0102\3\2\2\2\u010c")
        buf.write("\u0104\3\2\2\2\u010c\u0106\3\2\2\2\u010c\u0108\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\5")
        buf.write("\"\22\2\u010f\u0110\b\21\1\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u0113\5\"\22\2\u0112\u00ff\3\2\2\2\u0112\u0111\3\2\2")
        buf.write("\2\u0113!\3\2\2\2\u0114\u0115\5$\23\2\u0115\u0121\b\22")
        buf.write("\1\2\u0116\u0117\7\32\2\2\u0117\u011b\b\22\1\2\u0118\u0119")
        buf.write("\7\33\2\2\u0119\u011b\b\22\1\2\u011a\u0116\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\5$\23\2")
        buf.write("\u011d\u011e\b\22\1\2\u011e\u0120\3\2\2\2\u011f\u011a")
        buf.write("\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122#\3\2\2\2\u0123\u0121\3\2\2\2\u0124")
        buf.write("\u0125\5&\24\2\u0125\u0131\b\23\1\2\u0126\u0127\7\34\2")
        buf.write("\2\u0127\u012b\b\23\1\2\u0128\u0129\7\35\2\2\u0129\u012b")
        buf.write("\b\23\1\2\u012a\u0126\3\2\2\2\u012a\u0128\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\u012d\5&\24\2\u012d\u012e\b\23\1")
        buf.write("\2\u012e\u0130\3\2\2\2\u012f\u012a\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("%\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\7\24\2\2\u0135")
        buf.write("\u0136\b\24\1\2\u0136\u0137\5\36\20\2\u0137\u0138\7\25")
        buf.write("\2\2\u0138\u0139\b\24\1\2\u0139\u013f\3\2\2\2\u013a\u013c")
        buf.write("\t\3\2\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013f\5(\25\2\u013e\u0134\3\2\2\2")
        buf.write("\u013e\u013b\3\2\2\2\u013f\'\3\2\2\2\u0140\u0141\7;\2")
        buf.write("\2\u0141\u0142\7\24\2\2\u0142\u0143\b\25\1\2\u0143\u0144")
        buf.write("\b\25\1\2\u0144\u0145\b\25\1\2\u0145\u0151\b\25\1\2\u0146")
        buf.write("\u0147\5\36\20\2\u0147\u014e\b\25\1\2\u0148\u0149\7\30")
        buf.write("\2\2\u0149\u014a\5\36\20\2\u014a\u014b\b\25\1\2\u014b")
        buf.write("\u014d\3\2\2\2\u014c\u0148\3\2\2\2\u014d\u0150\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0152\3")
        buf.write("\2\2\2\u0150\u014e\3\2\2\2\u0151\u0146\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\b\25\1\2\u0154")
        buf.write("\u0155\7\25\2\2\u0155\u0156\b\25\1\2\u0156\u016b\b\25")
        buf.write("\1\2\u0157\u0158\7;\2\2\u0158\u015f\b\25\1\2\u0159\u015a")
        buf.write("\7\22\2\2\u015a\u015b\5\"\22\2\u015b\u015c\7\23\2\2\u015c")
        buf.write("\u015e\3\2\2\2\u015d\u0159\3\2\2\2\u015e\u0161\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u016b\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163\7\'\2\2\u0163\u016b")
        buf.write("\b\25\1\2\u0164\u0165\7)\2\2\u0165\u016b\b\25\1\2\u0166")
        buf.write("\u0167\7(\2\2\u0167\u016b\b\25\1\2\u0168\u0169\7*\2\2")
        buf.write("\u0169\u016b\b\25\1\2\u016a\u0140\3\2\2\2\u016a\u0157")
        buf.write("\3\2\2\2\u016a\u0162\3\2\2\2\u016a\u0164\3\2\2\2\u016a")
        buf.write("\u0166\3\2\2\2\u016a\u0168\3\2\2\2\u016b)\3\2\2\2\u016c")
        buf.write("\u016d\7\7\2\2\u016d\u016e\b\26\1\2\u016e\u016f\5\36\20")
        buf.write("\2\u016f\u0170\b\26\1\2\u0170\u0171\5\24\13\2\u0171\u0172")
        buf.write("\b\26\1\2\u0172+\3\2\2\2\u0173\u0174\7;\2\2\u0174\u0175")
        buf.write("\7\24\2\2\u0175\u0176\b\27\1\2\u0176\u0177\b\27\1\2\u0177")
        buf.write("\u0178\b\27\1\2\u0178\u0184\b\27\1\2\u0179\u017a\5\36")
        buf.write("\20\2\u017a\u0181\b\27\1\2\u017b\u017c\7\30\2\2\u017c")
        buf.write("\u017d\5\36\20\2\u017d\u017e\b\27\1\2\u017e\u0180\3\2")
        buf.write("\2\2\u017f\u017b\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0184\u0179\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0187\b\27\1\2\u0187\u0188")
        buf.write("\7\25\2\2\u0188\u0189\b\27\1\2\u0189\u018a\7\31\2\2\u018a")
        buf.write("-\3\2\2\2\u018b\u018c\7\21\2\2\u018c\u018d\7\24\2\2\u018d")
        buf.write("\u018e\7;\2\2\u018e\u0191\b\30\1\2\u018f\u0190\7\30\2")
        buf.write("\2\u0190\u0192\7(\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\7\25\2\2\u0194")
        buf.write("\u0195\7\31\2\2\u0195/\3\2\2\2\u0196\u0197\t\4\2\2\u0197")
        buf.write("\u0198\7\24\2\2\u0198\u0199\7;\2\2\u0199\u019a\7\25\2")
        buf.write("\2\u019a\u01c7\7\31\2\2\u019b\u019c\7\66\2\2\u019c\u019d")
        buf.write("\7\24\2\2\u019d\u01a0\7;\2\2\u019e\u019f\7\30\2\2\u019f")
        buf.write("\u01a1\7;\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a3\7\25\2\2\u01a3\u01c7")
        buf.write("\7\31\2\2\u01a4\u01a5\7\67\2\2\u01a5\u01a6\7\24\2\2\u01a6")
        buf.write("\u01a7\7;\2\2\u01a7\u01a8\7\30\2\2\u01a8\u01a9\7;\2\2")
        buf.write("\u01a9\u01aa\7\25\2\2\u01aa\u01c7\7\31\2\2\u01ab\u01ac")
        buf.write("\78\2\2\u01ac\u01ad\7\24\2\2\u01ad\u01ae\7)\2\2\u01ae")
        buf.write("\u01af\7\30\2\2\u01af\u01b0\7)\2\2\u01b0\u01b1\7\30\2")
        buf.write("\2\u01b1\u01b2\7\'\2\2\u01b2\u01b3\7\25\2\2\u01b3\u01c7")
        buf.write("\7\31\2\2\u01b4\u01b5\79\2\2\u01b5\u01b6\7\24\2\2\u01b6")
        buf.write("\u01b7\7;\2\2\u01b7\u01b8\7\30\2\2\u01b8\u01b9\5(\25\2")
        buf.write("\u01b9\u01ba\7\30\2\2\u01ba\u01bb\5(\25\2\u01bb\u01bc")
        buf.write("\7\25\2\2\u01bc\u01bd\7\31\2\2\u01bd\u01c7\3\2\2\2\u01be")
        buf.write("\u01bf\7:\2\2\u01bf\u01c0\7\24\2\2\u01c0\u01c1\7;\2\2")
        buf.write("\u01c1\u01c2\7\30\2\2\u01c2\u01c3\5(\25\2\u01c3\u01c4")
        buf.write("\7\25\2\2\u01c4\u01c5\7\31\2\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u0196\3\2\2\2\u01c6\u019b\3\2\2\2\u01c6\u01a4\3\2\2\2")
        buf.write("\u01c6\u01ab\3\2\2\2\u01c6\u01b4\3\2\2\2\u01c6\u01be\3")
        buf.write("\2\2\2\u01c7\61\3\2\2\2(\66;GSbhpuz\u008a\u0095\u009e")
        buf.write("\u00a8\u00b7\u00c5\u00ce\u00dd\u00ea\u00ed\u00f5\u00fc")
        buf.write("\u010c\u0112\u011a\u0121\u012a\u0131\u013b\u013e\u014e")
        buf.write("\u0151\u015f\u016a\u0181\u0184\u0191\u01a0\u01c6")
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
            self.state = 73
            localctx._tipo = self.tipo()
            self.state = 74
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 76
                self.match(LilaParser.COMMA)
                self.state = 77
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_var(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
            self.state = 86
            self.match(LilaParser.MAIN)
            gen.contextChange()
            self.state = 88
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
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 91
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 92
                self.match(LilaParser.CTE_INT)
                self.state = 93
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 98
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
            self.state = 99
            self.match(LilaParser.FUNC)
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.INT, LilaParser.NUM, LilaParser.TEXT, LilaParser.BOOL]:
                self.state = 100
                localctx._tipo = self.tipo()
                pass
            elif token in [LilaParser.VOID]:
                self.state = 101
                localctx._VOID = self.match(LilaParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 104
            localctx._ID = self.match(LilaParser.ID)
            index = len(gen.Quadruples)
            Semantic.enterFunciones((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),(None if localctx._VOID is None else localctx._VOID.text),index)
            gen.contextChange()
            self.state = 108
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.INT) | (1 << LilaParser.NUM) | (1 << LilaParser.TEXT) | (1 << LilaParser.BOOL))) != 0):
                self.state = 109
                self.params()


            self.state = 112
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 113
            self.match(LilaParser.OPEN_CURLY)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.VAR:
                self.state = 114
                self.data()


            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.estatuto()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0)):
                    break

            self.state = 122
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
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._tipo = self.tipo()
            self.state = 127
            localctx._ID = self.match(LilaParser.ID)
            Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 129
                self.match(LilaParser.COMMA)
                self.state = 130
                localctx._tipo = self.tipo()
                self.state = 131
                localctx._ID = self.match(LilaParser.ID)
                Semantic.add_param(Operand((None if localctx._ID is None else localctx._ID.text),(None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))),None))
                self.state = 138
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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.swhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.display()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.getinput()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.invocacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.sreturn()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
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
            self.state = 149
            self.match(LilaParser.IF)
            self.state = 150
            self.expresion()
            gen.checkExpresion()
            self.state = 152
            self.bloque()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.ELSE:
                self.state = 153
                self.match(LilaParser.ELSE)
                gen.conditionElse()
                self.state = 155
                self.bloque()


            self.state = 158
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
            self.state = 161
            self.match(LilaParser.OPEN_CURLY)
            self.state = 162
            self.estatuto()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.DISPLAY) | (1 << LilaParser.WHILE) | (1 << LilaParser.IF) | (1 << LilaParser.RETURN) | (1 << LilaParser.GETINPUT) | (1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR) | (1 << LilaParser.QUICKSHOW) | (1 << LilaParser.PEARSONCORRELATION) | (1 << LilaParser.NORMALDISTRIBUTION) | (1 << LilaParser.FILLVALUE) | (1 << LilaParser.REMOVEVALUE) | (1 << LilaParser.ID))) != 0):
                self.state = 163
                self.estatuto()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
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
            self.state = 171
            self.match(LilaParser.DISPLAY)
            self.state = 172
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 173
            self.expresion()
            gen.display()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.COMMA:
                self.state = 175
                self.match(LilaParser.COMMA)
                self.state = 176
                self.expresion()
                gen.display()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 185
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
            self.state = 187
            localctx._ID = self.match(LilaParser.ID)
            gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.OPEN_BRACKET:
                self.state = 189
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 190
                self.exp()
                self.state = 191
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            localctx._EQUAL = self.match(LilaParser.EQUAL)
            gen.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 200
                self.expresion()
                gen.assign()
                pass

            elif la_ == 2:
                self.state = 203
                self.arr()
                pass


            self.state = 206
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
            self.state = 208
            self.match(LilaParser.RETURN)
            self.state = 209
            self.expresion()
            Semantic.checkReturn(gen.top_variables())
            gen.func_return()
            self.state = 212
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
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.var_cte()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 215
                    self.match(LilaParser.COMMA)
                    self.state = 216
                    self.var_cte()
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [LilaParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(LilaParser.OPEN_BRACKET)
                self.state = 223
                self.arr()
                self.state = 224
                self.match(LilaParser.CLOSE_BRACKET)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 225
                    self.match(LilaParser.COMMA)
                    self.state = 226
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 227
                    self.arr()
                    self.state = 228
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 234
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
            self.state = 237
            self.comparacion()
            gen.exitExpresion()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.AND or _la==LilaParser.OR:
                self.state = 243
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.AND]:
                    self.state = 239
                    self.match(LilaParser.AND)
                    gen.addOperator('AND')
                    pass
                elif token in [LilaParser.OR]:
                    self.state = 241
                    self.match(LilaParser.OR)
                    gen.addOperator('OR')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 245
                self.comparacion()
                gen.exitExpresion()
                self.state = 252
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
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.exp()
                self.state = 266
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.GREATER_THAN]:
                    self.state = 254
                    self.match(LilaParser.GREATER_THAN)
                    gen.addOperator('>')
                    pass
                elif token in [LilaParser.LESS_THAN]:
                    self.state = 256
                    self.match(LilaParser.LESS_THAN)
                    gen.addOperator('<')
                    pass
                elif token in [LilaParser.NOTEQUAL]:
                    self.state = 258
                    self.match(LilaParser.NOTEQUAL)
                    gen.addOperator('!=')
                    pass
                elif token in [LilaParser.EQUALITY]:
                    self.state = 260
                    self.match(LilaParser.EQUALITY)
                    gen.addOperator('==')
                    pass
                elif token in [LilaParser.GREATER_THAN_EQUAL]:
                    self.state = 262
                    self.match(LilaParser.GREATER_THAN_EQUAL)
                    gen.addOperator('>=')
                    pass
                elif token in [LilaParser.LESS_THAN_EQUAL]:
                    self.state = 264
                    self.match(LilaParser.LESS_THAN_EQUAL)
                    gen.addOperator('<=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 268
                self.exp()
                gen.exitComparacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
            self.state = 274
            self.termino()
            gen.exitExp()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                self.state = 280
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.PLUS]:
                    self.state = 276
                    self.match(LilaParser.PLUS)
                    gen.addOperator('+')
                    pass
                elif token in [LilaParser.MINUS]:
                    self.state = 278
                    self.match(LilaParser.MINUS)
                    gen.addOperator('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 282
                self.termino()
                gen.exitExp()
                self.state = 289
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
            self.state = 290
            self.factor()
            gen.exitTermino()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LilaParser.MULTIPLICATION or _la==LilaParser.DIVISION:
                self.state = 296
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LilaParser.MULTIPLICATION]:
                    self.state = 292
                    self.match(LilaParser.MULTIPLICATION)
                    gen.addOperator('*')
                    pass
                elif token in [LilaParser.DIVISION]:
                    self.state = 294
                    self.match(LilaParser.DIVISION)
                    gen.addOperator('/')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 298
                self.factor()
                gen.exitTermino()
                self.state = 305
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
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.OPEN_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(LilaParser.OPEN_PARENTHESIS)
                gen.addOperator('(')
                self.state = 308
                self.expresion()
                self.state = 309
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                pass
            elif token in [LilaParser.PLUS, LilaParser.MINUS, LilaParser.CTE_INT, LilaParser.CTE_STRING, LilaParser.CTE_F, LilaParser.CTE_BOOL, LilaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.PLUS or _la==LilaParser.MINUS:
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==LilaParser.PLUS or _la==LilaParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 315
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
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                localctx._ID = self.match(LilaParser.ID)
                self.state = 319
                self.match(LilaParser.OPEN_PARENTHESIS)
                Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
                Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), False)
                gen.era((None if localctx._ID is None else localctx._ID.text))
                gen.addOperator('(')
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                    self.state = 324
                    self.expresion()
                    gen.params()
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LilaParser.COMMA:
                        self.state = 326
                        self.match(LilaParser.COMMA)
                        self.state = 327
                        self.expresion()
                        gen.params()
                        self.state = 334
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                gen.goSub((None if localctx._ID is None else localctx._ID.text))
                self.state = 338
                self.match(LilaParser.CLOSE_PARENTHESIS)
                gen.finParentesis()
                gen.addFunct(Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                localctx._ID = self.match(LilaParser.ID)
                gen.addVar(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.OPEN_BRACKET:
                    self.state = 343
                    self.match(LilaParser.OPEN_BRACKET)
                    self.state = 344
                    self.exp()
                    self.state = 345
                    self.match(LilaParser.CLOSE_BRACKET)
                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                localctx._CTE_INT = self.match(LilaParser.CTE_INT)
                gen.addConst(Operand(None,'int',(None if localctx._CTE_INT is None else localctx._CTE_INT.text)))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                localctx._CTE_F = self.match(LilaParser.CTE_F)
                gen.addConst(Operand(None,'num',(None if localctx._CTE_F is None else localctx._CTE_F.text)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                localctx._CTE_STRING = self.match(LilaParser.CTE_STRING)
                gen.addConst(Operand(None,'text',(None if localctx._CTE_STRING is None else localctx._CTE_STRING.text)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 358
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
            self.state = 362
            self.match(LilaParser.WHILE)
            gen.swhile()
            self.state = 364
            self.expresion()
            gen.checkExpresion()
            self.state = 366
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
            self.state = 369
            localctx._ID = self.match(LilaParser.ID)
            self.state = 370
            self.match(LilaParser.OPEN_PARENTHESIS)
            Semantic.look_for_function((None if localctx._ID is None else localctx._ID.text))
            Semantic.isVoid((None if localctx._ID is None else localctx._ID.text), True)
            gen.era((None if localctx._ID is None else localctx._ID.text))
            gen.addOperator('(')
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.OPEN_PARENTHESIS) | (1 << LilaParser.PLUS) | (1 << LilaParser.MINUS) | (1 << LilaParser.CTE_INT) | (1 << LilaParser.CTE_STRING) | (1 << LilaParser.CTE_F) | (1 << LilaParser.CTE_BOOL) | (1 << LilaParser.ID))) != 0):
                self.state = 375
                self.expresion()
                gen.params()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LilaParser.COMMA:
                    self.state = 377
                    self.match(LilaParser.COMMA)
                    self.state = 378
                    self.expresion()
                    gen.params()
                    self.state = 385
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            gen.goSub((None if localctx._ID is None else localctx._ID.text))
            self.state = 389
            self.match(LilaParser.CLOSE_PARENTHESIS)
            gen.finParentesis()
            self.state = 391
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
            self.state = 393
            self.match(LilaParser.GETINPUT)
            self.state = 394
            self.match(LilaParser.OPEN_PARENTHESIS)
            self.state = 395
            localctx._ID = self.match(LilaParser.ID)
            gen.getinput(Semantic.look_for_variable((None if localctx._ID is None else localctx._ID.text)))
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LilaParser.COMMA:
                self.state = 397
                self.match(LilaParser.COMMA)
                self.state = 398
                self.match(LilaParser.CTE_STRING)


            self.state = 401
            self.match(LilaParser.CLOSE_PARENTHESIS)
            self.state = 402
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
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LilaParser.GETOUTLIERS, LilaParser.REMOVEOUTLIERS, LilaParser.TELLMEWHATTOUSE, LilaParser.PRINTMEASURES, LilaParser.MEAN, LilaParser.MEDIAN, LilaParser.MODE, LilaParser.RANGE, LilaParser.MIN, LilaParser.MAX, LilaParser.DESESTANDAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LilaParser.GETOUTLIERS) | (1 << LilaParser.REMOVEOUTLIERS) | (1 << LilaParser.TELLMEWHATTOUSE) | (1 << LilaParser.PRINTMEASURES) | (1 << LilaParser.MEAN) | (1 << LilaParser.MEDIAN) | (1 << LilaParser.MODE) | (1 << LilaParser.RANGE) | (1 << LilaParser.MIN) | (1 << LilaParser.MAX) | (1 << LilaParser.DESESTANDAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 405
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 406
                self.match(LilaParser.ID)
                self.state = 407
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 408
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.QUICKSHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(LilaParser.QUICKSHOW)
                self.state = 410
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 411
                self.match(LilaParser.ID)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LilaParser.COMMA:
                    self.state = 412
                    self.match(LilaParser.COMMA)
                    self.state = 413
                    self.match(LilaParser.ID)


                self.state = 416
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 417
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.PEARSONCORRELATION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.match(LilaParser.PEARSONCORRELATION)
                self.state = 419
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 420
                self.match(LilaParser.ID)
                self.state = 421
                self.match(LilaParser.COMMA)
                self.state = 422
                self.match(LilaParser.ID)
                self.state = 423
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 424
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.NORMALDISTRIBUTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 425
                self.match(LilaParser.NORMALDISTRIBUTION)
                self.state = 426
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 427
                self.match(LilaParser.CTE_F)
                self.state = 428
                self.match(LilaParser.COMMA)
                self.state = 429
                self.match(LilaParser.CTE_F)
                self.state = 430
                self.match(LilaParser.COMMA)
                self.state = 431
                self.match(LilaParser.CTE_INT)
                self.state = 432
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 433
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.FILLVALUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 434
                self.match(LilaParser.FILLVALUE)
                self.state = 435
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 436
                self.match(LilaParser.ID)
                self.state = 437
                self.match(LilaParser.COMMA)
                self.state = 438
                self.var_cte()
                self.state = 439
                self.match(LilaParser.COMMA)
                self.state = 440
                self.var_cte()
                self.state = 441
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 442
                self.match(LilaParser.SEMICOLON)
                pass
            elif token in [LilaParser.REMOVEVALUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 444
                self.match(LilaParser.REMOVEVALUE)
                self.state = 445
                self.match(LilaParser.OPEN_PARENTHESIS)
                self.state = 446
                self.match(LilaParser.ID)
                self.state = 447
                self.match(LilaParser.COMMA)
                self.state = 448
                self.var_cte()
                self.state = 449
                self.match(LilaParser.CLOSE_PARENTHESIS)
                self.state = 450
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





