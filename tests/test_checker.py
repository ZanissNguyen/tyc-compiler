"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_010)
# ============================================================================

def test_001_program_empty():
    source = """void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_002_entrypoint_no():
    source = """void add() {
}
"""
    expected = "UndeclaredFunction(main)"
    assert Checker(source).check_from_source() == expected

def test_003_entrypoint_wrong():
    source = """int main() {
}
"""
    expected = "TypeMismatchInExpression(FuncCall(main, []))"
    assert Checker(source).check_from_source() == expected

def test_004_entrypoint_wrong():
    source = """void main(int x, int y) {
}
"""
    expected = "TypeMismatchInExpression(FuncCall(main, []))"
    assert Checker(source).check_from_source() == expected

def test_005_builtin_valid():
    source = """void main() {
    printInt(1);
    printFloat(2.4);
    printString(\"Zanis\");
    readInt();
    readFloat();
    readString();
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006_builtin_wrong():
    source = """void main() {
    printInt(0.8);
    printFloat(4);
    printString(\"Zanis\");
    readInt();
    readFloat();
    readString();
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printInt, [FloatLiteral(0.8)]))"
    assert Checker(source).check_from_source() == expected

def test_007_structDecl_valid():
    source = """struct Point {
    int x;
    int y;
};

void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008_struct_recursive():
    source = """struct Node {
    int value;
    Node next;
};

void main() {
}
"""
    expected = "UndeclaredStruct(Node)"
    assert Checker(source).check_from_source() == expected

def test_009_member_as_struct():
    source = """struct Point2d {
    int x;
    int y;
};
struct Point3d {
    Point2d p;
    int z;
};

void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010_struct_redeclared():
    source = """struct Point2d {
    int x;
    int y;
};
struct Point2d {
    int z;
    int w;
};

void main() {
}
"""
    expected = "Redeclared(Struct, Point2d)"
    assert Checker(source).check_from_source() == expected

def test_011_member_redeclared():
    source = """struct Point2d {
    int x;
    int x;
};

void main() {
}
"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_012_struct_equivalent():
    source = """struct A {
    int a;
    int b;
};
struct B {
    int x;
    int y;
};

void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013_namespace_district():
    source = """struct A {
    int a;
    int b;
};
void A() {
}

void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_014_function_declared():
    source = """void printSum(int x, int y) {
    printInt(x+y);
}

void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_015_function_redeclared():
    source = """void A() {
}
// Redeclared as name, no overloading!
int A(int z) {
    return z*2;
}

void main() {
}
"""
    expected = "Redeclared(Function, A)"
    assert Checker(source).check_from_source() == expected

def test_016_params_redeclared():
    source = """void A(int x, int x) {
}

void main() {
}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_017_params_local_redeclared():
    source = """void A(int x) {
    int x;
}

void main() {
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_018_params_local_nested_redeclared():
    source = """void A(int x) {
    {
        {
            int x;
        }
    }
}

void main() {
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_019_variable_declared():
    source = """void main() {
    int x;
    float y;
    string z;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020_variable_redeclared():
    source = """void main() {
    int x;
    float x;
    string x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_021_variable_declared_init():
    source = """void main() {
    int x = 2.48;
    float x = \"Hello\";
}
"""
    expected = "TypeMismatchInStatement(VarDecl(IntType(), x = FloatLiteral(2.48)))"
    assert Checker(source).check_from_source() == expected

def test_022_auto_not_used():
    source = """void main() {
    auto x;
    auto y;
    auto z;
}
"""
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x), VarDecl(auto, y), VarDecl(auto, z)]))"
    assert Checker(source).check_from_source() == expected

def test_023_auto_not_used_nested():
    source = """void main() {
    {
        auto x;
        {
            auto y;
        }
        auto z;
    }
}
"""
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, y)]))"
    assert Checker(source).check_from_source() == expected

def test_024_variable_auto_valid():
    source = """void main() {
    auto x = 5; // infer int
    auto y = 3.14; // infer float
    auto z = \"Hello\"; // infer string
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_025_variable_auto_cannot_infer():
    source = """void main() {
    auto x;
    auto y = x; // cannot be infer
}
"""
    expected = "TypeCannotBeInferred(y)"
    assert Checker(source).check_from_source() == expected

def test_026_variable_auto_chain_infer():
    source = """void main() {
    auto x = 5; // as int
    auto y = x; // infer as int
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_027_variable_auto_infer_typemismatch():
    source = """void main() {
    auto x = 5;
    float y = x; // x as int so type mismatch
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), y = Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_028_assign_statement():
    source = """void main() {
    auto x;
    x = 5;
    float y;
    y = 3.14;
    string z;
    z = \"Hello\"; 
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_029_assign_typemismatch():
    source = """void main() {
    auto x;
    x = 5;
    float y;
    y = 3; // type mismatch int assigned to float
    string z;
    z = \"Hello\"; 
}
"""
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(y) = IntLiteral(3)))"
    assert Checker(source).check_from_source() == expected

def test_030_assign_auto():
    source = """void main() {
    auto x;
    auto y;
    x = y; // both x and y are auto and cannot infer type
}
"""
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(x) = Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_031_assign_basic_expression():
    source = """void main() {
    auto x = 5;
    auto y = 3.14 + x;
    float z = y / 2; // Float / int is float
    int w = 2408;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_032_block_scope():
    source = """void main() {
    int x = 5;
    {
        int x = 10; // valid shawdowing outer x
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_033_block_scope():
    source = """void main() {
    int x = 5;
    {
        int x = 10; // valid shawdowing outer x
        printFloat(x); // x in this scope is int so type mismatch
    }
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printFloat, [Identifier(x)]))"
    assert Checker(source).check_from_source() == expected

def test_034_bin_expression_arithmetic():
    source = """void main() {
    int x;
    x = 5 + 4;
    float y = 4.5 - 8;
    float z = 0.5 * 2.0;
    float w = 4.8 / 5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_035_bin_expression_arithmetic_error():
    source = """void main() {
    int x = 5;
    string text = "hello";
    
    int sum = x + text;     // Error: TypeMismatchInExpression at binary operation
    float result = x * text; // Error: TypeMismatchInExpression at binary operation
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_036_bin_expression_mod_error():
    source = """void main() {
    4 % 3.6; // type mismatch: float is not allow in mod
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(4), %, FloatLiteral(3.6)))"
    assert Checker(source).check_from_source() == expected

def test_037_bin_expression_have_auto():
    source = """void main() {
    int x;
    auto y;
    y+x; // y can infer as int so this is valid
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_038_chained_assign_error():
    source = """void main() {
    int x = 10;
    string text = "hello";
    float f = 3.14;
    
    int result = (x = text) + 5;     // Error: TypeMismatchInExpression at assignment expression (int = string)
    int value = (x = f) + 3;         // Error: TypeMismatchInExpression at assignment expression (int = float)
}
"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_039_chained_assign_error():
    # TODO: checking lhs not literal or experssion it must be access member or Id
    source = """void main() {
    int x = 5;
    int y = (5 = x) + 3;             // Error: TypeMismatchInExpression at assignment expression (cannot assign to literal)
    int z = ((x + 1) = 10) + 2;      // Error: TypeMismatchInExpression at assignment expression (cannot assign to expression)
}
"""
    expected = "TypeMismatchInExpression(AssignExpr(IntLiteral(5) = Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_040_expression_comparison_proper():
    source = """void main() {
    // ["==", "!=", "<", "<=", ">", ">="]:
    int x;
    int q;
    float y;
    float z;

    auto w = x == q; // comparison output is Int
    printInt(w); // checking is w int
    w = x != y;
    printInt(w); // checking again
    y < x;
    y >= z;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_041_expression_comparison_error():
    source = """void main() {
    // ["==", "!=", "<", "<=", ">", ">="]:
    int x;

    auto z = x <= \"Zanis\";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), <=, StringLiteral('Zanis')))"
    assert Checker(source).check_from_source() == expected

def test_042_expression_logical_proper():
    source = """void main() {
    // ["||", "&&"]:
    int x;
    int y;

    auto z = x || y && x;
    printInt(z);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_043_expression_logical_error():
    source = """void main() {
    float f = 3.14;
    int x = 10;
    
    int result = f && x;     // Error: TypeMismatchInExpression at binary operation
    int not = !f;            // Error: TypeMismatchInExpression at unary operation
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_044_error_order():
    source = """void main() {
    auto x;
    auto y;
    auto x = x + y; // type cannot be infer > redeclared
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_045_return_auto():
    source = """void main() {
}
// Error: return uses an auto that still has no type (inferred-return function; needs `void main()` in full program)
func() {
    auto x;
    return x;  // TypeCannotBeInferred(ReturnStmt(return Identifier(x)))
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_046_binary_infer():
    source = """void main() {
    auto value;
    auto result = value + 5;  // Valid: value inferred as int (other operand is IntLiteral 5)
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_047_postfix_proper():
    source = """void main() {
    int a;
    a++;
    (a+5)--;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_048_postfix_error():
    source = """void main() {
    int a;
    a++;
    (a+5.9)--; // Type mismatch (a+5.9)--
}
"""
    expected = "TypeMismatchInStatement(PostfixOp(BinaryOp(Identifier(a), +, FloatLiteral(5.9))--))"
    assert Checker(source).check_from_source() == expected

def test_049_prefix_proper():
    source = """void main() {
    int a;
    float b;
    -a;
    +b;
    ++a;
    --(a+2);
    !(a >= 1);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_050_prefix_error():
    source = """void main() {
    int a;
    float b;
    -a;
    +b;
    ++a;
    --(b+2); // type mismatch --(b+2) because b is float
    !\"Zanis\"; // type mismatch !\"Zanis\"
}
"""
    expected = "TypeMismatchInStatement(PrefixOp(--BinaryOp(Identifier(b), +, IntLiteral(2))))"
    assert Checker(source).check_from_source() == expected

def test_051_prefix_infer():
    source = """void main() {
    auto x;
    auto y = ++x; // y and x infer as int
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_052_prefix_infer():
    source = """void main() {
    auto x;
    auto y = -x; // - operator can infer as int or float so cannot be inferred
}
"""
    expected = "TypeCannotBeInferred(PrefixOp(-Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_053_postfix_infer():
    source = """void main() {
    auto x;
    auto y = x--; // x and y infer as int
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_054_function_declare_proper():
    source = """int add(int x, int y) {
    return x + y;
}
    
void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_055_function_declare_redeclared():
    source = """int add(int x, int y) {
    return x + y;
}

float add(float a, float b) {
    return a + b;
}
    
void main() {
}
"""
    expected = "Redeclared(Function, add)"
    assert Checker(source).check_from_source() == expected

def test_056_function_declare_redeclared_param():
    source = """int add(int x, int x) {
    return x + x;
}
    
void main() {
}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_057_function_declare_redeclared_local():
    source = """int add(int x, int y) {
    int x = 5; // redeclared x as local variable
    return x + x;
}
    
void main() {
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_058_function_declare_redeclared_nested():
    source = """int add(int x, int y) {
    {
        {
            {
                int x = 5; // redeclared x as local variable although it is nested
            }
        }
    }
    return x + y;
}
    
void main() {
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_059_function_declare_no_return_type(): # inferred
    source = """add(int x, int y) {
    return x + y; // infer as int
}
    
void main() {
    printInt(add(5, 3)); // check if add is inferred as int
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_060_function_declare_return_type_mismatch():
    source = """int pi() {
    return 3.14; // type mismatch: return float in function declared to return int
}
    
void main() {
}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_061_function_declare_return_auto(): # can not inferred
    source = """float foo() {
    auto x;
    return x; // x cannot be infer here, there is no rule
}
    
void main() {
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_062_function_recursive():
    source = """int foo(int x) {
    return foo(x-1);
}
    
void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_063_function_recursive_auto():
    source = """foo() {
    return foo();
}
    
void main() {
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return FuncCall(foo, [])))"
    assert Checker(source).check_from_source() == expected

def test_064_type_inference_binary_op():
    source = """void main() {
    auto a;
    auto b;
    int c = a * b;  // TypeCannotBeInferred(BinaryOp(Identifier(a), *, Identifier(b)))
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(a), *, Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_065_string_mix():
    source = """void main() {
    auto x;
    auto y;  // unused here; failure is reported on the next line’s initializer
    auto result = x + "hello";  // TypeCannotBeInferred(BinaryOp(Identifier(x), +, StringLiteral('hello')))
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_066_function_infer_recursive_proper():
    source = """f(int x) {
    if (x >= 1) return 10; // the first return statement -> f inferred as int
    return f(x-1); // so the return type is clearly here
}
    
void main() {
    printInt(f(5)); // checking if f is int?
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_067_function_infer_recursive_proper():
    source = """f(int x) {
    if (x <= 1) return f(x-1); // ở vòng infer này không suy luận được gì thì 
    return 5; // thì sẽ xem tiếp hay type cannot be infer luôn
}
    
void main() {
    printInt(f(5)); // checking if f is int?
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return FuncCall(f, [BinaryOp(Identifier(x), -, IntLiteral(1))])))"
    assert Checker(source).check_from_source() == expected

def test_068_function_no_return_and_type():
    source = """f(int x) {
    printInt(x);
}
    
void main() {
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_069_undeclared_variable():
    source = """// Error: Undeclared Variable
void example() {
    int result = undeclaredVar + 10;  // UndeclaredIdentifier(undeclaredVar)
}
"""
    expected = "UndeclaredIdentifier(undeclaredVar)"
    assert Checker(source).check_from_source() == expected

def test_070_used_before_declared():
    source = """// Error: Using variable before declaration in same scope
void test() {
    int x = y + 5;  // UndeclaredIdentifier(y) - y used before declaration
    int y = 10;
}
"""
    expected = "UndeclaredIdentifier(y)"
    assert Checker(source).check_from_source() == expected

def test_071_out_of_scope():
    source = """// Error: Out of scope access
void method1() {
    int localVar = 42;
}

void method2() {
    int value = localVar + 1;  // UndeclaredIdentifier(localVar) - different function scope
}
"""
    expected = "UndeclaredIdentifier(localVar)"
    assert Checker(source).check_from_source() == expected

def test_072_enclosing_scope():
    source = """// Valid: Variable in enclosing scope
void main() {
    int outer = 10;
    {
        int inner = outer + 5;  // Valid: outer is in enclosing scope
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_073_member_access_undeclared_struct():
    source = """void main() {
    Point p;
    p.x;
}
"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

def test_074_member_access_non_struct_access():
    source = """void main() {
    int p;
    p.x;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).x))"
    assert Checker(source).check_from_source() == expected

def test_075_member_access_no_member():
    source = """struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.z;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).z))"
    assert Checker(source).check_from_source() == expected

def test_076_member_access_assign():
    source = """struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_077_member_access_used_in_expression():
    source = """struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    int x = p.x + 5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_078_infer_from_member_access():
    source = """struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    auto x = p.x; // x as int
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_079_chained_access_proper():
    source = """struct Point2d {
    int x;
    int y;
};

struct Point3d {
    Point2d p;
    float z;
};

void main() {
    Point3d p;
    p.p.x; // return Point2d x attribute
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_080_chained_access_infer():
    source = """struct Point2d {
    int x;
    int y;
};

struct Point3d {
    Point2d p;
    float z;
};

void main() {
    Point3d p;

    auto y = p.p.y; // as int
    printInt(y);
    auto z = p.z; // as float
    printFloat(z);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_081_expr_stmt_error_scope():
    source = """void main() {
    int a;
    a++;
    (a+\"Zanis\")--; // Type mismatch - expr (a+\"Zanis\")
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(a), +, StringLiteral('Zanis')))"
    assert Checker(source).check_from_source() == expected

def test_082_struct_literal_init_proper():
    source = """struct Point2d {
    int x;
    int y;
};
    
struct Point3d {
    Point2d p;
    int z;    
};

void main() {
    Point2d p = {1,2};
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_083_struct_literal_init_error():
    source = """struct Point2d {
    int x;
    int y;
};
    
struct Point3d {
    Point2d p;
    int z;    
};

void main() {
    Point2d p = {1.5,2};
    Point2d p2 = {1,2,3}; // both cause error
}
"""
    expected = "TypeMismatchInExpression(StructLiteral({FloatLiteral(1.5), IntLiteral(2)}))"
    assert Checker(source).check_from_source() == expected

def test_084_struct_lit_as_argument():
    source = """struct Point2d {
    int x;
    int y;
};

int foo(Point2d p) {
    return p.x + p.y;
}

void main() {
    printInt(foo({1.5,2})); // expected point2d but get a mystery struct {float, int}
}
"""
    expected = "TypeMismatchInExpression(StructLiteral({FloatLiteral(1.5), IntLiteral(2)}))"
    assert Checker(source).check_from_source() == expected

def test_085_struct_lit_infer_proper():
    source = """struct Point2d {
    int x;
    int y;
};

int foo(Point2d p) {
    return p.x + p.y;
}

void main() {
    auto p;
    foo(p); // p inferred as Point2d
    p.x;
    p.y; 
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_086_struct_lit_infer_error():
    pass

def test_087_ambigious_struct_type():
    source = """struct A {
    int x;
    int y;
};

struct B {
    int x;
    int y;
};

int foo(A a) {
    // cannot pass a B struct although they are equivalent
    return a.x + a.y;
}

void main() {
    B b = {3,5};
    auto a;
    foo(a); // a infer as A
    foo(b); // type mismatch
}
"""
    expected = "TypeMismatchInExpression(FuncCall(foo, [Identifier(b)]))"
    assert Checker(source).check_from_source() == expected

def test_088_if_cond_error():
    source = """void main() {
    int a = 5;
    if (a + 1.5) { }   // condition must be int
}
"""
    expected = "TypeMismatchInStatement(IfStmt(if BinaryOp(Identifier(a), +, FloatLiteral(1.5)) then BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_089_if_else_proper():
    source = """void main() {
    int a = 5;
    if (a > 0) {
        a = a + 1;
    } else {
        a = a - 1;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_090_if_scope():
    source = """void main() {
    if (1) {
        int x = 10;
    }
    x = 5; // x out of scope
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_091_if_redeclared():
    source = """void main() {
    int a = 5;
    if (a > 0) {
        int a = 10; // shadowing inside block
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_092_while_cond_error():
    source = """void main() {
    float x = 1.2;
    while (x) { } // sai kiểu condition
}
"""
    expected = "TypeMismatchInStatement(WhileStmt(while Identifier(x) do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_093_while_scope():
    source = """void main() {
    while (1) {
        int x = 10;
    }
    x = 5; // out of scope
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_094_while_redeclared():
    source = """void main() {
    int a = 5;
    while (a > 0) {
        int a = 10; // as the for having {} or not the statement just create a new scope
        a = a - 1;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_095_for_scope():
    source = """void main() {
    for (int i = 0; i < 10; i = i + 1) {
        int x = i;
    }
    x = 5; // out of scope
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_095_for_init_float():
    source = """void main() {
    for (float i = 0.0; i < 10.0; i = i + 1.5) { } 
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_096_break_continue_in_loop():
    source = """void main() {
    auto j = 0;
    while (j < 10) {
        if (j == 3) {
            continue;  // Valid: in while loop
        }
        if (j == 8) {
            break;     // Valid: in while loop
        }
        printInt(j);
        ++j;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_097_break_continue_error():
    source = """void main() {
    break; // outside loop
}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_098_switch_cond_error():
    source = """void main() {
    float x = 1.5;
    switch (x) { // switch phải int
        case 1: break;
    }
}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"
    assert Checker(source).check_from_source() == expected

def test_099_switch_case_constant():
    source = """void main() {
    int x = 2;
    switch (x) {
        case 1:
        case 2:
            break;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_100_switch_case_constant_error():
    source = """void main() {
    int x = 2;
    int y = 1;
    switch (x) {
        case y: break; // case phải constant
    }
}
"""
    expected = "TypeMismatchInStatement(CaseStmt(case Identifier(y): [BreakStmt()]))"
    assert Checker(source).check_from_source() == expected

def test_101_switch_case_scope():
    source = """void main() {
    int x = 1;
    switch (x) {
        case 1: {
            int a = 5;
            break;
        }
    }
    a = 10; // out of scope
}
"""
    expected = "UndeclaredIdentifier(a)"
    assert Checker(source).check_from_source() == expected

def test_102_switch_default():
    source = """void main() {
    int x = 1;
    switch (x) {
        default:
            x = 2;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_103_switch_break():
    source = """void main() {
    int x = 1;
    switch (x) {
        case 1:
            x = 2;
            break;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_104_break_error():
    source = """void main() {
    switch (1) {
        case 1:
            break;
    }
    break; // ngoài switch
}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_105_switch_case_error():
    source = """void main() {
    int x = 1;
    switch (x) {
        case 1.5: break; // case phải int constant
    }
}
"""
    expected = "TypeMismatchInStatement(CaseStmt(case FloatLiteral(1.5): [BreakStmt()]))"
    assert Checker(source).check_from_source() == expected

def test_106_function_call_undeclared():
    source = """int foo(int x, int y) {
    return x+y;
}
void main() {
    far(1,2); // undeclared function far
}
"""
    expected = "UndeclaredFunction(far)"
    assert Checker(source).check_from_source() == expected

def test_107_function_call_wrong_argument_type():
    source = """int foo(int x, int y) {
    return x+y;
}
void main() {
    float a = 1.5;
    foo(1,a); // wrong argument type
}
"""
    expected = "TypeMismatchInExpression(FuncCall(foo, [IntLiteral(1), Identifier(a)]))"
    assert Checker(source).check_from_source() == expected

def test_108_function_call_assign():
    source = """int foo(int x, int y) {
    return x+y;
}
void main() {
    int a = 1;
    int p = foo(1,a);
    p++;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_109_function_call_infer():
    source = """int foo(int x, int y) {
    return x+y;
}
void main() {
    int a = 1;
    auto p = foo(1,a); // p inferred as int
    p++;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_110_function_call_infer_arg():
    source = """int foo(int x) {
    return x+5;    
}

void main() {
    auto x;
    foo(x); //x infer as int

    printInt(x);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_111_function_call_struct_params():
    source = """struct Point2d {
    int x;
    int y;
};
    
int foo(Point2d p) {
    return p.x+p.y;
}
void main() {
    Point2d p;
    foo(p);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_112_initializer_it_self_var_decl():
    source = """void main() {
    int a = a + 1;    
}
"""
    expected = "UndeclaredIdentifier(a)"
    assert Checker(source).check_from_source() == expected

def test_113_nested_struct_literal():
    source = """struct Point2d {
    int x;
    int y;
};
    
struct Point3d {
    Point2d p;
    int z;    
};

int foo(Point3d p) { return p.p.x + p.p.y + p.z; }

void main() { 
    // auto p;
    foo({{1,2}, 5}); // p as Point
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_114_struct_literal_as_return():
    source = """struct Point2d {
    int x;
    int y;
};
    
Point2d foo(int x, int y) {
    return {x,y};
}
void main() {
    auto p = foo(1,2); // p infer as Point2d
    p.x;
    p.y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_115_for_scope():
    source = """void main() {
    int i = 5;
    for (int i = 0; i < 10; i = i + 1) { // redeclared i
        int x = i;
    }
}
"""
    expected = "Redeclared(Variable, i)"
    assert Checker(source).check_from_source() == expected

def test_116_for_scope():
    source = """void main() {
    for (int i = 0; i < 10; i = i + 1) { 
        int x = i;
    }
    printInt(i); // i exist even after for
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_117_for_scope_shadowing():
    source = """void main() {
    for (int i = 0; i < 10; i = i + 1) { 
        float i = 5.0; // valid: i shadowing even no block 
    }

    for (int j = 0; j < 10; j = j + 1) 
        float j = 5.0; // valid: i shadowing even no block 
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_119_struct_literal_using_expr_proper():
    source = """struct Point2d {
    int x;
    int y;
};
    
struct Point3d {
    Point2d p;
    int z;    
};

void main() {
    int a;
    int b;
    float z;
    Point2d p = {a+1,b+5};
    Point2d p2 = {p,z}; // z is float type error here!
}
"""
    expected = "TypeMismatchInExpression(StructLiteral({Identifier(p), Identifier(z)}))"
    assert Checker(source).check_from_source() == expected

def test_120_for_nested():
    source = """// Valid: Nested loops
void main() {
    for (auto i = 0; i < 5; ++i) {
        for (auto j = 0; j < 5; ++j) {
            if (i == j) {
                continue;  // Valid: affects inner loop
            }
            if (j > 3) {
                break;     // Valid: breaks inner loop
            }
        }
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_121_switch_case_cases_scope():
    source = """void main() {
    int x = 1;
    switch (x) {
        case 1: 
            int a = 3;
        case 2+1:
            int a = 5; // redeclared here
    }
}
"""
    expected = "Redeclared(Variable, a)"
    assert Checker(source).check_from_source() == expected

def test_122_switch_case_cases_scope():
    source = """void main() {
    int x = 1;
    switch (x) {
        case 1: {
            int a = 3;
        }
        case 2+1: {
            int a = 5; // allowed here
        }
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_123_function_void():
    source = """foo(int x, int y) {
    printInt(x+y);
}
void main() {
    int a = 1;
    int b = 2;
    foo(a*1, b%2);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_123_function_void_assign():
    source = """foo(int x, int y) {
    printInt(x+y);
}
void main() {
    int a = 1;
    int b = 2;
    int c = foo(a*1, b%2); // type mismatch
}
"""
    expected = "TypeMismatchInStatement(VarDecl(IntType(), c = FuncCall(foo, [BinaryOp(Identifier(a), *, IntLiteral(1)), BinaryOp(Identifier(b), %, IntLiteral(2))])))"
    assert Checker(source).check_from_source() == expected