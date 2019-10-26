// Generated from /Users/lizzie/Documents/GitHub/lila/Lila.g4 by ANTLR 4.7.1

from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Var
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
		RULE_programa = 0, RULE_data = 1, RULE_data2 = 2, RULE_main = 3, RULE_tipo = 4, 
		RULE_funciones = 5, RULE_params = 6, RULE_estatuto = 7, RULE_condicion = 8, 
		RULE_bloque = 9, RULE_display = 10, RULE_asignacion = 11, RULE_sreturn = 12, 
		RULE_arr = 13, RULE_expresion = 14, RULE_comparacion = 15, RULE_exp = 16, 
		RULE_termino = 17, RULE_factor = 18, RULE_var_cte = 19, RULE_swhile = 20, 
		RULE_invocacion = 21, RULE_getinput = 22, RULE_especiales = 23;
	public static final String[] ruleNames = {
		"programa", "data", "data2", "main", "tipo", "funciones", "params", "estatuto", 
		"condicion", "bloque", "display", "asignacion", "sreturn", "arr", "expresion", 
		"comparacion", "exp", "termino", "factor", "var_cte", "swhile", "invocacion", 
		"getinput", "especiales"
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
			setState(48);
			match(LILA);
			setState(49);
			match(ID);
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(50);
				data();
				}
			}

			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNC) {
				{
				{
				setState(53);
				funciones();
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			main();
			gen.test_final()
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
			setState(62);
			match(VAR);
			setState(64); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(63);
				data2();
				}
				}
				setState(66); 
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
			setState(70);
			((Data2Context)_localctx).tipo = tipo();
			setState(71);
			((Data2Context)_localctx).ID = match(ID);
			Semantic.add_var(Var((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(73);
				match(COMMA);
				setState(74);
				((Data2Context)_localctx).ID = match(ID);
				Semantic.add_var(Var((((Data2Context)_localctx).ID!=null?((Data2Context)_localctx).ID.getText():null),(((Data2Context)_localctx).tipo!=null?_input.getText(((Data2Context)_localctx).tipo.start,((Data2Context)_localctx).tipo.stop):null),None))
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(81);
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
			setState(83);
			match(MAIN);
			setState(84);
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

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(LilaParser.INT, 0); }
		public TerminalNode NUM() { return getToken(LilaParser.NUM, 0); }
		public TerminalNode TEXT() { return getToken(LilaParser.TEXT, 0); }
		public TerminalNode BOOL() { return getToken(LilaParser.BOOL, 0); }
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
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACKET) {
				{
				{
				setState(87);
				match(OPEN_BRACKET);
				setState(88);
				match(CTE_INT);
				setState(89);
				match(CLOSE_BRACKET);
				}
				}
				setState(94);
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
		enterRule(_localctx, 10, RULE_funciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(FUNC);
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case NUM:
			case TEXT:
			case BOOL:
				{
				setState(96);
				((FuncionesContext)_localctx).tipo = tipo();
				}
				break;
			case VOID:
				{
				setState(97);
				((FuncionesContext)_localctx).VOID = match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(100);
			((FuncionesContext)_localctx).ID = match(ID);
			Semantic.enterFunciones((((FuncionesContext)_localctx).ID!=null?((FuncionesContext)_localctx).ID.getText():null),(((FuncionesContext)_localctx).tipo!=null?_input.getText(((FuncionesContext)_localctx).tipo.start,((FuncionesContext)_localctx).tipo.stop):null),(((FuncionesContext)_localctx).VOID!=null?((FuncionesContext)_localctx).VOID.getText():null))
			setState(102);
			match(OPEN_PARENTHESIS);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << NUM) | (1L << TEXT) | (1L << BOOL))) != 0)) {
				{
				setState(103);
				params();
				}
			}

			setState(106);
			match(CLOSE_PARENTHESIS);
			setState(107);
			match(OPEN_CURLY);
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(108);
				data();
				}
			}

			setState(112); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(111);
				estatuto();
				}
				}
				setState(114); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0) );
			setState(116);
			match(CLOSE_CURLY);
			Semantic.display_test()
			Semantic.dump_varFunt()
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
		enterRule(_localctx, 12, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			((ParamsContext)_localctx).tipo = tipo();
			setState(121);
			((ParamsContext)_localctx).ID = match(ID);
			Semantic.add_param(Var((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),''))
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(123);
				match(COMMA);
				setState(124);
				((ParamsContext)_localctx).tipo = tipo();
				setState(125);
				((ParamsContext)_localctx).ID = match(ID);
				Semantic.add_param(Var((((ParamsContext)_localctx).ID!=null?((ParamsContext)_localctx).ID.getText():null),(((ParamsContext)_localctx).tipo!=null?_input.getText(((ParamsContext)_localctx).tipo.start,((ParamsContext)_localctx).tipo.stop):null),''))
				}
				}
				setState(132);
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
		enterRule(_localctx, 14, RULE_estatuto);
		try {
			setState(141);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(135);
				swhile();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(136);
				display();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(137);
				getinput();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(138);
				invocacion();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(139);
				sreturn();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(140);
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
		enterRule(_localctx, 16, RULE_condicion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(IF);
			setState(144);
			expresion();
			gen.checkExpresion()
			setState(146);
			bloque();
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(147);
				match(ELSE);
				gen.conditionElse()
				setState(149);
				bloque();
				}
			}

			setState(152);
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
		enterRule(_localctx, 18, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(OPEN_CURLY);
			setState(156);
			estatuto();
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DISPLAY) | (1L << WHILE) | (1L << IF) | (1L << RETURN) | (1L << GETINPUT) | (1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR) | (1L << QUICKSHOW) | (1L << PEARSONCORRELATION) | (1L << NORMALDISTRIBUTION) | (1L << FILLVALUE) | (1L << REMOVEVALUE) | (1L << ID))) != 0)) {
				{
				{
				setState(157);
				estatuto();
				}
				}
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(163);
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
		enterRule(_localctx, 20, RULE_display);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(DISPLAY);
			setState(166);
			match(OPEN_PARENTHESIS);
			setState(167);
			expresion();
			gen.display()
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(169);
				match(COMMA);
				setState(170);
				expresion();
				gen.display()
				}
				}
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(178);
			match(CLOSE_PARENTHESIS);
			setState(179);
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
		enterRule(_localctx, 22, RULE_asignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			((AsignacionContext)_localctx).ID = match(ID);
			gen.addVar(Semantic.look_for_variable((((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACKET) {
				{
				{
				setState(183);
				match(OPEN_BRACKET);
				setState(184);
				exp();
				setState(185);
				match(CLOSE_BRACKET);
				}
				}
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(192);
			((AsignacionContext)_localctx).EQUAL = match(EQUAL);
			gen.addOperator((((AsignacionContext)_localctx).EQUAL!=null?((AsignacionContext)_localctx).EQUAL.getText():null))
			setState(198);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(194);
				expresion();
				gen.assign()
				}
				break;
			case 2:
				{
				setState(197);
				arr();
				}
				break;
			}
			setState(200);
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
		enterRule(_localctx, 24, RULE_sreturn);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(RETURN);
			print("Checar que funcion sea del tipo que se retorna")
			setState(204);
			expresion();
			setState(205);
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
		public List<Var_cteContext> var_cte() {
			return getRuleContexts(Var_cteContext.class);
		}
		public Var_cteContext var_cte(int i) {
			return getRuleContext(Var_cteContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
		}
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<ArrContext> arr() {
			return getRuleContexts(ArrContext.class);
		}
		public ArrContext arr(int i) {
			return getRuleContext(ArrContext.class,i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public ArrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr; }
	}

	public final ArrContext arr() throws RecognitionException {
		ArrContext _localctx = new ArrContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_arr);
		int _la;
		try {
			setState(228);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_INT:
			case CTE_STRING:
			case CTE_F:
			case CTE_BOOL:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(207);
				var_cte();
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(208);
					match(COMMA);
					setState(209);
					var_cte();
					}
					}
					setState(214);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				match(OPEN_BRACKET);
				setState(216);
				arr();
				setState(217);
				match(CLOSE_BRACKET);
				setState(225);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(218);
					match(COMMA);
					setState(219);
					match(OPEN_BRACKET);
					setState(220);
					arr();
					setState(221);
					match(CLOSE_BRACKET);
					}
					}
					setState(227);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
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
			setState(230);
			comparacion();
			gen.exitExpresion()
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(236);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(232);
					match(AND);
					gen.addOperator('AND')
					}
					break;
				case OR:
					{
					setState(234);
					match(OR);
					gen.addOperator('OR')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(238);
				comparacion();
				gen.exitExpresion()
				}
				}
				setState(245);
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
			setState(265);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				exp();
				setState(259);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GREATER_THAN:
					{
					setState(247);
					match(GREATER_THAN);
					gen.addOperator('>')
					}
					break;
				case LESS_THAN:
					{
					setState(249);
					match(LESS_THAN);
					gen.addOperator('<')
					}
					break;
				case NOTEQUAL:
					{
					setState(251);
					match(NOTEQUAL);
					gen.addOperator('!=')
					}
					break;
				case EQUALITY:
					{
					setState(253);
					match(EQUALITY);
					gen.addOperator('==')
					}
					break;
				case GREATER_THAN_EQUAL:
					{
					setState(255);
					match(GREATER_THAN_EQUAL);
					gen.addOperator('>=')
					}
					break;
				case LESS_THAN_EQUAL:
					{
					setState(257);
					match(LESS_THAN_EQUAL);
					gen.addOperator('<=')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(261);
				exp();
				gen.exitComparacion()
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
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
			setState(267);
			termino();
			gen.exitExp()
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(273);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(269);
					match(PLUS);
					gen.addOperator('+')
					}
					break;
				case MINUS:
					{
					setState(271);
					match(MINUS);
					gen.addOperator('-')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(275);
				termino();
				gen.exitExp()
				}
				}
				setState(282);
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
			setState(283);
			factor();
			gen.exitTermino()
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULTIPLICATION || _la==DIVISION) {
				{
				{
				setState(289);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(285);
					match(MULTIPLICATION);
					gen.addOperator('*')
					}
					break;
				case DIVISION:
					{
					setState(287);
					match(DIVISION);
					gen.addOperator('/')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(291);
				factor();
				gen.exitTermino()
				}
				}
				setState(298);
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
		int _la;
		try {
			setState(309);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PARENTHESIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(299);
				match(OPEN_PARENTHESIS);
				gen.addOperator('(')
				setState(301);
				expresion();
				setState(302);
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
				setState(306);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(305);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(308);
				var_cte();
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
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode CLOSE_PARENTHESIS() { return getToken(LilaParser.CLOSE_PARENTHESIS, 0); }
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(LilaParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(LilaParser.OPEN_BRACKET, i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(LilaParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(LilaParser.CLOSE_BRACKET, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LilaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LilaParser.COMMA, i);
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
			setState(343);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				((Var_cteContext)_localctx).ID = match(ID);
				gen.addVar(Semantic.look_for_variable((((Var_cteContext)_localctx).ID!=null?((Var_cteContext)_localctx).ID.getText():null)))
				setState(333);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
				case 1:
					{
					setState(319);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==OPEN_BRACKET) {
						{
						{
						setState(313);
						match(OPEN_BRACKET);
						setState(314);
						exp();
						setState(315);
						match(CLOSE_BRACKET);
						}
						}
						setState(321);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					break;
				case 2:
					{
					{
					setState(322);
					match(OPEN_PARENTHESIS);
					setState(323);
					exp();
					setState(328);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(324);
						match(COMMA);
						setState(325);
						exp();
						}
						}
						setState(330);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(331);
					match(CLOSE_PARENTHESIS);
					}
					}
					break;
				}
				}
				break;
			case CTE_INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(335);
				((Var_cteContext)_localctx).CTE_INT = match(CTE_INT);
				gen.addVar(Var(None,'int',(((Var_cteContext)_localctx).CTE_INT!=null?((Var_cteContext)_localctx).CTE_INT.getText():null)))
				}
				break;
			case CTE_F:
				enterOuterAlt(_localctx, 3);
				{
				setState(337);
				((Var_cteContext)_localctx).CTE_F = match(CTE_F);
				gen.addVar(Var(None,'num',(((Var_cteContext)_localctx).CTE_F!=null?((Var_cteContext)_localctx).CTE_F.getText():null)))
				}
				break;
			case CTE_STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(339);
				((Var_cteContext)_localctx).CTE_STRING = match(CTE_STRING);
				gen.addVar(Var(None,'text',(((Var_cteContext)_localctx).CTE_STRING!=null?((Var_cteContext)_localctx).CTE_STRING.getText():null)))
				}
				break;
			case CTE_BOOL:
				enterOuterAlt(_localctx, 5);
				{
				setState(341);
				((Var_cteContext)_localctx).CTE_BOOL = match(CTE_BOOL);
				gen.addVar(Var(None,'bool',(((Var_cteContext)_localctx).CTE_BOOL!=null?((Var_cteContext)_localctx).CTE_BOOL.getText():null)))
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
			setState(345);
			match(WHILE);
			gen.swhile()
			setState(347);
			expresion();
			gen.checkExpresion()
			setState(349);
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
			setState(352);
			match(ID);
			setState(353);
			match(OPEN_PARENTHESIS);
			setState(362);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OPEN_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_STRING) | (1L << CTE_F) | (1L << CTE_BOOL) | (1L << ID))) != 0)) {
				{
				setState(354);
				expresion();
				setState(359);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(355);
					match(COMMA);
					setState(356);
					expresion();
					}
					}
					setState(361);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(364);
			match(CLOSE_PARENTHESIS);
			setState(365);
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
			setState(367);
			match(GETINPUT);
			setState(368);
			match(OPEN_PARENTHESIS);
			setState(369);
			((GetinputContext)_localctx).ID = match(ID);
			gen.getinput(Semantic.look_for_variable((((GetinputContext)_localctx).ID!=null?((GetinputContext)_localctx).ID.getText():null)))
			setState(373);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(371);
				match(COMMA);
				setState(372);
				match(CTE_STRING);
				}
			}

			setState(375);
			match(CLOSE_PARENTHESIS);
			setState(376);
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
		enterRule(_localctx, 46, RULE_especiales);
		int _la;
		try {
			setState(426);
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
				setState(378);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GETOUTLIERS) | (1L << REMOVEOUTLIERS) | (1L << TELLMEWHATTOUSE) | (1L << PRINTMEASURES) | (1L << MEAN) | (1L << MEDIAN) | (1L << MODE) | (1L << RANGE) | (1L << MIN) | (1L << MAX) | (1L << DESESTANDAR))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(379);
				match(OPEN_PARENTHESIS);
				setState(380);
				match(ID);
				setState(381);
				match(CLOSE_PARENTHESIS);
				setState(382);
				match(SEMICOLON);
				}
				break;
			case QUICKSHOW:
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
				match(QUICKSHOW);
				setState(384);
				match(OPEN_PARENTHESIS);
				setState(385);
				match(ID);
				setState(388);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(386);
					match(COMMA);
					setState(387);
					match(ID);
					}
				}

				setState(390);
				match(CLOSE_PARENTHESIS);
				setState(391);
				match(SEMICOLON);
				}
				break;
			case PEARSONCORRELATION:
				enterOuterAlt(_localctx, 3);
				{
				setState(392);
				match(PEARSONCORRELATION);
				setState(393);
				match(OPEN_PARENTHESIS);
				setState(394);
				match(ID);
				setState(395);
				match(COMMA);
				setState(396);
				match(ID);
				setState(397);
				match(CLOSE_PARENTHESIS);
				setState(398);
				match(SEMICOLON);
				}
				break;
			case NORMALDISTRIBUTION:
				enterOuterAlt(_localctx, 4);
				{
				setState(399);
				match(NORMALDISTRIBUTION);
				setState(400);
				match(OPEN_PARENTHESIS);
				setState(401);
				match(CTE_F);
				setState(402);
				match(COMMA);
				setState(403);
				match(CTE_F);
				setState(404);
				match(COMMA);
				setState(405);
				match(CTE_INT);
				setState(406);
				match(CLOSE_PARENTHESIS);
				setState(407);
				match(SEMICOLON);
				}
				break;
			case FILLVALUE:
				enterOuterAlt(_localctx, 5);
				{
				setState(408);
				match(FILLVALUE);
				setState(409);
				match(OPEN_PARENTHESIS);
				setState(410);
				match(ID);
				setState(411);
				match(COMMA);
				setState(412);
				var_cte();
				setState(413);
				match(COMMA);
				setState(414);
				var_cte();
				setState(415);
				match(CLOSE_PARENTHESIS);
				setState(416);
				match(SEMICOLON);
				}
				break;
			case REMOVEVALUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(418);
				match(REMOVEVALUE);
				setState(419);
				match(OPEN_PARENTHESIS);
				setState(420);
				match(ID);
				setState(421);
				match(COMMA);
				setState(422);
				var_cte();
				setState(423);
				match(CLOSE_PARENTHESIS);
				setState(424);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=\u01af\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\3\2\3\2\5\2\66\n\2\3\2\7\29\n\2\f\2\16\2<\13\2\3\2\3\2\3\2\3\3\3"+
		"\3\6\3C\n\3\r\3\16\3D\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4O\n\4\f\4\16"+
		"\4R\13\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6]\n\6\f\6\16\6`\13\6\3"+
		"\7\3\7\3\7\5\7e\n\7\3\7\3\7\3\7\3\7\5\7k\n\7\3\7\3\7\3\7\5\7p\n\7\3\7"+
		"\6\7s\n\7\r\7\16\7t\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7"+
		"\b\u0083\n\b\f\b\16\b\u0086\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0090"+
		"\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0099\n\n\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\7\13\u00a1\n\13\f\13\16\13\u00a4\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\7\f\u00b0\n\f\f\f\16\f\u00b3\13\f\3\f\3\f\3\f\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\7\r\u00be\n\r\f\r\16\r\u00c1\13\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\5\r\u00c9\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17"+
		"\u00d5\n\17\f\17\16\17\u00d8\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\7\17\u00e2\n\17\f\17\16\17\u00e5\13\17\5\17\u00e7\n\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00ef\n\20\3\20\3\20\3\20\7\20\u00f4\n\20\f"+
		"\20\16\20\u00f7\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\5\21\u0106\n\21\3\21\3\21\3\21\3\21\5\21\u010c\n\21\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\5\22\u0114\n\22\3\22\3\22\3\22\7\22\u0119"+
		"\n\22\f\22\16\22\u011c\13\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0124"+
		"\n\23\3\23\3\23\3\23\7\23\u0129\n\23\f\23\16\23\u012c\13\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\5\24\u0135\n\24\3\24\5\24\u0138\n\24\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\7\25\u0140\n\25\f\25\16\25\u0143\13\25\3\25\3"+
		"\25\3\25\3\25\7\25\u0149\n\25\f\25\16\25\u014c\13\25\3\25\3\25\5\25\u0150"+
		"\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u015a\n\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\7\27\u0168\n\27\f\27"+
		"\16\27\u016b\13\27\5\27\u016d\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\5\30\u0178\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\5\31\u0187\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\5\31\u01ad\n\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34"+
		"\36 \"$&(*,.\60\2\5\3\2\f\17\3\2\32\33\3\2+\65\2\u01ce\2\62\3\2\2\2\4"+
		"@\3\2\2\2\6H\3\2\2\2\bU\3\2\2\2\nX\3\2\2\2\fa\3\2\2\2\16z\3\2\2\2\20\u008f"+
		"\3\2\2\2\22\u0091\3\2\2\2\24\u009d\3\2\2\2\26\u00a7\3\2\2\2\30\u00b7\3"+
		"\2\2\2\32\u00cc\3\2\2\2\34\u00e6\3\2\2\2\36\u00e8\3\2\2\2 \u010b\3\2\2"+
		"\2\"\u010d\3\2\2\2$\u011d\3\2\2\2&\u0137\3\2\2\2(\u0159\3\2\2\2*\u015b"+
		"\3\2\2\2,\u0162\3\2\2\2.\u0171\3\2\2\2\60\u01ac\3\2\2\2\62\63\7\4\2\2"+
		"\63\65\7;\2\2\64\66\5\4\3\2\65\64\3\2\2\2\65\66\3\2\2\2\66:\3\2\2\2\67"+
		"9\5\f\7\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2"+
		"\2=>\5\b\5\2>?\b\2\1\2?\3\3\2\2\2@B\7\t\2\2AC\5\6\4\2BA\3\2\2\2CD\3\2"+
		"\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG\b\3\1\2G\5\3\2\2\2HI\5\n\6\2IJ\7"+
		";\2\2JP\b\4\1\2KL\7\30\2\2LM\7;\2\2MO\b\4\1\2NK\3\2\2\2OR\3\2\2\2PN\3"+
		"\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\31\2\2T\7\3\2\2\2UV\7\3\2\2V"+
		"W\5\24\13\2W\t\3\2\2\2X^\t\2\2\2YZ\7\22\2\2Z[\7\'\2\2[]\7\23\2\2\\Y\3"+
		"\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\13\3\2\2\2`^\3\2\2\2ad\7\b\2\2"+
		"be\5\n\6\2ce\7\5\2\2db\3\2\2\2dc\3\2\2\2ef\3\2\2\2fg\7;\2\2gh\b\7\1\2"+
		"hj\7\24\2\2ik\5\16\b\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7\25\2\2mo\7\26"+
		"\2\2np\5\4\3\2on\3\2\2\2op\3\2\2\2pr\3\2\2\2qs\5\20\t\2rq\3\2\2\2st\3"+
		"\2\2\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\27\2\2wx\b\7\1\2xy\b\7\1\2y\r"+
		"\3\2\2\2z{\5\n\6\2{|\7;\2\2|\u0084\b\b\1\2}~\7\30\2\2~\177\5\n\6\2\177"+
		"\u0080\7;\2\2\u0080\u0081\b\b\1\2\u0081\u0083\3\2\2\2\u0082}\3\2\2\2\u0083"+
		"\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\17\3\2\2"+
		"\2\u0086\u0084\3\2\2\2\u0087\u0090\5\30\r\2\u0088\u0090\5\22\n\2\u0089"+
		"\u0090\5*\26\2\u008a\u0090\5\26\f\2\u008b\u0090\5.\30\2\u008c\u0090\5"+
		",\27\2\u008d\u0090\5\32\16\2\u008e\u0090\5\60\31\2\u008f\u0087\3\2\2\2"+
		"\u008f\u0088\3\2\2\2\u008f\u0089\3\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b"+
		"\3\2\2\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090"+
		"\21\3\2\2\2\u0091\u0092\7\13\2\2\u0092\u0093\5\36\20\2\u0093\u0094\b\n"+
		"\1\2\u0094\u0098\5\24\13\2\u0095\u0096\7\n\2\2\u0096\u0097\b\n\1\2\u0097"+
		"\u0099\5\24\13\2\u0098\u0095\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3"+
		"\2\2\2\u009a\u009b\7\31\2\2\u009b\u009c\b\n\1\2\u009c\23\3\2\2\2\u009d"+
		"\u009e\7\26\2\2\u009e\u00a2\5\20\t\2\u009f\u00a1\5\20\t\2\u00a0\u009f"+
		"\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3"+
		"\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\7\27\2\2\u00a6\25\3\2\2"+
		"\2\u00a7\u00a8\7\6\2\2\u00a8\u00a9\7\24\2\2\u00a9\u00aa\5\36\20\2\u00aa"+
		"\u00b1\b\f\1\2\u00ab\u00ac\7\30\2\2\u00ac\u00ad\5\36\20\2\u00ad\u00ae"+
		"\b\f\1\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1"+
		"\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2"+
		"\2\2\u00b4\u00b5\7\25\2\2\u00b5\u00b6\7\31\2\2\u00b6\27\3\2\2\2\u00b7"+
		"\u00b8\7;\2\2\u00b8\u00bf\b\r\1\2\u00b9\u00ba\7\22\2\2\u00ba\u00bb\5\""+
		"\22\2\u00bb\u00bc\7\23\2\2\u00bc\u00be\3\2\2\2\u00bd\u00b9\3\2\2\2\u00be"+
		"\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2"+
		"\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\7\"\2\2\u00c3\u00c8\b\r\1\2\u00c4"+
		"\u00c5\5\36\20\2\u00c5\u00c6\b\r\1\2\u00c6\u00c9\3\2\2\2\u00c7\u00c9\5"+
		"\34\17\2\u00c8\u00c4\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca"+
		"\u00cb\7\31\2\2\u00cb\31\3\2\2\2\u00cc\u00cd\7\20\2\2\u00cd\u00ce\b\16"+
		"\1\2\u00ce\u00cf\5\36\20\2\u00cf\u00d0\7\31\2\2\u00d0\33\3\2\2\2\u00d1"+
		"\u00d6\5(\25\2\u00d2\u00d3\7\30\2\2\u00d3\u00d5\5(\25\2\u00d4\u00d2\3"+
		"\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7"+
		"\u00e7\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\7\22\2\2\u00da\u00db\5"+
		"\34\17\2\u00db\u00e3\7\23\2\2\u00dc\u00dd\7\30\2\2\u00dd\u00de\7\22\2"+
		"\2\u00de\u00df\5\34\17\2\u00df\u00e0\7\23\2\2\u00e0\u00e2\3\2\2\2\u00e1"+
		"\u00dc\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2"+
		"\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00d1\3\2\2\2\u00e6"+
		"\u00d9\3\2\2\2\u00e7\35\3\2\2\2\u00e8\u00e9\5 \21\2\u00e9\u00f5\b\20\1"+
		"\2\u00ea\u00eb\7%\2\2\u00eb\u00ef\b\20\1\2\u00ec\u00ed\7&\2\2\u00ed\u00ef"+
		"\b\20\1\2\u00ee\u00ea\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\3\2\2\2"+
		"\u00f0\u00f1\5 \21\2\u00f1\u00f2\b\20\1\2\u00f2\u00f4\3\2\2\2\u00f3\u00ee"+
		"\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6"+
		"\37\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u0105\5\"\22\2\u00f9\u00fa\7\37"+
		"\2\2\u00fa\u0106\b\21\1\2\u00fb\u00fc\7\36\2\2\u00fc\u0106\b\21\1\2\u00fd"+
		"\u00fe\7 \2\2\u00fe\u0106\b\21\1\2\u00ff\u0100\7!\2\2\u0100\u0106\b\21"+
		"\1\2\u0101\u0102\7$\2\2\u0102\u0106\b\21\1\2\u0103\u0104\7#\2\2\u0104"+
		"\u0106\b\21\1\2\u0105\u00f9\3\2\2\2\u0105\u00fb\3\2\2\2\u0105\u00fd\3"+
		"\2\2\2\u0105\u00ff\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0103\3\2\2\2\u0106"+
		"\u0107\3\2\2\2\u0107\u0108\5\"\22\2\u0108\u0109\b\21\1\2\u0109\u010c\3"+
		"\2\2\2\u010a\u010c\5\"\22\2\u010b\u00f8\3\2\2\2\u010b\u010a\3\2\2\2\u010c"+
		"!\3\2\2\2\u010d\u010e\5$\23\2\u010e\u011a\b\22\1\2\u010f\u0110\7\32\2"+
		"\2\u0110\u0114\b\22\1\2\u0111\u0112\7\33\2\2\u0112\u0114\b\22\1\2\u0113"+
		"\u010f\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\5$"+
		"\23\2\u0116\u0117\b\22\1\2\u0117\u0119\3\2\2\2\u0118\u0113\3\2\2\2\u0119"+
		"\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b#\3\2\2\2"+
		"\u011c\u011a\3\2\2\2\u011d\u011e\5&\24\2\u011e\u012a\b\23\1\2\u011f\u0120"+
		"\7\34\2\2\u0120\u0124\b\23\1\2\u0121\u0122\7\35\2\2\u0122\u0124\b\23\1"+
		"\2\u0123\u011f\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126"+
		"\5&\24\2\u0126\u0127\b\23\1\2\u0127\u0129\3\2\2\2\u0128\u0123\3\2\2\2"+
		"\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b%\3"+
		"\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\7\24\2\2\u012e\u012f\b\24\1\2\u012f"+
		"\u0130\5\36\20\2\u0130\u0131\7\25\2\2\u0131\u0132\b\24\1\2\u0132\u0138"+
		"\3\2\2\2\u0133\u0135\t\3\2\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135"+
		"\u0136\3\2\2\2\u0136\u0138\5(\25\2\u0137\u012d\3\2\2\2\u0137\u0134\3\2"+
		"\2\2\u0138\'\3\2\2\2\u0139\u013a\7;\2\2\u013a\u014f\b\25\1\2\u013b\u013c"+
		"\7\22\2\2\u013c\u013d\5\"\22\2\u013d\u013e\7\23\2\2\u013e\u0140\3\2\2"+
		"\2\u013f\u013b\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142"+
		"\3\2\2\2\u0142\u0150\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7\24\2\2"+
		"\u0145\u014a\5\"\22\2\u0146\u0147\7\30\2\2\u0147\u0149\5\"\22\2\u0148"+
		"\u0146\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2"+
		"\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e\7\25\2\2\u014e"+
		"\u0150\3\2\2\2\u014f\u0141\3\2\2\2\u014f\u0144\3\2\2\2\u014f\u0150\3\2"+
		"\2\2\u0150\u015a\3\2\2\2\u0151\u0152\7\'\2\2\u0152\u015a\b\25\1\2\u0153"+
		"\u0154\7)\2\2\u0154\u015a\b\25\1\2\u0155\u0156\7(\2\2\u0156\u015a\b\25"+
		"\1\2\u0157\u0158\7*\2\2\u0158\u015a\b\25\1\2\u0159\u0139\3\2\2\2\u0159"+
		"\u0151\3\2\2\2\u0159\u0153\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0157\3\2"+
		"\2\2\u015a)\3\2\2\2\u015b\u015c\7\7\2\2\u015c\u015d\b\26\1\2\u015d\u015e"+
		"\5\36\20\2\u015e\u015f\b\26\1\2\u015f\u0160\5\24\13\2\u0160\u0161\b\26"+
		"\1\2\u0161+\3\2\2\2\u0162\u0163\7;\2\2\u0163\u016c\7\24\2\2\u0164\u0169"+
		"\5\36\20\2\u0165\u0166\7\30\2\2\u0166\u0168\5\36\20\2\u0167\u0165\3\2"+
		"\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a"+
		"\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u0164\3\2\2\2\u016c\u016d\3\2"+
		"\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7\25\2\2\u016f\u0170\7\31\2\2\u0170"+
		"-\3\2\2\2\u0171\u0172\7\21\2\2\u0172\u0173\7\24\2\2\u0173\u0174\7;\2\2"+
		"\u0174\u0177\b\30\1\2\u0175\u0176\7\30\2\2\u0176\u0178\7(\2\2\u0177\u0175"+
		"\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\7\25\2\2"+
		"\u017a\u017b\7\31\2\2\u017b/\3\2\2\2\u017c\u017d\t\4\2\2\u017d\u017e\7"+
		"\24\2\2\u017e\u017f\7;\2\2\u017f\u0180\7\25\2\2\u0180\u01ad\7\31\2\2\u0181"+
		"\u0182\7\66\2\2\u0182\u0183\7\24\2\2\u0183\u0186\7;\2\2\u0184\u0185\7"+
		"\30\2\2\u0185\u0187\7;\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187"+
		"\u0188\3\2\2\2\u0188\u0189\7\25\2\2\u0189\u01ad\7\31\2\2\u018a\u018b\7"+
		"\67\2\2\u018b\u018c\7\24\2\2\u018c\u018d\7;\2\2\u018d\u018e\7\30\2\2\u018e"+
		"\u018f\7;\2\2\u018f\u0190\7\25\2\2\u0190\u01ad\7\31\2\2\u0191\u0192\7"+
		"8\2\2\u0192\u0193\7\24\2\2\u0193\u0194\7)\2\2\u0194\u0195\7\30\2\2\u0195"+
		"\u0196\7)\2\2\u0196\u0197\7\30\2\2\u0197\u0198\7\'\2\2\u0198\u0199\7\25"+
		"\2\2\u0199\u01ad\7\31\2\2\u019a\u019b\79\2\2\u019b\u019c\7\24\2\2\u019c"+
		"\u019d\7;\2\2\u019d\u019e\7\30\2\2\u019e\u019f\5(\25\2\u019f\u01a0\7\30"+
		"\2\2\u01a0\u01a1\5(\25\2\u01a1\u01a2\7\25\2\2\u01a2\u01a3\7\31\2\2\u01a3"+
		"\u01ad\3\2\2\2\u01a4\u01a5\7:\2\2\u01a5\u01a6\7\24\2\2\u01a6\u01a7\7;"+
		"\2\2\u01a7\u01a8\7\30\2\2\u01a8\u01a9\5(\25\2\u01a9\u01aa\7\25\2\2\u01aa"+
		"\u01ab\7\31\2\2\u01ab\u01ad\3\2\2\2\u01ac\u017c\3\2\2\2\u01ac\u0181\3"+
		"\2\2\2\u01ac\u018a\3\2\2\2\u01ac\u0191\3\2\2\2\u01ac\u019a\3\2\2\2\u01ac"+
		"\u01a4\3\2\2\2\u01ad\61\3\2\2\2(\65:DP^djot\u0084\u008f\u0098\u00a2\u00b1"+
		"\u00bf\u00c8\u00d6\u00e3\u00e6\u00ee\u00f5\u0105\u010b\u0113\u011a\u0123"+
		"\u012a\u0134\u0137\u0141\u014a\u014f\u0159\u0169\u016c\u0177\u0186\u01ac";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}