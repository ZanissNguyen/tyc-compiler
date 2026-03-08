"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""

    # need to override!

    # Visit a parse tree produced by TyCParser#program.
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#type.
    def visitType(self, ctx:TyCParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#structdcl.
    def visitStructdcl(self, ctx:TyCParser.StructdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#member_list.
    def visitMember_list(self, ctx:TyCParser.Member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#member.
    def visitMember(self, ctx:TyCParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#member_type.
    def visitMember_type(self, ctx:TyCParser.Member_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#vardecl.
    def visitVardecl(self, ctx:TyCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_lit.
    def visitStruct_lit(self, ctx:TyCParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#memberdcl_prime.
    def visitMemberdcl_prime(self, ctx:TyCParser.Memberdcl_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#memberdcl_list.
    def visitMemberdcl_list(self, ctx:TyCParser.Memberdcl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#memberdcl.
    def visitMemberdcl(self, ctx:TyCParser.MemberdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#funcdecl.
    def visitFuncdecl(self, ctx:TyCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#parameter_prime.
    def visitParameter_prime(self, ctx:TyCParser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#parameter_list.
    def visitParameter_list(self, ctx:TyCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#parameter.
    def visitParameter(self, ctx:TyCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#body.
    def visitBody(self, ctx:TyCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#statement_prime.
    def visitStatement_prime(self, ctx:TyCParser.Statement_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#statement_list.
    def visitStatement_list(self, ctx:TyCParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#statement.
    def visitStatement(self, ctx:TyCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#ifStmt.
    def visitIfStmt(self, ctx:TyCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#whileStmt.
    def visitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#forStmt.
    def visitForStmt(self, ctx:TyCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#forInit.
    def visitForInit(self, ctx:TyCParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#forCondition.
    def visitForCondition(self, ctx:TyCParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#forUpdate.
    def visitForUpdate(self, ctx:TyCParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#breakStmt.
    def visitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#continueStmt.
    def visitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#returnStmt.
    def visitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#switchStmt.
    def visitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#switchBody.
    def visitSwitchBody(self, ctx:TyCParser.SwitchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_list.
    def visitCase_list(self, ctx:TyCParser.Case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#normal_case.
    def visitNormal_case(self, ctx:TyCParser.Normal_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#default_case.
    def visitDefault_case(self, ctx:TyCParser.Default_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expression.
    def visitExpression(self, ctx:TyCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#assignable.
    def visitAssignable(self, ctx:TyCParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#assignStmt.
    def visitAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#or_expr.
    def visitOr_expr(self, ctx:TyCParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#and_expr.
    def visitAnd_expr(self, ctx:TyCParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#equality_expr.
    def visitEquality_expr(self, ctx:TyCParser.Equality_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#equality.
    def visitEquality(self, ctx:TyCParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#compare_expr.
    def visitCompare_expr(self, ctx:TyCParser.Compare_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#compare.
    def visitCompare(self, ctx:TyCParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#add_expr.
    def visitAdd_expr(self, ctx:TyCParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#add.
    def visitAdd(self, ctx:TyCParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#mul_expr.
    def visitMul_expr(self, ctx:TyCParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#mul.
    def visitMul(self, ctx:TyCParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#unary_expr.
    def visitUnary_expr(self, ctx:TyCParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#unary.
    def visitUnary(self, ctx:TyCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#prefix_expr.
    def visitPrefix_expr(self, ctx:TyCParser.Prefix_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#postfix_expr.
    def visitPostfix_expr(self, ctx:TyCParser.Postfix_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#postfix_op.
    def visitPostfix_op(self, ctx:TyCParser.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#ppfix.
    def visitPpfix(self, ctx:TyCParser.PpfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#member_expr.
    def visitMember_expr(self, ctx:TyCParser.Member_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#member_access_tail.
    def visitMember_access_tail(self, ctx:TyCParser.Member_access_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#primary_expr.
    def visitPrimary_expr(self, ctx:TyCParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#argument_prime.
    def visitArgument_prime(self, ctx:TyCParser.Argument_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#argument_list.
    def visitArgument_list(self, ctx:TyCParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#argument.
    def visitArgument(self, ctx:TyCParser.ArgumentContext):
        return self.visitChildren(ctx)
