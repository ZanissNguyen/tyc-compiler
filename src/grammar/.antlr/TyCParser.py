# Generated from c:/Users/thanh/Downloads/HCMUT/_NamBa/_HocKy252/CO3005_PPL/btl/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,422,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,0,1,0,5,0,
        94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,3,3,114,8,3,1,4,1,4,3,4,118,8,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,3,5,127,8,5,1,5,1,5,1,5,1,5,3,5,133,8,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,144,8,5,1,6,1,6,3,6,148,8,6,1,7,
        1,7,1,7,1,7,1,7,3,7,155,8,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,164,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,172,8,10,10,10,12,10,175,
        9,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,183,8,11,10,11,12,11,186,
        9,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,194,8,12,10,12,12,12,197,
        9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,205,8,13,10,13,12,13,208,
        9,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,216,8,14,10,14,12,14,219,
        9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,227,8,15,10,15,12,15,230,
        9,15,1,16,1,16,1,16,3,16,235,8,16,1,17,1,17,1,17,3,17,240,8,17,1,
        18,1,18,5,18,244,8,18,10,18,12,18,247,9,18,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,257,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,267,8,20,1,21,1,21,3,21,271,8,21,1,22,1,22,1,22,1,22,
        1,22,3,22,278,8,22,1,23,1,23,1,24,1,24,1,24,3,24,285,8,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,25,1,25,3,25,295,8,25,1,26,1,26,1,26,1,
        26,1,26,3,26,302,8,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,
        29,3,29,313,8,29,1,30,1,30,1,30,1,30,3,30,319,8,30,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,333,8,31,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,3,33,352,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,
        1,35,1,35,3,35,363,8,35,1,35,1,35,3,35,367,8,35,1,35,1,35,3,35,371,
        8,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,3,38,
        384,8,38,1,38,1,38,1,38,3,38,389,8,38,1,39,1,39,1,39,1,39,1,39,1,
        39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,3,41,405,8,41,1,42,4,
        42,408,8,42,11,42,12,42,409,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,
        43,3,43,420,8,43,1,43,0,6,20,22,24,26,28,30,44,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,0,7,1,0,4,6,1,0,24,25,
        1,0,26,29,1,0,19,20,1,0,21,23,2,0,19,20,32,32,1,0,33,34,432,0,95,
        1,0,0,0,2,100,1,0,0,0,4,102,1,0,0,0,6,113,1,0,0,0,8,117,1,0,0,0,
        10,143,1,0,0,0,12,147,1,0,0,0,14,154,1,0,0,0,16,156,1,0,0,0,18,163,
        1,0,0,0,20,165,1,0,0,0,22,176,1,0,0,0,24,187,1,0,0,0,26,198,1,0,
        0,0,28,209,1,0,0,0,30,220,1,0,0,0,32,234,1,0,0,0,34,239,1,0,0,0,
        36,241,1,0,0,0,38,256,1,0,0,0,40,266,1,0,0,0,42,270,1,0,0,0,44,277,
        1,0,0,0,46,279,1,0,0,0,48,284,1,0,0,0,50,294,1,0,0,0,52,301,1,0,
        0,0,54,303,1,0,0,0,56,306,1,0,0,0,58,312,1,0,0,0,60,318,1,0,0,0,
        62,332,1,0,0,0,64,334,1,0,0,0,66,351,1,0,0,0,68,353,1,0,0,0,70,359,
        1,0,0,0,72,375,1,0,0,0,74,378,1,0,0,0,76,388,1,0,0,0,78,390,1,0,
        0,0,80,396,1,0,0,0,82,404,1,0,0,0,84,407,1,0,0,0,86,419,1,0,0,0,
        88,94,3,4,2,0,89,90,3,10,5,0,90,91,5,41,0,0,91,94,1,0,0,0,92,94,
        3,48,24,0,93,88,1,0,0,0,93,89,1,0,0,0,93,92,1,0,0,0,94,97,1,0,0,
        0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,
        5,0,0,1,99,1,1,0,0,0,100,101,7,0,0,0,101,3,1,0,0,0,102,103,5,8,0,
        0,103,104,5,48,0,0,104,105,5,37,0,0,105,106,3,6,3,0,106,107,5,38,
        0,0,107,108,5,41,0,0,108,5,1,0,0,0,109,110,3,8,4,0,110,111,3,6,3,
        0,111,114,1,0,0,0,112,114,1,0,0,0,113,109,1,0,0,0,113,112,1,0,0,
        0,114,7,1,0,0,0,115,118,3,2,1,0,116,118,5,48,0,0,117,115,1,0,0,0,
        117,116,1,0,0,0,118,119,1,0,0,0,119,120,5,48,0,0,120,121,5,41,0,
        0,121,9,1,0,0,0,122,123,3,2,1,0,123,126,5,48,0,0,124,125,5,35,0,
        0,125,127,3,20,10,0,126,124,1,0,0,0,126,127,1,0,0,0,127,144,1,0,
        0,0,128,129,5,3,0,0,129,132,5,48,0,0,130,131,5,35,0,0,131,133,3,
        20,10,0,132,130,1,0,0,0,132,133,1,0,0,0,133,144,1,0,0,0,134,135,
        5,48,0,0,135,144,5,48,0,0,136,137,5,48,0,0,137,138,5,48,0,0,138,
        139,5,35,0,0,139,140,5,37,0,0,140,141,3,12,6,0,141,142,5,38,0,0,
        142,144,1,0,0,0,143,122,1,0,0,0,143,128,1,0,0,0,143,134,1,0,0,0,
        143,136,1,0,0,0,144,11,1,0,0,0,145,148,3,14,7,0,146,148,1,0,0,0,
        147,145,1,0,0,0,147,146,1,0,0,0,148,13,1,0,0,0,149,150,3,16,8,0,
        150,151,5,42,0,0,151,152,3,14,7,0,152,155,1,0,0,0,153,155,3,16,8,
        0,154,149,1,0,0,0,154,153,1,0,0,0,155,15,1,0,0,0,156,157,3,20,10,
        0,157,17,1,0,0,0,158,159,3,36,18,0,159,160,5,35,0,0,160,161,3,18,
        9,0,161,164,1,0,0,0,162,164,3,20,10,0,163,158,1,0,0,0,163,162,1,
        0,0,0,164,19,1,0,0,0,165,166,6,10,-1,0,166,167,3,22,11,0,167,173,
        1,0,0,0,168,169,10,2,0,0,169,170,5,30,0,0,170,172,3,22,11,0,171,
        168,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,
        21,1,0,0,0,175,173,1,0,0,0,176,177,6,11,-1,0,177,178,3,24,12,0,178,
        184,1,0,0,0,179,180,10,2,0,0,180,181,5,31,0,0,181,183,3,24,12,0,
        182,179,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,
        185,23,1,0,0,0,186,184,1,0,0,0,187,188,6,12,-1,0,188,189,3,26,13,
        0,189,195,1,0,0,0,190,191,10,2,0,0,191,192,7,1,0,0,192,194,3,26,
        13,0,193,190,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,
        0,0,196,25,1,0,0,0,197,195,1,0,0,0,198,199,6,13,-1,0,199,200,3,28,
        14,0,200,206,1,0,0,0,201,202,10,2,0,0,202,203,7,2,0,0,203,205,3,
        28,14,0,204,201,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,
        1,0,0,0,207,27,1,0,0,0,208,206,1,0,0,0,209,210,6,14,-1,0,210,211,
        3,30,15,0,211,217,1,0,0,0,212,213,10,2,0,0,213,214,7,3,0,0,214,216,
        3,30,15,0,215,212,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,
        1,0,0,0,218,29,1,0,0,0,219,217,1,0,0,0,220,221,6,15,-1,0,221,222,
        3,32,16,0,222,228,1,0,0,0,223,224,10,2,0,0,224,225,7,4,0,0,225,227,
        3,32,16,0,226,223,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,
        1,0,0,0,229,31,1,0,0,0,230,228,1,0,0,0,231,232,7,5,0,0,232,235,3,
        32,16,0,233,235,3,34,17,0,234,231,1,0,0,0,234,233,1,0,0,0,235,33,
        1,0,0,0,236,237,7,6,0,0,237,240,3,36,18,0,238,240,3,36,18,0,239,
        236,1,0,0,0,239,238,1,0,0,0,240,35,1,0,0,0,241,245,3,40,20,0,242,
        244,3,38,19,0,243,242,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,
        246,1,0,0,0,246,37,1,0,0,0,247,245,1,0,0,0,248,257,5,33,0,0,249,
        257,5,34,0,0,250,251,5,36,0,0,251,257,5,48,0,0,252,253,5,39,0,0,
        253,254,3,42,21,0,254,255,5,40,0,0,255,257,1,0,0,0,256,248,1,0,0,
        0,256,249,1,0,0,0,256,250,1,0,0,0,256,252,1,0,0,0,257,39,1,0,0,0,
        258,267,5,45,0,0,259,267,5,46,0,0,260,267,5,47,0,0,261,267,5,48,
        0,0,262,263,5,39,0,0,263,264,3,18,9,0,264,265,5,40,0,0,265,267,1,
        0,0,0,266,258,1,0,0,0,266,259,1,0,0,0,266,260,1,0,0,0,266,261,1,
        0,0,0,266,262,1,0,0,0,267,41,1,0,0,0,268,271,3,44,22,0,269,271,1,
        0,0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,43,1,0,0,0,272,273,3,46,
        23,0,273,274,5,42,0,0,274,275,3,44,22,0,275,278,1,0,0,0,276,278,
        3,46,23,0,277,272,1,0,0,0,277,276,1,0,0,0,278,45,1,0,0,0,279,280,
        3,20,10,0,280,47,1,0,0,0,281,285,3,2,1,0,282,285,5,7,0,0,283,285,
        5,48,0,0,284,281,1,0,0,0,284,282,1,0,0,0,284,283,1,0,0,0,285,286,
        1,0,0,0,286,287,5,48,0,0,287,288,5,39,0,0,288,289,3,50,25,0,289,
        290,5,40,0,0,290,291,3,56,28,0,291,49,1,0,0,0,292,295,3,52,26,0,
        293,295,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,51,1,0,0,0,296,
        297,3,54,27,0,297,298,5,42,0,0,298,299,3,52,26,0,299,302,1,0,0,0,
        300,302,1,0,0,0,301,296,1,0,0,0,301,300,1,0,0,0,302,53,1,0,0,0,303,
        304,3,2,1,0,304,305,5,48,0,0,305,55,1,0,0,0,306,307,5,37,0,0,307,
        308,3,58,29,0,308,309,5,38,0,0,309,57,1,0,0,0,310,313,3,60,30,0,
        311,313,1,0,0,0,312,310,1,0,0,0,312,311,1,0,0,0,313,59,1,0,0,0,314,
        315,3,62,31,0,315,316,3,60,30,0,316,319,1,0,0,0,317,319,1,0,0,0,
        318,314,1,0,0,0,318,317,1,0,0,0,319,61,1,0,0,0,320,321,3,10,5,0,
        321,322,5,41,0,0,322,333,1,0,0,0,323,333,3,64,32,0,324,333,3,56,
        28,0,325,333,3,66,33,0,326,333,3,68,34,0,327,333,3,70,35,0,328,333,
        3,78,39,0,329,333,3,72,36,0,330,333,3,74,37,0,331,333,3,76,38,0,
        332,320,1,0,0,0,332,323,1,0,0,0,332,324,1,0,0,0,332,325,1,0,0,0,
        332,326,1,0,0,0,332,327,1,0,0,0,332,328,1,0,0,0,332,329,1,0,0,0,
        332,330,1,0,0,0,332,331,1,0,0,0,333,63,1,0,0,0,334,335,3,18,9,0,
        335,336,5,41,0,0,336,65,1,0,0,0,337,338,5,15,0,0,338,339,5,39,0,
        0,339,340,3,18,9,0,340,341,5,40,0,0,341,342,3,62,31,0,342,343,5,
        13,0,0,343,344,3,62,31,0,344,352,1,0,0,0,345,346,5,15,0,0,346,347,
        5,39,0,0,347,348,3,18,9,0,348,349,5,40,0,0,349,350,3,62,31,0,350,
        352,1,0,0,0,351,337,1,0,0,0,351,345,1,0,0,0,352,67,1,0,0,0,353,354,
        5,18,0,0,354,355,5,39,0,0,355,356,3,18,9,0,356,357,5,40,0,0,357,
        358,3,62,31,0,358,69,1,0,0,0,359,360,5,14,0,0,360,362,5,39,0,0,361,
        363,3,10,5,0,362,361,1,0,0,0,362,363,1,0,0,0,363,364,1,0,0,0,364,
        366,5,41,0,0,365,367,3,18,9,0,366,365,1,0,0,0,366,367,1,0,0,0,367,
        368,1,0,0,0,368,370,5,41,0,0,369,371,3,18,9,0,370,369,1,0,0,0,370,
        371,1,0,0,0,371,372,1,0,0,0,372,373,5,40,0,0,373,374,3,62,31,0,374,
        71,1,0,0,0,375,376,5,9,0,0,376,377,5,41,0,0,377,73,1,0,0,0,378,379,
        5,11,0,0,379,380,5,41,0,0,380,75,1,0,0,0,381,383,5,17,0,0,382,384,
        3,18,9,0,383,382,1,0,0,0,383,384,1,0,0,0,384,385,1,0,0,0,385,389,
        5,41,0,0,386,387,5,17,0,0,387,389,5,41,0,0,388,381,1,0,0,0,388,386,
        1,0,0,0,389,77,1,0,0,0,390,391,5,16,0,0,391,392,5,39,0,0,392,393,
        3,18,9,0,393,394,5,40,0,0,394,395,3,80,40,0,395,79,1,0,0,0,396,397,
        5,37,0,0,397,398,3,82,41,0,398,399,5,38,0,0,399,81,1,0,0,0,400,401,
        3,84,42,0,401,402,3,82,41,0,402,405,1,0,0,0,403,405,1,0,0,0,404,
        400,1,0,0,0,404,403,1,0,0,0,405,83,1,0,0,0,406,408,3,86,43,0,407,
        406,1,0,0,0,408,409,1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,
        411,1,0,0,0,411,412,3,60,30,0,412,85,1,0,0,0,413,414,5,10,0,0,414,
        415,3,18,9,0,415,416,5,43,0,0,416,420,1,0,0,0,417,418,5,12,0,0,418,
        420,5,43,0,0,419,413,1,0,0,0,419,417,1,0,0,0,420,87,1,0,0,0,38,93,
        95,113,117,126,132,143,147,154,163,173,184,195,206,217,228,234,239,
        245,256,266,270,277,284,294,301,312,318,332,351,362,366,370,383,
        388,404,409,419
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'float'", 
                     "'int'", "'string'", "'void'", "'struct'", "'break'", 
                     "'case'", "'continue'", "'default'", "'else'", "'for'", 
                     "'if'", "'switch'", "'return'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'!'", "'++'", "'--'", 
                     "'='", "'.'", "'{'", "'}'", "'('", "')'", "';'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "MULTI_LINE_COMMENT", "SINGLE_LINE_COMMENT", 
                      "TYPE_AUTO", "TYPE_FLOAT", "TYPE_INT", "TYPE_STRING", 
                      "TYPE_VOID", "TYPE_STRUCT", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FOR", "IF", "SWITCH", "RETURN", 
                      "WHILE", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", 
                      "IS_EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER", "LESS_OR_EQUAL", 
                      "GREATER_OR_EQUAL", "LOG_OR", "LOG_AND", "LOG_NOT", 
                      "INCREMENT", "DECREMENT", "ASSIGNMENT", "MEMBER_ACCESS", 
                      "LBR", "RBR", "LP", "RP", "SEMI", "COMMA", "COLON", 
                      "NEWLINE", "LIT_INT", "LIT_FLOAT", "LIT_STRING", "ID", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_type = 1
    RULE_structdcl = 2
    RULE_member_list = 3
    RULE_member = 4
    RULE_vardecl = 5
    RULE_memberdcl_prime = 6
    RULE_memberdcl_list = 7
    RULE_memberdcl = 8
    RULE_assignment_expr = 9
    RULE_or_expr = 10
    RULE_and_expr = 11
    RULE_equality_expr = 12
    RULE_compare_expr = 13
    RULE_add_expr = 14
    RULE_mul_expr = 15
    RULE_unary_expr = 16
    RULE_prefix_expr = 17
    RULE_postfix_expr = 18
    RULE_postfix_op = 19
    RULE_primary_expr = 20
    RULE_argument_prime = 21
    RULE_argument_list = 22
    RULE_argument = 23
    RULE_funcdecl = 24
    RULE_parameter_prime = 25
    RULE_parameter_list = 26
    RULE_parameter = 27
    RULE_body = 28
    RULE_statement_prime = 29
    RULE_statement_list = 30
    RULE_statement = 31
    RULE_assignStmt = 32
    RULE_ifStmt = 33
    RULE_whileStmt = 34
    RULE_forStmt = 35
    RULE_breakStmt = 36
    RULE_continueStmt = 37
    RULE_returnStmt = 38
    RULE_switchStmt = 39
    RULE_switchBody = 40
    RULE_case_list = 41
    RULE_case = 42
    RULE_case_label = 43

    ruleNames =  [ "program", "type", "structdcl", "member_list", "member", 
                   "vardecl", "memberdcl_prime", "memberdcl_list", "memberdcl", 
                   "assignment_expr", "or_expr", "and_expr", "equality_expr", 
                   "compare_expr", "add_expr", "mul_expr", "unary_expr", 
                   "prefix_expr", "postfix_expr", "postfix_op", "primary_expr", 
                   "argument_prime", "argument_list", "argument", "funcdecl", 
                   "parameter_prime", "parameter_list", "parameter", "body", 
                   "statement_prime", "statement_list", "statement", "assignStmt", 
                   "ifStmt", "whileStmt", "forStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "switchStmt", "switchBody", "case_list", 
                   "case", "case_label" ]

    EOF = Token.EOF
    MULTI_LINE_COMMENT=1
    SINGLE_LINE_COMMENT=2
    TYPE_AUTO=3
    TYPE_FLOAT=4
    TYPE_INT=5
    TYPE_STRING=6
    TYPE_VOID=7
    TYPE_STRUCT=8
    BREAK=9
    CASE=10
    CONTINUE=11
    DEFAULT=12
    ELSE=13
    FOR=14
    IF=15
    SWITCH=16
    RETURN=17
    WHILE=18
    OP_ADD=19
    OP_SUB=20
    OP_MUL=21
    OP_DIV=22
    OP_MOD=23
    IS_EQUAL=24
    NOT_EQUAL=25
    LESS_THAN=26
    GREATER=27
    LESS_OR_EQUAL=28
    GREATER_OR_EQUAL=29
    LOG_OR=30
    LOG_AND=31
    LOG_NOT=32
    INCREMENT=33
    DECREMENT=34
    ASSIGNMENT=35
    MEMBER_ACCESS=36
    LBR=37
    RBR=38
    LP=39
    RP=40
    SEMI=41
    COMMA=42
    COLON=43
    NEWLINE=44
    LIT_INT=45
    LIT_FLOAT=46
    LIT_STRING=47
    ID=48
    WS=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def structdcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructdclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructdclContext,i)


        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VardeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VardeclContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474976711160) != 0):
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.structdcl()
                    pass

                elif la_ == 2:
                    self.state = 89
                    self.vardecl()
                    self.state = 90
                    self.match(TyCParser.SEMI)
                    pass

                elif la_ == 3:
                    self.state = 92
                    self.funcdecl()
                    pass


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_FLOAT(self):
            return self.getToken(TyCParser.TYPE_FLOAT, 0)

        def TYPE_INT(self):
            return self.getToken(TyCParser.TYPE_INT, 0)

        def TYPE_STRING(self):
            return self.getToken(TyCParser.TYPE_STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_STRUCT(self):
            return self.getToken(TyCParser.TYPE_STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LBR(self):
            return self.getToken(TyCParser.LBR, 0)

        def member_list(self):
            return self.getTypedRuleContext(TyCParser.Member_listContext,0)


        def RBR(self):
            return self.getToken(TyCParser.RBR, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structdcl




    def structdcl(self):

        localctx = TyCParser.StructdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structdcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(TyCParser.TYPE_STRUCT)
            self.state = 103
            self.match(TyCParser.ID)
            self.state = 104
            self.match(TyCParser.LBR)
            self.state = 105
            self.member_list()
            self.state = 106
            self.match(TyCParser.RBR)
            self.state = 107
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(TyCParser.MemberContext,0)


        def member_list(self):
            return self.getTypedRuleContext(TyCParser.Member_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_member_list




    def member_list(self):

        localctx = TyCParser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member_list)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.member()
                self.state = 110
                self.member_list()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_member




    def member(self):

        localctx = TyCParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.state = 115
                self.type_()
                pass
            elif token in [48]:
                self.state = 116
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self.match(TyCParser.ID)
            self.state = 120
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def TYPE_AUTO(self):
            return self.getToken(TyCParser.TYPE_AUTO, 0)

        def LBR(self):
            return self.getToken(TyCParser.LBR, 0)

        def memberdcl_prime(self):
            return self.getTypedRuleContext(TyCParser.Memberdcl_primeContext,0)


        def RBR(self):
            return self.getToken(TyCParser.RBR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_vardecl




    def vardecl(self):

        localctx = TyCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.type_()
                self.state = 123
                self.match(TyCParser.ID)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 124
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 125
                    self.or_expr(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(TyCParser.TYPE_AUTO)
                self.state = 129
                self.match(TyCParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 130
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 131
                    self.or_expr(0)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(TyCParser.ID)
                self.state = 135
                self.match(TyCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(TyCParser.ID)
                self.state = 137
                self.match(TyCParser.ID)
                self.state = 138
                self.match(TyCParser.ASSIGNMENT)
                self.state = 139
                self.match(TyCParser.LBR)
                self.state = 140
                self.memberdcl_prime()
                self.state = 141
                self.match(TyCParser.RBR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Memberdcl_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberdcl_list(self):
            return self.getTypedRuleContext(TyCParser.Memberdcl_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memberdcl_prime




    def memberdcl_prime(self):

        localctx = TyCParser.Memberdcl_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_memberdcl_prime)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32, 33, 34, 39, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.memberdcl_list()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Memberdcl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberdcl(self):
            return self.getTypedRuleContext(TyCParser.MemberdclContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def memberdcl_list(self):
            return self.getTypedRuleContext(TyCParser.Memberdcl_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memberdcl_list




    def memberdcl_list(self):

        localctx = TyCParser.Memberdcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_memberdcl_list)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.memberdcl()
                self.state = 150
                self.match(TyCParser.COMMA)
                self.state = 151
                self.memberdcl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.memberdcl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberdclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memberdcl




    def memberdcl(self):

        localctx = TyCParser.MemberdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_memberdcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.or_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix_expr(self):
            return self.getTypedRuleContext(TyCParser.Postfix_exprContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignment_expr




    def assignment_expr(self):

        localctx = TyCParser.Assignment_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment_expr)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.postfix_expr()
                self.state = 159
                self.match(TyCParser.ASSIGNMENT)
                self.state = 160
                self.assignment_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.or_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(TyCParser.And_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def LOG_OR(self):
            return self.getToken(TyCParser.LOG_OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_or_expr



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 168
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 169
                    self.match(TyCParser.LOG_OR)
                    self.state = 170
                    self.and_expr(0) 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expr(self):
            return self.getTypedRuleContext(TyCParser.Equality_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(TyCParser.And_exprContext,0)


        def LOG_AND(self):
            return self.getToken(TyCParser.LOG_AND, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_and_expr



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.equality_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 179
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 180
                    self.match(TyCParser.LOG_AND)
                    self.state = 181
                    self.equality_expr(0) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Equality_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compare_expr(self):
            return self.getTypedRuleContext(TyCParser.Compare_exprContext,0)


        def equality_expr(self):
            return self.getTypedRuleContext(TyCParser.Equality_exprContext,0)


        def IS_EQUAL(self):
            return self.getToken(TyCParser.IS_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(TyCParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_equality_expr



    def equality_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Equality_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_equality_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.compare_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Equality_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expr)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 192
                    self.compare_expr(0) 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Compare_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(TyCParser.Add_exprContext,0)


        def compare_expr(self):
            return self.getTypedRuleContext(TyCParser.Compare_exprContext,0)


        def LESS_THAN(self):
            return self.getToken(TyCParser.LESS_THAN, 0)

        def GREATER(self):
            return self.getToken(TyCParser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(TyCParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(TyCParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_compare_expr



    def compare_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Compare_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_compare_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Compare_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare_expr)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 203
                    self.add_expr(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(TyCParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(TyCParser.Add_exprContext,0)


        def OP_ADD(self):
            return self.getToken(TyCParser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(TyCParser.OP_SUB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_add_expr



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.mul_expr(0) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(TyCParser.Unary_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(TyCParser.Mul_exprContext,0)


        def OP_MUL(self):
            return self.getToken(TyCParser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(TyCParser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(TyCParser.OP_MOD, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_mul_expr



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.unary_expr() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(TyCParser.Unary_exprContext,0)


        def LOG_NOT(self):
            return self.getToken(TyCParser.LOG_NOT, 0)

        def OP_SUB(self):
            return self.getToken(TyCParser.OP_SUB, 0)

        def OP_ADD(self):
            return self.getToken(TyCParser.OP_ADD, 0)

        def prefix_expr(self):
            return self.getTypedRuleContext(TyCParser.Prefix_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unary_expr




    def unary_expr(self):

        localctx = TyCParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4296540160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.unary_expr()
                pass
            elif token in [33, 34, 39, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.prefix_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix_expr(self):
            return self.getTypedRuleContext(TyCParser.Postfix_exprContext,0)


        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_prefix_expr




    def prefix_expr(self):

        localctx = TyCParser.Prefix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_prefix_expr)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.postfix_expr()
                pass
            elif token in [39, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.postfix_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expr(self):
            return self.getTypedRuleContext(TyCParser.Primary_exprContext,0)


        def postfix_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(TyCParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfix_expr




    def postfix_expr(self):

        localctx = TyCParser.Postfix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_postfix_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.primary_expr()
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 242
                    self.postfix_op() 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def MEMBER_ACCESS(self):
            return self.getToken(TyCParser.MEMBER_ACCESS, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def argument_prime(self):
            return self.getTypedRuleContext(TyCParser.Argument_primeContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_postfix_op




    def postfix_op(self):

        localctx = TyCParser.Postfix_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_postfix_op)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(TyCParser.INCREMENT)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(TyCParser.DECREMENT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 251
                self.match(TyCParser.ID)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(TyCParser.LP)
                self.state = 253
                self.argument_prime()
                self.state = 254
                self.match(TyCParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT_INT(self):
            return self.getToken(TyCParser.LIT_INT, 0)

        def LIT_FLOAT(self):
            return self.getToken(TyCParser.LIT_FLOAT, 0)

        def LIT_STRING(self):
            return self.getToken(TyCParser.LIT_STRING, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primary_expr




    def primary_expr(self):

        localctx = TyCParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primary_expr)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(TyCParser.LIT_INT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(TyCParser.LIT_FLOAT)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(TyCParser.LIT_STRING)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(TyCParser.ID)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.match(TyCParser.LP)
                self.state = 263
                self.assignment_expr()
                self.state = 264
                self.match(TyCParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_list(self):
            return self.getTypedRuleContext(TyCParser.Argument_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_argument_prime




    def argument_prime(self):

        localctx = TyCParser.Argument_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argument_prime)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32, 33, 34, 39, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.argument_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(TyCParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def argument_list(self):
            return self.getTypedRuleContext(TyCParser.Argument_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_argument_list




    def argument_list(self):

        localctx = TyCParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argument_list)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.argument()
                self.state = 273
                self.match(TyCParser.COMMA)
                self.state = 274
                self.argument_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_argument




    def argument(self):

        localctx = TyCParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.or_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def parameter_prime(self):
            return self.getTypedRuleContext(TyCParser.Parameter_primeContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def body(self):
            return self.getTypedRuleContext(TyCParser.BodyContext,0)


        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def TYPE_VOID(self):
            return self.getToken(TyCParser.TYPE_VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.state = 281
                self.type_()
                pass
            elif token in [7]:
                self.state = 282
                self.match(TyCParser.TYPE_VOID)
                pass
            elif token in [48]:
                self.state = 283
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 286
            self.match(TyCParser.ID)
            self.state = 287
            self.match(TyCParser.LP)
            self.state = 288
            self.parameter_prime()
            self.state = 289
            self.match(TyCParser.RP)
            self.state = 290
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_list(self):
            return self.getTypedRuleContext(TyCParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_parameter_prime




    def parameter_prime(self):

        localctx = TyCParser.Parameter_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_parameter_prime)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(TyCParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(TyCParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_parameter_list




    def parameter_list(self):

        localctx = TyCParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_parameter_list)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.parameter()

                self.state = 297
                self.match(TyCParser.COMMA)
                self.state = 298
                self.parameter_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_parameter




    def parameter(self):

        localctx = TyCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.type_()
            self.state = 304
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(TyCParser.LBR, 0)

        def statement_prime(self):
            return self.getTypedRuleContext(TyCParser.Statement_primeContext,0)


        def RBR(self):
            return self.getToken(TyCParser.RBR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_body




    def body(self):

        localctx = TyCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(TyCParser.LBR)
            self.state = 307
            self.statement_prime()
            self.state = 308
            self.match(TyCParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(TyCParser.Statement_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_statement_prime




    def statement_prime(self):

        localctx = TyCParser.Statement_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement_prime)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(TyCParser.Statement_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_statement_list




    def statement_list(self):

        localctx = TyCParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement_list)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 9, 11, 14, 15, 16, 17, 18, 19, 20, 32, 33, 34, 37, 39, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.statement()
                self.state = 315
                self.statement_list()
                pass
            elif token in [10, 12, 38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def assignStmt(self):
            return self.getTypedRuleContext(TyCParser.AssignStmtContext,0)


        def body(self):
            return self.getTypedRuleContext(TyCParser.BodyContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(TyCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(TyCParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(TyCParser.ForStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(TyCParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(TyCParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(TyCParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_statement




    def statement(self):

        localctx = TyCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.vardecl()
                self.state = 321
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.body()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 326
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 327
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 328
                self.switchStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 329
                self.breakStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 330
                self.continueStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 331
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_assignStmt




    def assignStmt(self):

        localctx = TyCParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.assignment_expr()
            self.state = 335
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifStmt




    def ifStmt(self):

        localctx = TyCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifStmt)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(TyCParser.IF)
                self.state = 338
                self.match(TyCParser.LP)
                self.state = 339
                self.assignment_expr()
                self.state = 340
                self.match(TyCParser.RP)
                self.state = 341
                self.statement()
                self.state = 342
                self.match(TyCParser.ELSE)
                self.state = 343
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(TyCParser.IF)
                self.state = 346
                self.match(TyCParser.LP)
                self.state = 347
                self.assignment_expr()
                self.state = 348
                self.match(TyCParser.RP)
                self.state = 349
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whileStmt




    def whileStmt(self):

        localctx = TyCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(TyCParser.WHILE)
            self.state = 354
            self.match(TyCParser.LP)
            self.state = 355
            self.assignment_expr()
            self.state = 356
            self.match(TyCParser.RP)
            self.state = 357
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def assignment_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.Assignment_exprContext)
            else:
                return self.getTypedRuleContext(TyCParser.Assignment_exprContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_forStmt




    def forStmt(self):

        localctx = TyCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(TyCParser.FOR)
            self.state = 360
            self.match(TyCParser.LP)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474976710776) != 0):
                self.state = 361
                self.vardecl()


            self.state = 364
            self.match(TyCParser.SEMI)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 528345403490304) != 0):
                self.state = 365
                self.assignment_expr()


            self.state = 368
            self.match(TyCParser.SEMI)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 528345403490304) != 0):
                self.state = 369
                self.assignment_expr()


            self.state = 372
            self.match(TyCParser.RP)
            self.state = 373
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakStmt




    def breakStmt(self):

        localctx = TyCParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(TyCParser.BREAK)
            self.state = 376
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continueStmt




    def continueStmt(self):

        localctx = TyCParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(TyCParser.CONTINUE)
            self.state = 379
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_returnStmt




    def returnStmt(self):

        localctx = TyCParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(TyCParser.RETURN)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 528345403490304) != 0):
                    self.state = 382
                    self.assignment_expr()


                self.state = 385
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.match(TyCParser.RETURN)
                self.state = 387
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def switchBody(self):
            return self.getTypedRuleContext(TyCParser.SwitchBodyContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchStmt




    def switchStmt(self):

        localctx = TyCParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(TyCParser.SWITCH)
            self.state = 391
            self.match(TyCParser.LP)
            self.state = 392
            self.assignment_expr()
            self.state = 393
            self.match(TyCParser.RP)
            self.state = 394
            self.switchBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(TyCParser.LBR, 0)

        def case_list(self):
            return self.getTypedRuleContext(TyCParser.Case_listContext,0)


        def RBR(self):
            return self.getToken(TyCParser.RBR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_switchBody




    def switchBody(self):

        localctx = TyCParser.SwitchBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_switchBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(TyCParser.LBR)
            self.state = 397
            self.case_list()
            self.state = 398
            self.match(TyCParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case(self):
            return self.getTypedRuleContext(TyCParser.CaseContext,0)


        def case_list(self):
            return self.getTypedRuleContext(TyCParser.Case_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_case_list




    def case_list(self):

        localctx = TyCParser.Case_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_case_list)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.case()
                self.state = 401
                self.case_list()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(TyCParser.Statement_listContext,0)


        def case_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.Case_labelContext)
            else:
                return self.getTypedRuleContext(TyCParser.Case_labelContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_case




    def case(self):

        localctx = TyCParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 406
                    self.case_label()

                else:
                    raise NoViableAltException(self)
                self.state = 409 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 411
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def assignment_expr(self):
            return self.getTypedRuleContext(TyCParser.Assignment_exprContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_case_label




    def case_label(self):

        localctx = TyCParser.Case_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_case_label)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(TyCParser.CASE)
                self.state = 414
                self.assignment_expr()
                self.state = 415
                self.match(TyCParser.COLON)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(TyCParser.DEFAULT)
                self.state = 418
                self.match(TyCParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.or_expr_sempred
        self._predicates[11] = self.and_expr_sempred
        self._predicates[12] = self.equality_expr_sempred
        self._predicates[13] = self.compare_expr_sempred
        self._predicates[14] = self.add_expr_sempred
        self._predicates[15] = self.mul_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def or_expr_sempred(self, localctx:Or_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def equality_expr_sempred(self, localctx:Equality_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def compare_expr_sempred(self, localctx:Compare_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




