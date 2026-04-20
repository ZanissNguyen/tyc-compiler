"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from os import name
from platform import node
from turtle import clone
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
class ErrorType: pass
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType, ErrorType]
VarType = Union[IntType, FloatType, StringType, StructType, ErrorType]
# 

from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Symbol Table and enviroment management
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Context(): pass
class LoopContext(Context): pass
class SwitchContext(Context): pass
class FunctionContext(Context):pass

class Symbol:
    def __init__(self, name: str, type: VarType, kind: str):
        self.name = name
        self.type = type
        self.kind = kind # can be "variable", "parameter", "member"
    def __str__(self):
        return f"Symbol({self.name}, {self.type}, {self.kind})"

class Scope: # basically a list of symbols that can be nested
    def __init__(self, loop: bool = False):
        self.symbols: Dict[str, Symbol] = {}
        self.loop = loop
    def __str__(self):
        return f"Scope({[str(s) for s in self.symbols.values()]}, Loop: {self.loop})"

class StructSymbol: # a symbol for struct decl, contain name, member as a scope
    def __init__(self, name: str, members: Scope):
        self.name = name
        self.members = members
    def __str__(self):
        return f"StructSymbol(Name: {self.name}, Members: {self.members})"

class FunctionSymbol: # a symbol for function decl, contain name, return type, param list
    def __init__(self, name: str, return_type: TyCType, params: List[VarType], builtin: bool = False):
        self.name = name
        self.return_type = return_type
        self.scopes: List[Scope] = [] 
        self.params = params
        self.builtin = builtin
    def __str__(self):
        return f"FunctionSymbol(Name: {self.name}, Return Type: {self.return_type}, Params: {self.params}, Builtin: {self.builtin})"

class ProgramSymbol:
    def __init__(self):
        self.structs: Dict[str, StructSymbol] = {}
        self.functions: Dict[str, FunctionSymbol] = {}
    def __str__(self):
        return f"ProgramSymbol(Structs: {[str(s) for s in self.structs.values()]}, Functions: {[str(f) for f in self.functions.values()]})"

class Environment:
    def __init__(self,
                program: ProgramSymbol,
                scopes: List[Scope],
                current_function: FunctionSymbol = None,
                current_struct: StructSymbol = None,
                context: List[Context] = [],
                stmt: bool = False):
        self.program = program
        self.scopes = scopes
        self.current_function = current_function
        self.current_struct = current_struct
        self.stack_context = context
        self.is_statement = stmt
    def __str__(self):
        return f"Environment(Program: {self.program}, Scopes: {[str(s) for s in self.scopes]}, Current Function: {str(self.current_function)}, Current Struct: {str(self.current_struct)}, Context Stack: {self.stack_context})"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Some helper functions for type check, lookup, type inference
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# lookup_struct -> searching struct in struct namespace
# lookup_function -> searching function in function namespace
# lookup_variable -> searching variable in current scope and parents scope
# infer_type(symbol, type) -> assign new type to symbol
# check_type(expected, actual) -> check if two types are the same
# built_in(program):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def built_in(program: ProgramSymbol):
    # functions need adding builtin function:
    # builtin function:
    # int readInt()
    readInt = FunctionSymbol("readInt", IntType(), [], True)
    # float readFloat()
    readFloat = FunctionSymbol("readFloat", FloatType(), [], True)
    # string readString()
    readString = FunctionSymbol("readString", StringType(), [], True)
    # void printInt(int value)
    printInt = FunctionSymbol("printInt", VoidType(), [IntType()], True)
    # void printFloat(float value)
    printFloat = FunctionSymbol("printFloat", VoidType(), [FloatType()], True)
    # void printString(string value)
    printString = FunctionSymbol("printString", VoidType(), [StringType()], True)

    for builtin in [readInt, readFloat, readString, printInt, printFloat, printString]:
        program.functions[builtin.name] = builtin

def lookup_function(name, function_namespace) -> Optional[FunctionSymbol]:
    # searching function in function namespace
    find = function_namespace.get(name)
    if find is None:
        return None
    return find

def lookup_struct(name, struct_namespace) -> Optional[StructSymbol]:
    # searching struct in struct namespace
    find = struct_namespace.get(name)
    if find is None:
        return None
    return find

def lookup_variable(name, scopes) -> Optional[Symbol]:
    # searching struct in struct namespace
    for scope in scopes:  # inner → outer
        if name in scope.symbols:
            return scope.symbols[name]
    return None

def lookup_context(context_stack, context_type) -> Optional[Context]:
    # searching Context in current scope and parents scope
    for ctx in context_stack:  # inner → outer
        if type(ctx) is type(context_type):
            return ctx
    return None

def check_type(type_1, type_2):
    if type(type_1) is StructType and type(type_2) is StructType:
        return type_1.struct_name == type_2.struct_name
    return type(type_1) is type(type_2)

def infer(symbol, type):
    symbol.type = type

def is_assignable(ast_node):
    # must be identifier or member access
    if (type(ast_node) in [Identifier, MemberAccess]):
        return True
    return False

def is_constant_expression(ast_node: "Expr"):
    if type(ast_node) is BinaryOp:
        return is_constant_expression(ast_node.left) and is_constant_expression(ast_node.right)
    elif type(ast_node) in [PrefixOp, PostfixOp]:
        return is_constant_expression(ast_node.operand)
    elif type(ast_node) is IntLiteral:
        return True
    else:
        return False

class StaticChecker(ASTVisitor):

    def check_program(self, ast: Program):
        return self.visit(ast, None)

    def visit_program(self, node: "Program", o: Any = None):
        # Program node: decls
        # --> return ProgramSymbol: structs, functions
        # init program
        program = ProgramSymbol()

        # adding builtin functions
        built_in(program)

        # load program
        for decl in node.decls:
            self.visit(decl, program)

        # check Entry Point
        main_find = lookup_function("main", program.functions)
        if main_find is None:
            raise UndeclaredFunction("main")
        else:
            # print(main_find.return_type)
            # print(len(main_find.params))
            if type(main_find.return_type) is not VoidType or len(main_find.params) != 0:
                raise TypeMismatchInExpression(FuncCall("main", []))

        # return final ProgramSymbol for code generation
        return program

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        # StructDecl: name, members
        # --> StructSymbol: name, members
        # check redeclaration of struct name (struct name space)
        find_struct = lookup_struct(node.name, o.structs)
        if find_struct is not None:
            raise Redeclared("Struct", node.name)

        # init struct
        struct = StructSymbol(node.name, Scope())

        # reverse members and init members scope
        struct_env = Environment(o, [Scope()], None, struct)
        for mdecl in node.members:
            self.visit(mdecl, struct_env)
        
        struct.members = struct_env.scopes[0]
        o.structs[node.name] = struct

        return o

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        # MemberDecl: member_type, name
        # checking redeclared
        if o.scopes[0].symbols.get(node.name) is not None:
            raise Redeclared("Member", node.name)
        
        typ = self.visit(node.member_type, o)
            
        o.scopes[0].symbols[node.name] = Symbol(node.name, typ, "Member")
        return o

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        # FuncDecl: return_type = None, name, params, body
        find_function = lookup_function(node.name, o.functions)
        # print("checking function: ", node.name)
        if find_function is not None:
            raise Redeclared("Function", node.name)

        # init struct
        func = FunctionSymbol(node.name, node.return_type, [], False)
        func_env = Environment(o, [Scope()], func, None, [FunctionContext()])

        # checking redeclared parameter names and update param list
        for p in node.params:
            self.visit(p, func_env)
        o.functions[node.name] = func

        # run body with new environment 
        self.visit(node.body, func_env)
    
        func_env.stack_context = func_env.stack_context[1:] # pop function context
        return o

    def visit_param(self, node: "Param", o: Environment = None): # o -> Environment
        # Param: param_type, name
        if node.name in o.scopes[0].symbols:
            raise Redeclared("Parameter", node.name)
        
        typ = self.visit(node.param_type, o)

        o.current_function.params.append(typ)
        o.scopes[0].symbols[node.name] = Symbol(node.name, typ, "Parameter")
        return o

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None) -> TyCType:
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None) -> TyCType:
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None) -> TyCType:
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None) -> TyCType:
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None) -> TyCType:
        # checking undeclared struct
        if lookup_struct(node.struct_name, o.program.structs) is None:
            raise UndeclaredStruct(node.struct_name)
        
        return StructType(node.struct_name)

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        # BlockStmt: statements
        # create new scope for block stmt
        # thêm tạo một environment mới cho block stmt để quản lý scope và current function/struct
        block_env = Environment(o.program, [Scope()] + o.scopes, o.current_function, o.current_struct, o.stack_context)
        for stmt in node.statements:    
            self.visit(stmt, block_env)

        for sym in block_env.scopes[0].symbols.values():
            if not sym.type:
                raise TypeCannotBeInferred(node)

        return o

    def visit_var_decl(self, node: "VarDecl", o: Any = None): #Environment
        # VarDecl: var_type = None, name, init_value = None
        # checking redeclared if in function context having additional checking
        init_typ = None
        typ = None
        if not node.init_value: # không có phần initialize
            if not node.var_type: # auto luôn
                typ = None
            else:
                typ = self.visit(node.var_type, o)
        else: # có init
            if not node.var_type: # auto
                if type(node.init_value) is StructLiteral:
                    raise TypeCannotBeInferred(node)
                else:
                    init_typ = init_typ = self.visit(node.init_value, o)

                if (init_typ is None):
                    raise TypeCannotBeInferred(node)
                typ = init_typ
            else: 
                typ = self.visit(node.var_type, o)

                if type(node.init_value) is StructLiteral:
                    # print(node.init_value)
                    # print(type(typ))
                    if (type(typ) is StructType):
                        init_typ = self.visit(node.init_value, (o, typ))
                    elif not typ:
                        raise TypeCannotBeInferred(node)
                    else:
                        raise TypeMismatchInStatement(node)
                else:
                    init_typ = self.visit(node.init_value, o)

                if not check_type(typ, init_typ):
                    raise TypeMismatchInStatement(node)

        if o.stack_context and type(o.stack_context[0]) is FunctionContext:
            if (node.name in o.scopes[-1].symbols):
                raise Redeclared("Variable", node.name)
        if (node.name in o.scopes[0].symbols):
            raise Redeclared("Variable", node.name)
        
        o.scopes[0].symbols[node.name] = Symbol(node.name, typ, "Variable")
        # print(o)
        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        # IfStmt: condition, then_stmt, else_stmt
        cond_type = self.visit(node.condition, o)
        if type(cond_type) is not IntType:
            raise TypeMismatchInStatement(node)
        
        # then_stmt
        self.visit(node.then_stmt, o)

        # else_stmt
        if node.else_stmt:
            self.visit(node.else_stmt, o)

        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        # WhileStmt: condition, body)
        cond_type = self.visit(node.condition, o)
        if type(cond_type) is not IntType:
            raise TypeMismatchInStatement(node)

        o.stack_context = [LoopContext()] + o.stack_context
        if (type(node.body) is BlockStmt):
            self.visit(node.body, o)
        else:
            new_o = Environment(o.program, [Scope()]+o.scopes, o.current_function, o.current_struct, o.stack_context, stmt)
            self.visit(node.body, new_o)
        o.stack_context = o.stack_context[1:]

        return o

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        # ForStmt: init, condition, update, body
        # checking init if init is vardecl?
        # o lúc này là env của function:
        # --> program, [[]], func, none
        self.visit(node.init, o) # lúc này thêm vô scope nếu là vardecl
        cond_type = self.visit(node.condition, o)
        if type(cond_type) is not IntType:
            raise TypeMismatchInStatement(node)
        self.visit(node.update, o)

        o.stack_context = [LoopContext()] + o.stack_context
        if (type(node.body) is BlockStmt):
            self.visit(node.body, o)
        else:
            new_o = Environment(o.program, [Scope()]+o.scopes, o.current_function, o.current_struct, o.stack_context)
            self.visit(node.body, new_o)
        o.stack_context = o.stack_context[1:]

        # remove the i if init is vardecl?
        # if type(node.init) is VarDecl:
        #     o.scopes[0] = o.scopes[0][1:]

        return o

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        # SwitchStmt: expr, cases, default_case
        # các case <expr> thì <expr> là constant expr (các operand nguyên tố là literal)
        # các scope của case là đồng nhất vẫn ở local của switch
        expr_type = self.visit(node.expr, o)
        if type(expr_type) is not IntType:
            raise TypeMismatchInStatement(node)

        o.stack_context = [SwitchContext()] + o.stack_context
        if node.cases:
            for case in node.cases:
                self.visit(case, o)
        
        if node.default_case:
            self.visit(node.default_case, o)
        o.stack_context = o.stack_context[1:]

        return o

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        # CaseStmt: expr, statements
        print(node.expr)
        if not is_constant_expression(node.expr):
            raise TypeMismatchInStatement(node)
        
        if node.statements:
            for stmt in node.statements:
                self.visit(stmt, o)
        
        return o

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        # DefautStmt: statements
        if node.statements:
            for stmt in node.statements:
                self.visit(stmt, o)
        
        return o

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        # checking break in loop or switch context
        if lookup_context(o.stack_context, LoopContext()) is None and lookup_context(o.stack_context, SwitchContext()) is None:
            raise MustInLoop(node)

        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        # checking continue in loop context
        if lookup_context(o.stack_context, LoopContext()) is None:
            raise MustInLoop(node)

        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        # ReturnStmt: expr
        expected_type = o.current_function.return_type
            
        if not expected_type: # need to infer không khai báo return type

            if not node.expr: # return; -> suy ra Void
                o.current_function.return_type = VoidType()
            else: # return biểu thức, check biểu thức, 
                if type(node.expr) is StructLiteral:
                    raise TypeCannotBeInferred(node)
                # nếu biểu thức None -> type cannot infer
                return_type = self.visit(node.expr, o)
                if not return_type: 
                    raise TypeCannotBeInferred(node)
                o.current_function.return_type = return_type
        else: # có return type
            if type(expected_type) is VoidType: # nếu return void
                if node.expr: # return <expr>; # mà return <expr> lỗi
                    raise TypeMismatchInStatement(node)

            # trường hợp non-void
            if not node.expr: # không có expr return;
                if type(expected_type) is not VoidType:
                    raise TypeMismatchInStatement(node)
            else:
                return_type = None
                if type(expected_type) is StructType and type(node.expr) is StructLiteral:
                    return_type = self.visit(node.expr, (o, expected_type))
                else:
                    return_type = self.visit(node.expr, o)
                        
                # có expr nhưng expr chưa rõ type
                if not return_type: 
                    raise TypeCannotBeInferred(node)
                o.current_function.return_type = return_type
            
            if not check_type(return_type, expected_type):
                raise TypeMismatchInStatement(node)
        
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        # ExprStmt: expr
        o.is_statement = True
        self.visit(node.expr, o)
        o.is_statement = False

        return o

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None) -> TyCType:
        # BinaryOp: left, operator, right
        error = None
        if o.is_statement:
            error = TypeMismatchInStatement
        else:
            error = TypeMismatchInExpression

        expr_env = Environment(o.program, o.scopes, o.current_function, o.current_struct, o.stack_context)

        left_type = self.visit(node.left, expr_env)
        right_type = self.visit(node.right, expr_env)

        if not left_type and not right_type:
            raise TypeCannotBeInferred(node)

        if node.operator in ["+", "-", "*", "/"]:
            if not left_type:
                if (type(right_type) in [IntType, FloatType]):
                    sym = lookup_variable(node.left.name, o.scopes)
                    left_type = right_type
                    infer(sym, right_type)
                else:
                    raise TypeCannotBeInferred(node)
                
            if not right_type:
                if (type(left_type) in [IntType, FloatType]):
                    sym = lookup_variable(node.right.name, o.scopes)
                    right_type = left_type
                    infer(sym, left_type)
                else:
                    raise TypeCannotBeInferred(node)

            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType()
            elif type(left_type) is FloatType and type(right_type) is IntType:
                return FloatType()
            elif type(left_type) is IntType and type(right_type) is FloatType:
                return FloatType()
            elif type(left_type) is FloatType and type(right_type) is FloatType:
                return FloatType()
            else:
                raise error(node)
        elif node.operator in ["==", "!=", "<", "<=", ">", ">="]:
            if not left_type:
                if (type(right_type) in [IntType, FloatType]):
                    sym = lookup_variable(node.left.name, o.scopes)
                    left_type = right_type
                    infer(sym, right_type)
                else:
                    raise TypeCannotBeInferred(node)
                
            if not right_type:
                if (type(left_type) in [IntType, FloatType]):
                    sym = lookup_variable(node.right.name, o.scopes)
                    right_type = left_type
                    infer(sym, left_type)
                else:
                    raise TypeCannotBeInferred(node)

            if (type(left_type) in [IntType, FloatType]) and (type(right_type) in [IntType, FloatType]):
                return IntType()
            else:
                raise error(node)
        elif node.operator in ["||", "&&", "%"]:
            if not left_type:
                sym = lookup_variable(node.left.name, o.scopes)
                infer(sym, IntType())
            if not right_type:
                sym = lookup_variable(node.right.name, o.scopes)
                infer(sym, IntType())

            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(node)
        else:
            raise error(node)

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None) -> TyCType:
        # PrefixOp: operator, operand
        error = None
        if o.is_statement:
            error = TypeMismatchInStatement
        else:
            error = TypeMismatchInExpression

        expr_env = Environment(o.program, o.scopes, o.current_function, o.current_struct, o.stack_context)

        typ = self.visit(node.operand, expr_env)

        if node.operator in ["++", "--", "!"]:
            if not typ:
                symbol = lookup_variable(node.operand.name, o.scopes)
                infer(symbol, IntType())
                return IntType()
            
            if (type(typ) is IntType):
                return IntType()
            else:
                raise error(node)
        elif node.operator in ["+", "-"]:
            if not typ:
                raise TypeCannotBeInferred(node)
            
            if (type(typ) in [IntType, FloatType]):
                return typ
            else:
                raise error(node)
        else:
            raise error(node)

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None) -> TyCType:
        # PostfixOp: operator, operand
        error = None
        if o.is_statement:
            error = TypeMismatchInStatement
        else:
            error = TypeMismatchInExpression

        expr_env = Environment(o.program, o.scopes, o.current_function, o.current_struct, o.stack_context)
        typ = self.visit(node.operand, expr_env)
        
        if node.operator in ["++", "--"]:
            if not typ:
                symbol = lookup_variable(node.operand.name, o.scopes)
                infer(symbol, IntType())
                return IntType()

            if (type(typ) is IntType):
                return IntType()
            else:
                raise error(node)
        else:
            raise error(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None) -> TyCType:
        # AssignExpr: lhs, rhs
        error = None
        if o.is_statement:
            error = TypeMismatchInStatement
        else:
            error = TypeMismatchInExpression

        expr_env = Environment(o.program, o.scopes, o.current_function, o.current_struct, o.stack_context)

        right_type = self.visit(node.rhs, expr_env)
        left_type = self.visit(node.lhs, expr_env)
        
        # check lhs assignable
        if not is_assignable(node.lhs):
            raise error(node)

        if not left_type:
            if not right_type:
                raise TypeCannotBeInferred(node)
            var = lookup_variable(node.lhs.name, o.scopes)
            infer(var, right_type)
            return right_type
        
        if not check_type(left_type, right_type):
            raise error(node)

        return left_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None) -> VarType:
        # MemberAccess: obj, member
        # đảm bảo obj là struct type
        obj_type = self.visit(node.obj, o)
        if type(obj_type) is not StructType:
            raise TypeMismatchInExpression(node)
        
        struct = lookup_struct(obj_type.struct_name, o.program.structs)
        # đảm bảo member tồn tại trong struct
        if (node.member not in struct.members.symbols):
            raise TypeMismatchInExpression(node)
                
        return struct.members.symbols[node.member].type

    def visit_func_call(self, node: "FuncCall", o: Any = None) -> TyCType:
        # FuncCall: name, args
        func = lookup_function(node.name, o.program.functions)
        if func is None:
            raise UndeclaredFunction(node.name)

        if len(node.args) != len(func.params):
            raise TypeMismatchInExpression(node)
        
        # check argument types 
        # print(func.params)
        for i, arg in enumerate(node.args):
            to_pass = o
            if (type(func.params[i]) is StructType and type(arg) is StructLiteral):
                to_pass = (o, func.params[i])
                # current environment and expected struct type 
                # expection: struct literal visit 
                
            arg_type = self.visit(arg, to_pass)

            if arg_type is None:
                arg_sym = lookup_variable(arg.name, o.scopes)
                arg_type = func.params[i]
                infer(arg_sym, func.params[i])

            if not check_type(arg_type, func.params[i]):
                raise TypeMismatchInExpression(node)

        return func.return_type

    def visit_identifier(self, node: "Identifier", o: Any = None) -> VarType:
        # Identifier: name
        var = lookup_variable(node.name, o.scopes)
        if var is None:
            raise UndeclaredIdentifier(node.name)
        return var.type

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None) -> TyCType:
        # StructLiteral: values -> List"Expr"
        expected_struct = o[1]
        env = o[0] 

        struct_decl = lookup_struct(expected_struct.struct_name, env.program.structs)
        struct_members = struct_decl.members #scope
        struct_type = [sym.type for sym in struct_members.symbols.values()]

        if len(node.values) != len(struct_type):
            raise TypeMismatchInExpression(node)

        for i, expr in enumerate(node.values):
            expected_type = struct_type[i]
            to_pass = env
            if (type(struct_type[i]) is StructType and type(expr) is StructLiteral):
                to_pass = (env, struct_type[i])
            
            typ = self.visit(expr, to_pass)

            if typ is None:
                sym = lookup_variable(expr.name, env.scopes)
                typ = struct_type[i]
                infer(sym, struct_type[i])

            if not check_type(typ, struct_type[i]):
                raise TypeMismatchInExpression(node)
            
        return expected_struct

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None) -> TyCType:
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None) -> TyCType:
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None) -> TyCType:
        return StringType()
