grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: (structdcl | funcdecl)* EOF;

/* ========================================
                    LEXER
   ======================================== */

// comment:
MULTI_LINE_COMMENT: '/*' .* '*/' -> skip; //ignore warning bro!
SINGLE_LINE_COMMENT: '//' ~[\n\r]* -> skip;

// type keywords:
TYPE_AUTO: 'auto';
TYPE_FLOAT: 'float';
TYPE_INT: 'int';
TYPE_STRING: 'string';
TYPE_VOID: 'void';
TYPE_STRUCT: 'struct';
// control keywords:
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FOR: 'for';
IF: 'if';
SWITCH: 'switch';
RETURN: 'return';
WHILE: 'while';
// Operators:
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_MOD: '%';
IS_EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';
LOG_OR: '||';
LOG_AND: '&&';
LOG_NOT: '!';
INCREMENT: '++';
DECREMENT: '--';
ASSIGNMENT: '=';
MEMBER_ACCESS: '.';
// separator:
LBR: '{'; 
RBR: '}'; 
LP: '('; 
RP: ')'; 
SEMI: ';'; 
COMMA: ','; 
COLON: ':';
// NEWLINE: [\n] -> skip; // count?

// literal:
LIT_INT: DIGIT+;
LIT_FLOAT: DIGIT+ '.' DIGIT*  EXPONENT?
        | '.' DIGIT+ EXPONENT?
        |  DIGIT+ EXPONENT;
fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+|-]? DIGIT+;
LIT_STRING: '"' (~["\\\r\n] | ESCAPE)* '"' {self.text = self.text[1:-1]};
fragment ESCAPE: '\\' [bfrnt"\\];

// identifier:
ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \n\t\r]+ -> skip ; // skip spaces, tabs

// exception handling
UNCLOSE_STRING: '"' (~["\\\r\n] | ESCAPE)* '\\'? ([\r]? [\n] | EOF) {
    raise UncloseString(self.text[1:])
    };
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESCAPE)* '\\' ~[bfrnt"\\\r\n] {
    raise IllegalEscape(self.text[1:])
    };
ERROR_CHAR: . { 
    raise ErrorToken(self.text); 
    };

/* ========================================
                    PARSER
   ======================================== */

// comment: MULTI_LINE_COMMENT | SINGLE_LINE_COMMENT;
type: TYPE_FLOAT
    | TYPE_INT
    | TYPE_STRING;
// void
// struct
structdcl: TYPE_STRUCT ID LBR member_list RBR SEMI;
member_list: member member_list | ;  
member: member_type ID SEMI;
member_type: type | ID;
// auto

vardecl: type ID (ASSIGNMENT or_expr)
    |    type ID   
    |    TYPE_AUTO ID (ASSIGNMENT or_expr)
    |    TYPE_AUTO ID
    |    ID ID // struct
    |    ID ID ASSIGNMENT struct_lit;
struct_lit: LBR memberdcl_prime RBR;
memberdcl_prime: memberdcl_list | ;
memberdcl_list: memberdcl COMMA memberdcl_list | memberdcl;
memberdcl: or_expr | struct_lit;

// parameter: null-able separated by comma
funcdecl: (type | TYPE_VOID | ID)? ID LP parameter_prime RP body;
parameter_prime: parameter_list | ;
parameter_list: parameter COMMA parameter_list | parameter; 
parameter: (type | ID) ID;

body: LBR statement_prime RBR;
statement_prime: statement_list | ;
statement_list: statement statement_list | ;
statement: vardecl SEMI
        | assignStmt SEMI
        | or_expr SEMI
        | body
        | ifStmt
        | whileStmt
        | forStmt
        | switchStmt
        | breakStmt
        | continueStmt
        | returnStmt;
ifStmt: IF LP expression RP statement ELSE statement
        | IF LP expression RP statement;
whileStmt: WHILE LP expression RP statement;
forStmt: FOR LP forInit SEMI forCondition SEMI forUpdate RP statement;
forInit: vardecl | assignStmt | ;
forCondition: expression | ;
forUpdate: assignStmt | prefix_expr |;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN expression SEMI
        | RETURN SEMI;
switchStmt: SWITCH LP expression RP switchBody;
switchBody: LBR case_list default_case RBR; // error: can having more than 1 default clause
case_list: normal_case case_list | ; // switch a {}
normal_case: CASE expression COLON statement_prime;
default_case: DEFAULT COLON statement_prime | ;

expression: assignStmt | or_expr;
assignable: ID | member_expr; // assignable
assignStmt: assignable ASSIGNMENT assignStmt | assignable ASSIGNMENT or_expr;
or_expr: or_expr LOG_OR and_expr | and_expr;
and_expr: and_expr LOG_AND equality_expr | equality_expr;
equality_expr: equality_expr equality compare_expr | compare_expr;
equality: IS_EQUAL | NOT_EQUAL;
compare_expr: compare_expr compare add_expr | add_expr;
compare: LESS_THAN | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL;
add_expr: add_expr add mul_expr | mul_expr;
add: OP_ADD | OP_SUB;
mul_expr: mul_expr mul unary_expr | unary_expr;
mul: OP_MUL | OP_DIV | OP_MOD;
unary_expr: unary unary_expr | prefix_expr;
unary: LOG_NOT | OP_SUB | OP_ADD;
prefix_expr: ppfix postfix_expr | postfix_expr;
postfix_expr: member_expr postfix_op* | member_expr;
postfix_op: ppfix | LP argument_prime RP;
ppfix: INCREMENT | DECREMENT;
member_expr: primary_expr member_access_tail;
member_access_tail: MEMBER_ACCESS ID member_access_tail | ;
primary_expr: LIT_INT
        | LIT_FLOAT
        | LIT_STRING
        | ID
        | struct_lit
        | LP expression RP;
argument_prime: argument_list | ;
argument_list: argument COMMA argument_list | argument;
argument: or_expr;