"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator

# 001: Empty program
def test_001_ast_gen_empty_program():
    source = """void main() {}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 002: Program with only main
def test_002_ast_gen_main_only():
    source = """void main() { int a; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a)]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 003: Program with comments
def test_003_ast_gen_with_comments():
    source = """// line comment\nvoid main() {/* block comment */} // end"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 004: Multiple functions and structs interleaved
def test_004_ast_gen_multiple_funcs_structs():
    source = """struct S { int x; }; void main() {} int foo() { return 1; }"""
    expected = (
        "Program([StructDecl(S, [MemberDecl(IntType(), x)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([])), "
        "FuncDecl(IntType(), foo, [], BlockStmt([ReturnStmt(return IntLiteral(1))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 005: Empty struct
def test_005_ast_gen_empty_struct():
    source = """struct Empty {}; void main() {}"""
    expected = "Program([StructDecl(Empty, []), FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 006: Struct with another struct as member
def test_006_ast_gen_struct_with_struct_member():
    source = """struct A { int x; }; struct B { A a; }; void main() {}"""
    expected = (
        "Program([StructDecl(A, [MemberDecl(IntType(), x)]), "
        "StructDecl(B, [MemberDecl(StructType(A), a)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 007: Self-referencing struct (syntax only)
def test_007_ast_gen_self_ref_struct():
    source = """struct Node { Node next; }; void main() {}"""
    expected = (
        "Program([StructDecl(Node, [MemberDecl(StructType(Node), next)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 008: Function declaration void/no params
def test_008_ast_gen_func_void_no_params():
    source = """void foo() {} void main() {}"""
    expected = (
        "Program([FuncDecl(VoidType(), foo, [], BlockStmt([])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 009: Function declaration int with params
def test_009_ast_gen_func_int_with_params():
    source = """int sum(int a, int b) { return a + b; } void main() {}"""
    expected = (
        "Program([FuncDecl(IntType(), sum, [Param(IntType(), a), Param(IntType(), b)], "
        "BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 010: Function declaration with struct params
def test_010_ast_gen_function_struct_params():
    source = """
struct Point {
    int x;
    int y;
};

void foo(Point p) {
}
"""
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), foo, [Param(StructType(Point), p)], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 011: Function inference (no return type)
def test_011_ast_gen_function_inference():
    source = """
foo() {
    return 1;
}
"""
    expected = (
        "Program([FuncDecl(auto, foo, [], BlockStmt([ReturnStmt(return IntLiteral(1))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 012: Return with literal, variable
def test_012_ast_gen_return_literal_variable():
    source = """
int foo() {
    int a = 10;
    return a;
}
"""
    expected = (
        "Program([FuncDecl(IntType(), foo, [], BlockStmt(["
        "VarDecl(IntType(), a = IntLiteral(10)), "
        "ReturnStmt(return Identifier(a))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 013: Return with function call
def test_013_ast_gen_return_function_call():
    source = """
int bar() {
    return foo();
}
"""
    expected = (
        "Program([FuncDecl(IntType(), bar, [], BlockStmt(["
        "ReturnStmt(return FuncCall(foo, []))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 014: Variable declaration with normal type
def test_014_ast_gen_var_decl_normal_type():
    source = """
void main() {
    int a;
    float b;
    string s;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a), "
        "VarDecl(FloatType(), b), "
        "VarDecl(StringType(), s)]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 015: Variable declaration having normal type init
def test_015_ast_gen_var_decl_with_init():
    source = """
void main() {
    int a = 5;
    float b = 2.5;
    string c = \" Hello \";
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = IntLiteral(5)), "
        "VarDecl(FloatType(), b = FloatLiteral(2.5)), "
        "VarDecl(StringType(), c = StringLiteral(' Hello '))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 016: Variable declaration with struct type
def test_016_ast_gen_struct_var_decl():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point p;
}
"""
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 017: Variable declaration having struct init
def test_017_ast_gen_struct_init():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point p = {1, 2};
}
"""
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
            "VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 018: Variable declaration having struct nested init
def test_018_ast_gen_struct_nested_init():
    source = """
struct Point {
    int x;
    int y;
};

struct Line {
    Point a;
    Point b;
};

void main() {
    Line l = {{1,2}, {3,4}};
}
"""
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "StructDecl(Line, [MemberDecl(StructType(Point), a), MemberDecl(StructType(Point), b)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
            "VarDecl(StructType(Line), l = StructLiteral({StructLiteral({IntLiteral(1), IntLiteral(2)}), StructLiteral({IntLiteral(3), IntLiteral(4)})}))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 019: Using auto
def test_019_ast_gen_auto_type():
    source = """
void main() {
    auto a = 10;
    auto b = foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(auto, a = IntLiteral(10)), "
        "VarDecl(auto, b = FuncCall(foo, []))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


# 020: Using expression, function call as initializer
def test_020_ast_gen_expression_initializer():
    source = """
void main() {
    int a = 1 + 2 * 3;
    int b = foo(1, 2) + bar();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = BinaryOp(IntLiteral(1), +, BinaryOp(IntLiteral(2), *, IntLiteral(3)))), "
        "VarDecl(IntType(), b = BinaryOp(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]), +, FuncCall(bar, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 021: unary expression
def test_021_ast_gen_unary():
    source = """
void main() {
    int a = -5;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = PrefixOp(-IntLiteral(5)))"
        "]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 022: nested unary expression
def test_022_ast_gen_nested_unary():
    source = """
void main() {
    int b = -(+(-5));
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), b = PrefixOp(-PrefixOp(+PrefixOp(-IntLiteral(5)))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 023: normal arithmetic expression (+,-,*,/)
def test_023_ast_gen_arithmetic():
    source = """
void main() {
    a = 1 + 3;
    b = 4 - b;
    c = 7 * a;
    d = 35 / b;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = BinaryOp(IntLiteral(1), +, IntLiteral(3)))), "
        "ExprStmt(AssignExpr(Identifier(b) = BinaryOp(IntLiteral(4), -, Identifier(b)))), "
        "ExprStmt(AssignExpr(Identifier(c) = BinaryOp(IntLiteral(7), *, Identifier(a)))), "
        "ExprStmt(AssignExpr(Identifier(d) = BinaryOp(IntLiteral(35), /, Identifier(b))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 024: nested arithmetic expression
def test_024_ast_gen_nested_arithmetic():
    source = """
void main() {
    int c = (1 + 2) * (3 - 4);
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), c = BinaryOp("
        "BinaryOp(IntLiteral(1), +, IntLiteral(2)), *, "
        "BinaryOp(IntLiteral(3), -, IntLiteral(4)))"
        ")]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 025: complex expression with multiple operators and parentheses
def test_025_ast_gen_long_chain_arithmetic():
    source = """
void main() {
    int d = 1 + 2 - 3 * (4 / 5) % 2;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), d = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), -, "
        "BinaryOp(BinaryOp(IntLiteral(3), *, BinaryOp(IntLiteral(4), /, IntLiteral(5))), %, IntLiteral(2))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 026: another complex example as above
def test_026_ast_gen_long_chain_arithmetic():
    source = """
void main() {
    int a = -(ab + c * 5 - 7) % -(d + 1) / 3;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = "
        "BinaryOp(BinaryOp("
        "PrefixOp(-BinaryOp(BinaryOp(Identifier(ab), +, BinaryOp(Identifier(c), *, IntLiteral(5))), -, IntLiteral(7))), "
        "%, "
        "PrefixOp(-BinaryOp(Identifier(d), +, IntLiteral(1)))), "
        "/, "
        "IntLiteral(3)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 027: Relational expression
def test_027_ast_gen_relational():
    source = """
void main() {
    int e = 5 > 3;
    a < 6;
    c >= 5;
    d <= 9;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), e = BinaryOp(IntLiteral(5), >, IntLiteral(3))), "
        "ExprStmt(BinaryOp(Identifier(a), <, IntLiteral(6))), "
        "ExprStmt(BinaryOp(Identifier(c), >=, IntLiteral(5))), "
        "ExprStmt(BinaryOp(Identifier(d), <=, IntLiteral(9)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 028: Equality expression
def test_028_ast_gen_equality():
    source = """
void main() {
    a == f;
    a != 6;
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(BinaryOp(Identifier(a), ==, Identifier(f))), "
        "ExprStmt(BinaryOp(Identifier(a), !=, IntLiteral(6)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 029: Chained relational expression
def test_029_ast_gen_chained_relational():
    source = """
void main() {
    a < b >= c < e == 1 != foo();
}
"""
#   (((((a < b) >= c) < e) == 1) != foo())
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(BinaryOp(BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), >=, Identifier(c)), <, Identifier(e)), ==, IntLiteral(1)), !=, FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 030: Logical
def test_030_ast_gen_logical():
    source = """
void main() {
    a && b;
    c || d;
    !e;
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(BinaryOp(Identifier(a), &&, Identifier(b))), "
        "ExprStmt(BinaryOp(Identifier(c), ||, Identifier(d))), "
        "ExprStmt(PrefixOp(!Identifier(e)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 031: Logical priority / chained
def test_031_ast_gen_chained_logical():
    source = """
void main() {
    int a = a || b && !foo() && !(4 || 5);
}
"""
#   (a || ((b && (!foo())) && (!(4 || 5))))
    expected = ( #TODO
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = "
        "BinaryOp(Identifier(a), ||, "
        "BinaryOp(BinaryOp(Identifier(b), &&, PrefixOp(!FuncCall(foo, []))), &&, PrefixOp(!BinaryOp(IntLiteral(4), ||, IntLiteral(5))))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 032: Prefix, postfix
def test_032_ast_gen_pre_post_fix():
    source = """
void main() {
    int a = b++;
    int c = --c;
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = PostfixOp(Identifier(b)++)), "
        "VarDecl(IntType(), c = PrefixOp(--Identifier(c)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 033: Chained assignment
def test_033_ast_gen_chained_assignment():
    source = """
void main() {
    a = b = c = d = 2;
}
"""
    # (a = (b = (c = (d = 2))))
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = AssignExpr(Identifier(d) = IntLiteral(2))))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 034: assign as subexpression
def test_034_ast_gen_assign_subexpr():
    source = """
void main() {
    a = b + (c=d);
}
"""
    # (a = (b + (c=d)))
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, AssignExpr(Identifier(c) = Identifier(d)))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 035: struct assignment
def test_035_ast_gen_struct_assignment():
    source = """
void main() {
    a = {1, 3};
}
"""
    # (a = {1, 3})
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = StructLiteral({IntLiteral(1), IntLiteral(3)})))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 036: struct member assignment
def test_036_ast_gen_struct_member_assignment():
    source = """
void main() {
    a.b = {2, 5};
}
"""
    # (a.b = {2, 5})
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = StructLiteral({IntLiteral(2), IntLiteral(5)})))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 037: struct member access
def test_037_ast_gen_struct_member_access():
    source = """
void main() {
    a.b;
    e = p.x;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(MemberAccess(Identifier(a).b)), ExprStmt(AssignExpr(Identifier(e) = MemberAccess(Identifier(p).x)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 038: struct member chained
def test_038_ast_gen_struct_member_chained():
    source = """
void main() {
    a.b.c.d.e;
    c = p.x.y.z.f;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(MemberAccess(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d).e)), "
        "ExprStmt(AssignExpr(Identifier(c) = MemberAccess(MemberAccess(MemberAccess(MemberAccess(Identifier(p).x).y).z).f)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 039: struct member pre/post fix
def test_039_ast_gen_struct_member_pre_post_fix():
    source = """
void main() {
    a.b++;
    --x.y.z;
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(PostfixOp(MemberAccess(Identifier(a).b)++)), "
        "ExprStmt(PrefixOp(--MemberAccess(MemberAccess(Identifier(x).y).z)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 040: function that return a struct
def test_040_ast_gen_struct_from_function():
    source = """
void main() {
    foo().x;
    bar().y.z = a + b;
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(MemberAccess(FuncCall(foo, []).x)), "
        "ExprStmt(AssignExpr(MemberAccess(MemberAccess(FuncCall(bar, []).y).z) = BinaryOp(Identifier(a), +, Identifier(b))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 041: simple function call
def test_041_ast_gen_simple_funccall():
    source = """
int foo() {}
int bar(int a, int b) {}
void main() {
    foo();
    bar(1,2);
}
"""
    expected = ( 
        "Program([FuncDecl(IntType(), foo, [], BlockStmt([])), "
        "FuncDecl(IntType(), bar, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([])), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(FuncCall(foo, [])), "
        "ExprStmt(FuncCall(bar, [IntLiteral(1), IntLiteral(2)]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 042: nested function call
def test_042_ast_gen_nested_funccall():
    source = """
int foo() {}
int bar(int a, int b) {}
void main() {
    foo();
    bar(foo(),b+c);
}
"""
    expected = ( 
        "Program([FuncDecl(IntType(), foo, [], BlockStmt([])), "
        "FuncDecl(IntType(), bar, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([])), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(FuncCall(foo, [])), "
        "ExprStmt(FuncCall(bar, [FuncCall(foo, []), BinaryOp(Identifier(b), +, Identifier(c))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 043: struct as argument
def test_043_ast_gen_struct_argument():
    source = """
int foo() {}
int bar(S s, int b) {}
void main() {
    foo();
    bar({1,3,5});
}
"""
    expected = ( 
        "Program([FuncDecl(IntType(), foo, [], BlockStmt([])), "
        "FuncDecl(IntType(), bar, [Param(StructType(S), s), Param(IntType(), b)], BlockStmt([])), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(FuncCall(foo, [])), "
        "ExprStmt(FuncCall(bar, [StructLiteral({IntLiteral(1), IntLiteral(3), IntLiteral(5)})]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 044: complex expression
def test_044_ast_gen_complex_expression():
    source = """
void main() {
    string a = \"Complex one\";
    b = -a + d >= e && !(6e-2 / 9.7) % foo() * \"mul\";
}
"""
# b = ((((-a) + d) >= e) && ((!(6e-2 / 9.7) % (foo())) * \"mul\"));
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(StringType(), a = StringLiteral('Complex one')), "
        "ExprStmt(AssignExpr(Identifier(b) = BinaryOp(BinaryOp(BinaryOp(PrefixOp(-Identifier(a)), +, Identifier(d)), >=, Identifier(e)), &&, BinaryOp(BinaryOp(PrefixOp(!BinaryOp(FloatLiteral(0.06), /, FloatLiteral(9.7))), %, FuncCall(foo, [])), *, StringLiteral('mul')))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 045: Simple if statement
def test_045_ast_gen_if_simple():
    source = """
void main() {
    if (1) {
        printInt(b);
    }
}
"""
    expected = ( 
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "IfStmt(if IntLiteral(1) then BlockStmt([ExprStmt(FuncCall(printInt, [Identifier(b)]))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 046: Dangling if-else statement (chain)
def test_046_ast_gen_dangling_if_else_chain():
    source = """
void main() {
    if (a)
        if (b)
            foo();
        else
            bar();
}
"""
    expected = (
        "Program(["
        "FuncDecl(VoidType(), main, [], BlockStmt(["
        "IfStmt(if Identifier(a) then "
            "IfStmt(if Identifier(b) then ExprStmt(FuncCall(foo, [])), "
            "else ExprStmt(FuncCall(bar, []))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 047: Nested if-else statement
def test_047_ast_gen_nested_if_else():
    source = """
void main() {
    if (a) {
        if (b) {
            foo();
        } else {
            bar();
        }
    } else {
        baz();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "IfStmt(if Identifier(a) then BlockStmt(["
            "IfStmt(if Identifier(b) then BlockStmt(["
                "ExprStmt(FuncCall(foo, []))]), "
            "else BlockStmt(["
                "ExprStmt(FuncCall(bar, []))]))]), "
        "else BlockStmt([ExprStmt(FuncCall(baz, []))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 048: for statement - empty
def test_048_ast_gen_for_empty():
    source = """
void main() {
    for (;;)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for None; None; None do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 049: simple for statement (normal)
def test_049_ast_gen_for_normal():
    source = """
void main() {
    for (i = 0; i < 10; i = i + 1)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 050: missing init
def test_050_ast_gen_for_missing_init():
    source = """
void main() {
    for (; i < 10; i = i + 1)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 051: missing condition
def test_051_ast_gen_for_missing_condition():
    source = """
void main() {
    for (i = 0; ; i = i + 1)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); None; AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 052: missing update
def test_052_ast_gen_for_missing_update():
    source = """
void main() {
    for (i = 0; i < 10;)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 053: missing both init_condition
def test_053_ast_gen_for_missing_init_condition():
    source = """
void main() {
    for (;; i = i + 1)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for None; None; AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 054: missing both init_update
def test_054_ast_gen_for_missing_init_update():
    source = """
void main() {
    for (; i < 10;)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 055: missing both condition_update
def test_055_ast_gen_for_missing_condition_update():
    source = """
void main() {
    for (i = 0;;)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); None; None do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 056: assign a struct var in init
def test_056_ast_gen_for_struct_assign():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point p;
    for (p = Point(1,2); i < 10; i = i + 1)
        foo();
}
"""
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
            "VarDecl(StructType(Point), p), "
            "ForStmt(for AssignExpr(Identifier(p) = FuncCall(Point, [IntLiteral(1), IntLiteral(2)])); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
                "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 057: using function call in for composition
def test_057_ast_gen_for_function_call():
    source = """
void main() {
    for (i = init(); check(); update())
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = FuncCall(init, [])); FuncCall(check, []); FuncCall(update, []) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 058: nested for
def test_058_ast_gen_nested_for():
    source = """
void main() {
    for (i = 0; i < 10; i = i + 1)
        for (j = 0; j < 5; j = j + 1)
            foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ForStmt(for AssignExpr(Identifier(j) = IntLiteral(0)); BinaryOp(Identifier(j), <, IntLiteral(5)); AssignExpr(Identifier(j) = BinaryOp(Identifier(j), +, IntLiteral(1))) do "
                "ExprStmt(FuncCall(foo, []))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 059: using auto assignment in init
def test_059_ast_gen_for_auto_init():
    source = """
void main() {
    auto i = 0;
    for (i = 0; i < 10; i = i + 1)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(auto, i = IntLiteral(0)), "
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 060: empty switch
def test_060_ast_gen_empty_switch():
    source = """
void main() {
    switch (a) {
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases [])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 061: switch having only case (no default)
def test_061_ast_gen_switch_case_only():
    source = """
void main() {
    switch (a) {
        case 1:
            foo();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(1): ["
                "ExprStmt(FuncCall(foo, []))])])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 062: switch having only default
def test_062_ast_gen_switch_default_only():
    source = """
void main() {
    switch (a) {
        default:
            foo();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases [], "
            "default DefaultStmt(default: ["
                "ExprStmt(FuncCall(foo, []))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 063: a normal switch
def test_063_ast_gen_normal_switch():
    source = """
void main() {
    switch (a) {
        case 1:
            foo();
        case 2:
            bar();
        default:
            baz();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(1): ["
                "ExprStmt(FuncCall(foo, []))]), "
            "CaseStmt(case IntLiteral(2): ["
                "ExprStmt(FuncCall(bar, []))])], "
            "default DefaultStmt(default: ["
                "ExprStmt(FuncCall(baz, []))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 064: using function call, expression in case_expression
def test_064_ast_gen_case_expression():
    source = """
void main() {
    switch (a) {
        case foo():
            bar();
        case 1 + 2:
            baz();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case FuncCall(foo, []): ["
                "ExprStmt(FuncCall(bar, []))]), "
            "CaseStmt(case BinaryOp(IntLiteral(1), +, IntLiteral(2)): ["
                "ExprStmt(FuncCall(baz, []))])])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 065: the downthrough of cases
def test_065_ast_gen_switch_fallthrough():
    source = """
void main() {
    switch (a) {
        case 1:
        case 2:
            foo();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(1): []), "
            "CaseStmt(case IntLiteral(2): ["
                "ExprStmt(FuncCall(foo, []))])])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 066: using constant in case_expression as normal
def test_066_ast_gen_case_constant():
    source = """
void main() {
    switch (a) {
        case 10:
            foo();
        case 20:
            bar();
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(10): ["
                "ExprStmt(FuncCall(foo, []))]), "
            "CaseStmt(case IntLiteral(20): ["
                "ExprStmt(FuncCall(bar, []))])])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 067: empty while
def test_067_ast_gen_empty_while():
    source = """
void main() {
    while (a) {}
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do BlockStmt([]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 068: a normal while
def test_068_ast_gen_normal_while():
    source = """
void main() {
    while (a < 10)
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "WhileStmt(while BinaryOp(Identifier(a), <, IntLiteral(10)) do "
            "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 069: while using function call
def test_069_ast_gen_while_function_call():
    source = """
void main() {
    while (check())
        foo();
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "WhileStmt(while FuncCall(check, []) do "
        "ExprStmt(FuncCall(foo, [])))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 070: nested while
def test_070_ast_gen_nested_while():
    source = """
void main() {
    while (a) {
        while (b) {
            b--;
        }
        a--;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "WhileStmt(while Identifier(a) do BlockStmt(["
            "WhileStmt(while Identifier(b) do BlockStmt(["
                "ExprStmt(PostfixOp(Identifier(b)--))])), "
            "ExprStmt(PostfixOp(Identifier(a)--))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 071: using break, continue in while, for
def test_071_ast_gen_break_continue():
    source = """
void main() {
    for(i=0;i<10;i++){
        if(i==5) continue;
        if(i==8) break;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt(["
            "IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then ContinueStmt()), "
            "IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(8)) then BreakStmt())]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 072: using break in switch
def test_072_ast_gen_break_switch():
    source = """
void main() {
    switch(a){
        case 1:
            break;
        default:
            break;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(1): ["
                "BreakStmt()])], "
            "default DefaultStmt(default: ["
                "BreakStmt()]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 073: return statement with and without expression
def test_073_ast_gen_return_forms():
    source = """
int foo(){ return 1; }
void bar(){ return; }
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), foo, [], BlockStmt(["
            "ReturnStmt(return IntLiteral(1))])), "
        "FuncDecl(VoidType(), bar, [], BlockStmt(["
            "ReturnStmt(return)])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 074: a statement block
def test_074_ast_gen_block_stmt():
    source = """
void main(){
    {
        int a;
        a=1;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "BlockStmt(["
            "VarDecl(IntType(), a), "
            "ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 075: empty statement block
def test_075_ast_gen_empty_block():
    source = """
void main(){
    {}
}
"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([])]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 076: nested statement block
def test_076_ast_gen_nested_block():
    source = """
void main(){
    {
        {
            int a;
        }
    }
}
"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([BlockStmt([VarDecl(IntType(), a)])])]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 077: chained relational tricky
def test_077_ast_gen_relational_chain():
    source = """
void main(){ a < b >= c < d; }
"""
    # (((a < b) >= c) < d)
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
            "ExprStmt(BinaryOp(BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), >=, Identifier(c)), <, Identifier(d)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 078: chained logical tricky
def test_078_ast_gen_logical_chain():
    source = """
void main(){ a || b && c || d; }
"""
# ((a || (b && c)) || d)
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(BinaryOp(BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c))), ||, Identifier(d)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 079: assignment inside parentheses in a tricky expression
def test_079_ast_gen_assign_paren():
    source = """
void main(){ a = b + !(c=d) * e / f && 5 > 6; }
"""
# a = ((b + (((!(c=d)) * e) / f)) && (5 > 6))
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = "
        "BinaryOp(BinaryOp(Identifier(b), +, BinaryOp(BinaryOp(PrefixOp(!AssignExpr(Identifier(c) = Identifier(d))), *, Identifier(e)), /, Identifier(f))), &&, BinaryOp(IntLiteral(5), >, IntLiteral(6)))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 080: nested function calls
def test_080_ast_gen_nested_calls():
    source = """
void main(){ foo(bar(baz(1))); }
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(FuncCall(foo, [FuncCall(bar, [FuncCall(baz, [IntLiteral(1)])])]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 081: mixing relational and logical operators
def test_081_mix_relational_logical():
    source = """
void main() {
    int a = a>=b && c<d || !(e!=f); 
}
"""
    # (((a>=b) && (c<d)) || (!(e!=f)))
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "VarDecl(IntType(), a = "
        "BinaryOp(BinaryOp(BinaryOp(Identifier(a), >=, Identifier(b)), &&, BinaryOp(Identifier(c), <, Identifier(d))), ||, PrefixOp(!BinaryOp(Identifier(e), !=, Identifier(f)))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 082: complex arithmetic
def test_082_ast_gen_complex_expr():
    source = """
void main(){ a + b * c - d / e % f; }
"""
# ((a + (b * c)) - ((d / e) % f))
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))), -, BinaryOp(BinaryOp(Identifier(d), /, Identifier(e)), %, Identifier(f))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 083: postfix chain
def test_083_ast_gen_postfix_chain():
    source = """
void main(){ a++++; }
"""
# ((a++)++)
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PostfixOp(PostfixOp(Identifier(a)++)++))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# 084: nested assignments
def test_084_ast_gen_nested_assign():
    source = """
void main(){ a = b = c = e.xyz = d = foo(); }
"""
# (a = (b = (c = ((e.xyz) = (d = foo()))))) 
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = AssignExpr(MemberAccess(Identifier(e).xyz) = AssignExpr(Identifier(d) = FuncCall(foo, [])))))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 085: struct member assignment
def test_085_ast_gen_struct_member_assign():
    source = """
struct A{int x;};
void main(){ A a; a.x = 1; }
"""
    expected = (
        "Program(["
        "StructDecl(A, [MemberDecl(IntType(), x)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt(["
            "VarDecl(StructType(A), a), "
            "ExprStmt(AssignExpr(MemberAccess(Identifier(a).x) = IntLiteral(1)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 086: for with call in update
def test_086_ast_gen_for_call_update():
    source = """
void main(){
    for(i=0;i<10;inc(i)){
        printInt(i);
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); FuncCall(inc, [Identifier(i)]) do "
            "BlockStmt([ExprStmt(FuncCall(printInt, [Identifier(i)]))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 087: nested for and while
def test_087_ast_gen_nested_loops():
    source = """
void main(){
    for(i=0;i<10;i++){
        while(j){
            j--;
        }
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do "
        "BlockStmt(["
            "WhileStmt(while Identifier(j) do "
            "BlockStmt(["
                "ExprStmt(PostfixOp(Identifier(j)--))]))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 088: switch inside loop
def test_088_ast_gen_switch_loop():
    source = """
void main(){
    while(a){
        switch(a){
            case 1: break;
        }
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "WhileStmt(while Identifier(a) do "
        "BlockStmt(["
            "SwitchStmt(switch Identifier(a) cases ["
                "CaseStmt(case IntLiteral(1): ["
                    "BreakStmt()])])]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 089: if inside switch
def test_089_ast_gen_if_switch():
    source = """
void main(){
    switch(a){
        case 1:
            if(a) a=1;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt(["
        "SwitchStmt(switch Identifier(a) cases ["
            "CaseStmt(case IntLiteral(1): ["
                "IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))))])])]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 090: program power calculation
def test_090_ast_gen_power_program():
    source = """
int pow(int a,int b){
    int r;
    r=1;
    for(i=0;i<b;i++){
        r=r*a;
    }
    return r;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), pow, [Param(IntType(), a), Param(IntType(), b)], "
        "BlockStmt(["
            "VarDecl(IntType(), r), "
            "ExprStmt(AssignExpr(Identifier(r) = IntLiteral(1))), "
            "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(b)); PostfixOp(Identifier(i)++) do "
            "BlockStmt(["
                "ExprStmt(AssignExpr(Identifier(r) = BinaryOp(Identifier(r), *, Identifier(a))))])), "
            "ReturnStmt(return Identifier(r))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 091: sum program
def test_091_ast_gen_sum_program():
    source = """
int sum(int n){
    int s;
    s=0;
    for(i=0;i<n;i++){
        s=s+i;
    }
    return s;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), sum, [Param(IntType(), n)], "
        "BlockStmt(["
            "VarDecl(IntType(), s), "
            "ExprStmt(AssignExpr(Identifier(s) = IntLiteral(0))), "
            "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); PostfixOp(Identifier(i)++) do "
            "BlockStmt(["
                "ExprStmt(AssignExpr(Identifier(s) = BinaryOp(Identifier(s), +, Identifier(i))))])), "
            "ReturnStmt(return Identifier(s))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 092: factorial
def test_092_ast_gen_factorial():
    source = """
int fact(int n){
    if(n==0) return 1;
    return n*fact(n-1);
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), fact, [Param(IntType(), n)], "
        "BlockStmt(["
            "IfStmt(if BinaryOp(Identifier(n), ==, IntLiteral(0)) then ReturnStmt(return IntLiteral(1))), "
            "ReturnStmt(return BinaryOp(Identifier(n), *, FuncCall(fact, [BinaryOp(Identifier(n), -, IntLiteral(1))])))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 093: area circle
def test_093_ast_gen_area_circle():
    source = """
float area(float r){
    return 3.14*r*r;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(FloatType(), area, [Param(FloatType(), r)], "
        "BlockStmt(["
            "ReturnStmt(return BinaryOp(BinaryOp(FloatLiteral(3.14), *, Identifier(r)), *, Identifier(r)))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 094: student grade
def test_094_ast_gen_grade():
    source = """
int grade(int s){
    if(s>90) return 4;
    if(s>75) return 3;
    return 2;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), grade, [Param(IntType(), s)], "
        "BlockStmt(["
            "IfStmt(if BinaryOp(Identifier(s), >, IntLiteral(90)) then ReturnStmt(return IntLiteral(4))), "
            "IfStmt(if BinaryOp(Identifier(s), >, IntLiteral(75)) then ReturnStmt(return IntLiteral(3))), "
            "ReturnStmt(return IntLiteral(2))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 095: electricity bill
def test_095_ast_gen_bill():
    source = """
int bill(int k){
    if(k<50) return k*2;
    return k*3;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), bill, [Param(IntType(), k)], "
        "BlockStmt(["
            "IfStmt(if BinaryOp(Identifier(k), <, IntLiteral(50)) then ReturnStmt(return BinaryOp(Identifier(k), *, IntLiteral(2)))), "
            "ReturnStmt(return BinaryOp(Identifier(k), *, IntLiteral(3)))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 096: fibonacci iterative
def test_096_ast_gen_fib():
    source = """
int fib(int n){
    int a; int b; int c;
    a=0; b=1;
    for(i=2;i<n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    return b;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), fib, [Param(IntType(), n)], "
        "BlockStmt(["
            "VarDecl(IntType(), a), "
            "VarDecl(IntType(), b), "
            "VarDecl(IntType(), c), "
            "ExprStmt(AssignExpr(Identifier(a) = IntLiteral(0))), "
            "ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), "
            "ForStmt(for AssignExpr(Identifier(i) = IntLiteral(2)); BinaryOp(Identifier(i), <, Identifier(n)); PostfixOp(Identifier(i)++) do "
            "BlockStmt(["
                "ExprStmt(AssignExpr(Identifier(c) = BinaryOp(Identifier(a), +, Identifier(b)))), "
                "ExprStmt(AssignExpr(Identifier(a) = Identifier(b))), "
                "ExprStmt(AssignExpr(Identifier(b) = Identifier(c)))])), "
            "ReturnStmt(return Identifier(b))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 097: max of two
def test_097_ast_gen_max():
    source = """
int max(int a,int b){
    if(a>b) return a;
    return b;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), max, [Param(IntType(), a), Param(IntType(), b)], "
        "BlockStmt(["
            "IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then ReturnStmt(return Identifier(a))), "
            "ReturnStmt(return Identifier(b))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 098: min of three
def test_098_ast_gen_min_three():
    source = """
int min3(int a,int b,int c){
    int m;
    m=a;
    if(b<m) m=b;
    if(c<m) m=c;
    return m;
}
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), min3, [Param(IntType(), a), Param(IntType(), b), Param(IntType(), c)], "
        "BlockStmt(["
            "VarDecl(IntType(), m), "
            "ExprStmt(AssignExpr(Identifier(m) = Identifier(a))), "
            "IfStmt(if BinaryOp(Identifier(b), <, Identifier(m)) then ExprStmt(AssignExpr(Identifier(m) = Identifier(b)))), "
            "IfStmt(if BinaryOp(Identifier(c), <, Identifier(m)) then ExprStmt(AssignExpr(Identifier(m) = Identifier(c)))), "
            "ReturnStmt(return Identifier(m))])), "
        "FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 099: simple calculator
def test_099_ast_gen_calculator():
    source = """
int add(int a,int b){ return a+b; }
int sub(int a,int b){ return a-b; }
void main(){}
"""
    expected = (
        "Program(["
        "FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], "
        "BlockStmt(["
            "ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))])), "
        "FuncDecl(IntType(), sub, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), -, Identifier(b)))])), FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected

# 100: 2d squared O distance
def test_100_ast_gen_2d_squared_O_distance():
    source = """
struct Point{int x; int y;};
int O_sq_dist(Point p){
    return p.x*p.x + p.y*p.y;
}
void main(){}
"""
# (((p.x)*(p.x)) + ((p.y)*(p.y)))
    expected = (
        "Program(["
        "StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(IntType(), O_sq_dist, [Param(StructType(Point), p)], "
        "BlockStmt(["
            "ReturnStmt(return BinaryOp(BinaryOp(MemberAccess(Identifier(p).x), *, MemberAccess(Identifier(p).x)), +, BinaryOp(MemberAccess(Identifier(p).y), *, MemberAccess(Identifier(p).y))))])), FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected
