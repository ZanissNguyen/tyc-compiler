import pytest
from tests.utils import Parser


def test_empty_program():
    """Testcase 1: empty_program"""
    source = """


void main() {
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_simple_struct():
    """Testcase 2: simple_struct"""
    source = """
struct Point2D {
    int x;
    int y;
};

void main() {
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_member_is_struct():
    """Testcase 3: member_is_struct"""
    source = """
struct Point3D {
    Point2D p2d;
    int z;
};

void main() {
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_longer_struct():
    """Testcase 4: longer_struct"""
    source = """
struct Student {
    string name;
    string id;
    float avgGrade;
    int height;
    int gender;
};

void main() {
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_empty_struct():
    """Testcase 5: empty_struct"""
    source = """
struct Course {
};

void main() {
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_miss_member_semi():
    """Testcase 6: miss_member_semi"""
    source = """
struct Point2D {
    int x;
    int y
};

void main() {
}
    """
    expected = "Error on line 5 col 0: }"
    assert Parser(source).parse() == expected

def test_miss_struct_endsemi():
    """Testcase 7: miss_struct_endsemi"""
    source = """
struct Point2D {
    int x;
    int y;
}

void main() {
}
    """
    expected = "Error on line 7 col 0: void"
    assert Parser(source).parse() == expected

def test_using_auto_as_member():
    """Testcase 8: using_auto_as_member"""
    source = """
struct Point2D {
    int x;
    auto y;
};

void main() {
}
    """
    expected = "Error on line 4 col 4: auto"
    assert Parser(source).parse() == expected

def test_using_void_as_member():
    """Testcase 9: using_void_as_member"""
    source = """
struct Point3D {
    Point2D p2d;
    void z;
};

void main() {
}
    """
    expected = "Error on line 4 col 4: void"
    assert Parser(source).parse() == expected

def test_empty_switch():
    """Testcase 10: empty_switch"""
    source = """


void main() {
    switch(x) {
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_multiple_default():
    """Testcase 11: switch_multiple_default"""
    source = """


void main() {
    switch(x) {
        default:
        default:
            a=a+1;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_normal_case():
    """Testcase 12: switch_normal_case"""
    source = """


void main() {
    switch(x) {
        case 0:
            a=1;
        case 1+2:
            a=2;
        case (5):
            a=3;
        case -6:
            a=4;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_forgot_colon():
    """Testcase 13: switch_forgot_colon"""
    source = """


void main() {
    switch(x) {
        case 0:
            a=1;
        case 1+2
            a=2;
    }
}
    """
    expected = "Error on line 9 col 12: a"
    assert Parser(source).parse() == expected

def test_switch_fallthrough():
    """Testcase 14: switch_fallthrough"""
    source = """


void main() {
    switch(x) {
        case a:
        case b:
            d=1;
        case c:
        default:
            d=2;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_having_break():
    """Testcase 15: switch_having_break"""
    source = """


void main() {
    switch(x) {
        case a:
        case b:
            d=1;
            break;
        case c:
           break;
        default:
            d=2;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_forgot_semi():
    """Testcase 16: switch_forgot_semi"""
    source = """


void main() {
    switch(x) {
        case a:
        case b:
            d=1;
            break
        case c:
           break;
        default:
            d=2;
    }
}
    """
    expected = "Error on line 10 col 8: case"
    assert Parser(source).parse() == expected

def test_switch_looklike_enum():
    """Testcase 17: switch_looklike_enum"""
    source = """


void main() {
    switch(a.type) {
        case A_PLUS:
            grade = 9.5;
            break;
        case A:
            grade = 8.5;
            break;
        case B:
           grade = 7.5;
           break;
        default:
            grade = 5.0;
            break;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_switch_function_call():
    """Testcase 18: switch_function_call"""
    source = """


void main() {
    switch(a.type) {
        case 0:
        case boo(3,5):
            break;
        case foo():
            printInt(b);
            break;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_one_statement():
    """Testcase 19: for_one_statement"""
    source = """


void main() {
    for (auto i = 0; i < 10; ++i) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_block_statement():
    """Testcase 20: for_block_statement"""
    source = """


void main() {
    for (auto i = 0; i < 10; ++i) {
        a = i * 2;
        printInt(a);
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_just_expression():
    """Testcase 21: for_just_expression"""
    source = """


void main() {
    for (1;1;1) {
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_init():
    """Testcase 22: for_not_init"""
    source = """


void main() {
    auto i = 0;
    for (; i < 10; ++i) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_condition():
    """Testcase 23: for_not_condition"""
    source = """


void main() {
    for (auto i = 0;; ++i) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_update():
    """Testcase 24: for_not_update"""
    source = """


void main() {
    for (auto i = 0;i<10;) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_init_condition():
    """Testcase 25: for_not_init_condition"""
    source = """


void main() {
    for (;; 1) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_condition_update():
    """Testcase 26: for_not_condition_update"""
    source = """


void main() {
    for (1;;) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_init_update():
    """Testcase 27: for_not_init_update"""
    source = """


void main() {
    for (;1;) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_not_both():
    """Testcase 28: for_not_both"""
    source = """


void main() {
    for (;;) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_for_miss_semi():
    """Testcase 29: for_miss_semi"""
    source = """


void main() {
    for (auto i = 0;i<10) printInt(i);
}
    """
    expected = "Error on line 5 col 24: )"
    assert Parser(source).parse() == expected

def test_for_comment():
    """Testcase 30: for_comment"""
    source = """


void main() {
    // test comment here
    for (auto i = 0;i<10; /* how about this*/) printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_return_void_for_unvoid_func():
    """Testcase 31: return_void_for_unvoid_func"""
    source = """


int sum(int a, int b) {
    return;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_return_unvoid_for_void_func():
    """Testcase 32: return_unvoid_for_void_func"""
    source = """


void printSum(int a, int b) {
    return a+b;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_return_just_return():
    """Testcase 33: return_just_return"""
    source = """


printSum(int a, int b) {
    return a+b;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_block_nested():
    """Testcase 34: block_nested"""
    source = """


void main() {
    {
        {
        }
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_block_unclosed():
    """Testcase 35: block_unclosed"""
    source = """


void main() {
    {
        {
        
    }
}
    """
    expected = "Error on line 10 col 4: <EOF>"
    assert Parser(source).parse() == expected

def test_vardcl_auto():
    """Testcase 36: vardcl_auto"""
    source = """


void main() {
    auto a;
    a = 5;
    auto b;
    b = \" hello world \";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_auto_init():
    """Testcase 37: vardcl_auto_init"""
    source = """


void main() {
    auto a = 5;
    auto b = \" hello world \";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_type_init():
    """Testcase 38: vardcl_type_init"""
    source = """


void main() {
    int a = 5;
    string b = \" hello world \";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_type():
    """Testcase 39: vardcl_type"""
    source = """


void main() {
    int a;
    a = 5;
    string b;
    b = \" hello world \";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_struct():
    """Testcase 40: vardcl_struct"""
    source = """


void main() {
    // point2D as {x,y} and point3D as {Point2D, z}
    Point2D p2d;
    Point3D p3d;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_struct_init():
    """Testcase 41: vardcl_struct_init"""
    source = """


void main() {
    // point2D as {x,y} and point3D as {Point2D, z}
    Point2D p2d = {2,4};
    Point3D p3d_0 = {p2d, 8};
    Point3D p3d_1 = {{20,0}, 5};
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_wrong_sematic():
    """Testcase 42: vardcl_wrong_sematic"""
    source = """


void main() {
    // parser don't care about type system
    Point2D p2d;
    p2d = 248;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_vardcl_miss_semi():
    """Testcase 43: vardcl_miss_semi"""
    source = """


void main() {
    int a = 5
    string b = \" hello world \";
}
    """
    expected = "Error on line 6 col 4: string"
    assert Parser(source).parse() == expected

def test_vardcl_void():
    """Testcase 44: vardcl_void"""
    source = """


void main() {
    void a = 5;
}
    """
    expected = "Error on line 5 col 4: void"
    assert Parser(source).parse() == expected

def test_expr_plus_01():
    """Testcase 45: expr_plus_01"""
    source = """


void main() {
    int a = 0;
    a = 2 + 4 + 8 + 2++;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_plus_02():
    """Testcase 46: expr_plus_02"""
    source = """


void main() {
    int a = 0;
    a = +(2) + (0++ + 0 + +5);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_subtract_01():
    """Testcase 47: expr_subtract_01"""
    source = """


void main() {
    int a = 0;
    a = 2 - 4 - 8-- - 2;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_subtract_02():
    """Testcase 48: expr_subtract_02"""
    source = """


void main() {
    int a = 0;
    a = -(2) - (--1 - 2 - -5--);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_multiple_01():
    """Testcase 49: expr_multiple_01"""
    source = """


void main() {
    int a = 1;
    a = a * 9 * 10;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_multiple_02():
    """Testcase 50: expr_multiple_02"""
    source = """


void main() {
    int a = 1;
    a = *a * 9 * 10;
}
    """
    expected = "Error on line 10 col 8: *"
    assert Parser(source).parse() == expected

def test_expr_div_01():
    """Testcase 51: expr_div_01"""
    source = """


void main() {
    int a = 10;
    a = a / 5 / 2;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_div_02():
    """Testcase 52: expr_div_02"""
    source = """


void main() {
    int a = 1;
    a = /a / (9 / 0);
}
    """
    expected = "Error on line 10 col 8: /"
    assert Parser(source).parse() == expected

def test_expr_mod_01():
    """Testcase 53: expr_mod_01"""
    source = """


void main() {
    int a = 10;
    a = a % 5 % 2;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_mod_02():
    """Testcase 54: expr_mod_02"""
    source = """


void main() {
    int a = 10;
    a = %a % 5 % 2;
}
    """
    expected = "Error on line 10 col 8: %"
    assert Parser(source).parse() == expected

def test_expr_arthmetic_01():
    """Testcase 55: expr_arthmetic_01"""
    source = """


void main() {
    // still accept in parser phase
    int a = \"one\";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_arthmetic_02():
    """Testcase 56: expr_arthmetic_02"""
    source = """


void main() {
    // basic math multiple operator
    auto a;
    a = 8/2+2*4-5++;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_arthmetic_03():
    """Testcase 57: expr_arthmetic_03"""
    source = """


void main() {
    // cause sematic error!
    auto a;
    a = --(b++)+3%7*\"five\";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_chained_assign_01():
    """Testcase 58: expr_chained_assign_01"""
    source = """


void main() {
    auto x;
    x = y = z = 5;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_assigment_as_child():
    """Testcase 59: expr_assigment_as_child"""
    source = """


void main() {
    auto x;
    x =5 + (z=9);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_forgot_semi():
    """Testcase 60: expr_forgot_semi"""
    source = """


void main() {
    auto x;
    x =5 + (z=9)
}
    """
    expected = "Error on line 7 col 0: }"
    assert Parser(source).parse() == expected

def test_expr_missing_operand():
    """Testcase 61: expr_missing_operand"""
    source = """


void main() {
    auto x;
    x =5 + ;
}
    """
    expected = "Error on line 6 col 10: ;"
    assert Parser(source).parse() == expected

def test_expr_greater():
    """Testcase 62: expr_greater"""
    source = """


void main() {
    a= i>a;
    b =i>=a;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_less_than():
    """Testcase 63: expr_less_than"""
    source = """


void main() {
    a = i<a;
    b = i<=a;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_relation_missing_operand():
    """Testcase 64: expr_relation_missing_operand"""
    source = """


void main() {
    a = i<;
}
    """
    expected = "Error on line 6 col 10: )"
    assert Parser(source).parse() == expected

def test_expr_is_equal():
    """Testcase 65: expr_is_equal"""
    source = """


void main() {
    a= i==5;
    b = i!=3;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_string_logic():
    """Testcase 66: expr_string_logic"""
    source = """


void main() {
    // sematic error here
    a = i ==\"hello world\";
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_complex():
    """Testcase 67: expr_complex"""
    source = """


void main() {
    c = i==3<5>=b;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_complex_missing_operand():
    """Testcase 68: expr_complex_missing_operand"""
    source = """


void main() {
    c = i==3<5>=;
}
    """
    expected = "Error on line 6 col 16: )"
    assert Parser(source).parse() == expected

def test_expr_complex_missing_semi():
    """Testcase 69: expr_complex_missing_semi"""
    source = """


void main() {
    c = i==3<5>=b
}
    """
    expected = "Error on line 7 col 0: }"
    assert Parser(source).parse() == expected

def test_expr_complex_missing_in_operand():
    """Testcase 70: expr_complex_missing_in_operand"""
    source = """


void main() {
    c = i==3<>=b;
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_expr_logic_and_relation():
    """Testcase 71: expr_logic_and_relation"""
    source = """


void main() {
    a = !(b>=1));
    b= c<=5 || a==1;
    d= a>b && a!=c;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_logic_missing_operand():
    """Testcase 72: expr_logic_missing_operand"""
    source = """


void main() {
    a = || a==1;
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_expr_logic_using_literal():
    """Testcase 73: expr_logic_using_literal"""
    source = """


void main() {
    // literal as logic operand
    b= !(-1>=1)
    a= \"huh?\" || foo();
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_another_complex():
    """Testcase 74: expr_another_complex"""
    source = """


void main() {
    a = c<=5 || !a==1 && a>b+6;
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_logic_as_return():
    """Testcase 75: expr_logic_as_return"""
    source = """


void main() {
    return !(b && \"abc\");
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_basic_access():
    """Testcase 76: expr_basic_access"""
    source = """
struct Point2D {
    int x;
    int y;
};

void main() {
    Point2D p = {10,20};
    printInt(p.x);
    printInt(p.y);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_chained_access():
    """Testcase 77: expr_chained_access"""
    source = """
struct Point2D {
    int x;
    int y;
};

struct Point3D {
    Point2D p2d;
    int z;
};

void main() {
    Point2D p = {10,20};
    Point3D p3 = {p, 30};
    printInt(p3.p2d.x);
    printInt(p3.p2d.y);
    printInt(p3.z);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_access_postfix():
    """Testcase 78: expr_access_postfix"""
    source = """
// as above testcase

void main() {
    // more postfix there, in parser phase i think it work
    Point3D p = {{10,20},30};
    p.z++;
    p.call_func();
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_expr_struct_operation():
    """Testcase 79: expr_struct_operation"""
    source = """
// as above testcase

void main () {
    Point2D p1 = {1,2};
    Point2D p2 = {4,5};
    p1 = p2;
    if (p1 == p2) printInt(p1.x); //condition is sematic error
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcdecl():
    """Testcase 80: funcdecl"""
    source = """


int add(int x, int y) {
    return x + y;
}

float multiply(float a, float b) {
    return a * b;
}

void greet(string name) {
    printString("Hello, ");
    printString(name);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcdecl_empty():
    """Testcase 81: funcdecl_empty"""
    source = """


void foo() {
}

void greet() {
    printString(\"Hello?\");
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcdecl_last_comma():
    """Testcase 82: funcdecl_last_comma"""
    source = """


int add(int x, int y,) {
    return x + y;
}

float multiply(float a, float b,) {
    return a * b;
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_funcdecl_type_infer():
    """Testcase 83: funcdecl_type_infer"""
    source = """


add(int x, int y) {
    return x + y;
}

multiply(float a, float b) {
    return a * b;
}

greet(string name) {
    printString("Hello, ");
    printString(name);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcdecl_type_auto():
    """Testcase 84: funcdecl_type_auto"""
    source = """


auto banAuto(int a, string b) {
    return 1+2;
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_if_literal():
    """Testcase 85: if_literal"""
    source = """


void main() {
    if (\"true string\") {}
    if (1) {}
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_expr():
    """Testcase 86: if_expr"""
    source = """


void main() {
    if (a>threshold) printInt(5);
    if (b<=threshold) printInt(4);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_expr_logic():
    """Testcase 87: if_expr_logic"""
    source = """


void main() {
    if (a>threshold || a<=10) printInt(5);
    if (b<=threshold && c>99) printInt(4);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_blockstmt():
    """Testcase 88: if_blockstmt"""
    source = """


void main() {
    if (1) {
    }
    if (a>5) {
        printInt(a);
        a=10;
    }
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_dangling_else_01():
    """Testcase 89: dangling_else_01"""
    source = """


void main() {
    // else for a>5 if (nearest)
    if (1) 
        if (a>5)
            printInt(a);
    else printInt(-99);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_dangling_else_02():
    """Testcase 90: dangling_else_02"""
    source = """


void main() {
    // using {} for correct scope
    if (1) {
        if (a>5)
            printInt(a);
    }
    else printInt(-99);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_empty():
    """Testcase 91: if_empty"""
    source = """


void main() {
    if () {}
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_if_empty_elsestmt():
    """Testcase 92: if_empty_elsestmt"""
    source = """


void main() {
    if (1) {}
    else;
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

def test_if_else_empty_body():
    """Testcase 93: if_else_empty_body"""
    source = """


void main() {
    if (1) {}
    else {};
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_else_nested_01():
    """Testcase 94: if_else_nested_01"""
    source = """


void main() {
    if (1) 
        if (2) 
            if (3) 
                printInt(i);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_if_else_nested_02():
    """Testcase 95: if_else_nested_02"""
    source = """


void main() {
    if (1) 
        if (2) 
            printInt(i);
        else 
            if (3) printInt(33);
            else 
                if (4) printInt(44);
                else printInt(55);
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcall():
    """Testcase 96: funcall"""
    source = """
//used functions above

void main() {
    c = add(a,b);
    d = multiple(c,\"B\"); // still accept in parser
    greet(\"Zanis\");
}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_funcall_last_comma():
    """Testcase 97: funcall_last_comma"""
    source = """
// used functions above

void main() {
    c = add(a,b,);
    d = multiple(c,\"B\",); // still accept in parser
    greet(\"Zanis\");
}
    """
    expected = "?"
    assert Parser(source).parse() == expected

