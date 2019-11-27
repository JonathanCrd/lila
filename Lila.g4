 // Define the grammar
grammar Lila;

@header{
from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Operand, VirtualAddress
gen = IntermediateGenerator()
}

programa
    : LILA ID {gen.goTo()} (data)? (funciones)*  {gen.conditionEnd()} main {gen.end()} {Semantic.display_test()}{gen.test_final()} {return gen.getObj()}
    ;

data
    : VAR data2+ {Semantic.isGlobal = False}
    ;

data2
    : (tipo | tipo array) ID {Semantic.add_var(Operand($ID.text,$tipo.text,None))} (COMMA ID {Semantic.add_var(Operand($ID.text,$tipo.text,None))})* {Semantic.reset_array_setup()} SEMICOLON
    ;

main
    : MAIN {gen.contextChange()} bloque
    ;

array
    : {Semantic.array_declaration()} (OPEN_BRACKET CTE_INT {Semantic.array_dimension($CTE_INT.text)} CLOSE_BRACKET {Semantic.array_next_dim()})* {Semantic.arr_second_round()}
    ;

tipo
    : (INT | NUM | TEXT | BOOL) 
    ;

funciones
    : FUNC (tipo | VOID) ID {index = len(gen.Quadruples)} {Semantic.enterFunciones($ID.text,$tipo.text,$VOID.text,index)} {gen.contextChange()} OPEN_PARENTHESIS (params)? CLOSE_PARENTHESIS OPEN_CURLY (data)? (estatuto)+ CLOSE_CURLY {gen.endProc()} {Semantic.end_function()}
    ;

params
    : tipo ID {Semantic.add_param(Operand($ID.text,$tipo.text,None))} (COMMA tipo ID {Semantic.add_param(Operand($ID.text,$tipo.text,None))})* 
    ;

estatuto
    : asignacion
    | condicion 
    | swhile 
    | display 
    | getinput 
    | invocacion 
    | sreturn 
    | especiales
    ;

condicion
    : IF expresion {gen.checkExpresion()} bloque (ELSE {gen.conditionElse()} bloque)?  {gen.conditionEnd()}
    ;

bloque
    : OPEN_CURLY estatuto (estatuto)* CLOSE_CURLY
    ;

display
    : DISPLAY OPEN_PARENTHESIS expresion {gen.display()} (COMMA expresion {gen.display()})* CLOSE_PARENTHESIS SEMICOLON
    ;
    
asignacion
    : (ID {gen.addVar(Semantic.look_for_variable($ID.text))} | ID {gen.addVar(Semantic.look_for_variable($ID.text))} {gen.addOperator('(')} {gen.access_array_begin()} (OPEN_BRACKET {Semantic.check_var_dim($ID.text)} exp {gen.VER($ID.text)} CLOSE_BRACKET)+ {Semantic.check_dims($ID.text)}{gen.access_array_end($ID.text)} {gen.finParentesis()}) EQUAL {gen.addOperator($EQUAL.text)} (expresion {gen.assign()}) SEMICOLON 
    ;

sreturn
    : RETURN expresion {Semantic.checkReturn(gen.top_variables())} {gen.func_return()} SEMICOLON
    ;

arr
    : OPEN_BRACKET var_cte (COMMA var_cte)* CLOSE_BRACKET (COMMA OPEN_BRACKET var_cte (COMMA var_cte)* CLOSE_BRACKET)*
    ;

expresion
    : comparacion {gen.exitExpresion()} ((AND {gen.addOperator('AND')}| OR {gen.addOperator('OR')}) comparacion {gen.exitExpresion()})* 
    ;

comparacion
    : exp (GREATER_THAN {gen.addOperator('>')}| LESS_THAN {gen.addOperator('<')} | NOTEQUAL {gen.addOperator('!=')}| EQUALITY {gen.addOperator('==')}| GREATER_THAN_EQUAL {gen.addOperator('>=')}| LESS_THAN_EQUAL {gen.addOperator('<=')}) exp {gen.exitComparacion()}
    | exp 
    ;

exp
    : termino {gen.exitExp()} ((PLUS {gen.addOperator('+')} | MINUS {gen.addOperator('-')}) termino {gen.exitExp()})*
    ;

termino
    : factor {gen.exitTermino()} ((MULTIPLICATION {gen.addOperator('*')}| DIVISION {gen.addOperator('/')}) factor {gen.exitTermino()})* 
    ;

factor
    : OPEN_PARENTHESIS {gen.addOperator('(')}expresion CLOSE_PARENTHESIS {gen.finParentesis()}
    | (PLUS| MINUS {gen.isNegative()})? var_cte {gen.makeNegative($MINUS.text)}
    ;

var_cte
    : ID OPEN_PARENTHESIS {gen.incoming_Params()} {Semantic.look_for_function($ID.text)} {Semantic.isVoid($ID.text, False)} {gen.era($ID.text)} {gen.addOperator('(')} (expresion {gen.params()} (COMMA expresion {gen.params()})*)? {gen.goSub($ID.text)} CLOSE_PARENTHESIS {gen.check_params($ID.text)} {gen.finParentesis()} {gen.addFunct(Semantic.look_for_function($ID.text))}
    | ID {gen.addVar(Semantic.look_for_variable($ID.text))}
    | ID {gen.addVar(Semantic.look_for_variable($ID.text))} {gen.addOperator('(')} {gen.access_array_begin()} ( OPEN_BRACKET exp  {gen.VER($ID.text)}  CLOSE_BRACKET)+  {Semantic.check_dims($ID.text)}{gen.access_array_end($ID.text)} {gen.finParentesis()}  
    | CTE_INT {gen.addConst(Operand(None,'int',$CTE_INT.text))}
    | CTE_F {gen.addConst(Operand(None,'num',$CTE_F.text))}
    | CTE_STRING {gen.addConst(Operand(None,'text',$CTE_STRING.text))}
    | CTE_BOOL {gen.addConst(Operand(None,'bool',$CTE_BOOL.text))}
    ;

swhile
    : WHILE {gen.swhile()} expresion {gen.checkExpresion()} bloque {gen.whileEnd()}
    ;

invocacion
    : ID OPEN_PARENTHESIS {gen.incoming_Params()} {Semantic.look_for_function($ID.text)} {Semantic.isVoid($ID.text, True)} {gen.era($ID.text)} {gen.addOperator('(')}  (expresion {gen.params()} (COMMA expresion {gen.params()})*)? {gen.goSub($ID.text)} CLOSE_PARENTHESIS {gen.check_params($ID.text)} {gen.finParentesis()} SEMICOLON
    ;

getinput
    : GETINPUT OPEN_PARENTHESIS ID (COMMA CTE_STRING)? {gen.getinput(Semantic.look_for_variable($ID.text), $CTE_STRING.text)}CLOSE_PARENTHESIS SEMICOLON
    ;

especiales
    : MEAN OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'MEAN')} CLOSE_PARENTHESIS SEMICOLON
    | MEDIAN OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'MEDIAN')} CLOSE_PARENTHESIS SEMICOLON
    | MODE OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'MODE')} CLOSE_PARENTHESIS SEMICOLON
    | MIN OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'MIN')} CLOSE_PARENTHESIS SEMICOLON
    | MAX OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'MAX')} CLOSE_PARENTHESIS SEMICOLON
    | RANGE OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'RANGE')} CLOSE_PARENTHESIS SEMICOLON
    | DESESTANDAR OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'DESESTANDAR')} CLOSE_PARENTHESIS SEMICOLON
    | PRINTMEASURES OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'PRINTMEASURES')} CLOSE_PARENTHESIS SEMICOLON
    | GETOUTLIERS OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'GETOUTLIERS')} CLOSE_PARENTHESIS SEMICOLON
    | REMOVEOUTLIERS OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'REMOVEOUTLIERS')} CLOSE_PARENTHESIS SEMICOLON
    | FILLVALUE OPEN_PARENTHESIS ID {Semantic.checkIsOneDim($ID.text)} COMMA var_cte COMMA var_cte {gen.q_fill_value($ID.text,'FILLVALUE')} CLOSE_PARENTHESIS SEMICOLON
    | REMOVEVALUE OPEN_PARENTHESIS ID {Semantic.checkIsOneDim($ID.text)} COMMA var_cte {gen.q_remove_value($ID.text,'REMOVEVALUE')} CLOSE_PARENTHESIS SEMICOLON
    | TELLMEWHATTOUSE OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.q_basics($ID.text,'TELLMEWHATTOUSE')} CLOSE_PARENTHESIS SEMICOLON
    | QUICKSHOW OPEN_PARENTHESIS ID {Semantic.checkIsOneDim($ID.text)} {gen.addVar(Semantic.look_for_variable($ID.text))} COMMA ID {Semantic.checkIsOneDim($ID.text)} {gen.addVar(Semantic.look_for_variable($ID.text))} {gen.q_twoParams($ID.text,'QUICKSHOWTWO')} CLOSE_PARENTHESIS SEMICOLON
    | QUICKSHOW OPEN_PARENTHESIS ID {Semantic.checkIsOneDim($ID.text)} {gen.q_basics($ID.text,'QUICKSHOWONE')} CLOSE_PARENTHESIS SEMICOLON
    | PEARSONCORRELATION OPEN_PARENTHESIS ID {Semantic.checkSpecialParam($ID.text)} {gen.addVar(Semantic.look_for_variable($ID.text))} COMMA ID {Semantic.checkSpecialParam($ID.text)} {gen.addVar(Semantic.look_for_variable($ID.text))} {gen.q_twoParams($ID.text,'PEARSONCORRELATION')} CLOSE_PARENTHESIS SEMICOLON
    | NORMALDISTRIBUTION OPEN_PARENTHESIS CTE_F COMMA CTE_F COMMA CTE_INT CLOSE_PARENTHESIS SEMICOLON
    ;

//TOKENS 
MAIN : 'main';
LILA    : 'lila';
VOID    : 'void';
DISPLAY   : 'display';
WHILE   : 'while';
FUNC    : 'func';
VAR     : 'var';
ELSE    : 'else';
IF      : 'if';
INT     : 'int';
NUM     : 'num';
TEXT    : 'text';
BOOL    : 'bool';
RETURN  : 'return';
GETINPUT   : 'getinput';
OPEN_BRACKET    : '[';
CLOSE_BRACKET   : ']';
OPEN_PARENTHESIS    : '(';
CLOSE_PARENTHESIS   : ')';
OPEN_CURLY  : '{';
CLOSE_CURLY : '}';
COMMA   : ',';
SEMICOLON : ';';
PLUS    : '+';
MINUS   : '-';
MULTIPLICATION  : '*';
DIVISION    : '/';
LESS_THAN   : '<';
GREATER_THAN    : '>';
NOTEQUAL   : '!=';
EQUALITY   : '==';
EQUAL   : '=';
LESS_THAN_EQUAL : '<=';
GREATER_THAN_EQUAL  : '>=';
AND : 'AND';
OR  : 'OR';

CTE_INT : ('0'..'9')+   ;
CTE_STRING: ["] ( ~["\r\n\\] | '\\' ~[\r\n] )* ["]  ; 
CTE_F: CTE_INT '.' CTE_INT  ;
CTE_BOOL: ('TRUE' | 'FALSE') ;

GETOUTLIERS : 'getOutliers';
REMOVEOUTLIERS  : 'removeOutliers';
TELLMEWHATTOUSE : 'tellMeWhatToUse';
PRINTMEASURES   : 'printMeasures';
MEAN    : 'mean';
MEDIAN  : 'median';
MODE    : 'mode';
RANGE   : 'range';
MIN     : 'min';
MAX     : 'max';
DESESTANDAR : 'desEstandar';
QUICKSHOW   : 'quickShow';
PEARSONCORRELATION  : 'pearsonCorrelation';
NORMALDISTRIBUTION  : 'normalDistribution';
FILLVALUE   : 'fillValue';
REMOVEVALUE : 'removeValue';

ID : [a-z]+[a-zA-Z0-9]* ;
WS : [ \t\r\n]+ -> skip ; 
Comment : '//' ~[\r\n]* -> skip ;
