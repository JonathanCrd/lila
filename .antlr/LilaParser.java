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
		RULE_sreturn = 13, RULE_expresion = 14, RULE_comparacion = 15, RULE_exp = 16, 
		RULE_termino = 17, RULE_factor = 18, RULE_var_cte = 19, RULE_swhile = 20, 
		RULE_invocacion = 21, RULE_getinput = 22, RULE_especiales = 23;
	public static final String[] ruleNames = {
		"programa", "data", "data2", "main", "array", "tipo", "funciones", "params", 
		"estatuto", "condicion", "bloque", "display", "asignacion", "sreturn", 
		"expresion", "comparacion", "exp", "termino", "factor", "var_cte", "swhile", 
		"invocacion", "getinput", "especiales"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'main'", "'lila'", "'void'", "'display'", "'while'", "'func'", 
		"'var'", "'else'", "'if'", "'int'", "'num'", "'text'", "'bool'", "'return'", 
		"'getinput'", "'['", "']'", "'('", "')'", "'{'", "'}'", "','", "';'", 
		"'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!='", "'=='", "'='", "'<='", 
		"'>='", "'AND'", "'OR'", null, null, null, null, "'getOutliers'", "'removeOutliers'", 
		"'tellMeWhatToUse'", "'printMeasures'", "'mean'", "'median'", "'mode'", 
		"'range'", "'min'", "'max'", "'desEstandar'", "'quickShow'", "'pearsonCorrelation'", 
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
			setState(48);
			match(LILA);
			setState(49);
			match(ID);
			gen.goTo()
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(51);
				data();
				}
			}

			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNC) {
				{
				{
				setState(54);
				funciones();
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			gen.conditionEnd()
			setState(61);
			main();
			gen.end()
			Semantic.display_test()
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
			setState(67);
			match(VAR);
			setState(69); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(68);
				data2();
				}
				}
				setState(71); 
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
		public List<TerminalNode> ID() { return getTokens(LilaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LilaParser.ID, i);
		}
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
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
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(75);
				((Data2Context)_localctx).tipo = tipo();
				}
				break;
			case 2:
				{
				setState(76);
				((Data2Context)_localctx).tipo = tipo();
				setState(77);
				array();
				}
				break;
			}
			setState(81);
			((Data2Context)_localctx).ID = match(ID);
			Semantic.add_var(Operand((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(83);
				match(COMMA);
				setState(84);
				((Data2Context)_localctx).ID = match(ID);
				Semantic.add_var(Operand((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
				}
				}
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			Semantic.reset_array_setup()
			setState(92);
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
			setState(94);
			match(MAIN);
			gen.contextChange()
			setState(96);
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
		public Token CTE_INT;
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<TerminalNode> CTE_INT() { return getTokens(LilaParser.CTE_INT); }
		public TerminalNode CTE_INT(int i) {
			return getToken(LilaParser.CTE_INT, i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			Semantic.array_declaration()
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACKET) {
				{
				{
				setState(99);
				match(OPEN_BRACKET);
				setState(100);
				((ArrayContext)_localctx).CTE_INT = match(CTE_INT);
				Semantic.array_dimension((((ArrayContext)_localctx).CTE_INT!=null?((ArrayContext)_localctx).CTE_INT.getText():null))
				setState(102);
				match(CLOSE_BRACKET);
				Semantic.array_next_dim()
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			Semantic.arr_second_round()
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
			setState(111);
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
			setState(113);
			match(FUNC);
			setState(116);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case NUM:
			case TEXT:
			case BOOL:
				{
				setState(114);
				((FuncionesContext)_localctx).tipo = tipo();
				}
				break;
			case VOID:
				{
				setState(115);
				((FuncionesContext)_localctx).VOID = match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(118);
			((FuncionesContext)_localctx).ID = match(ID);
			index = len(gen.Quadruples)
			Semantic.enterFunciones((((FuncionesContext)_localctx).ID!=null?((FuncionesContext)_localctx).ID.getText():null),(((FuncionesContext)_localctx).tipo!=null?_input.getText(((FuncionesContext)_localctx).tipo.start,((FuncionesContext)_localctx).tipo.stop):null),(((FuncionesContext)_localctx).VOID!=null?((FuncionesContext)_localctx).VOID.getText():null),index)
			gen.contextChange()
			setState(122);
			match(OPEN_PARENTHESIS);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0)) {
				{
				setState(123);
				params();
				}
			}

			setState(126);
			match(CLOSE_PARENTHESIS);
			setState(127);
			match(OPEN_CURLY);
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(128);
				data();
				}
			}

			setState(132); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(131);
				estatuto();
				}
				}
				setState(134); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0) );
			setState(136);
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
			setState(140);
			((ParamsContext)_localctx).tipo = tipo();
			setState(141);
			((ParamsContext)_localctx).ID = match(ID);
			Semantic.add_param(Operand((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),None))
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(143);
				match(COMMA);
				setState(144);
				((ParamsContext)_localctx).tipo = tipo();
				setState(145);
				((ParamsContext)_localctx).ID = match(ID);
				Semantic.add_param(Operand((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),None))
				}
				}
				setState(152);
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
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(153);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(154);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(155);
				swhile();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(156);
				display();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(157);
				getinput();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(158);
				invocacion();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(159);
				sreturn();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(160);
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
			setState(163);
			match(IF);
			setState(164);
			expresion();
			gen.checkExpresion()
			setState(166);
			bloque();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(167);
				match(ELSE);
				gen.conditionElse()
				setState(169);
				bloque();
				}
			}

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
			setState(174);
			match(OPEN_CURLY);
			setState(175);
			estatuto();
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0)) {
				{
				{
				setState(176);
				estatuto();
				}
				}
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(182);
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
			setState(184);
			match(DISPLAY);
			setState(185);
			match(OPEN_PARENTHESIS);
			setState(186);
			expresion();
			gen.display()
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(188);
				match(COMMA);
				setState(189);
				expresion();
				gen.display()
				}
				}
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(197);
			match(CLOSE_PARENTHESIS);
			setState(198);
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
		public TerminalNode EQUAL() { return getToken(LilaParser.EQUAL, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TerminalNode ID() { return getToken(LilaParser.ID, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
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
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(200);
				((AsignacionContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
				}
				break;
			case 2:
				{
				setState(202);
				((AsignacionContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
				gen.addOperator('(')
				gen.access_array_begin()
				setState(212); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(206);
					match(OPEN_BRACKET);
					Semantic.check_var_dim((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null))
					setState(208);
					exp();
					gen.VER((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null))
					setState(210);
					match(CLOSE_BRACKET);
					}
					}
					setState(214); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==OPEN_BRACKET );
				Semantic.check_dims((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null))
				gen.access_array_end((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null))
				gen.finParentesis()
				}
				break;
			}
			setState(222);
			((AsignacionContext)_localctx).EQUAL = match(EQUAL);
			gen.addOperator((((AsignacionContext)_localctx).EQUAL!=null?((AsignacionContext)_localctx).EQUAL.getText():null))
			{
			setState(224);
			expresion();
			gen.assign()
			}
			setState(227);
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
			setState(229);
			match(RETURN);
			setState(230);
			expresion();
			Semantic.checkReturn(gen.top_variables())
			gen.func_return()
			setState(233);
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
		enterRule(_localctx, 28, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			comparacion();
			gen.exitExpresion()
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(241);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(237);
					match(AND);
					gen.addOperator('AND')
					}
					break;
				case OR:
					{
					setState(239);
					match(OR);
					gen.addOperator('OR')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(243);
				comparacion();
				gen.exitExpresion()
				}
				}
				setState(250);
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
		enterRule(_localctx, 30, RULE_comparacion);
		try {
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(251);
				exp();
				setState(264);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GREATER_THAN:
					{
					setState(252);
					match(GREATER_THAN);
					gen.addOperator('>')
					}
					break;
				case LESS_THAN:
					{
					setState(254);
					match(LESS_THAN);
					gen.addOperator('<')
					}
					break;
				case NOTEQUAL:
					{
					setState(256);
					match(NOTEQUAL);
					gen.addOperator('!=')
					}
					break;
				case EQUALITY:
					{
					setState(258);
					match(EQUALITY);
					gen.addOperator('==')
					}
					break;
				case GREATER_THAN_EQUAL:
					{
					setState(260);
					match(GREATER_THAN_EQUAL);
					gen.addOperator('>=')
					}
					break;
				case LESS_THAN_EQUAL:
					{
					setState(262);
					match(LESS_THAN_EQUAL);
					gen.addOperator('<=')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(266);
				exp();
				gen.exitComparacion()
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(269);
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
		enterRule(_localctx, 32, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			termino();
			gen.exitExp()
			setState(285);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(278);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(274);
					match(PLUS);
					gen.addOperator('+')
					}
					break;
				case MINUS:
					{
					setState(276);
					match(MINUS);
					gen.addOperator('-')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(280);
				termino();
				gen.exitExp()
				}
				}
				setState(287);
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
		enterRule(_localctx, 34, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			factor();
			gen.exitTermino()
			setState(301);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULTIPLICATION || _la==DIVISION) {
				{
				{
				setState(294);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(290);
					match(MULTIPLICATION);
					gen.addOperator('*')
					}
					break;
				case DIVISION:
					{
					setState(292);
					match(DIVISION);
					gen.addOperator('/')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(296);
				factor();
				gen.exitTermino()
				}
				}
				setState(303);
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
		enterRule(_localctx, 36, RULE_factor);
		try {
			setState(318);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PARENTHESIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				match(OPEN_PARENTHESIS);
				gen.addOperator('(')
				setState(306);
				expresion();
				setState(307);
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
				setState(313);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(310);
					match(PLUS);
					}
					break;
				case MINUS:
					{
					setState(311);
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
				setState(315);
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
		enterRule(_localctx, 38, RULE_var_cte);
		int _la;
		try {
			setState(372);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(320);
				((Var_cteContext)_localctx).ID = match(ID);
				setState(321);
				match(OPEN_PARENTHESIS);
				gen.incoming_Params()
				Semantic.look_for_function((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				Semantic.isVoid((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null), False)
				gen.era((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.addOperator('(')
				setState(338);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OPEN_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_STRING) | (1L << CTE_F) | (1L << CTE_BOOL) | (1L << ID))) != 0)) {
					{
					setState(327);
					expresion();
					gen.params()
					setState(335);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(329);
						match(COMMA);
						setState(330);
						expresion();
						gen.params()
						}
						}
						setState(337);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				gen.goSub((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				setState(341);
				match(CLOSE_PARENTHESIS);
				gen.check_params((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.finParentesis()
				gen.addFunct(Semantic.look_for_function((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(345);
				((Var_cteContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(347);
				((Var_cteContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				gen.addOperator('(')
				gen.access_array_begin()
				setState(356); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(351);
					match(OPEN_BRACKET);
					setState(352);
					exp();
					gen.VER((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
					setState(354);
					match(CLOSE_BRACKET);
					}
					}
					setState(358); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==OPEN_BRACKET );
				Semantic.check_dims((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.access_array_end((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null))
				gen.finParentesis()
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(364);
				((Var_cteContext)_localctx).CTE_INT = match(CTE_INT);
				gen.addConst(Operand(None,'int',(((Var_cteContext)_localctx).CTE_INT!=null?((Var_cteContext)_localctx).CTE_INT.getText():null)))
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(366);
				((Var_cteContext)_localctx).CTE_F = match(CTE_F);
				gen.addConst(Operand(None,'num',(((Var_cteContext)_localctx).CTE_F!=null?((Var_cteContext)_localctx).CTE_F.getText():null)))
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(368);
				((Var_cteContext)_localctx).CTE_STRING = match(CTE_STRING);
				gen.addConst(Operand(None,'text',(((Var_cteContext)_localctx).CTE_STRING!=null?((Var_cteContext)_localctx).CTE_STRING.getText():null)))
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(370);
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
		enterRule(_localctx, 40, RULE_swhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			match(WHILE);
			gen.swhile()
			setState(376);
			expresion();
			gen.checkExpresion()
			setState(378);
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
		enterRule(_localctx, 42, RULE_invocacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(381);
			((InvocacionContext)_localctx).ID = match(ID);
			setState(382);
			match(OPEN_PARENTHESIS);
			gen.incoming_Params()
			Semantic.look_for_function((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			Semantic.isVoid((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null), True)
			gen.era((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			gen.addOperator('(')
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OPEN_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_STRING) | (1L << CTE_F) | (1L << CTE_BOOL) | (1L << ID))) != 0)) {
				{
				setState(388);
				expresion();
				gen.params()
				setState(396);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(390);
					match(COMMA);
					setState(391);
					expresion();
					gen.params()
					}
					}
					setState(398);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			gen.goSub((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			setState(402);
			match(CLOSE_PARENTHESIS);
			gen.check_params((((InvocacionContext)_localctx).ID!=null?((InvocacionContext)_localctx).ID.getText():null))
			gen.finParentesis()
			setState(405);
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
		enterRule(_localctx, 44, RULE_getinput);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(407);
			match(GETINPUT);
			setState(408);
			match(OPEN_PARENTHESIS);
			setState(409);
			((GetinputContext)_localctx).ID = match(ID);
			setState(412);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(410);
				match(COMMA);
				setState(411);
				((GetinputContext)_localctx).CTE_STRING = match(CTE_STRING);
				}
			}

			gen.getinput(Semantic.look_for_variable((((GetinputContext)_localctx).ID!=null?((GetinputContext)_localctx).ID.getText():null)), (((GetinputContext)_localctx).CTE_STRING!=null?((GetinputContext)_localctx).CTE_STRING.getText():null))
			setState(415);
			match(CLOSE_PARENTHESIS);
			setState(416);
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
		public Token ID;
		public TerminalNode MEAN() { return getToken(LilaParser.MEAN, 0); }
		public TerminalNode OPEN_PARENTHESIS() { return getToken(LilaParser.OPEN_PARENTHESIS, 0); }
		public List<TerminalNode> ID() { return getTokens(LilaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LilaParser.ID, i);
		}
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(LilaParser.SEMICOLON, 0); }
		public TerminalNode MEDIAN() { return getToken(LilaParser.MEDIAN, 0); }
		public TerminalNode MODE() { return getToken(LilaParser.MODE, 0); }
		public TerminalNode MIN() { return getToken(LilaParser.MIN, 0); }
		public TerminalNode MAX() { return getToken(LilaParser.MAX, 0); }
		public TerminalNode RANGE() { return getToken(LilaParser.RANGE, 0); }
		public TerminalNode DESESTANDAR() { return getToken(LilaParser.DESESTANDAR, 0); }
		public TerminalNode PRINTMEASURES() { return getToken(LilaParser.PRINTMEASURES, 0); }
		public TerminalNode GETOUTLIERS() { return getToken(LilaParser.GETOUTLIERS, 0); }
		public TerminalNode REMOVEOUTLIERS() { return getToken(LilaParser.REMOVEOUTLIERS, 0); }
		public TerminalNode FILLVALUE() { return getToken(LilaParser.FILLVALUE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public List<Var_cteContext> var_cte() {
			return getRuleContexts(Var_cteContext.class);
		}
		public Var_cteContext var_cte(int i) {
			return getRuleContext(Var_cteContext.class,i);
		}
		public TerminalNode REMOVEVALUE() { return getToken(LilaParser.REMOVEVALUE, 0); }
		public TerminalNode TELLMEWHATTOUSE() { return getToken(LilaParser.TELLMEWHATTOUSE, 0); }
		public TerminalNode QUICKSHOW() { return getToken(LilaParser.QUICKSHOW, 0); }
		public TerminalNode PEARSONCORRELATION() { return getToken(LilaParser.PEARSONCORRELATION, 0); }
		public TerminalNode NORMALDISTRIBUTION() { return getToken(LilaParser.NORMALDISTRIBUTION, 0); }
		public List<TerminalNode> CTE_F() { return getTokens(LilaParser.CTE_F); }
		public TerminalNode CTE_F(int i) {
			return getToken(LilaParser.CTE_F, i);
		}
		public TerminalNode CTE_INT() { return getToken(LilaParser.CTE_INT, 0); }
		public EspecialesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_especiales; }
	}

	public final EspecialesContext especiales() throws RecognitionException {
		EspecialesContext _localctx = new EspecialesContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_especiales);
		try {
			setState(557);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(418);
				match(MEAN);
				setState(419);
				match(OPEN_PARENTHESIS);
				setState(420);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'MEAN')
				setState(423);
				match(CLOSE_PARENTHESIS);
				setState(424);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(425);
				match(MEDIAN);
				setState(426);
				match(OPEN_PARENTHESIS);
				setState(427);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'MEDIAN')
				setState(430);
				match(CLOSE_PARENTHESIS);
				setState(431);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(432);
				match(MODE);
				setState(433);
				match(OPEN_PARENTHESIS);
				setState(434);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'MODE')
				setState(437);
				match(CLOSE_PARENTHESIS);
				setState(438);
				match(SEMICOLON);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(439);
				match(MIN);
				setState(440);
				match(OPEN_PARENTHESIS);
				setState(441);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'MIN')
				setState(444);
				match(CLOSE_PARENTHESIS);
				setState(445);
				match(SEMICOLON);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(446);
				match(MAX);
				setState(447);
				match(OPEN_PARENTHESIS);
				setState(448);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'MAX')
				setState(451);
				match(CLOSE_PARENTHESIS);
				setState(452);
				match(SEMICOLON);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(453);
				match(RANGE);
				setState(454);
				match(OPEN_PARENTHESIS);
				setState(455);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'RANGE')
				setState(458);
				match(CLOSE_PARENTHESIS);
				setState(459);
				match(SEMICOLON);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(460);
				match(DESESTANDAR);
				setState(461);
				match(OPEN_PARENTHESIS);
				setState(462);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'DESESTANDAR')
				setState(465);
				match(CLOSE_PARENTHESIS);
				setState(466);
				match(SEMICOLON);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(467);
				match(PRINTMEASURES);
				setState(468);
				match(OPEN_PARENTHESIS);
				setState(469);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'PRINTMEASURES')
				setState(472);
				match(CLOSE_PARENTHESIS);
				setState(473);
				match(SEMICOLON);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(474);
				match(GETOUTLIERS);
				setState(475);
				match(OPEN_PARENTHESIS);
				setState(476);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'GETOUTLIERS')
				setState(479);
				match(CLOSE_PARENTHESIS);
				setState(480);
				match(SEMICOLON);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(481);
				match(REMOVEOUTLIERS);
				setState(482);
				match(OPEN_PARENTHESIS);
				setState(483);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'REMOVEOUTLIERS')
				setState(486);
				match(CLOSE_PARENTHESIS);
				setState(487);
				match(SEMICOLON);
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(488);
				match(FILLVALUE);
				setState(489);
				match(OPEN_PARENTHESIS);
				setState(490);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkIsOneDim((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				setState(492);
				match(COMMA);
				setState(493);
				var_cte();
				setState(494);
				match(COMMA);
				setState(495);
				var_cte();
				gen.q_fill_value((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'FILLVALUE')
				setState(497);
				match(CLOSE_PARENTHESIS);
				setState(498);
				match(SEMICOLON);
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(500);
				match(REMOVEVALUE);
				setState(501);
				match(OPEN_PARENTHESIS);
				setState(502);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkIsOneDim((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				setState(504);
				match(COMMA);
				setState(505);
				var_cte();
				gen.q_remove_value((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'REMOVEVALUE')
				setState(507);
				match(CLOSE_PARENTHESIS);
				setState(508);
				match(SEMICOLON);
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(510);
				match(TELLMEWHATTOUSE);
				setState(511);
				match(OPEN_PARENTHESIS);
				setState(512);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'TELLMEWHATTOUSE')
				setState(515);
				match(CLOSE_PARENTHESIS);
				setState(516);
				match(SEMICOLON);
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(517);
				match(QUICKSHOW);
				setState(518);
				match(OPEN_PARENTHESIS);
				setState(519);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkIsOneDim((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.addVar(Semantic.look_for_variable((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null)))
				setState(522);
				match(COMMA);
				setState(523);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkIsOneDim((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.addVar(Semantic.look_for_variable((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null)))
				gen.q_twoParams((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'QUICKSHOWTWO')
				setState(527);
				match(CLOSE_PARENTHESIS);
				setState(528);
				match(SEMICOLON);
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(529);
				match(QUICKSHOW);
				setState(530);
				match(OPEN_PARENTHESIS);
				setState(531);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkIsOneDim((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.q_basics((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'QUICKSHOWONE')
				setState(534);
				match(CLOSE_PARENTHESIS);
				setState(535);
				match(SEMICOLON);
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(536);
				match(PEARSONCORRELATION);
				setState(537);
				match(OPEN_PARENTHESIS);
				setState(538);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.addVar(Semantic.look_for_variable((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null)))
				setState(541);
				match(COMMA);
				setState(542);
				((EspecialesContext)_localctx).ID = match(ID);
				Semantic.checkSpecialParam((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null))
				gen.addVar(Semantic.look_for_variable((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null)))
				gen.q_twoParams((((EspecialesContext)_localctx).ID!=null?((EspecialesContext)_localctx).ID.getText():null),'PEARSONCORRELATION')
				setState(546);
				match(CLOSE_PARENTHESIS);
				setState(547);
				match(SEMICOLON);
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(548);
				match(NORMALDISTRIBUTION);
				setState(549);
				match(OPEN_PARENTHESIS);
				setState(550);
				match(CTE_F);
				setState(551);
				match(COMMA);
				setState(552);
				match(CTE_F);
				setState(553);
				match(COMMA);
				setState(554);
				match(CTE_INT);
				setState(555);
				match(CLOSE_PARENTHESIS);
				setState(556);
				match(SEMICOLON);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=\u0232\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\3\2\3\2\3\2\5\2\67\n\2\3\2\7\2:\n\2\f\2\16\2=\13\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\6\3H\n\3\r\3\16\3I\3\3\3\3\3\4\3\4\3\4\3\4\5\4"+
		"R\n\4\3\4\3\4\3\4\3\4\3\4\7\4Y\n\4\f\4\16\4\\\13\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6k\n\6\f\6\16\6n\13\6\3\6\3\6\3\7\3"+
		"\7\3\b\3\b\3\b\5\bw\n\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\177\n\b\3\b\3\b\3"+
		"\b\5\b\u0084\n\b\3\b\6\b\u0087\n\b\r\b\16\b\u0088\3\b\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0097\n\t\f\t\16\t\u009a\13\t\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a4\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\5\13\u00ad\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b4\n\f\f\f\16\f\u00b7"+
		"\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c3\n\r\f\r\16\r\u00c6"+
		"\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\6\16\u00d7\n\16\r\16\16\16\u00d8\3\16\3\16\3\16\3\16\5\16\u00df"+
		"\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f4\n\20\3\20\3\20\3\20\7\20\u00f9"+
		"\n\20\f\20\16\20\u00fc\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\5\21\u010b\n\21\3\21\3\21\3\21\3\21\5\21\u0111"+
		"\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0119\n\22\3\22\3\22\3\22\7\22"+
		"\u011e\n\22\f\22\16\22\u0121\13\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23"+
		"\u0129\n\23\3\23\3\23\3\23\7\23\u012e\n\23\f\23\16\23\u0131\13\23\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u013c\n\24\3\24\3\24\3\24"+
		"\5\24\u0141\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\7\25\u0150\n\25\f\25\16\25\u0153\13\25\5\25\u0155\n\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\6\25\u0167\n\25\r\25\16\25\u0168\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\5\25\u0177\n\25\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\7\27\u018d\n\27\f\27\16\27\u0190\13\27\5\27\u0192\n\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u019f\n\30\3\30\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\5\31\u0230\n\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34"+
		"\36 \"$&(*,.\60\2\3\3\2\f\17\2\u025b\2\62\3\2\2\2\4E\3\2\2\2\6Q\3\2\2"+
		"\2\b`\3\2\2\2\nd\3\2\2\2\fq\3\2\2\2\16s\3\2\2\2\20\u008e\3\2\2\2\22\u00a3"+
		"\3\2\2\2\24\u00a5\3\2\2\2\26\u00b0\3\2\2\2\30\u00ba\3\2\2\2\32\u00de\3"+
		"\2\2\2\34\u00e7\3\2\2\2\36\u00ed\3\2\2\2 \u0110\3\2\2\2\"\u0112\3\2\2"+
		"\2$\u0122\3\2\2\2&\u0140\3\2\2\2(\u0176\3\2\2\2*\u0178\3\2\2\2,\u017f"+
		"\3\2\2\2.\u0199\3\2\2\2\60\u022f\3\2\2\2\62\63\7\4\2\2\63\64\7;\2\2\64"+
		"\66\b\2\1\2\65\67\5\4\3\2\66\65\3\2\2\2\66\67\3\2\2\2\67;\3\2\2\28:\5"+
		"\16\b\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?"+
		"\b\2\1\2?@\5\b\5\2@A\b\2\1\2AB\b\2\1\2BC\b\2\1\2CD\b\2\1\2D\3\3\2\2\2"+
		"EG\7\t\2\2FH\5\6\4\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2"+
		"KL\b\3\1\2L\5\3\2\2\2MR\5\f\7\2NO\5\f\7\2OP\5\n\6\2PR\3\2\2\2QM\3\2\2"+
		"\2QN\3\2\2\2RS\3\2\2\2ST\7;\2\2TZ\b\4\1\2UV\7\30\2\2VW\7;\2\2WY\b\4\1"+
		"\2XU\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^\b\4"+
		"\1\2^_\7\31\2\2_\7\3\2\2\2`a\7\3\2\2ab\b\5\1\2bc\5\26\f\2c\t\3\2\2\2d"+
		"l\b\6\1\2ef\7\22\2\2fg\7\'\2\2gh\b\6\1\2hi\7\23\2\2ik\b\6\1\2je\3\2\2"+
		"\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2nl\3\2\2\2op\b\6\1\2p\13\3\2"+
		"\2\2qr\t\2\2\2r\r\3\2\2\2sv\7\b\2\2tw\5\f\7\2uw\7\5\2\2vt\3\2\2\2vu\3"+
		"\2\2\2wx\3\2\2\2xy\7;\2\2yz\b\b\1\2z{\b\b\1\2{|\b\b\1\2|~\7\24\2\2}\177"+
		"\5\20\t\2~}\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\7\25\2"+
		"\2\u0081\u0083\7\26\2\2\u0082\u0084\5\4\3\2\u0083\u0082\3\2\2\2\u0083"+
		"\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0087\5\22\n\2\u0086\u0085\3"+
		"\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089"+
		"\u008a\3\2\2\2\u008a\u008b\7\27\2\2\u008b\u008c\b\b\1\2\u008c\u008d\b"+
		"\b\1\2\u008d\17\3\2\2\2\u008e\u008f\5\f\7\2\u008f\u0090\7;\2\2\u0090\u0098"+
		"\b\t\1\2\u0091\u0092\7\30\2\2\u0092\u0093\5\f\7\2\u0093\u0094\7;\2\2\u0094"+
		"\u0095\b\t\1\2\u0095\u0097\3\2\2\2\u0096\u0091\3\2\2\2\u0097\u009a\3\2"+
		"\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\21\3\2\2\2\u009a\u0098"+
		"\3\2\2\2\u009b\u00a4\5\32\16\2\u009c\u00a4\5\24\13\2\u009d\u00a4\5*\26"+
		"\2\u009e\u00a4\5\30\r\2\u009f\u00a4\5.\30\2\u00a0\u00a4\5,\27\2\u00a1"+
		"\u00a4\5\34\17\2\u00a2\u00a4\5\60\31\2\u00a3\u009b\3\2\2\2\u00a3\u009c"+
		"\3\2\2\2\u00a3\u009d\3\2\2\2\u00a3\u009e\3\2\2\2\u00a3\u009f\3\2\2\2\u00a3"+
		"\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\23\3\2\2"+
		"\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7\5\36\20\2\u00a7\u00a8\b\13\1\2\u00a8"+
		"\u00ac\5\26\f\2\u00a9\u00aa\7\n\2\2\u00aa\u00ab\b\13\1\2\u00ab\u00ad\5"+
		"\26\f\2\u00ac\u00a9\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae"+
		"\u00af\b\13\1\2\u00af\25\3\2\2\2\u00b0\u00b1\7\26\2\2\u00b1\u00b5\5\22"+
		"\n\2\u00b2\u00b4\5\22\n\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5"+
		"\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2"+
		"\2\2\u00b8\u00b9\7\27\2\2\u00b9\27\3\2\2\2\u00ba\u00bb\7\6\2\2\u00bb\u00bc"+
		"\7\24\2\2\u00bc\u00bd\5\36\20\2\u00bd\u00c4\b\r\1\2\u00be\u00bf\7\30\2"+
		"\2\u00bf\u00c0\5\36\20\2\u00c0\u00c1\b\r\1\2\u00c1\u00c3\3\2\2\2\u00c2"+
		"\u00be\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2"+
		"\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7\25\2\2\u00c8"+
		"\u00c9\7\31\2\2\u00c9\31\3\2\2\2\u00ca\u00cb\7;\2\2\u00cb\u00df\b\16\1"+
		"\2\u00cc\u00cd\7;\2\2\u00cd\u00ce\b\16\1\2\u00ce\u00cf\b\16\1\2\u00cf"+
		"\u00d6\b\16\1\2\u00d0\u00d1\7\22\2\2\u00d1\u00d2\b\16\1\2\u00d2\u00d3"+
		"\5\"\22\2\u00d3\u00d4\b\16\1\2\u00d4\u00d5\7\23\2\2\u00d5\u00d7\3\2\2"+
		"\2\u00d6\u00d0\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9"+
		"\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\b\16\1\2\u00db\u00dc\b\16\1\2"+
		"\u00dc\u00dd\b\16\1\2\u00dd\u00df\3\2\2\2\u00de\u00ca\3\2\2\2\u00de\u00cc"+
		"\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7\"\2\2\u00e1\u00e2\b\16\1\2"+
		"\u00e2\u00e3\5\36\20\2\u00e3\u00e4\b\16\1\2\u00e4\u00e5\3\2\2\2\u00e5"+
		"\u00e6\7\31\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\7\20\2\2\u00e8\u00e9\5\36"+
		"\20\2\u00e9\u00ea\b\17\1\2\u00ea\u00eb\b\17\1\2\u00eb\u00ec\7\31\2\2\u00ec"+
		"\35\3\2\2\2\u00ed\u00ee\5 \21\2\u00ee\u00fa\b\20\1\2\u00ef\u00f0\7%\2"+
		"\2\u00f0\u00f4\b\20\1\2\u00f1\u00f2\7&\2\2\u00f2\u00f4\b\20\1\2\u00f3"+
		"\u00ef\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\5 "+
		"\21\2\u00f6\u00f7\b\20\1\2\u00f7\u00f9\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f9"+
		"\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\37\3\2\2"+
		"\2\u00fc\u00fa\3\2\2\2\u00fd\u010a\5\"\22\2\u00fe\u00ff\7\37\2\2\u00ff"+
		"\u010b\b\21\1\2\u0100\u0101\7\36\2\2\u0101\u010b\b\21\1\2\u0102\u0103"+
		"\7 \2\2\u0103\u010b\b\21\1\2\u0104\u0105\7!\2\2\u0105\u010b\b\21\1\2\u0106"+
		"\u0107\7$\2\2\u0107\u010b\b\21\1\2\u0108\u0109\7#\2\2\u0109\u010b\b\21"+
		"\1\2\u010a\u00fe\3\2\2\2\u010a\u0100\3\2\2\2\u010a\u0102\3\2\2\2\u010a"+
		"\u0104\3\2\2\2\u010a\u0106\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\3\2"+
		"\2\2\u010c\u010d\5\"\22\2\u010d\u010e\b\21\1\2\u010e\u0111\3\2\2\2\u010f"+
		"\u0111\5\"\22\2\u0110\u00fd\3\2\2\2\u0110\u010f\3\2\2\2\u0111!\3\2\2\2"+
		"\u0112\u0113\5$\23\2\u0113\u011f\b\22\1\2\u0114\u0115\7\32\2\2\u0115\u0119"+
		"\b\22\1\2\u0116\u0117\7\33\2\2\u0117\u0119\b\22\1\2\u0118\u0114\3\2\2"+
		"\2\u0118\u0116\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\5$\23\2\u011b\u011c"+
		"\b\22\1\2\u011c\u011e\3\2\2\2\u011d\u0118\3\2\2\2\u011e\u0121\3\2\2\2"+
		"\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120#\3\2\2\2\u0121\u011f\3"+
		"\2\2\2\u0122\u0123\5&\24\2\u0123\u012f\b\23\1\2\u0124\u0125\7\34\2\2\u0125"+
		"\u0129\b\23\1\2\u0126\u0127\7\35\2\2\u0127\u0129\b\23\1\2\u0128\u0124"+
		"\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\5&\24\2\u012b"+
		"\u012c\b\23\1\2\u012c\u012e\3\2\2\2\u012d\u0128\3\2\2\2\u012e\u0131\3"+
		"\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130%\3\2\2\2\u0131\u012f"+
		"\3\2\2\2\u0132\u0133\7\24\2\2\u0133\u0134\b\24\1\2\u0134\u0135\5\36\20"+
		"\2\u0135\u0136\7\25\2\2\u0136\u0137\b\24\1\2\u0137\u0141\3\2\2\2\u0138"+
		"\u013c\7\32\2\2\u0139\u013a\7\33\2\2\u013a\u013c\b\24\1\2\u013b\u0138"+
		"\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d"+
		"\u013e\5(\25\2\u013e\u013f\b\24\1\2\u013f\u0141\3\2\2\2\u0140\u0132\3"+
		"\2\2\2\u0140\u013b\3\2\2\2\u0141\'\3\2\2\2\u0142\u0143\7;\2\2\u0143\u0144"+
		"\7\24\2\2\u0144\u0145\b\25\1\2\u0145\u0146\b\25\1\2\u0146\u0147\b\25\1"+
		"\2\u0147\u0148\b\25\1\2\u0148\u0154\b\25\1\2\u0149\u014a\5\36\20\2\u014a"+
		"\u0151\b\25\1\2\u014b\u014c\7\30\2\2\u014c\u014d\5\36\20\2\u014d\u014e"+
		"\b\25\1\2\u014e\u0150\3\2\2\2\u014f\u014b\3\2\2\2\u0150\u0153\3\2\2\2"+
		"\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151"+
		"\3\2\2\2\u0154\u0149\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156"+
		"\u0157\b\25\1\2\u0157\u0158\7\25\2\2\u0158\u0159\b\25\1\2\u0159\u015a"+
		"\b\25\1\2\u015a\u0177\b\25\1\2\u015b\u015c\7;\2\2\u015c\u0177\b\25\1\2"+
		"\u015d\u015e\7;\2\2\u015e\u015f\b\25\1\2\u015f\u0160\b\25\1\2\u0160\u0166"+
		"\b\25\1\2\u0161\u0162\7\22\2\2\u0162\u0163\5\"\22\2\u0163\u0164\b\25\1"+
		"\2\u0164\u0165\7\23\2\2\u0165\u0167\3\2\2\2\u0166\u0161\3\2\2\2\u0167"+
		"\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2"+
		"\2\2\u016a\u016b\b\25\1\2\u016b\u016c\b\25\1\2\u016c\u016d\b\25\1\2\u016d"+
		"\u0177\3\2\2\2\u016e\u016f\7\'\2\2\u016f\u0177\b\25\1\2\u0170\u0171\7"+
		")\2\2\u0171\u0177\b\25\1\2\u0172\u0173\7(\2\2\u0173\u0177\b\25\1\2\u0174"+
		"\u0175\7*\2\2\u0175\u0177\b\25\1\2\u0176\u0142\3\2\2\2\u0176\u015b\3\2"+
		"\2\2\u0176\u015d\3\2\2\2\u0176\u016e\3\2\2\2\u0176\u0170\3\2\2\2\u0176"+
		"\u0172\3\2\2\2\u0176\u0174\3\2\2\2\u0177)\3\2\2\2\u0178\u0179\7\7\2\2"+
		"\u0179\u017a\b\26\1\2\u017a\u017b\5\36\20\2\u017b\u017c\b\26\1\2\u017c"+
		"\u017d\5\26\f\2\u017d\u017e\b\26\1\2\u017e+\3\2\2\2\u017f\u0180\7;\2\2"+
		"\u0180\u0181\7\24\2\2\u0181\u0182\b\27\1\2\u0182\u0183\b\27\1\2\u0183"+
		"\u0184\b\27\1\2\u0184\u0185\b\27\1\2\u0185\u0191\b\27\1\2\u0186\u0187"+
		"\5\36\20\2\u0187\u018e\b\27\1\2\u0188\u0189\7\30\2\2\u0189\u018a\5\36"+
		"\20\2\u018a\u018b\b\27\1\2\u018b\u018d\3\2\2\2\u018c\u0188\3\2\2\2\u018d"+
		"\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0192\3\2"+
		"\2\2\u0190\u018e\3\2\2\2\u0191\u0186\3\2\2\2\u0191\u0192\3\2\2\2\u0192"+
		"\u0193\3\2\2\2\u0193\u0194\b\27\1\2\u0194\u0195\7\25\2\2\u0195\u0196\b"+
		"\27\1\2\u0196\u0197\b\27\1\2\u0197\u0198\7\31\2\2\u0198-\3\2\2\2\u0199"+
		"\u019a\7\21\2\2\u019a\u019b\7\24\2\2\u019b\u019e\7;\2\2\u019c\u019d\7"+
		"\30\2\2\u019d\u019f\7(\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f"+
		"\u01a0\3\2\2\2\u01a0\u01a1\b\30\1\2\u01a1\u01a2\7\25\2\2\u01a2\u01a3\7"+
		"\31\2\2\u01a3/\3\2\2\2\u01a4\u01a5\7/\2\2\u01a5\u01a6\7\24\2\2\u01a6\u01a7"+
		"\7;\2\2\u01a7\u01a8\b\31\1\2\u01a8\u01a9\b\31\1\2\u01a9\u01aa\7\25\2\2"+
		"\u01aa\u0230\7\31\2\2\u01ab\u01ac\7\60\2\2\u01ac\u01ad\7\24\2\2\u01ad"+
		"\u01ae\7;\2\2\u01ae\u01af\b\31\1\2\u01af\u01b0\b\31\1\2\u01b0\u01b1\7"+
		"\25\2\2\u01b1\u0230\7\31\2\2\u01b2\u01b3\7\61\2\2\u01b3\u01b4\7\24\2\2"+
		"\u01b4\u01b5\7;\2\2\u01b5\u01b6\b\31\1\2\u01b6\u01b7\b\31\1\2\u01b7\u01b8"+
		"\7\25\2\2\u01b8\u0230\7\31\2\2\u01b9\u01ba\7\63\2\2\u01ba\u01bb\7\24\2"+
		"\2\u01bb\u01bc\7;\2\2\u01bc\u01bd\b\31\1\2\u01bd\u01be\b\31\1\2\u01be"+
		"\u01bf\7\25\2\2\u01bf\u0230\7\31\2\2\u01c0\u01c1\7\64\2\2\u01c1\u01c2"+
		"\7\24\2\2\u01c2\u01c3\7;\2\2\u01c3\u01c4\b\31\1\2\u01c4\u01c5\b\31\1\2"+
		"\u01c5\u01c6\7\25\2\2\u01c6\u0230\7\31\2\2\u01c7\u01c8\7\62\2\2\u01c8"+
		"\u01c9\7\24\2\2\u01c9\u01ca\7;\2\2\u01ca\u01cb\b\31\1\2\u01cb\u01cc\b"+
		"\31\1\2\u01cc\u01cd\7\25\2\2\u01cd\u0230\7\31\2\2\u01ce\u01cf\7\65\2\2"+
		"\u01cf\u01d0\7\24\2\2\u01d0\u01d1\7;\2\2\u01d1\u01d2\b\31\1\2\u01d2\u01d3"+
		"\b\31\1\2\u01d3\u01d4\7\25\2\2\u01d4\u0230\7\31\2\2\u01d5\u01d6\7.\2\2"+
		"\u01d6\u01d7\7\24\2\2\u01d7\u01d8\7;\2\2\u01d8\u01d9\b\31\1\2\u01d9\u01da"+
		"\b\31\1\2\u01da\u01db\7\25\2\2\u01db\u0230\7\31\2\2\u01dc\u01dd\7+\2\2"+
		"\u01dd\u01de\7\24\2\2\u01de\u01df\7;\2\2\u01df\u01e0\b\31\1\2\u01e0\u01e1"+
		"\b\31\1\2\u01e1\u01e2\7\25\2\2\u01e2\u0230\7\31\2\2\u01e3\u01e4\7,\2\2"+
		"\u01e4\u01e5\7\24\2\2\u01e5\u01e6\7;\2\2\u01e6\u01e7\b\31\1\2\u01e7\u01e8"+
		"\b\31\1\2\u01e8\u01e9\7\25\2\2\u01e9\u0230\7\31\2\2\u01ea\u01eb\79\2\2"+
		"\u01eb\u01ec\7\24\2\2\u01ec\u01ed\7;\2\2\u01ed\u01ee\b\31\1\2\u01ee\u01ef"+
		"\7\30\2\2\u01ef\u01f0\5(\25\2\u01f0\u01f1\7\30\2\2\u01f1\u01f2\5(\25\2"+
		"\u01f2\u01f3\b\31\1\2\u01f3\u01f4\7\25\2\2\u01f4\u01f5\7\31\2\2\u01f5"+
		"\u0230\3\2\2\2\u01f6\u01f7\7:\2\2\u01f7\u01f8\7\24\2\2\u01f8\u01f9\7;"+
		"\2\2\u01f9\u01fa\b\31\1\2\u01fa\u01fb\7\30\2\2\u01fb\u01fc\5(\25\2\u01fc"+
		"\u01fd\b\31\1\2\u01fd\u01fe\7\25\2\2\u01fe\u01ff\7\31\2\2\u01ff\u0230"+
		"\3\2\2\2\u0200\u0201\7-\2\2\u0201\u0202\7\24\2\2\u0202\u0203\7;\2\2\u0203"+
		"\u0204\b\31\1\2\u0204\u0205\b\31\1\2\u0205\u0206\7\25\2\2\u0206\u0230"+
		"\7\31\2\2\u0207\u0208\7\66\2\2\u0208\u0209\7\24\2\2\u0209\u020a\7;\2\2"+
		"\u020a\u020b\b\31\1\2\u020b\u020c\b\31\1\2\u020c\u020d\7\30\2\2\u020d"+
		"\u020e\7;\2\2\u020e\u020f\b\31\1\2\u020f\u0210\b\31\1\2\u0210\u0211\b"+
		"\31\1\2\u0211\u0212\7\25\2\2\u0212\u0230\7\31\2\2\u0213\u0214\7\66\2\2"+
		"\u0214\u0215\7\24\2\2\u0215\u0216\7;\2\2\u0216\u0217\b\31\1\2\u0217\u0218"+
		"\b\31\1\2\u0218\u0219\7\25\2\2\u0219\u0230\7\31\2\2\u021a\u021b\7\67\2"+
		"\2\u021b\u021c\7\24\2\2\u021c\u021d\7;\2\2\u021d\u021e\b\31\1\2\u021e"+
		"\u021f\b\31\1\2\u021f\u0220\7\30\2\2\u0220\u0221\7;\2\2\u0221\u0222\b"+
		"\31\1\2\u0222\u0223\b\31\1\2\u0223\u0224\b\31\1\2\u0224\u0225\7\25\2\2"+
		"\u0225\u0230\7\31\2\2\u0226\u0227\78\2\2\u0227\u0228\7\24\2\2\u0228\u0229"+
		"\7)\2\2\u0229\u022a\7\30\2\2\u022a\u022b\7)\2\2\u022b\u022c\7\30\2\2\u022c"+
		"\u022d\7\'\2\2\u022d\u022e\7\25\2\2\u022e\u0230\7\31\2\2\u022f\u01a4\3"+
		"\2\2\2\u022f\u01ab\3\2\2\2\u022f\u01b2\3\2\2\2\u022f\u01b9\3\2\2\2\u022f"+
		"\u01c0\3\2\2\2\u022f\u01c7\3\2\2\2\u022f\u01ce\3\2\2\2\u022f\u01d5\3\2"+
		"\2\2\u022f\u01dc\3\2\2\2\u022f\u01e3\3\2\2\2\u022f\u01ea\3\2\2\2\u022f"+
		"\u01f6\3\2\2\2\u022f\u0200\3\2\2\2\u022f\u0207\3\2\2\2\u022f\u0213\3\2"+
		"\2\2\u022f\u021a\3\2\2\2\u022f\u0226\3\2\2\2\u0230\61\3\2\2\2%\66;IQZ"+
		"lv~\u0083\u0088\u0098\u00a3\u00ac\u00b5\u00c4\u00d8\u00de\u00f3\u00fa"+
		"\u010a\u0110\u0118\u011f\u0128\u012f\u013b\u0140\u0151\u0154\u0168\u0176"+
		"\u018e\u0191\u019e\u022f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}