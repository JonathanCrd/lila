// Define the grammar
grammar Lila;

@header{
from IntermediateGenerator import IntermediateGenerator
from Classes import Semantic, Function, Var
c = IntermediateGenerator()
}

programa
    : LILA ID (data)? (funciones)* main
    ;

data
    : VAR data2+ {Semantic.isGlobal = False}
    ;

data2
    : tipo ID {Semantic.add_var(Var($ID.text,$tipo.text,''))} (COMMA ID {Semantic.add_var(Var($ID.text,$tipo.text,''))})* SEMICOLON
    ;

main
    : MAIN bloque
    ;

tipo
    : (INT | NUM | TEXT | BOOL) (OPEN_BRACKET CTE_INT CLOSE_BRACKET)*
    ;

funciones
    : FUNC (tipo | VOID) ID {Semantic.enterFunciones($ID.text,$tipo.text,$VOID.text)} OPEN_PARENTHESIS (params)? CLOSE_PARENTHESIS OPEN_CURLY (data)? (estatuto)+ CLOSE_CURLY {Semantic.dump_varFunt()}
    ;

params
    : tipo ID {Semantic.add_param(Var($ID.text,$tipo.text,''))} (COMMA tipo ID {Semantic.add_param(Var($ID.text,$tipo.text,''))})* 
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
    : IF expresion bloque (ELSE bloque)? SEMICOLON
    ;

bloque
    : OPEN_CURLY estatuto (estatuto)* CLOSE_CURLY
    ;

display
    : DISPLAY OPEN_PARENTHESIS (expresion | CTE_STRING) (COMMA (expresion | CTE_STRING))* CLOSE_PARENTHESIS SEMICOLON
    ;
    
asignacion
    : ID (OPEN_BRACKET exp CLOSE_BRACKET)* EQUAL (expresion | arr) SEMICOLON
    ;

sreturn
    : RETURN expresion SEMICOLON
    ;

arr
    : var_cte (COMMA var_cte)*
    | OPEN_BRACKET arr CLOSE_BRACKET (COMMA OPEN_BRACKET arr CLOSE_BRACKET)*
    ;

expresion
    : comparacion ((AND {c.addOperator('AND')}| OR {c.addOperator('OR')}) comparacion)*
    ;

exp
    : termino ((PLUS {c.addOperator('+')} | MINUS {c.addOperator('-')}) termino)*
    ;

termino
    : factor ((MULTIPLICATION {c.addOperator('*')}| DIVISION {c.addOperator('/')}) factor)*
    ;

factor
    : OPEN_PARENTHESIS {c.addOperator('(')}expresion CLOSE_PARENTHESIS {c.finParentesis()}
    | (PLUS| MINUS)? var_cte
    ;

comparacion
    : exp (GREATER_THAN {c.addOperator('>')}| LESS_THAN {c.addOperator('<')} | NOTEQUAL {c.addOperator('!=')}| EQUALITY {c.addOperator('==')}| GREATER_THAN_EQUAL {c.addOperator('>=')}| LESS_THAN_EQUAL {c.addOperator('<=')}) exp
    | exp
    ;

var_cte
    : ID ((OPEN_BRACKET exp CLOSE_BRACKET)* | (OPEN_PARENTHESIS exp (COMMA exp)* CLOSE_PARENTHESIS))?
    | CTE_INT
    | CTE_F
    | CTE_STRING
    | CTE_BOOL
    ;

swhile
    : WHILE expresion bloque
    ;

invocacion
    : ID OPEN_PARENTHESIS (expresion (COMMA expresion)*)? CLOSE_PARENTHESIS SEMICOLON
    ;

getinput
    : GETINPUT OPEN_PARENTHESIS ID (COMMA CTE_STRING)? CLOSE_PARENTHESIS SEMICOLON
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
