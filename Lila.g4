 // Define the grammar
grammar Lila;

@header{
from IntermediateGenerator import IntermediateGenerator, Quadruple
from Classes import Semantic, Function, Operand, VirtualAddress
gen = IntermediateGenerator()
}

programa
    : LILA ID {gen.goTo()} (data)? (funciones)*  {gen.conditionEnd()} main {gen.end()} {gen.test_final()} {return gen.getObj()}
    ;

data
    : VAR data2+ {Semantic.isGlobal = False}
    ;

data2
    : tipo ID {Semantic.add_var(Operand($ID.text,$tipo.text,None))} (COMMA ID {Semantic.add_var(Operand($ID.text,$tipo.text,None))})* SEMICOLON
    ;

main
    : MAIN {gen.contextChange()} bloque
    ;

tipo
    : (INT | NUM | TEXT | BOOL) (OPEN_BRACKET CTE_INT CLOSE_BRACKET)*
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
    : IF expresion {gen.checkExpresion()} bloque (ELSE {gen.conditionElse()} bloque)? SEMICOLON {gen.conditionEnd()}
    ;

bloque
    : OPEN_CURLY estatuto (estatuto)* CLOSE_CURLY
    ;

display
    : DISPLAY OPEN_PARENTHESIS expresion {gen.display()} (COMMA expresion {gen.display()})* CLOSE_PARENTHESIS SEMICOLON
    ;
    
asignacion
    : ID {gen.addVar(Semantic.look_for_variable($ID.text))} (OPEN_BRACKET exp CLOSE_BRACKET)* EQUAL {gen.addOperator($EQUAL.text)} (expresion {gen.assign()}| arr) SEMICOLON 
    ;

sreturn
    : RETURN expresion {Semantic.checkReturn(gen.top_variables())} {gen.func_return()} SEMICOLON
    ;

arr
    : var_cte (COMMA var_cte)*
    | OPEN_BRACKET arr CLOSE_BRACKET (COMMA OPEN_BRACKET arr CLOSE_BRACKET)*
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
    | (PLUS| MINUS)? var_cte
    ;

var_cte
    : ID OPEN_PARENTHESIS {gen.incoming_Params()} {Semantic.look_for_function($ID.text)} {Semantic.isVoid($ID.text, False)} {gen.era($ID.text)} {gen.addOperator('(')} (expresion {gen.params()} (COMMA expresion {gen.params()})*)? {gen.goSub($ID.text)} CLOSE_PARENTHESIS {gen.check_params($ID.text)} {gen.finParentesis()} {gen.addFunct(Semantic.look_for_function($ID.text))}
    | ID {gen.addVar(Semantic.look_for_variable($ID.text))} (OPEN_BRACKET exp CLOSE_BRACKET)*
    | CTE_INT {gen.addConst(Operand(None,'int',$CTE_INT.text))}
    | CTE_F {gen.addConst(Operand(None,'num',$CTE_F.text))}
    | CTE_STRING {gen.addConst(Operand(None,'text',$CTE_STRING.text))}
    | CTE_BOOL {gen.addConst(Operand(None,'bool',$CTE_BOOL.text))}
    ;

swhile
    : WHILE {gen.swhile()} expresion {gen.checkExpresion()} bloque {gen.whileEnd()}
    ;

invocacion
    : ID OPEN_PARENTHESIS {Semantic.look_for_function($ID.text)} {Semantic.isVoid($ID.text, True)} {gen.era($ID.text)} {gen.addOperator('(')}  (expresion {gen.params()} (COMMA expresion {gen.params()})*)? {gen.goSub($ID.text)} CLOSE_PARENTHESIS {gen.finParentesis()} SEMICOLON
    ;

getinput
    : GETINPUT OPEN_PARENTHESIS ID (COMMA CTE_STRING)? {gen.getinput(Semantic.look_for_variable($ID.text), $CTE_STRING.text)}CLOSE_PARENTHESIS SEMICOLON
    ;

especiales
    :   (GETOUTLIERS 
        | REMOVEOUTLIERS 
        | TELLMEWHATTOUSE 
        | PRINTMEASURES 
        | MEAN 
        | MEDIAN 
        | MODE 
        | RANGE 
        | MIN 
        | MAX 
        | DESESTANDAR
            ) OPEN_PARENTHESIS ID CLOSE_PARENTHESIS SEMICOLON
    | QUICKSHOW OPEN_PARENTHESIS ID (COMMA ID)? CLOSE_PARENTHESIS SEMICOLON
    | PEARSONCORRELATION OPEN_PARENTHESIS ID COMMA ID CLOSE_PARENTHESIS SEMICOLON
    | NORMALDISTRIBUTION OPEN_PARENTHESIS CTE_F COMMA CTE_F COMMA CTE_INT CLOSE_PARENTHESIS SEMICOLON
    | FILLVALUE OPEN_PARENTHESIS ID COMMA var_cte COMMA var_cte CLOSE_PARENTHESIS SEMICOLON
    | REMOVEVALUE OPEN_PARENTHESIS ID COMMA var_cte CLOSE_PARENTHESIS SEMICOLON
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
PEARSONCORRELATION  : 'pearsoneCorrelation';
NORMALDISTRIBUTION  : 'normalDistribution';
FILLVALUE   : 'fillValue';
REMOVEVALUE : 'removeValue';

ID : [a-x]+[a-zA-Z0-9]* ;
WS : [ \t\r\n]+ -> skip ; 
Comment : '//' ~[\r\n]* -> skip ;
