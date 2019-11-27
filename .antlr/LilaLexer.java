// Generated from /Users/lizzie/Documents/GitHub/lila/Lila.g4 by ANTLR 4.7.1

from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Operand, VirtualAddress
gen = IntermediateGenerator()

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LilaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MAIN=1, LILA=2, VOID=3, DISPLAY=4, WHILE=5, FUNC=6, VAR=7, ELSE=8, IF=9, 
		INT=10, NUM=11, TEXT=12, BOOL=13, RETURN=14, GETINPUT=15, OPEN_BRACKET=16, 
		CLOSE_BRACKET=17, OPEN_PARENTHESIS=18, CLOSE_PARENTHESIS=19, OPEN_CURLY=20, 
		CLOSE_CURLY=21, COMMA=22, SEMICOLON=23, PLUS=24, MINUS=25, MULTIPLICATION=26, 
		DIVISION=27, LESS_THAN=28, GREATER_THAN=29, NOTEQUAL=30, EQUALITY=31, 
		EQUAL=32, LESS_THAN_EQUAL=33, GREATER_THAN_EQUAL=34, AND=35, OR=36, CTE_INT=37, 
		CTE_STRING=38, CTE_F=39, CTE_BOOL=40, GETOUTLIERS=41, REMOVEOUTLIERS=42, 
		TELLMEWHATTOUSE=43, PRINTMEASURES=44, MEAN=45, MEDIAN=46, MODE=47, RANGE=48, 
		MIN=49, MAX=50, DESESTANDAR=51, QUICKSHOW=52, PEARSONCORRELATION=53, NORMALDISTRIBUTION=54, 
		FILLVALUE=55, REMOVEVALUE=56, ID=57, WS=58, Comment=59;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"MAIN", "LILA", "VOID", "DISPLAY", "WHILE", "FUNC", "VAR", "ELSE", "IF", 
		"INT", "NUM", "TEXT", "BOOL", "RETURN", "GETINPUT", "OPEN_BRACKET", "CLOSE_BRACKET", 
		"OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_CURLY", "CLOSE_CURLY", 
		"COMMA", "SEMICOLON", "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "LESS_THAN", 
		"GREATER_THAN", "NOTEQUAL", "EQUALITY", "EQUAL", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
		"AND", "OR", "CTE_INT", "CTE_STRING", "CTE_F", "CTE_BOOL", "GETOUTLIERS", 
		"REMOVEOUTLIERS", "TELLMEWHATTOUSE", "PRINTMEASURES", "MEAN", "MEDIAN", 
		"MODE", "RANGE", "MIN", "MAX", "DESESTANDAR", "QUICKSHOW", "PEARSONCORRELATION", 
		"NORMALDISTRIBUTION", "FILLVALUE", "REMOVEVALUE", "ID", "WS", "Comment"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'main'", "'lila'", "'void'", "'display'", "'while'", "'func'", 
		"'var'", "'else'", "'if'", "'int'", "'num'", "'text'", "'bool'", "'return'", 
		"'getinput'", "'['", "']'", "'('", "')'", "'{'", "'}'", "','", "';'", 
		"'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!='", "'=='", "'='", "'<='", 
		"'>='", "'AND'", "'OR'", null, null, null, null, "'getOutliers'", "'removeOutliers'", 
		"'tellMeWhatToUse'", "'printMeasures'", "'mean'", "'median'", "'mode'", 
		"'range'", "'min'", "'max'", "'desEstandar'", "'quickShow'", "'pearsoneCorrelation'", 
		"'normalDistribution'", "'fillValue'", "'removeValue'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "MAIN", "LILA", "VOID", "DISPLAY", "WHILE", "FUNC", "VAR", "ELSE", 
		"IF", "INT", "NUM", "TEXT", "BOOL", "RETURN", "GETINPUT", "OPEN_BRACKET", 
		"CLOSE_BRACKET", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_CURLY", 
		"CLOSE_CURLY", "COMMA", "SEMICOLON", "PLUS", "MINUS", "MULTIPLICATION", 
		"DIVISION", "LESS_THAN", "GREATER_THAN", "NOTEQUAL", "EQUALITY", "EQUAL", 
		"LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "AND", "OR", "CTE_INT", "CTE_STRING", 
		"CTE_F", "CTE_BOOL", "GETOUTLIERS", "REMOVEOUTLIERS", "TELLMEWHATTOUSE", 
		"PRINTMEASURES", "MEAN", "MEDIAN", "MODE", "RANGE", "MIN", "MAX", "DESESTANDAR", 
		"QUICKSHOW", "PEARSONCORRELATION", "NORMALDISTRIBUTION", "FILLVALUE", 
		"REMOVEVALUE", "ID", "WS", "Comment"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public LilaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Lila.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=\u01e1\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\3\2\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f"+
		"\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30"+
		"\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37"+
		"\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\6&\u00fc"+
		"\n&\r&\16&\u00fd\3\'\3\'\3\'\3\'\7\'\u0104\n\'\f\'\16\'\u0107\13\'\3\'"+
		"\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0118\n)\3*\3*\3*\3*\3"+
		"*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3"+
		",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3"+
		"-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60"+
		"\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63"+
		"\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64"+
		"\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66"+
		"\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66"+
		"\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\39\3"+
		"9\39\39\39\39\39\39\39\39\39\39\3:\6:\u01c6\n:\r:\16:\u01c7\3:\7:\u01cb"+
		"\n:\f:\16:\u01ce\13:\3;\6;\u01d1\n;\r;\16;\u01d2\3;\3;\3<\3<\3<\3<\7<"+
		"\u01db\n<\f<\16<\u01de\13<\3<\3<\2\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.["+
		"/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=\3\2\b\3\2$$\6\2\f\f\17\17"+
		"$$^^\4\2\f\f\17\17\3\2c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2\u01e8\2\3\3"+
		"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2"+
		"\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3"+
		"\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2"+
		"%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61"+
		"\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2"+
		"\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I"+
		"\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2"+
		"\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2"+
		"\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o"+
		"\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5~\3\2"+
		"\2\2\7\u0083\3\2\2\2\t\u0088\3\2\2\2\13\u0090\3\2\2\2\r\u0096\3\2\2\2"+
		"\17\u009b\3\2\2\2\21\u009f\3\2\2\2\23\u00a4\3\2\2\2\25\u00a7\3\2\2\2\27"+
		"\u00ab\3\2\2\2\31\u00af\3\2\2\2\33\u00b4\3\2\2\2\35\u00b9\3\2\2\2\37\u00c0"+
		"\3\2\2\2!\u00c9\3\2\2\2#\u00cb\3\2\2\2%\u00cd\3\2\2\2\'\u00cf\3\2\2\2"+
		")\u00d1\3\2\2\2+\u00d3\3\2\2\2-\u00d5\3\2\2\2/\u00d7\3\2\2\2\61\u00d9"+
		"\3\2\2\2\63\u00db\3\2\2\2\65\u00dd\3\2\2\2\67\u00df\3\2\2\29\u00e1\3\2"+
		"\2\2;\u00e3\3\2\2\2=\u00e5\3\2\2\2?\u00e8\3\2\2\2A\u00eb\3\2\2\2C\u00ed"+
		"\3\2\2\2E\u00f0\3\2\2\2G\u00f3\3\2\2\2I\u00f7\3\2\2\2K\u00fb\3\2\2\2M"+
		"\u00ff\3\2\2\2O\u010a\3\2\2\2Q\u0117\3\2\2\2S\u0119\3\2\2\2U\u0125\3\2"+
		"\2\2W\u0134\3\2\2\2Y\u0144\3\2\2\2[\u0152\3\2\2\2]\u0157\3\2\2\2_\u015e"+
		"\3\2\2\2a\u0163\3\2\2\2c\u0169\3\2\2\2e\u016d\3\2\2\2g\u0171\3\2\2\2i"+
		"\u017d\3\2\2\2k\u0187\3\2\2\2m\u019b\3\2\2\2o\u01ae\3\2\2\2q\u01b8\3\2"+
		"\2\2s\u01c5\3\2\2\2u\u01d0\3\2\2\2w\u01d6\3\2\2\2yz\7o\2\2z{\7c\2\2{|"+
		"\7k\2\2|}\7p\2\2}\4\3\2\2\2~\177\7n\2\2\177\u0080\7k\2\2\u0080\u0081\7"+
		"n\2\2\u0081\u0082\7c\2\2\u0082\6\3\2\2\2\u0083\u0084\7x\2\2\u0084\u0085"+
		"\7q\2\2\u0085\u0086\7k\2\2\u0086\u0087\7f\2\2\u0087\b\3\2\2\2\u0088\u0089"+
		"\7f\2\2\u0089\u008a\7k\2\2\u008a\u008b\7u\2\2\u008b\u008c\7r\2\2\u008c"+
		"\u008d\7n\2\2\u008d\u008e\7c\2\2\u008e\u008f\7{\2\2\u008f\n\3\2\2\2\u0090"+
		"\u0091\7y\2\2\u0091\u0092\7j\2\2\u0092\u0093\7k\2\2\u0093\u0094\7n\2\2"+
		"\u0094\u0095\7g\2\2\u0095\f\3\2\2\2\u0096\u0097\7h\2\2\u0097\u0098\7w"+
		"\2\2\u0098\u0099\7p\2\2\u0099\u009a\7e\2\2\u009a\16\3\2\2\2\u009b\u009c"+
		"\7x\2\2\u009c\u009d\7c\2\2\u009d\u009e\7t\2\2\u009e\20\3\2\2\2\u009f\u00a0"+
		"\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3\7g\2\2\u00a3"+
		"\22\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7h\2\2\u00a6\24\3\2\2\2\u00a7"+
		"\u00a8\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\26\3\2\2\2\u00ab"+
		"\u00ac\7p\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7o\2\2\u00ae\30\3\2\2\2\u00af"+
		"\u00b0\7v\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7z\2\2\u00b2\u00b3\7v\2\2"+
		"\u00b3\32\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7"+
		"q\2\2\u00b7\u00b8\7n\2\2\u00b8\34\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb"+
		"\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be"+
		"\u00bf\7p\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7i\2\2\u00c1\u00c2\7g\2\2\u00c2"+
		"\u00c3\7v\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7r\2\2"+
		"\u00c6\u00c7\7w\2\2\u00c7\u00c8\7v\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7]\2"+
		"\2\u00ca\"\3\2\2\2\u00cb\u00cc\7_\2\2\u00cc$\3\2\2\2\u00cd\u00ce\7*\2"+
		"\2\u00ce&\3\2\2\2\u00cf\u00d0\7+\2\2\u00d0(\3\2\2\2\u00d1\u00d2\7}\2\2"+
		"\u00d2*\3\2\2\2\u00d3\u00d4\7\177\2\2\u00d4,\3\2\2\2\u00d5\u00d6\7.\2"+
		"\2\u00d6.\3\2\2\2\u00d7\u00d8\7=\2\2\u00d8\60\3\2\2\2\u00d9\u00da\7-\2"+
		"\2\u00da\62\3\2\2\2\u00db\u00dc\7/\2\2\u00dc\64\3\2\2\2\u00dd\u00de\7"+
		",\2\2\u00de\66\3\2\2\2\u00df\u00e0\7\61\2\2\u00e08\3\2\2\2\u00e1\u00e2"+
		"\7>\2\2\u00e2:\3\2\2\2\u00e3\u00e4\7@\2\2\u00e4<\3\2\2\2\u00e5\u00e6\7"+
		"#\2\2\u00e6\u00e7\7?\2\2\u00e7>\3\2\2\2\u00e8\u00e9\7?\2\2\u00e9\u00ea"+
		"\7?\2\2\u00ea@\3\2\2\2\u00eb\u00ec\7?\2\2\u00ecB\3\2\2\2\u00ed\u00ee\7"+
		">\2\2\u00ee\u00ef\7?\2\2\u00efD\3\2\2\2\u00f0\u00f1\7@\2\2\u00f1\u00f2"+
		"\7?\2\2\u00f2F\3\2\2\2\u00f3\u00f4\7C\2\2\u00f4\u00f5\7P\2\2\u00f5\u00f6"+
		"\7F\2\2\u00f6H\3\2\2\2\u00f7\u00f8\7Q\2\2\u00f8\u00f9\7T\2\2\u00f9J\3"+
		"\2\2\2\u00fa\u00fc\4\62;\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd"+
		"\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00feL\3\2\2\2\u00ff\u0105\t\2\2\2"+
		"\u0100\u0104\n\3\2\2\u0101\u0102\7^\2\2\u0102\u0104\n\4\2\2\u0103\u0100"+
		"\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105"+
		"\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\t\2"+
		"\2\2\u0109N\3\2\2\2\u010a\u010b\5K&\2\u010b\u010c\7\60\2\2\u010c\u010d"+
		"\5K&\2\u010dP\3\2\2\2\u010e\u010f\7V\2\2\u010f\u0110\7T\2\2\u0110\u0111"+
		"\7W\2\2\u0111\u0118\7G\2\2\u0112\u0113\7H\2\2\u0113\u0114\7C\2\2\u0114"+
		"\u0115\7N\2\2\u0115\u0116\7U\2\2\u0116\u0118\7G\2\2\u0117\u010e\3\2\2"+
		"\2\u0117\u0112\3\2\2\2\u0118R\3\2\2\2\u0119\u011a\7i\2\2\u011a\u011b\7"+
		"g\2\2\u011b\u011c\7v\2\2\u011c\u011d\7Q\2\2\u011d\u011e\7w\2\2\u011e\u011f"+
		"\7v\2\2\u011f\u0120\7n\2\2\u0120\u0121\7k\2\2\u0121\u0122\7g\2\2\u0122"+
		"\u0123\7t\2\2\u0123\u0124\7u\2\2\u0124T\3\2\2\2\u0125\u0126\7t\2\2\u0126"+
		"\u0127\7g\2\2\u0127\u0128\7o\2\2\u0128\u0129\7q\2\2\u0129\u012a\7x\2\2"+
		"\u012a\u012b\7g\2\2\u012b\u012c\7Q\2\2\u012c\u012d\7w\2\2\u012d\u012e"+
		"\7v\2\2\u012e\u012f\7n\2\2\u012f\u0130\7k\2\2\u0130\u0131\7g\2\2\u0131"+
		"\u0132\7t\2\2\u0132\u0133\7u\2\2\u0133V\3\2\2\2\u0134\u0135\7v\2\2\u0135"+
		"\u0136\7g\2\2\u0136\u0137\7n\2\2\u0137\u0138\7n\2\2\u0138\u0139\7O\2\2"+
		"\u0139\u013a\7g\2\2\u013a\u013b\7Y\2\2\u013b\u013c\7j\2\2\u013c\u013d"+
		"\7c\2\2\u013d\u013e\7v\2\2\u013e\u013f\7V\2\2\u013f\u0140\7q\2\2\u0140"+
		"\u0141\7W\2\2\u0141\u0142\7u\2\2\u0142\u0143\7g\2\2\u0143X\3\2\2\2\u0144"+
		"\u0145\7r\2\2\u0145\u0146\7t\2\2\u0146\u0147\7k\2\2\u0147\u0148\7p\2\2"+
		"\u0148\u0149\7v\2\2\u0149\u014a\7O\2\2\u014a\u014b\7g\2\2\u014b\u014c"+
		"\7c\2\2\u014c\u014d\7u\2\2\u014d\u014e\7w\2\2\u014e\u014f\7t\2\2\u014f"+
		"\u0150\7g\2\2\u0150\u0151\7u\2\2\u0151Z\3\2\2\2\u0152\u0153\7o\2\2\u0153"+
		"\u0154\7g\2\2\u0154\u0155\7c\2\2\u0155\u0156\7p\2\2\u0156\\\3\2\2\2\u0157"+
		"\u0158\7o\2\2\u0158\u0159\7g\2\2\u0159\u015a\7f\2\2\u015a\u015b\7k\2\2"+
		"\u015b\u015c\7c\2\2\u015c\u015d\7p\2\2\u015d^\3\2\2\2\u015e\u015f\7o\2"+
		"\2\u015f\u0160\7q\2\2\u0160\u0161\7f\2\2\u0161\u0162\7g\2\2\u0162`\3\2"+
		"\2\2\u0163\u0164\7t\2\2\u0164\u0165\7c\2\2\u0165\u0166\7p\2\2\u0166\u0167"+
		"\7i\2\2\u0167\u0168\7g\2\2\u0168b\3\2\2\2\u0169\u016a\7o\2\2\u016a\u016b"+
		"\7k\2\2\u016b\u016c\7p\2\2\u016cd\3\2\2\2\u016d\u016e\7o\2\2\u016e\u016f"+
		"\7c\2\2\u016f\u0170\7z\2\2\u0170f\3\2\2\2\u0171\u0172\7f\2\2\u0172\u0173"+
		"\7g\2\2\u0173\u0174\7u\2\2\u0174\u0175\7G\2\2\u0175\u0176\7u\2\2\u0176"+
		"\u0177\7v\2\2\u0177\u0178\7c\2\2\u0178\u0179\7p\2\2\u0179\u017a\7f\2\2"+
		"\u017a\u017b\7c\2\2\u017b\u017c\7t\2\2\u017ch\3\2\2\2\u017d\u017e\7s\2"+
		"\2\u017e\u017f\7w\2\2\u017f\u0180\7k\2\2\u0180\u0181\7e\2\2\u0181\u0182"+
		"\7m\2\2\u0182\u0183\7U\2\2\u0183\u0184\7j\2\2\u0184\u0185\7q\2\2\u0185"+
		"\u0186\7y\2\2\u0186j\3\2\2\2\u0187\u0188\7r\2\2\u0188\u0189\7g\2\2\u0189"+
		"\u018a\7c\2\2\u018a\u018b\7t\2\2\u018b\u018c\7u\2\2\u018c\u018d\7q\2\2"+
		"\u018d\u018e\7p\2\2\u018e\u018f\7g\2\2\u018f\u0190\7E\2\2\u0190\u0191"+
		"\7q\2\2\u0191\u0192\7t\2\2\u0192\u0193\7t\2\2\u0193\u0194\7g\2\2\u0194"+
		"\u0195\7n\2\2\u0195\u0196\7c\2\2\u0196\u0197\7v\2\2\u0197\u0198\7k\2\2"+
		"\u0198\u0199\7q\2\2\u0199\u019a\7p\2\2\u019al\3\2\2\2\u019b\u019c\7p\2"+
		"\2\u019c\u019d\7q\2\2\u019d\u019e\7t\2\2\u019e\u019f\7o\2\2\u019f\u01a0"+
		"\7c\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2\7F\2\2\u01a2\u01a3\7k\2\2\u01a3"+
		"\u01a4\7u\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6\7t\2\2\u01a6\u01a7\7k\2\2"+
		"\u01a7\u01a8\7d\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab"+
		"\7k\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad\7p\2\2\u01adn\3\2\2\2\u01ae\u01af"+
		"\7h\2\2\u01af\u01b0\7k\2\2\u01b0\u01b1\7n\2\2\u01b1\u01b2\7n\2\2\u01b2"+
		"\u01b3\7X\2\2\u01b3\u01b4\7c\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6\7w\2\2"+
		"\u01b6\u01b7\7g\2\2\u01b7p\3\2\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7g\2"+
		"\2\u01ba\u01bb\7o\2\2\u01bb\u01bc\7q\2\2\u01bc\u01bd\7x\2\2\u01bd\u01be"+
		"\7g\2\2\u01be\u01bf\7X\2\2\u01bf\u01c0\7c\2\2\u01c0\u01c1\7n\2\2\u01c1"+
		"\u01c2\7w\2\2\u01c2\u01c3\7g\2\2\u01c3r\3\2\2\2\u01c4\u01c6\t\5\2\2\u01c5"+
		"\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2"+
		"\2\2\u01c8\u01cc\3\2\2\2\u01c9\u01cb\t\6\2\2\u01ca\u01c9\3\2\2\2\u01cb"+
		"\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cdt\3\2\2\2"+
		"\u01ce\u01cc\3\2\2\2\u01cf\u01d1\t\7\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2"+
		"\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4"+
		"\u01d5\b;\2\2\u01d5v\3\2\2\2\u01d6\u01d7\7\61\2\2\u01d7\u01d8\7\61\2\2"+
		"\u01d8\u01dc\3\2\2\2\u01d9\u01db\n\4\2\2\u01da\u01d9\3\2\2\2\u01db\u01de"+
		"\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de"+
		"\u01dc\3\2\2\2\u01df\u01e0\b<\2\2\u01e0x\3\2\2\2\13\2\u00fd\u0103\u0105"+
		"\u0117\u01c7\u01cc\u01d2\u01dc\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}