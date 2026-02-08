"""
Lexer test cases for TyC compiler
Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
# removed

# testcases submission:
def test_single_symbol_01():
    """ Testcase: 1 """
    source = "auto   AuTo "
    expected = "auto,AuTo,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_02():
    """ Testcase: 2 """
    source = "break   bReak"
    expected = "break,bReak,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_03():
    """ Testcase: 3 """
    source = "case     CasE"
    expected = "case,CasE,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_04():
    """ Testcase: 4 """
    source = "continue conTInue"
    expected = "continue,conTInue,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_05():
    """ Testcase: 5 """
    source = "default   deFaulT"
    expected = "default,deFaulT,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_06():
    """ Testcase: 6 """
    source = "else    ELSe"
    expected = "else,ELSe,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_07():
    """ Testcase: 7 """
    source = "float Float"
    expected = "float,Float,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_08():
    """ Testcase: 8 """
    source = "for FOr"
    expected = "for,FOr,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_09():
    """ Testcase: 9 """
    source = "if  iF"
    expected = "if,iF,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_10():
    """ Testcase: 10 """
    source = "int  inT"
    expected = "int,inT,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_11():
    """ Testcase: 11 """
    source = "return     RETURn"
    expected = "return,RETURn,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_12():
    """ Testcase: 12 """
    source = "string StriNG"
    expected = "string,StriNG,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_13():
    """ Testcase: 13 """
    source = "struct   STruCt"
    expected = "struct,STruCt,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_14():
    """ Testcase: 14 """
    source = "switch    sWiTcH"
    expected = "switch,sWiTcH,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_15():
    """ Testcase: 15 """
    source = "void   VoId"
    expected = "void,VoId,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_16():
    """ Testcase: 16 """
    source = "while   WHilE"
    expected = "while,WHilE,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_17():
    """ Testcase: 17 """
    source = "+ ++"
    expected = "+,++,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_18():
    """ Testcase: 18 """
    source = "- --"
    expected = "-,--,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_19():
    """ Testcase: 19 """
    source = "* / %"
    expected = "*,/,%,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_20():
    """ Testcase: 20 """
    source = "(     )"
    expected = "(,),<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_21():
    """ Testcase: 21 """
    source = "{       }"
    expected = "{,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_22():
    """ Testcase: 22 """
    source = ";      ,     :"
    expected = ";,,,:,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_23():
    """ Testcase: 23 """
    source = "!=    !    ==    ="
    expected = "!=,!,==,=,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_24():
    """ Testcase: 24 """
    source = "<     <=     >    >="
    expected = "<,<=,>,>=,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_single_symbol_25():
    """ Testcase: 25 """
    source = "||       &&"
    expected = "||,&&,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_01():
    """ Testcase: 26 """
    source = "// test line comment"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_02():
    """ Testcase: 27 """
    source = "/* test block comment*/"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_03():
    """ Testcase: 28 """
    source = "/* block comment in multi rows */"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_04():
    """ Testcase: 29 """
    source = "// keyword inside comment: if else"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_05():
    """ Testcase: 30 """
    source = "// nested comment */ // "
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_06():
    """ Testcase: 31 """
    source = "/*  another nested! */ */"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_comment_07():
    """ Testcase: 32 """
    source = "// TODO: doing something here"
    expected = "<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_01():
    """ Testcase: 33 """
    source = "0"
    expected = "0,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_02():
    """ Testcase: 34 """
    source = "24"
    expected = "24,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_03():
    """ Testcase: 35 """
    source = "2408"
    expected = "2408,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_04():
    """ Testcase: 36 """
    source = "-2005"
    expected = "-,2005,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_05():
    """ Testcase: 37 """
    source = "0.0"
    expected = "0.0,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_06():
    """ Testcase: 38 """
    source = "2e+4"
    expected = "2e+4,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_07():
    """ Testcase: 39 """
    source = "2.4e8"
    expected = "2.4e8,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_08():
    """ Testcase: 40 """
    source = "2.4E-8"
    expected = "2.4E-8,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_09():
    """ Testcase: 41 """
    source = "24.08"
    expected = "24.08,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_10():
    """ Testcase: 42 """
    source = "-2.48e-5"
    expected = "-,2.48e-5,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_11():
    """ Testcase: 43 """
    source = "-2.E1"
    expected = "-,2.E1,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_12():
    """ Testcase: 44 """
    source = ".65e-9"
    expected = ".65e-9,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_13():
    """ Testcase: 45 """
    source = "4."
    expected = "4.,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_14():
    """ Testcase: 46 """
    source = ".248"
    expected = ".248,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_15():
    """ Testcase: 47 """
    source = "0    1.5    -5     0.45e-5 "
    expected = "0,1.5,-,5,0.45e-5,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_16():
    """ Testcase: 48 """
    source = "-0.0   +0     3e3   +6E-6"
    expected = "-,0.0,+,0,3e3,+,6E-6,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_17():
    """ Testcase: 49 """
    source = "\"hello world\""
    expected = "hello world,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_18():
    """ Testcase: 50 """
    source = "\"zanis is author\""
    expected = "zanis is author,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_19():
    """ Testcase: 51 """
    source = "\"string have keyword: auto, int\""
    expected = "string have keyword: auto, int,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_20():
    """ Testcase: 52 """
    source = "\"string in multiple line \\n\""
    expected = "string in multiple line \\n,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_21():
    """ Testcase: 53 """
    source = "\"this is a tab \\t\""
    expected = "this is a tab \\t,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_22():
    """ Testcase: 54 """
    source = "\"quote quote \\\" backslashing \\\\\""
    expected = "quote quote \\\" backslashing \\\\,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_23():
    """ Testcase: 55 """
    source = "\"random \\f string @15$%566*&~\""
    expected = "random \\f string @15$%566*&~,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_24():
    """ Testcase: 56 """
    source = "\"Cam on cac thay a! \\r\""
    expected = "Cam on cac thay a! \\r,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_literal_25():
    """ Testcase: 57 """
    source = "\"UIA \\b uia 248 Zanis# \\\\ \\\" ' ' ,.!\""
    expected = "UIA \\b uia 248 Zanis# \\\\ \\\" ' ' ,.!,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_01():
    """ Testcase: 58 """
    source = "\"hello world world"
    expected = "Unclosed String: hello world world"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_02():
    """ Testcase: 59 """
    source = "\"abc\" \"xy"
    expected = "abc,Unclosed String: xy"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_03():
    """ Testcase: 60 """
    source = "\"@bc"
    expected = "Unclosed String: @bc"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_04():
    """ Testcase: 61 """
    source = "\"\\x01 \\x80\""
    expected = "Illegal Escape In String: \\x"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_05():
    """ Testcase: 62 """
    source = "\"\\abc\""
    expected = "Illegal Escape In String: \\a"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_06():
    """ Testcase: 63 """
    source = "\"illegal escape \\'\""
    expected = "Illegal Escape In String: illegal escape \\'"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_07():
    """ Testcase: 64 """
    source = "\"legal \\f and illegal \\sabotage\""
    expected = "Illegal Escape In String: legal \\f and illegal \\s"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_08():
    """ Testcase: 65 """
    source = "@"
    expected = "Error Token @"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_09():
    """ Testcase: 66 """
    source = "ab#"
    expected = "ab,Error Token #"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_10():
    """ Testcase: 67 """
    source = "$%xy"
    expected = "Error Token $"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_11():
    """ Testcase: 68 """
    source = "\"unclosed and illegal \\s escape"
    expected = "Illegal Escape In String: unclosed and illegal \\s"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_12():
    """ Testcase: 69 """
    source = "\"unclosed and legal \\f escape"
    expected = "Unclosed String: unclosed and legal \\f escape"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_exception_13():
    """ Testcase: 70 """
    source = "\"Just \\n another \\\"@ valid # string ! \\\"here  \\r\""
    expected = "Just \\n another \\\"@ valid # string ! \\\"here  \\r,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_01():
    """ Testcase: 71 """
    source = "int a;"
    expected = "int,a,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_02():
    """ Testcase: 72 """
    source = "auto b;"
    expected = "auto,b,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_03():
    """ Testcase: 73 """
    source = "float a = b = c;"
    expected = "float,a,=,b,=,c,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_04():
    """ Testcase: 74 """
    source = "a=a+4;"
    expected = "a,=,a,+,4,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_05():
    """ Testcase: 75 """
    source = "b=2*b+ (4*a / 8e-5 < c);"
    expected = "b,=,2,*,b,+,(,4,*,a,/,8e-5,<,c,),;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_06():
    """ Testcase: 76 """
    source = "return a*b*c;"
    expected = "return,a,*,b,*,c,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_07():
    """ Testcase: 77 """
    source = "a = \" hello world variable \";"
    expected = "a,=, hello world variable ,;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_08():
    """ Testcase: 78 """
    source = "-0.445-1.66"
    expected = "-,0.445,-,1.66,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_09():
    """ Testcase: 79 """
    source = "struct Point { int x; int y; };"
    expected = "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_statement_10():
    """ Testcase: 80 """
    source = "while (a<5) {a++;}"
    expected = "while,(,a,<,5,),{,a,++,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_01():
    """ Testcase: 81 """
    source = "void foo(int a, int b, int c) { return; }"
    expected = "void,foo,(,int,a,,,int,b,,,int,c,),{,return,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_02():
    """ Testcase: 82 """
    source = "void foo() {return;}"
    expected = "void,foo,(,),{,return,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_03():
    """ Testcase: 83 """
    source = "int foo() {return 5;}"
    expected = "int,foo,(,),{,return,5,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_04():
    """ Testcase: 84 """
    source = "void foo() {return 5;}"
    expected = "void,foo,(,),{,return,5,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_05():
    """ Testcase: 85 """
    source = "string foo(int a, string b) {return \"hello world\";}"
    expected = "string,foo,(,int,a,,,string,b,),{,return,hello world,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_06():
    """ Testcase: 86 """
    source = "string foo(int a, string b) {return \"hello world;}"
    expected = "string,foo,(,int,a,,,string,b,),{,return,Unclosed String: hello world;}"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_07():
    """ Testcase: 87 """
    source = "string foo(int a, string b) {return \"hello \\world\";}"
    expected = "string,foo,(,int,a,,,string,b,),{,return,Illegal Escape In String: hello \\w"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_08():
    """ Testcase: 88 """
    source = "string foo(int a, string b) {return;}"
    expected = "string,foo,(,int,a,,,string,b,),{,return,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_09():
    """ Testcase: 89 """
    source = "float foo(int a, string b, Point p) {return 5;}"
    expected = "float,foo,(,int,a,,,string,b,,,Point,p,),{,return,5,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_function_10():
    """ Testcase: 90 """
    source = "float foo(Player p, string b, Point p) {return -5.6;}"
    expected = "float,foo,(,Player,p,,,string,b,,,Point,p,),{,return,-,5.6,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_01():
    """ Testcase: 91 """
    source = """
    struct Point {
        int x;
        int y;
    };

    struct Person {
        string name;
        int age;
        float height;
    };
    """
    expected = "struct,Point,{,int,x,;,int,y,;,},;,struct,Person,{,string,name,;,int,age,;,float,height,;,},;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_02():
    """ Testcase: 92 """
    source = """
    struct Point {
        Line x;
        int y;
    };

    Point p1 = {10, 20};
    """
    expected = "struct,Point,{,Line,x,;,int,y,;,},;,Point,p1,=,{,10,,,20,},;,<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_03():
    """ Testcase: 93 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    int manhattan(Point2D p1, Point2D p2)
    {
        return p1.x-p2.x + p1.y - p2.y;
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,int,manhattan,(,Point2D,p1,,,Point2D,p2,),{,return,p1,.,x,-,p2,.,x,+,p1,.,y,-,p2,.,y,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_04():
    """ Testcase: 94 """
    source = """
    struct Point2D {
        int x;
        int y
    };

    int manhattan(Point2D p1)
    {
        return p1.x-p2.x + p1.y - p2.y;
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,},;,int,manhattan,(,Point2D,p1,),{,return,p1,.,x,-,p2,.,x,+,p1,.,y,-,p2,.,y,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_05():
    """ Testcase: 95 """
    source = """
    // comment line: defining struct Point 2D
    struct Point2D {
        int x;
        int y
    };

    /*
    There is no define of p2 and there is no absolute math function 
    */
    int manhattan(Point2D p1)
    {
        return p1.x-p2.x + p1.y - p2.y;
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,},;,int,manhattan,(,Point2D,p1,),{,return,p1,.,x,-,p2,.,x,+,p1,.,y,-,p2,.,y,;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_06():
    """ Testcase: 96 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    void printPoint(Point2D p)
    {
        printString(\"x =\");
        printInt(p.x);
        printString(\"y =\");
        printInt(p.y);
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,void,printPoint,(,Point2D,p,),{,printString,(,x =,),;,printInt,(,p,.,x,),;,printString,(,y =,),;,printInt,(,p,.,y,),;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_07():
    """ Testcase: 97 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    void printPoint(Point2D p)
    {
        printString(\"x =);
        printInt(p.x);
        printString(\"y =\");
        printInt(p.y);
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,void,printPoint,(,Point2D,p,),{,printString,(,Unclosed String: x =);\n"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_08():
    """ Testcase: 98 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    void printPoint(Point2D p)
    {
        ab@ = 1;
        printString(\"x =\");
        printInt(p.x);
        printString(\"y =\");
        printInt(p.y);
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,void,printPoint,(,Point2D,p,),{,ab,Error Token @"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_09():
    """ Testcase: 99 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    // Having legal escape
    void printPoint(Point2D p)
    {
        printString(\"x \\t=\");
        printInt(p.x);
        printString(\"y \\t=\");
        printInt(p.y);
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,void,printPoint,(,Point2D,p,),{,printString,(,x \\t=,),;,printInt,(,p,.,x,),;,printString,(,y \\t=,),;,printInt,(,p,.,y,),;,},<EOF>"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

def test_simple_program_10():
    """ Testcase: 100 """
    source = """
    struct Point2D {
        int x;
        int y;
    };

    // Having illegal escape
    void printPoint(Point2D p)
    {
        printString(\"x \\y=\");
        printInt(p.x);
        printString(\"y \\y=\");
        printInt(p.y);
    }
    """
    expected = "struct,Point2D,{,int,x,;,int,y,;,},;,void,printPoint,(,Point2D,p,),{,printString,(,Illegal Escape In String: x \\y"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected

# forum testcase
# def test_just_escape():
#     """ Testcase: 101 """
#     source = "\"hello \\\n"
#     expected = "Unclosed String: hello \\\n"
#     tokenizer = Tokenizer(source)
#     assert tokenizer.get_tokens_as_string() == expected