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

program: (structdcl | vardecl SEMI | funcdecl)* EOF;

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
NEWLINE: [\n] -> skip; // count?

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

WS : [ \t\r]+ -> skip ; // skip spaces, tabs

// exception handling
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESCAPE)* '\\' ~[bfrnt"\\] {
    raise IllegalEscape(self.text[1:])
    };
UNCLOSE_STRING: '"' (~["\\\r\n] | ESCAPE)* ('\r'? '\n' | EOF) {
    raise UncloseString(self.text[1:])
    };
ERROR_CHAR: . { 
    raise ErrorToken(self.text); 
    };

/* ========================================
                    PARSER
   ======================================== */

type: TYPE_FLOAT
    | TYPE_INT
    | TYPE_STRING;
// void
// struct
structdcl: TYPE_STRUCT ID LBR member_list RBR SEMI;
member_list: member member_list | ;  
member: (type | ID) ID SEMI;
// auto

vardecl: type ID (ASSIGNMENT or_expr)?
    |    TYPE_AUTO ID (ASSIGNMENT or_expr)?
    |    ID ID // struct
    |    ID ID ASSIGNMENT LBR memberdcl_prime RBR;
memberdcl_prime: memberdcl_list | ;
memberdcl_list: memberdcl COMMA memberdcl_list | memberdcl;
memberdcl: or_expr;

assignment_expr: postfix_expr ASSIGNMENT assignment_expr | or_expr; // postfix_expr ở đây là assignable
or_expr: or_expr LOG_OR and_expr | and_expr;
and_expr: and_expr LOG_AND equality_expr | equality_expr;
equality_expr: equality_expr (IS_EQUAL | NOT_EQUAL) compare_expr | compare_expr;
compare_expr: compare_expr (LESS_THAN | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) add_expr | add_expr;
add_expr: add_expr (OP_ADD | OP_SUB) mul_expr | mul_expr;
mul_expr: mul_expr (OP_MUL | OP_DIV | OP_MOD) unary_expr | unary_expr;
unary_expr: (LOG_NOT | OP_SUB | OP_ADD) unary_expr | prefix_expr;
prefix_expr: (INCREMENT | DECREMENT) postfix_expr | postfix_expr;
postfix_expr: primary_expr postfix_op*;
postfix_op: INCREMENT | DECREMENT | MEMBER_ACCESS ID | LP argument_prime RP;
primary_expr: LIT_INT
        | LIT_FLOAT
        | LIT_STRING
        | ID
        | LP assignment_expr RP;
argument_prime: argument_list | ;
argument_list: argument COMMA argument_list | argument;
argument: or_expr;

// parameter: null-able separated by comma
funcdecl: (type | TYPE_VOID | ID) ID LP parameter_prime RP body;
parameter_prime: parameter_list | ;
parameter_list: parameter (COMMA parameter_list) | ; 
parameter: type ID;

body: LBR statement_prime RBR;
statement_prime: statement_list | ;
statement_list: statement statement_list | ;
statement: vardecl SEMI
        | assignStmt
        | body
        | ifStmt
        | whileStmt
        | forStmt
        | switchStmt
        | breakStmt
        | continueStmt
        | returnStmt;
assignStmt: assignment_expr SEMI;
ifStmt: IF LP assignment_expr RP statement ELSE statement
        | IF LP assignment_expr RP statement;
whileStmt: WHILE LP assignment_expr RP statement;
forStmt: FOR LP vardecl? SEMI assignment_expr? SEMI assignment_expr? RP statement;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN assignment_expr? SEMI
        | RETURN SEMI;
switchStmt: SWITCH LP assignment_expr RP switchBody;
switchBody: LBR case_list RBR;
case_list: case case_list | ; // switch a {}
case: case_label+ statement_list; //
case_label: CASE assignment_expr COLON | DEFAULT COLON;


