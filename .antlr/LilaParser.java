// Generated from /Users/lizzie/Documents/GitHub/lila/Lila.g4 by ANTLR 4.7.1

from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Operand, VirtualAddress
gen = IntermediateGenerator()

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LilaParser extends Parser {
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
	public static final int
		RULE_programa = 0, RULE_data = 1, RULE_data2 = 2, RULE_main = 3, RULE_array = 4, 
		RULE_tipo = 5, RULE_funciones = 6, RULE_params = 7, RULE_estatuto = 8, 
		RULE_condicion = 9, RULE_bloque = 10, RULE_display = 11, RULE_asignacion = 12, 
		RULE_sreturn = 13, RULE_arr = 14, RULE_expresion = 15, RULE_comparacion = 16, 
		RULE_exp = 17, RULE_termino = 18, RULE_factor = 19, RULE_var_cte = 20, 
		RULE_swhile = 21, RULE_invocacion = 22, RULE_getinput = 23, RULE_especiales = 24;
	public static final String[] ruleNames = {
		"programa", "data", "data2", "main", "array", "tipo", "funciones", "params", 
		"estatuto", "condicion", "bloque", "display", "asignacion", "sreturn", 
		"arr", "expresion", "comparacion", "exp", "termino", "factor", "var_cte", 
		"swhile", "invocacion", "getinput", "especiales"
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

	@Override
	public String getGrammarFileName() { return "Lila.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LilaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode LILA() { return getToken(LilaParser.LILA, 0); }
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public List<FuncionesContext> funciones() {
			return getRuleContexts(FuncionesContext.class);
		}
		public FuncionesContext funciones(int i) {
			return getRuleContext(FuncionesContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(LILA);
			setState(51);
			match(ID);
			gen.goTo()
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(53);
				data();
				}
			}

			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNC) {
				{
				{
				setState(56);
				funciones();
				}
				}
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			gen.conditionEnd()
			setState(63);
			main();
			gen.end()
			gen.test_final()
			return gen.getObj()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DataContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(LilaParser.VAR, 0); }
		public List<Data2Context> data2() {
			return getRuleContexts(Data2Context.class);
		}
		public Data2Context data2(int i) {
			return getRuleContext(Data2Context.class,i);
		}
		public DataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data; }
	}

	public final DataContext data() throws RecognitionException {
		DataContext _localctx = new DataContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_data);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(VAR);
			setState(70); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(69);
				data2();
				}
				}
				setState(72); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0) );
			Semantic.isGlobal = False
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Data2Context extends ParserRuleContext {
		public TipoContext tipo;
		public Token ID;
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(LilaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LilaParser.ID, i);
		}
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public List<ArrayContext> array() {
			return getRuleContexts(ArrayContext.class);
		}
		public ArrayContext array(int i) {
			return getRuleContext(ArrayContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public Data2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data2; }
	}

	public final Data2Context data2() throws RecognitionException {
		Data2Context _localctx = new Data2Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_data2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			((Data2Context)_localctx).tipo = tipo();
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACKET) {
				{
				{
				setState(77);
				array();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			((Data2Context)_localctx).ID = match(ID);
			Semantic.add_var(Operand((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(85);
				match(COMMA);
				setState(86);
				((Data2Context)_localctx).ID = match(ID);
				Semantic.add_var(Operand((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(93);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(LilaParser.MAIN, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(MAIN);
			gen.contextChange()
			setState(97);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(LilaParser.OPEN_BRACKET, 0); }
		public TerminalNode CTE_INT() { return getToken(LilaParser.CTE_INT, 0); }
		public TerminalNode CLOSE_BRACKET() { return getToken(LilaParser.CLOSE_BRACKET, 0); }
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(OPEN_BRACKET);
			setState(100);
			match(CTE_INT);
			setState(101);
			match(CLOSE_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(LilaParser.INT, 0); }
		public TerminalNode NUM() { return getToken(LilaParser.NUM, 0); }
		public TerminalNode TEXT() { return getToken(LilaParser.TEXT, 0); }
		public TerminalNode BOOL() { return getToken(LilaParser.BOOL, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncionesContext extends ParserRuleContext {
		public TipoContext tipo;
		public Token VOID;
		public Token ID;
		public TerminalNode FUNC() { return getToken(LilaParser.FUNC, 0); }
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode OPEN_CURLY() { return getToken(LilaParser.OPEN_CURLY, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(LilaParser.CLOSE_CURLY, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VOID() { return getToken(LilaParser.VOID, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public FuncionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funciones; }
	}

	public final FuncionesContext funciones() throws RecognitionException {
		FuncionesContext _localctx = new FuncionesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(FUNC);
			setState(108);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case NUM:
			case TEXT:
			case BOOL:
				{
				setState(106);
				((FuncionesContext)_localctx).tipo = tipo();
				}
				break;
			case VOID:
				{
				setState(107);
				((FuncionesContext)_localctx).VOID = match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(110);
			((FuncionesContext)_localctx).ID = match(ID);
			index = len(gen.Quadruples)
			Semantic.enterFunciones((((FuncionesContext)_localctx).ID!=null?((FuncionesContext)_localctx).ID.getText():null),(((FuncionesContext)_localctx).tipo!=null?_input.getText(((FuncionesContext)_localctx).tipo.start,((FuncionesContext)_localctx).tipo.stop):null),(((FuncionesContext)_localctx).VOID!=null?((FuncionesContext)_localctx).VOID.getText():null),index)
			gen.contextChange()
			setState(114);
			match(OPEN_PARENTHESIS);
			setState(116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0)) {
				{
				setState(115);
				params();
				}
			}

			setState(118);
			match(CLOSE_PARENTHESIS);
			setState(119);
			match(OPEN_CURLY);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(120);
				data();
				}
			}

			setState(124); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(123);
				estatuto();
				}
				}
				setState(126); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0) );
			setState(128);
			match(CLOSE_CURLY);
			gen.endProc()
			Semantic.end_function()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public TipoContext tipo;
		public Token ID;
		public List<TipoContext> tipo() {
			return getRuleContexts(TipoContext.class);
		}
		public TipoContext tipo(int i) {
			return getRuleContext(TipoContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(LilaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LilaParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			((ParamsContext)_localctx).tipo = tipo();
			setState(133);
			((ParamsContext)_localctx).ID = match(ID);
			Semantic.add_param(Operand((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),None))
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(135);
				match(COMMA);
				setState(136);
				((ParamsContext)_localctx).tipo = tipo();
				setState(137);
				((ParamsContext)_localctx).ID = match(ID);
				Semantic.add_param(Operand((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),None))
				}
				}
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EstatutoContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public SwhileContext swhile() {
			return getRuleContext(SwhileContext.class,0);
		}
		public DisplayContext display() {
			return getRuleContext(DisplayContext.class,0);
		}
		public GetinputContext getinput() {
			return getRuleContext(GetinputContext.class,0);
		}
		public InvocacionContext invocacion() {
			return getRuleContext(InvocacionContext.class,0);
		}
		public SreturnContext sreturn() {
			return getRuleContext(SreturnContext.class,0);
		}
		public EspecialesContext especiales() {
			return getRuleContext(EspecialesContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_estatuto);
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				swhile();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(148);
				display();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(149);
				getinput();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(150);
				invocacion();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(151);
				sreturn();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(152);
				especiales();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(LilaParser.IF, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TerminalNode ELSE() { return getToken(LilaParser.ELSE, 0); }
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_condicion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(IF);
			setState(156);
			expresion();
			gen.checkExpresion()
			setState(158);
			bloque();
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(159);
				match(ELSE);
				gen.conditionElse()
				setState(161);
				bloque();
				}
			}

			setState(164);
			match(SEMICOLON);
			gen.conditionEnd()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode OPEN_CURLY() { return getToken(LilaParser.OPEN_CURLY, 0); }
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public TerminalNode CLOSE_CURLY() { return getToken(LilaParser.CLOSE_CURLY, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(OPEN_CURLY);
			setState(168);
			estatuto();
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0)) {
				{
				{
				setState(169);
				estatuto();
				}
				}
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(175);
			match(CLOSE_CURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DisplayContext extends ParserRuleContext {
		public TerminalNode DISPLAY() { return getToken(LilaParser.DISPLAY, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public DisplayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_display; }
	}

	public final DisplayContext display() throws RecognitionException {
		DisplayContext _localctx = new DisplayContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_display);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(DISPLAY);
			setState(178);
			match(OPEN_PARENTHESIS);
			setState(179);
			expresion();
			gen.display()
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(181);
				match(COMMA);
				setState(182);
				expresion();
				gen.display()
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(190);
			match(CLOSE_PARENTHESIS);
			setState(191);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AsignacionContext extends ParserRuleContext {
		public Token ID;
		public Token EQUAL;
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(LilaParser.EQUAL, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ArrContext arr() {
			return getRuleContext(ArrContext.class,0);
		}
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_asignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			((AsignacionContext)_localctx).ID = match(ID);
			gen.addVar(Semantic.look_for_variable((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACKET) {
				{
				{
				setState(195);
				match(OPEN_BRACKET);
				setState(196);
				exp();
				setState(197);
				match(CLOSE_BRACKET);
				}
				}
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(204);
			((AsignacionContext)_localctx).EQUAL = match(EQUAL);
			gen.addOperator((((AsignacionContext)_localctx).EQUAL!=null?((AsignacionContext)_localctx).EQUAL.getText():null))
			setState(210);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PARENTHESIS:
			case PLUS:
			case MINUS:
			case CTE_INT:
			case CTE_STRING:
			case CTE_F:
			case CTE_BOOL:
			case ID:
				{
				setState(206);
				expresion();
				gen.assign()
				}
				break;
			case OPEN_BRACKET:
				{
				setState(209);
				arr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(212);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SreturnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(LilaParser.RETURN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public SreturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sreturn; }
	}

	public final SreturnContext sreturn() throws RecognitionException {
		SreturnContext _localctx = new SreturnContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_sreturn);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(RETURN);
			setState(215);
			expresion();
			Semantic.checkReturn(gen.top_variables())
			gen.func_return()
			setState(218);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrContext extends ParserRuleContext {
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<Var_cteContext> var_cte() {
			return getRuleContexts(Var_cteContext.class);
		}
		public Var_cteContext var_cte(int i) {
			return getRuleContext(Var_cteContext.class,i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public ArrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr; }
	}

	public final ArrContext arr() throws RecognitionException {
		ArrContext _localctx = new ArrContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_arr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(OPEN_BRACKET);
			setState(221);
			var_cte();
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(222);
				match(COMMA);
				setState(223);
				var_cte();
				}
				}
				setState(228);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(229);
			match(CLOSE_BRACKET);
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(230);
				match(COMMA);
				setState(231);
				match(OPEN_BRACKET);
				setState(232);
				var_cte();
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(233);
					match(COMMA);
					setState(234);
					var_cte();
					}
					}
					setState(239);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(240);
				match(CLOSE_BRACKET);
				}
				}
				setState(246);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpresionContext extends ParserRuleContext {
		public List<ComparacionContext> comparacion() {
			return getRuleContexts(ComparacionContext.class);
		}
		public ComparacionContext comparacion(int i) {
			return getRuleContext(ComparacionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(LilaParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(LilaParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(LilaParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(LilaParser.OR, i);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			comparacion();
			gen.exitExpresion()
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(253);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(249);
					match(AND);
					gen.addOperator('AND')
					}
					break;
				case OR:
					{
					setState(251);
					match(OR);
					gen.addOperator('OR')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(255);
				comparacion();
				gen.exitExpresion()
				}
				}
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparacionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode GREATER_THAN() { return getToken(LilaParser.GREATER_THAN, 0); }
		public TerminalNode LESS_THAN() { return getToken(LilaParser.LESS_THAN, 0); }
		public TerminalNode NOTEQUAL() { return getToken(LilaParser.NOTEQUAL, 0); }
		public TerminalNode EQUALITY() { return getToken(LilaParser.EQUALITY, 0); }
		public TerminalNode GREATER_THAN_EQUAL() { return getToken(LilaParser.GREATER_THAN_EQUAL, 0); }
		public TerminalNode LESS_THAN_EQUAL() { return getToken(LilaParser.LESS_THAN_EQUAL, 0); }
		public ComparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacion; }
	}

	public final ComparacionContext comparacion() throws RecognitionException {
		ComparacionContext _localctx = new ComparacionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_comparacion);
		try {
			setState(282);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				exp();
				setState(276);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GREATER_THAN:
					{
					setState(264);
					match(GREATER_THAN);
					gen.addOperator('>')
					}
					break;
				case LESS_THAN:
					{
					setState(266);
					match(LESS_THAN);
					gen.addOperator('<')
					}
					break;
				case NOTEQUAL:
					{
					setState(268);
					match(NOTEQUAL);
					gen.addOperator('!=')
					}
					break;
				case EQUALITY:
					{
					setState(270);
					match(EQUALITY);
					gen.addOperator('==')
					}
					break;
				case GREATER_THAN_EQUAL:
					{
					setState(272);
					match(GREATER_THAN_EQUAL);
					gen.addOperator('>=')
					}
					break;
				case LESS_THAN_EQUAL:
					{
					setState(274);
					match(LESS_THAN_EQUAL);
					gen.addOperator('<=')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(278);
				exp();
				gen.exitComparacion()
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(281);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(LilaParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(LilaParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(LilaParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(LilaParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			termino();
			gen.exitExp()
			setState(297);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(290);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(286);
					match(PLUS);
					gen.addOperator('+')
					}
					break;
				case MINUS:
					{
					setState(288);
					match(MINUS);
					gen.addOperator('-')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(292);
				termino();
				gen.exitExp()
				}
				}
				setState(299);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULTIPLICATION() { return getTokens(LilaParser.MULTIPLICATION); }
		public TerminalNode MULTIPLICATION(int i) {
			return getToken(LilaParser.MULTIPLICATION, i);
		}
		public List<TerminalNode> DIVISION() { return getTokens(LilaParser.DIVISION); }
		public TerminalNode DIVISION(int i) {
			return getToken(LilaParser.DIVISION, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			factor();
			gen.exitTermino()
			setState(313);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULTIPLICATION || _la==DIVISION) {
				{
				{
				setState(306);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(302);
					match(MULTIPLICATION);
					gen.addOperator('*')
					}
					break;
				case DIVISION:
					{
					setState(304);
					match(DIVISION);
					gen.addOperator('/')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(308);
				factor();
				gen.exitTermino()
				}
				}
				setState(315);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public Token MINUS;
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public Var_cteContext var_cte() {
			return getRuleContext(Var_cteContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(LilaParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(LilaParser.MINUS, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_factor);
		try {
			setState(330);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PARENTHESIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				match(OPEN_PARENTHESIS);
				gen.addOperator('(')
				setState(318);
				expresion();
				setState(319);
				match(CLOSE_PARENTHESIS);
				gen.finParentesis()
				}
				break;
			case PLUS:
			case MINUS:
			case CTE_INT:
			case CTE_STRING:
			case CTE_F:
			case CTE_BOOL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(322);
					match(PLUS);
					}
					break;
				case MINUS:
					{
					setState(323);
					((FactorContext)_localctx).MINUS = match(MINUS);
					gen.isNegative()
					}
					break;
				case CTE_INT:
				case CTE_STRING:
				case CTE_F:
				case CTE_BOOL:
				case ID:
					break;
				default:
					break;
				}
				setState(327);
				var_cte();
				gen.makeNegative((((FactorContext)_localctx).MINUS!=null?((FactorContext)_localctx).MINUS.getText():null))
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_cteContext extends ParserRuleContext {
		public Token ID;
		public Token CTE_INT;
		public Token CTE_F;
		public Token CTE_STRING;
		public Token CTE_BOOL;
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public TerminalNode CTE_INT() { return getToken(LilaParser.CTE_INT, 0); }
		public TerminalNode CTE_F() { return getToken(LilaParser.CTE_F, 0); }
		public TerminalNode CTE_STRING() { return getToken(LilaParser.CTE_STRING, 0); }
		public TerminalNode CTE_BOOL() { return getToken(LilaParser.CTE_BOOL, 0); }
		public Var_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_cte; }
	}

	public final Var_cteContext var_cte() throws RecognitionException {
		Var_cteContext _localctx = new Var_cteContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_var_cte);
		int _la;
		try {
			setState(376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(332);
				((Var_cteContext)_localctx).ID = match(ID);
				setState(333);
				match(OPEN_PARENTHESIS);
				gen.incoming_Params()
				Semantic.look_for_function((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				Semantic.isVoid((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null), False)
				gen.era((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.addOperator('(')
				setState(350);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OPEN_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_STRING) | (1L << CTE_F) | (1L << CTE_BOOL) | (1L << ID))) != 0)) {
					{
					setState(339);
					expresion();
					gen.params()
					setState(347);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(341);
						match(COMMA);
						setState(342);
						expresion();
						gen.params()
						}
						}
						setState(349);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				gen.goSub((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				setState(353);
				match(CLOSE_PARENTHESIS);
				gen.check_params((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.finParentesis()
				gen.addFunct(Semantic.look_for_function((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				((Var_cteContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				setState(365);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==OPEN_BRACKET) {
					{
					{
					setState(359);
					match(OPEN_BRACKET);
					setState(360);
					exp();
					setState(361);
					match(CLOSE_BRACKET);
					}
					}
					setState(367);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(368);
				((Var_cteContext)_localctx).CTE_INT = match(CTE_INT);
				gen.addConst(Operand(None,'int',(((Var_cteContext)_localctx).CTE_INT!=null?((Var_cteContext)_localctx).CTE_INT.getText():null)))
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(370);
				((Var_cteContext)_localctx).CTE_F = match(CTE_F);
				gen.addConst(Operand(None,'num',(((Var_cteContext)_localctx).CTE_F!=null?((Var_cteContext)_localctx).CTE_F.getText():null)))
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(372);
				((Var_cteContext)_localctx).CTE_STRING = match(CTE_STRING);
				gen.addConst(Operand(None,'text',(((Var_cteContext)_localctx).CTE_STRING!=null?((Var_cteContext)_localctx).CTE_STRING.getText():null)))
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(374);
				((Var_cteContext)_localctx).CTE_BOOL = match(CTE_BOOL);
				gen.addConst(Operand(None,'bool',(((Var_cteContext)_localctx).CTE_BOOL!=null?((Var_cteContext)_localctx).CTE_BOOL.getText():null)))
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(LilaParser.WHILE, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public SwhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_swhile; }
	}

	public final SwhileContext swhile() throws RecognitionException {
		SwhileContext _localctx = new SwhileContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_swhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			match(WHILE);
			gen.swhile()
			setState(380);
			expresion();
			gen.checkExpresion()
			setState(382);
			bloque();
			gen.whileEnd()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InvocacionContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public InvocacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_invocacion; }
	}

	public final InvocacionContext invocacion() throws RecognitionException {
		InvocacionContext _localctx = new InvocacionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_invocacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(385);
			((InvocacionContext)_localctx).ID = match(ID);
			setState(386);
			match(OPEN_PARENTHESIS);
			gen.incoming_Params()
			Semantic.look_for_function((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			Semantic.isVoid((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null), True)
			gen.era((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			gen.addOperator('(')
			setState(403);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OPEN_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_STRING) | (1L << CTE_F) | (1L << CTE_BOOL) | (1L << ID))) != 0)) {
				{
				setState(392);
				expresion();
				gen.params()
				setState(400);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(394);
					match(COMMA);
					setState(395);
					expresion();
					gen.params()
					}
					}
					setState(402);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			gen.goSub((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			setState(406);
			match(CLOSE_PARENTHESIS);
			gen.check_params((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			gen.finParentesis()
			setState(409);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GetinputContext extends ParserRuleContext {
		public Token ID;
		public Token CTE_STRING;
		public TerminalNode GETINPUT() { return getToken(LilaParser.GETINPUT, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TerminalNode COMMA() { return getToken(LilaParser.COMMA, 0); }
		public TerminalNode CTE_STRING() { return getToken(LilaParser.CTE_STRING, 0); }
		public GetinputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_getinput; }
	}

	public final GetinputContext getinput() throws RecognitionException {
		GetinputContext _localctx = new GetinputContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_getinput);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(411);
			match(GETINPUT);
			setState(412);
			match(OPEN_PARENTHESIS);
			setState(413);
			((GetinputContext)_localctx).ID = match(ID);
			setState(416);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(414);
				match(COMMA);
				setState(415);
				((GetinputContext)_localctx).CTE_STRING = match(CTE_STRING);
				}
			}

			gen.getinput(Semantic.look_for_variable((((GetinputContext)_localctx).ID!=null?((GetinputContext)_localctx).ID.getText():null)), (((GetinputContext)_localctx).CTE_STRING!=null?((GetinputContext)_localctx).CTE_STRING.getText():null))
			setState(419);
			match(CLOSE_PARENTHESIS);
			setState(420);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EspecialesContext extends ParserRuleContext {
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public List<TerminalNode> ID() { return getTokens(LilaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LilaParser.ID, i);
		}
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TerminalNode GETOUTLIERS() { return getToken(LilaParser.GETOUTLIERS, 0); }
		public TerminalNode REMOVEOUTLIERS() { return getToken(LilaParser.REMOVEOUTLIERS, 0); }
		public TerminalNode TELLMEWHATTOUSE() { return getToken(LilaParser.TELLMEWHATTOUSE, 0); }
		public TerminalNode PRINTMEASURES() { return getToken(LilaParser.PRINTMEASURES, 0); }
		public TerminalNode MEAN() { return getToken(LilaParser.MEAN, 0); }
		public TerminalNode MEDIAN() { return getToken(LilaParser.MEDIAN, 0); }
		public TerminalNode MODE() { return getToken(LilaParser.MODE, 0); }
		public TerminalNode RANGE() { return getToken(LilaParser.RANGE, 0); }
		public TerminalNode MIN() { return getToken(LilaParser.MIN, 0); }
		public TerminalNode MAX() { return getToken(LilaParser.MAX, 0); }
		public TerminalNode DESESTANDAR() { return getToken(LilaParser.DESESTANDAR, 0); }
		public TerminalNode QUICKSHOW() { return getToken(LilaParser.QUICKSHOW, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public TerminalNode PEARSONCORRELATION() { return getToken(LilaParser.PEARSONCORRELATION, 0); }
		public TerminalNode NORMALDISTRIBUTION() { return getToken(LilaParser.NORMALDISTRIBUTION, 0); }
		public List<TerminalNode> CTE_F() { return getTokens(LilaParser.CTE_F); }
		public TerminalNode CTE_F(int i) {
			return getToken(LilaParser.CTE_F, i);
		}
		public TerminalNode CTE_INT() { return getToken(LilaParser.CTE_INT, 0); }
		public TerminalNode FILLVALUE() { return getToken(LilaParser.FILLVALUE, 0); }
		public List<Var_cteContext> var_cte() {
			return getRuleContexts(Var_cteContext.class);
		}
		public Var_cteContext var_cte(int i) {
			return getRuleContext(Var_cteContext.class,i);
		}
		public TerminalNode REMOVEVALUE() { return getToken(LilaParser.REMOVEVALUE, 0); }
		public EspecialesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_especiales; }
	}

	public final EspecialesContext especiales() throws RecognitionException {
		EspecialesContext _localctx = new EspecialesContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_especiales);
		int _la;
		try {
			setState(470);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GETOUTLIERS:
			case REMOVEOUTLIERS:
			case TELLMEWHATTOUSE:
			case PRINTMEASURES:
			case MEAN:
			case MEDIAN:
			case MODE:
			case RANGE:
			case MIN:
			case MAX:
			case DESESTANDAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(422);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(423);
				match(OPEN_PARENTHESIS);
				setState(424);
				match(ID);
				setState(425);
				match(CLOSE_PARENTHESIS);
				setState(426);
				match(SEMICOLON);
				}
				break;
			case QUICKSHOW:
				enterOuterAlt(_localctx, 2);
				{
				setState(427);
				match(QUICKSHOW);
				setState(428);
				match(OPEN_PARENTHESIS);
				setState(429);
				match(ID);
				setState(432);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(430);
					match(COMMA);
					setState(431);
					match(ID);
					}
				}

				setState(434);
				match(CLOSE_PARENTHESIS);
				setState(435);
				match(SEMICOLON);
				}
				break;
			case PEARSONCORRELATION:
				enterOuterAlt(_localctx, 3);
				{
				setState(436);
				match(PEARSONCORRELATION);
				setState(437);
				match(OPEN_PARENTHESIS);
				setState(438);
				match(ID);
				setState(439);
				match(COMMA);
				setState(440);
				match(ID);
				setState(441);
				match(CLOSE_PARENTHESIS);
				setState(442);
				match(SEMICOLON);
				}
				break;
			case NORMALDISTRIBUTION:
				enterOuterAlt(_localctx, 4);
				{
				setState(443);
				match(NORMALDISTRIBUTION);
				setState(444);
				match(OPEN_PARENTHESIS);
				setState(445);
				match(CTE_F);
				setState(446);
				match(COMMA);
				setState(447);
				match(CTE_F);
				setState(448);
				match(COMMA);
				setState(449);
				match(CTE_INT);
				setState(450);
				match(CLOSE_PARENTHESIS);
				setState(451);
				match(SEMICOLON);
				}
				break;
			case FILLVALUE:
				enterOuterAlt(_localctx, 5);
				{
				setState(452);
				match(FILLVALUE);
				setState(453);
				match(OPEN_PARENTHESIS);
				setState(454);
				match(ID);
				setState(455);
				match(COMMA);
				setState(456);
				var_cte();
				setState(457);
				match(COMMA);
				setState(458);
				var_cte();
				setState(459);
				match(CLOSE_PARENTHESIS);
				setState(460);
				match(SEMICOLON);
				}
				break;
			case REMOVEVALUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(462);
				match(REMOVEVALUE);
				setState(463);
				match(OPEN_PARENTHESIS);
				setState(464);
				match(ID);
				setState(465);
				match(COMMA);
				setState(466);
				var_cte();
				setState(467);
				match(CLOSE_PARENTHESIS);
				setState(468);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=\u01db\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\5\29\n\2\3\2\7\2<\n\2\f\2\16\2?\13\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3I\n\3\r\3\16\3J\3\3\3\3\3\4\3\4\7\4Q\n\4"+
		"\f\4\16\4T\13\4\3\4\3\4\3\4\3\4\3\4\7\4[\n\4\f\4\16\4^\13\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\bo\n\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\5\bw\n\b\3\b\3\b\3\b\5\b|\n\b\3\b\6\b\177\n\b\r\b\16\b"+
		"\u0080\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u008f\n\t\f"+
		"\t\16\t\u0092\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009c\n\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a5\n\13\3\13\3\13\3\13\3\f\3\f"+
		"\3\f\7\f\u00ad\n\f\f\f\16\f\u00b0\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\7\r\u00bc\n\r\f\r\16\r\u00bf\13\r\3\r\3\r\3\r\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\7\16\u00ca\n\16\f\16\16\16\u00cd\13\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\5\16\u00d5\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\7\20\u00e3\n\20\f\20\16\20\u00e6\13\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\7\20\u00ee\n\20\f\20\16\20\u00f1\13\20\3\20\3\20"+
		"\7\20\u00f5\n\20\f\20\16\20\u00f8\13\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\u0100\n\21\3\21\3\21\3\21\7\21\u0105\n\21\f\21\16\21\u0108\13\21"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22"+
		"\u0117\n\22\3\22\3\22\3\22\3\22\5\22\u011d\n\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\5\23\u0125\n\23\3\23\3\23\3\23\7\23\u012a\n\23\f\23\16\23\u012d"+
		"\13\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0135\n\24\3\24\3\24\3\24\7"+
		"\24\u013a\n\24\f\24\16\24\u013d\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\5\25\u0148\n\25\3\25\3\25\3\25\5\25\u014d\n\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u015c\n\26"+
		"\f\26\16\26\u015f\13\26\5\26\u0161\n\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\7\26\u016e\n\26\f\26\16\26\u0171\13\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u017b\n\26\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\7\30\u0191\n\30\f\30\16\30\u0194\13\30\5\30\u0196\n\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u01a3\n\31\3\31"+
		"\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32"+
		"\u01b3\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u01d9\n\32\3\32"+
		"\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\4\3\2"+
		"\f\17\3\2+\65\2\u01fa\2\64\3\2\2\2\4F\3\2\2\2\6N\3\2\2\2\ba\3\2\2\2\n"+
		"e\3\2\2\2\fi\3\2\2\2\16k\3\2\2\2\20\u0086\3\2\2\2\22\u009b\3\2\2\2\24"+
		"\u009d\3\2\2\2\26\u00a9\3\2\2\2\30\u00b3\3\2\2\2\32\u00c3\3\2\2\2\34\u00d8"+
		"\3\2\2\2\36\u00de\3\2\2\2 \u00f9\3\2\2\2\"\u011c\3\2\2\2$\u011e\3\2\2"+
		"\2&\u012e\3\2\2\2(\u014c\3\2\2\2*\u017a\3\2\2\2,\u017c\3\2\2\2.\u0183"+
		"\3\2\2\2\60\u019d\3\2\2\2\62\u01d8\3\2\2\2\64\65\7\4\2\2\65\66\7;\2\2"+
		"\668\b\2\1\2\679\5\4\3\28\67\3\2\2\289\3\2\2\29=\3\2\2\2:<\5\16\b\2;:"+
		"\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\b\2\1\2A"+
		"B\5\b\5\2BC\b\2\1\2CD\b\2\1\2DE\b\2\1\2E\3\3\2\2\2FH\7\t\2\2GI\5\6\4\2"+
		"HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\b\3\1\2M\5\3\2\2"+
		"\2NR\5\f\7\2OQ\5\n\6\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2"+
		"\2TR\3\2\2\2UV\7;\2\2V\\\b\4\1\2WX\7\30\2\2XY\7;\2\2Y[\b\4\1\2ZW\3\2\2"+
		"\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^\\\3\2\2\2_`\7\31\2\2`\7"+
		"\3\2\2\2ab\7\3\2\2bc\b\5\1\2cd\5\26\f\2d\t\3\2\2\2ef\7\22\2\2fg\7\'\2"+
		"\2gh\7\23\2\2h\13\3\2\2\2ij\t\2\2\2j\r\3\2\2\2kn\7\b\2\2lo\5\f\7\2mo\7"+
		"\5\2\2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2pq\7;\2\2qr\b\b\1\2rs\b\b\1\2st\b"+
		"\b\1\2tv\7\24\2\2uw\5\20\t\2vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7\25\2\2"+
		"y{\7\26\2\2z|\5\4\3\2{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}\177\5\22\n\2~}\3"+
		"\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082"+
		"\3\2\2\2\u0082\u0083\7\27\2\2\u0083\u0084\b\b\1\2\u0084\u0085\b\b\1\2"+
		"\u0085\17\3\2\2\2\u0086\u0087\5\f\7\2\u0087\u0088\7;\2\2\u0088\u0090\b"+
		"\t\1\2\u0089\u008a\7\30\2\2\u008a\u008b\5\f\7\2\u008b\u008c\7;\2\2\u008c"+
		"\u008d\b\t\1\2\u008d\u008f\3\2\2\2\u008e\u0089\3\2\2\2\u008f\u0092\3\2"+
		"\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\21\3\2\2\2\u0092\u0090"+
		"\3\2\2\2\u0093\u009c\5\32\16\2\u0094\u009c\5\24\13\2\u0095\u009c\5,\27"+
		"\2\u0096\u009c\5\30\r\2\u0097\u009c\5\60\31\2\u0098\u009c\5.\30\2\u0099"+
		"\u009c\5\34\17\2\u009a\u009c\5\62\32\2\u009b\u0093\3\2\2\2\u009b\u0094"+
		"\3\2\2\2\u009b\u0095\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b"+
		"\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\23\3\2\2"+
		"\2\u009d\u009e\7\13\2\2\u009e\u009f\5 \21\2\u009f\u00a0\b\13\1\2\u00a0"+
		"\u00a4\5\26\f\2\u00a1\u00a2\7\n\2\2\u00a2\u00a3\b\13\1\2\u00a3\u00a5\5"+
		"\26\f\2\u00a4\u00a1\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6"+
		"\u00a7\7\31\2\2\u00a7\u00a8\b\13\1\2\u00a8\25\3\2\2\2\u00a9\u00aa\7\26"+
		"\2\2\u00aa\u00ae\5\22\n\2\u00ab\u00ad\5\22\n\2\u00ac\u00ab\3\2\2\2\u00ad"+
		"\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2"+
		"\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7\27\2\2\u00b2\27\3\2\2\2\u00b3\u00b4"+
		"\7\6\2\2\u00b4\u00b5\7\24\2\2\u00b5\u00b6\5 \21\2\u00b6\u00bd\b\r\1\2"+
		"\u00b7\u00b8\7\30\2\2\u00b8\u00b9\5 \21\2\u00b9\u00ba\b\r\1\2\u00ba\u00bc"+
		"\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd"+
		"\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\7\25"+
		"\2\2\u00c1\u00c2\7\31\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\7;\2\2\u00c4\u00cb"+
		"\b\16\1\2\u00c5\u00c6\7\22\2\2\u00c6\u00c7\5$\23\2\u00c7\u00c8\7\23\2"+
		"\2\u00c8\u00ca\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9"+
		"\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce"+
		"\u00cf\7\"\2\2\u00cf\u00d4\b\16\1\2\u00d0\u00d1\5 \21\2\u00d1\u00d2\b"+
		"\16\1\2\u00d2\u00d5\3\2\2\2\u00d3\u00d5\5\36\20\2\u00d4\u00d0\3\2\2\2"+
		"\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7\31\2\2\u00d7\33"+
		"\3\2\2\2\u00d8\u00d9\7\20\2\2\u00d9\u00da\5 \21\2\u00da\u00db\b\17\1\2"+
		"\u00db\u00dc\b\17\1\2\u00dc\u00dd\7\31\2\2\u00dd\35\3\2\2\2\u00de\u00df"+
		"\7\22\2\2\u00df\u00e4\5*\26\2\u00e0\u00e1\7\30\2\2\u00e1\u00e3\5*\26\2"+
		"\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5"+
		"\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00f6\7\23\2\2"+
		"\u00e8\u00e9\7\30\2\2\u00e9\u00ea\7\22\2\2\u00ea\u00ef\5*\26\2\u00eb\u00ec"+
		"\7\30\2\2\u00ec\u00ee\5*\26\2\u00ed\u00eb\3\2\2\2\u00ee\u00f1\3\2\2\2"+
		"\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ef"+
		"\3\2\2\2\u00f2\u00f3\7\23\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00e8\3\2\2\2"+
		"\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\37"+
		"\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\5\"\22\2\u00fa\u0106\b\21\1\2"+
		"\u00fb\u00fc\7%\2\2\u00fc\u0100\b\21\1\2\u00fd\u00fe\7&\2\2\u00fe\u0100"+
		"\b\21\1\2\u00ff\u00fb\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\3\2\2\2"+
		"\u0101\u0102\5\"\22\2\u0102\u0103\b\21\1\2\u0103\u0105\3\2\2\2\u0104\u00ff"+
		"\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107"+
		"!\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u0116\5$\23\2\u010a\u010b\7\37\2\2"+
		"\u010b\u0117\b\22\1\2\u010c\u010d\7\36\2\2\u010d\u0117\b\22\1\2\u010e"+
		"\u010f\7 \2\2\u010f\u0117\b\22\1\2\u0110\u0111\7!\2\2\u0111\u0117\b\22"+
		"\1\2\u0112\u0113\7$\2\2\u0113\u0117\b\22\1\2\u0114\u0115\7#\2\2\u0115"+
		"\u0117\b\22\1\2\u0116\u010a\3\2\2\2\u0116\u010c\3\2\2\2\u0116\u010e\3"+
		"\2\2\2\u0116\u0110\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0114\3\2\2\2\u0117"+
		"\u0118\3\2\2\2\u0118\u0119\5$\23\2\u0119\u011a\b\22\1\2\u011a\u011d\3"+
		"\2\2\2\u011b\u011d\5$\23\2\u011c\u0109\3\2\2\2\u011c\u011b\3\2\2\2\u011d"+
		"#\3\2\2\2\u011e\u011f\5&\24\2\u011f\u012b\b\23\1\2\u0120\u0121\7\32\2"+
		"\2\u0121\u0125\b\23\1\2\u0122\u0123\7\33\2\2\u0123\u0125\b\23\1\2\u0124"+
		"\u0120\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\5&"+
		"\24\2\u0127\u0128\b\23\1\2\u0128\u012a\3\2\2\2\u0129\u0124\3\2\2\2\u012a"+
		"\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c%\3\2\2\2"+
		"\u012d\u012b\3\2\2\2\u012e\u012f\5(\25\2\u012f\u013b\b\24\1\2\u0130\u0131"+
		"\7\34\2\2\u0131\u0135\b\24\1\2\u0132\u0133\7\35\2\2\u0133\u0135\b\24\1"+
		"\2\u0134\u0130\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137"+
		"\5(\25\2\u0137\u0138\b\24\1\2\u0138\u013a\3\2\2\2\u0139\u0134\3\2\2\2"+
		"\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\'\3"+
		"\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\7\24\2\2\u013f\u0140\b\25\1\2\u0140"+
		"\u0141\5 \21\2\u0141\u0142\7\25\2\2\u0142\u0143\b\25\1\2\u0143\u014d\3"+
		"\2\2\2\u0144\u0148\7\32\2\2\u0145\u0146\7\33\2\2\u0146\u0148\b\25\1\2"+
		"\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149"+
		"\3\2\2\2\u0149\u014a\5*\26\2\u014a\u014b\b\25\1\2\u014b\u014d\3\2\2\2"+
		"\u014c\u013e\3\2\2\2\u014c\u0147\3\2\2\2\u014d)\3\2\2\2\u014e\u014f\7"+
		";\2\2\u014f\u0150\7\24\2\2\u0150\u0151\b\26\1\2\u0151\u0152\b\26\1\2\u0152"+
		"\u0153\b\26\1\2\u0153\u0154\b\26\1\2\u0154\u0160\b\26\1\2\u0155\u0156"+
		"\5 \21\2\u0156\u015d\b\26\1\2\u0157\u0158\7\30\2\2\u0158\u0159\5 \21\2"+
		"\u0159\u015a\b\26\1\2\u015a\u015c\3\2\2\2\u015b\u0157\3\2\2\2\u015c\u015f"+
		"\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0161\3\2\2\2\u015f"+
		"\u015d\3\2\2\2\u0160\u0155\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2"+
		"\2\2\u0162\u0163\b\26\1\2\u0163\u0164\7\25\2\2\u0164\u0165\b\26\1\2\u0165"+
		"\u0166\b\26\1\2\u0166\u017b\b\26\1\2\u0167\u0168\7;\2\2\u0168\u016f\b"+
		"\26\1\2\u0169\u016a\7\22\2\2\u016a\u016b\5$\23\2\u016b\u016c\7\23\2\2"+
		"\u016c\u016e\3\2\2\2\u016d\u0169\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d"+
		"\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u017b\3\2\2\2\u0171\u016f\3\2\2\2\u0172"+
		"\u0173\7\'\2\2\u0173\u017b\b\26\1\2\u0174\u0175\7)\2\2\u0175\u017b\b\26"+
		"\1\2\u0176\u0177\7(\2\2\u0177\u017b\b\26\1\2\u0178\u0179\7*\2\2\u0179"+
		"\u017b\b\26\1\2\u017a\u014e\3\2\2\2\u017a\u0167\3\2\2\2\u017a\u0172\3"+
		"\2\2\2\u017a\u0174\3\2\2\2\u017a\u0176\3\2\2\2\u017a\u0178\3\2\2\2\u017b"+
		"+\3\2\2\2\u017c\u017d\7\7\2\2\u017d\u017e\b\27\1\2\u017e\u017f\5 \21\2"+
		"\u017f\u0180\b\27\1\2\u0180\u0181\5\26\f\2\u0181\u0182\b\27\1\2\u0182"+
		"-\3\2\2\2\u0183\u0184\7;\2\2\u0184\u0185\7\24\2\2\u0185\u0186\b\30\1\2"+
		"\u0186\u0187\b\30\1\2\u0187\u0188\b\30\1\2\u0188\u0189\b\30\1\2\u0189"+
		"\u0195\b\30\1\2\u018a\u018b\5 \21\2\u018b\u0192\b\30\1\2\u018c\u018d\7"+
		"\30\2\2\u018d\u018e\5 \21\2\u018e\u018f\b\30\1\2\u018f\u0191\3\2\2\2\u0190"+
		"\u018c\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2"+
		"\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u018a\3\2\2\2\u0195"+
		"\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\b\30\1\2\u0198\u0199\7"+
		"\25\2\2\u0199\u019a\b\30\1\2\u019a\u019b\b\30\1\2\u019b\u019c\7\31\2\2"+
		"\u019c/\3\2\2\2\u019d\u019e\7\21\2\2\u019e\u019f\7\24\2\2\u019f\u01a2"+
		"\7;\2\2\u01a0\u01a1\7\30\2\2\u01a1\u01a3\7(\2\2\u01a2\u01a0\3\2\2\2\u01a2"+
		"\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b\31\1\2\u01a5\u01a6\7"+
		"\25\2\2\u01a6\u01a7\7\31\2\2\u01a7\61\3\2\2\2\u01a8\u01a9\t\3\2\2\u01a9"+
		"\u01aa\7\24\2\2\u01aa\u01ab\7;\2\2\u01ab\u01ac\7\25\2\2\u01ac\u01d9\7"+
		"\31\2\2\u01ad\u01ae\7\66\2\2\u01ae\u01af\7\24\2\2\u01af\u01b2\7;\2\2\u01b0"+
		"\u01b1\7\30\2\2\u01b1\u01b3\7;\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2"+
		"\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7\25\2\2\u01b5\u01d9\7\31\2\2\u01b6"+
		"\u01b7\7\67\2\2\u01b7\u01b8\7\24\2\2\u01b8\u01b9\7;\2\2\u01b9\u01ba\7"+
		"\30\2\2\u01ba\u01bb\7;\2\2\u01bb\u01bc\7\25\2\2\u01bc\u01d9\7\31\2\2\u01bd"+
		"\u01be\78\2\2\u01be\u01bf\7\24\2\2\u01bf\u01c0\7)\2\2\u01c0\u01c1\7\30"+
		"\2\2\u01c1\u01c2\7)\2\2\u01c2\u01c3\7\30\2\2\u01c3\u01c4\7\'\2\2\u01c4"+
		"\u01c5\7\25\2\2\u01c5\u01d9\7\31\2\2\u01c6\u01c7\79\2\2\u01c7\u01c8\7"+
		"\24\2\2\u01c8\u01c9\7;\2\2\u01c9\u01ca\7\30\2\2\u01ca\u01cb\5*\26\2\u01cb"+
		"\u01cc\7\30\2\2\u01cc\u01cd\5*\26\2\u01cd\u01ce\7\25\2\2\u01ce\u01cf\7"+
		"\31\2\2\u01cf\u01d9\3\2\2\2\u01d0\u01d1\7:\2\2\u01d1\u01d2\7\24\2\2\u01d2"+
		"\u01d3\7;\2\2\u01d3\u01d4\7\30\2\2\u01d4\u01d5\5*\26\2\u01d5\u01d6\7\25"+
		"\2\2\u01d6\u01d7\7\31\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01a8\3\2\2\2\u01d8"+
		"\u01ad\3\2\2\2\u01d8\u01b6\3\2\2\2\u01d8\u01bd\3\2\2\2\u01d8\u01c6\3\2"+
		"\2\2\u01d8\u01d0\3\2\2\2\u01d9\63\3\2\2\2(8=JR\\nv{\u0080\u0090\u009b"+
		"\u00a4\u00ae\u00bd\u00cb\u00d4\u00e4\u00ef\u00f6\u00ff\u0106\u0116\u011c"+
		"\u0124\u012b\u0134\u013b\u0147\u014c\u015d\u0160\u016f\u017a\u0192\u0195"+
		"\u01a2\u01b2\u01d8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}