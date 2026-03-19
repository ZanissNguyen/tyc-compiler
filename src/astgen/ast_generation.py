"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from ast import expr
from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):

# ======================================================
# PROGRAM
# ======================================================

    def visitProgram(self, ctx: TyCParser.ProgramContext):
        # program: decl* EOF
        decls = []
        for child in ctx.decl(): 
            decls.append(self.visit(child))
        return Program(decls)
    
    def visitDecl(self, ctx:TyCParser.DeclContext):
        # decl: structdcl | funcdecl;
        if ctx.structdcl():
            return self.visit(ctx.structdcl())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        
# ======================================================
# TYPE / STRUCT
# ======================================================

    def visitType(self, ctx):
        # TYPE_FLOAT | TYPE_INT | TYPE_STRING
        if ctx.TYPE_FLOAT():
            return FloatType()
        elif ctx.TYPE_INT():
            return IntType()
        elif ctx.TYPE_STRING():
            return StringType()

    def visitStructdcl(self, ctx):
        # structdcl: TYPE_STRUCT ID LBR member_list RBR SEMI;
        struct_name = ctx.ID().getText()
        members = self.visit(ctx.member_list())
        return StructDecl(name=struct_name, members=members)

    def visitMember_list(self, ctx):
        # member_list: member member_list | ;  
        if ctx.member():
            mem = self.visit(ctx.member())
            list = self.visit(ctx.member_list())
            return [mem] + list
        else:
            return []

    def visitMember(self, ctx):
        # member: member_type ID SEMI;
        typ = self.visit(ctx.member_type())
        name = ctx.ID().getText()
        return MemberDecl(typ, name)

    def visitMember_type(self, ctx):
        # member_type: type | ID;
        if ctx.type_():
            return self.visit(ctx.type_())
        elif ctx.ID():
            return StructType(ctx.ID().getText())

# ======================================================
# VARIABLE DECL
# ======================================================

    def visitVardecl(self, ctx):
        # vardecl: type ID (ASSIGNMENT or_expr)
        #       |  type ID   
        #       |  TYPE_AUTO ID (ASSIGNMENT or_expr)
        #       |  TYPE_AUTO ID
        #       |  ID ID // struct
        #       |  ID ID ASSIGNMENT struct_lit;
        if ctx.TYPE_AUTO():      # auto var declare
            init = self.visit(ctx.or_expr()) if ctx.or_expr() else None
            name_ = ctx.ID(0).getText()
            return VarDecl(var_type=None, name=name_, init_value=init)
        elif ctx.type_():         # normal var declare
            typ = self.visit(ctx.type_())
            init = self.visit(ctx.or_expr()) if ctx.or_expr() else None
            name_ = ctx.ID(0).getText()
            return VarDecl(var_type = typ, name=name_, init_value=init)
        elif len(ctx.ID()) == 2: # var struct declare
            typ = StructType(ctx.ID(0).getText())
            init = self.visit(ctx.struct_lit()) if ctx.struct_lit() else None
            name_ = ctx.ID(1).getText()
            return VarDecl(var_type=typ, name=name_, init_value=init)

    def visitStruct_lit(self, ctx):
        # struct_lit: LBR memberdcl_prime RBR
        list = self.visit(ctx.memberdcl_prime())
        return StructLiteral(list)

    def visitMemberdcl_prime(self, ctx):
        # memberdcl_prime: memberdcl_list | ;
        if ctx.memberdcl_list():
            return self.visit(ctx.memberdcl_list())
        else:
            return []
        
    def visitMemberdcl_list(self, ctx):
        # memberdcl_list: memberdcl COMMA memberdcl_list | memberdcl;
        if ctx.memberdcl_list():
            mem = self.visit(ctx.memberdcl())
            mem_list = self.visit(ctx.memberdcl_list())
            return [mem] + mem_list
        else:
            return [self.visit(ctx.memberdcl())]

    def visitMemberdcl(self, ctx):
        # memberdcl: or_expr | struct_lit;
        if ctx.or_expr():
            return self.visit(ctx.or_expr())
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())

# ======================================================
# FUNCTION
# ======================================================

    def visitFuncdecl(self, ctx):
        # funcdecl: functyp ID LP parameter_prime RP body;
        typ = self.visit(ctx.functyp())
        name = ctx.ID().getText()
        params = self.visit(ctx.parameter_prime())
        body = self.visit(ctx.body())
        return FuncDecl(typ, name, params, body)

    def visitFunctyp(self, ctx:TyCParser.FunctypContext):
        # functyp: type | TYPE_VOID | ID | ;
        if ctx.type_():
            return self.visit(ctx.type_())
        elif ctx.TYPE_VOID():
            return VoidType()
        elif ctx.ID():
            return StructType(ctx.ID().getText())
        else:
            return None

    def visitParameter_prime(self, ctx):
        # parameter_prime: parameter_list | ;
        if ctx.parameter_list():
            return self.visit(ctx.parameter_list())
        else:
            return []

    def visitParameter_list(self, ctx):
        # parameter_list: parameter COMMA parameter_list | parameter; 
        if ctx.parameter_list():
            param = self.visit(ctx.parameter())
            list = self.visit(ctx.parameter_list())
            return [param] + list
        else:
            param = self.visit(ctx.parameter())
            return [param]

    def visitParameter(self, ctx):
        # (type | ID) ID
        if ctx.type_():
            typ = self.visit(ctx.type_())
            param = ctx.ID(0).getText()
            return Param(typ, param)
        else:
            struct = ctx.ID(0).getText()
            param = ctx.ID(1).getText()
            return Param(StructType(struct), param)

# ======================================================
# BODY / STATEMENT
# ======================================================

    def visitBody(self, ctx):
        # body: LBR statement_prime RBR;
        if ctx.statement_prime():
            stmt_list = self.visit(ctx.statement_prime())
            return BlockStmt(stmt_list)

    def visitStatement_prime(self, ctx):
        # statement_prime: statement_list | ;
        if ctx.statement_list():
            return self.visit(ctx.statement_list())
        else:
            return []

    def visitStatement_list(self, ctx):
        # statement_list: statement statement_list | ;
        if ctx.getChildCount() > 0:
            stmt = self.visit(ctx.statement())
            stmt_list = self.visit(ctx.statement_list())
            return [stmt] + stmt_list
        else:
            return []

    def visitStatement(self, ctx):
        # statement: vardecl SEMI
        #           | assignStmt SEMI
        #           | or_expr SEMI
        #           | body
        #           | ifStmt
        #           | whileStmt
        #           | forStmt
        #           | switchStmt
        #           | breakStmt
        #           | continueStmt
        #           | returnStmt;
        if ctx.vardecl():
            return self.visit(ctx.vardecl())

        elif ctx.assignStmt():
            return ExprStmt(self.visit(ctx.assignStmt()))
        
        elif ctx.or_expr():
            return ExprStmt(self.visit(ctx.or_expr()))

        elif ctx.body():
            return self.visit(ctx.body())

        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())

        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())

        elif ctx.forStmt():
            return self.visit(ctx.forStmt())

        elif ctx.switchStmt():
            return self.visit(ctx.switchStmt())

        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())

        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())

        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())

# ======================================================
# CONTROL FLOW
# ======================================================

    def visitIfStmt(self, ctx):
        # ifStmt: IF LP expression RP statement ELSE statement
        #       | IF LP expression RP statement;
        expr = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))

        if ctx.ELSE():
            else_stmt = self.visit(ctx.statement(1))
            return IfStmt(condition=expr, then_stmt=then_stmt, else_stmt=else_stmt)
        
        return IfStmt(condition=expr, then_stmt=then_stmt)

    def visitWhileStmt(self, ctx):
        # whileStmt: WHILE LP expression RP statement;
        cond = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        return WhileStmt(condition=cond, body=stmt)

    def visitForStmt(self, ctx):
        # forStmt: FOR LP forInit SEMI forCondition SEMI forUpdate RP statement;
        init_ = self.visit(ctx.forInit()) if (ctx.forInit()) else None
        cond_ = self.visit(ctx.forCondition()) if (ctx.forCondition()) else None
        update_ = self.visit(ctx.forUpdate()) if (ctx.forUpdate()) else None
        stmt_ = self.visit(ctx.statement())
        
        return ForStmt(init=init_, condition=cond_, update=update_, body=stmt_)

    def visitForInit(self, ctx:TyCParser.ForInitContext):
        # forInit: vardecl | assignStmt | ;
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        else: 
            return None

    def visitForCondition(self, ctx:TyCParser.ForConditionContext):
        # forCondition: expression | ;
        if ctx.expression():
            return self.visit(ctx.expression())
        else: 
            return None

    def visitForUpdate(self, ctx:TyCParser.ForUpdateContext):
        # forUpdate: assignStmt | prefix_expr |;
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.prefix_expr():
            return self.visit(ctx.prefix_expr())
        else: 
            return None

    def visitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        return BreakStmt()

    def visitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        return ContinueStmt()

    def visitReturnStmt(self, ctx):
        # returnStmt: RETURN expression SEMI
        #   | RETURN SEMI;
        if ctx.expression():
            expr = self.visit(ctx.expression())
            return ReturnStmt(expr)
        else:   
            return ReturnStmt()

    def visitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        # switchStmt: SWITCH LP expression RP switchBody;
        expr = self.visit(ctx.expression())
        body = self.visit(ctx.switchBody())
        if body["default"] is None:
            return SwitchStmt(expr, body["cases"])
        else:
            return SwitchStmt(expr, body["cases"], body["default"])

    def visitSwitchBody(self, ctx:TyCParser.SwitchBodyContext):
        # switchBody: LBR case_list default_case RBR;
        body = {
            "cases": [],
            "default": None
        }
        body["cases"] = self.visit(ctx.case_list())
        body["default"] = self.visit(ctx.default_case())
        return body

    def visitCase_list(self, ctx:TyCParser.Case_listContext):
        # case_list: normal_case case_list | ;
        if ctx.getChildCount() > 0:
            normal_case = self.visit(ctx.normal_case())
            case_list = self.visit(ctx.case_list())
            return [normal_case] + case_list
        else:
            return []

    def visitNormal_case(self, ctx:TyCParser.Normal_caseContext):
        # normal_case: CASE expression COLON statement_prime;
        expr = self.visit(ctx.expression())
        stmts = self.visit(ctx.statement_prime())
        return CaseStmt(expr, stmts)

    def visitDefault_case(self, ctx:TyCParser.Default_caseContext):
        # default_case: DEFAULT COLON statement_prime | ;  
        if ctx.getChildCount() > 1:
            stmts = self.visit(ctx.statement_prime())
            return DefaultStmt(stmts)
        else:
            return None

# ======================================================
# EXPRESSIONS
# ======================================================

    def visitExpression(self, ctx):
        # expression: assignStmt | or_expr;
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        else:
            return self.visit(ctx.or_expr())

    def visitAssignable(self, ctx):
        # assignable: ID | member_expr; 
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        elif ctx.member_expr():
            return self.visit(ctx.member_expr())

    def visitAssignStmt(self, ctx):
        # assignStmt: assignable ASSIGNMENT assignStmt | assignable ASSIGNMENT or_expr;
        lhs = self.visit(ctx.assignable())

        if ctx.assignStmt():
            rhs = self.visit(ctx.assignStmt())
            return AssignExpr(lhs, rhs)
        elif ctx.or_expr():
            rhs = self.visit(ctx.or_expr())
            return AssignExpr(lhs, rhs)

# ======================================================
# PRECEDENCE LEVELS
# ======================================================

    def visitOr_expr(self, ctx):
        # or_expr: or_expr LOG_OR and_expr | and_expr;
        if ctx.LOG_OR():
            lhs = self.visit(ctx.or_expr())
            rhs = self.visit(ctx.and_expr())
            return BinaryOp(lhs, ctx.LOG_OR().getText(), rhs)
        else:
            return self.visit(ctx.and_expr())


    def visitAnd_expr(self, ctx):
        # and_expr: and_expr LOG_AND equality_expr | equality_expr;
        if ctx.LOG_AND():
            lhs = self.visit(ctx.and_expr())
            rhs = self.visit(ctx.equality_expr())
            return BinaryOp(lhs, ctx.LOG_AND().getText(), rhs)
        else:
            return self.visit(ctx.equality_expr())

    def visitEquality_expr(self, ctx):
        # equality_expr: equality_expr equality compare_expr | compare_expr;
        if ctx.equality_expr():
            lhs = self.visit(ctx.equality_expr())
            op = self.visit(ctx.equality())
            rhs = self.visit(ctx.compare_expr())
            return BinaryOp(lhs, op, rhs)
        else:
            return self.visit(ctx.compare_expr())

    def visitEquality(self, ctx:TyCParser.EqualityContext):
        if ctx.IS_EQUAL():
            return ctx.IS_EQUAL().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()

    def visitCompare_expr(self, ctx):
        # compare_expr: compare_expr compare add_expr | add_expr;
        if ctx.compare():
            lhs = self.visit(ctx.compare_expr())
            op = self.visit(ctx.compare())
            rhs = self.visit(ctx.add_expr())
            return BinaryOp(lhs, op, rhs)
        else:
            return self.visit(ctx.add_expr())

    def visitCompare(self, ctx:TyCParser.CompareContext):
        # compare: LESS_THAN | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL;
        if ctx.LESS_THAN():
            return ctx.LESS_THAN().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()  
        elif ctx.LESS_OR_EQUAL():
            return ctx.LESS_OR_EQUAL().getText()
        elif ctx.GREATER_OR_EQUAL():
            return ctx.GREATER_OR_EQUAL().getText()

    def visitAdd_expr(self, ctx):
        # add_expr: add_expr add mul_expr | mul_expr;
        if ctx.add():
            lhs = self.visit(ctx.add_expr())
            op = self.visit(ctx.add())
            rhs = self.visit(ctx.mul_expr())
            return BinaryOp(lhs, op, rhs)
        else:
            return self.visit(ctx.mul_expr())

    # Visit a parse tree produced by TyCParser#add.
    def visitAdd(self, ctx:TyCParser.AddContext):
        # add: OP_ADD | OP_SUB;
        if ctx.OP_ADD():
            return ctx.OP_ADD().getText()
        elif ctx.OP_SUB():
            return ctx.OP_SUB().getText()

    def visitMul_expr(self, ctx):
        # mul_expr: mul_expr mul unary_expr | unary_expr;
        if ctx.mul():
            lhs = self.visit(ctx.mul_expr())
            op = self.visit(ctx.mul())
            rhs = self.visit(ctx.unary_expr())
            return BinaryOp(lhs, op, rhs)
        else:
            return self.visit(ctx.unary_expr())
    
    def visitMul(self, ctx:TyCParser.MulContext):
        # mul: OP_MUL | OP_DIV | OP_MOD;
        if ctx.OP_MUL():
            return ctx.OP_MUL().getText()
        elif ctx.OP_DIV():
            return ctx.OP_DIV().getText()
        elif ctx.OP_MOD():
            return ctx.OP_MOD().getText()

    def visitUnary_expr(self, ctx):
        # unary_expr: unary unary_expr | prefix_expr;
        if ctx.unary():
            op = self.visit(ctx.unary())
            operand = self.visit(ctx.unary_expr())
            return PrefixOp(op, operand)
        else:
            return self.visit(ctx.prefix_expr())

    def visitUnary(self, ctx:TyCParser.UnaryContext):
        # unary: LOG_NOT | OP_SUB | OP_ADD;
        if ctx.LOG_NOT():
            return ctx.LOG_NOT().getText()
        elif ctx.OP_SUB():
            return ctx.OP_SUB().getText()
        elif ctx.OP_ADD():
            return ctx.OP_ADD().getText()

# ======================================================
# POSTFIX / MEMBER
# ======================================================

    def visitPrefix_expr(self, ctx):
        # prefix_expr: fix_op prefix_expr | postfix_expr;
        if ctx.fix_op():
            op = self.visit(ctx.fix_op())
            operand = self.visit(ctx.prefix_expr())
            return PrefixOp(op, operand)
        else:
            return self.visit(ctx.postfix_expr())

    def visitPostfix_expr(self, ctx):
        # postfix_expr: postfix_expr fix_op | member_expr;
        if (ctx.fix_op()):
            op = self.visit(ctx.fix_op())
            operand = self.visit(ctx.postfix_expr())
            return PostfixOp(op, operand)
        else:
            return self.visit(ctx.member_expr())
        
    def visitFix_op(self, ctx):
        # ppfix: INCREMENT | DECREMENT;
        if ctx.INCREMENT():
            return ctx.INCREMENT().getText()
        else: 
            return ctx.DECREMENT().getText()

    def visitMember_expr(self, ctx):
        # member_expr: primary_expr member_access_tail;
        if ctx.member_access_tail():
            obj = self.visit(ctx.primary_expr())
            tail = self.visit(ctx.member_access_tail())
            # ở đây thiết kế mà Member
            return reduce(lambda x, member: MemberAccess(x, member), tail, obj)
        else:
            return self.visit(ctx.primary_expr())

    def visitMember_access_tail(self, ctx):
        # member_access_tail: MEMBER_ACCESS ID member_access_tail | ;
        if ctx.ID():
            tail = self.visit(ctx.member_access_tail())
            return [ctx.ID().getText()] + tail
        else:
            return []

# ======================================================
# PRIMARY
# ======================================================

    def visitPrimary_expr(self, ctx):
        # primary_expr: LIT_INT
        #   | LIT_FLOAT
        #   | LIT_STRING
        #   | ID
        #   | funcall
        #   | struct_lit
        #   | LP expression RP;
        if ctx.LIT_INT():
            return IntLiteral(int(ctx.LIT_INT().getText()))
        elif ctx.LIT_FLOAT():
            return FloatLiteral(float(ctx.LIT_FLOAT().getText()))
        elif ctx.LIT_STRING():
            return StringLiteral(ctx.LIT_STRING().getText())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
        elif ctx.funcall():
            return self.visit(ctx.funcall())
        else:
            return self.visit(ctx.expression())

# ======================================================
# ARGUMENT
# ======================================================

    def visitFuncall(self, ctx:TyCParser.FuncallContext):
        # funcall: ID LP argument_prime RP; //
        name = ctx.ID().getText()
        args = self.visit(ctx.argument_prime())
        return FuncCall(name, args)

    def visitArgument_prime(self, ctx):
        # argument_prime: argument_list | ;
        if ctx.argument_list():
            return self.visit(ctx.argument_list())
        else:
            return []

    def visitArgument_list(self, ctx):
        # argument_list: argument COMMA argument_list | argument;
        if ctx.COMMA():
            argument_list = self.visit(ctx.argument_list())
            argument = self.visit(ctx.argument())
            return [argument] + argument_list
        else:
            argument = self.visit(ctx.argument())
            return [argument]

    def visitArgument(self, ctx):
        # argument: or_expr;
        return self.visit(ctx.or_expr())
