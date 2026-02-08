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
        4,1,51,428,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,5,0,93,
        8,0,10,0,12,0,96,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,3,3,113,8,3,1,4,1,4,3,4,117,8,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,3,5,126,8,5,1,5,1,5,1,5,1,5,3,5,132,8,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,143,8,5,1,6,1,6,3,6,147,8,6,1,7,1,7,
        1,7,1,7,1,7,3,7,154,8,7,1,8,1,8,1,8,1,8,1,8,3,8,161,8,8,1,9,1,9,
        1,9,3,9,166,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,176,8,10,
        1,11,1,11,1,11,1,11,1,11,3,11,183,8,11,1,12,1,12,3,12,187,8,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,3,14,197,8,14,1,15,1,15,1,
        15,1,15,3,15,203,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,217,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,236,8,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,248,8,
        20,1,20,1,20,3,20,252,8,20,1,20,1,20,3,20,256,8,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,3,23,269,8,23,1,23,1,23,
        1,23,3,23,274,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,3,26,290,8,26,1,27,1,27,3,27,294,8,27,1,
        28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,
        30,3,30,310,8,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,318,8,31,10,
        31,12,31,321,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,329,8,32,10,
        32,12,32,332,9,32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,340,8,33,10,
        33,12,33,343,9,33,1,34,1,34,1,34,1,34,1,34,1,34,5,34,351,8,34,10,
        34,12,34,354,9,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,362,8,35,10,
        35,12,35,365,9,35,1,36,1,36,1,36,1,36,1,36,1,36,5,36,373,8,36,10,
        36,12,36,376,9,36,1,37,1,37,1,37,3,37,381,8,37,1,38,1,38,1,38,3,
        38,386,8,38,1,39,1,39,5,39,390,8,39,10,39,12,39,393,9,39,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,403,8,40,1,41,1,41,1,41,1,
        41,1,41,1,41,1,41,1,41,3,41,413,8,41,1,42,1,42,3,42,417,8,42,1,43,
        1,43,1,43,1,43,1,43,3,43,424,8,43,1,44,1,44,1,44,0,6,62,64,66,68,
        70,72,45,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,0,7,1,0,4,6,1,0,24,25,1,0,26,29,1,0,19,20,1,0,21,23,2,0,
        19,20,32,32,1,0,33,34,439,0,94,1,0,0,0,2,99,1,0,0,0,4,101,1,0,0,
        0,6,112,1,0,0,0,8,116,1,0,0,0,10,142,1,0,0,0,12,146,1,0,0,0,14,153,
        1,0,0,0,16,160,1,0,0,0,18,165,1,0,0,0,20,175,1,0,0,0,22,182,1,0,
        0,0,24,186,1,0,0,0,26,190,1,0,0,0,28,196,1,0,0,0,30,202,1,0,0,0,
        32,216,1,0,0,0,34,218,1,0,0,0,36,235,1,0,0,0,38,237,1,0,0,0,40,243,
        1,0,0,0,42,260,1,0,0,0,44,263,1,0,0,0,46,273,1,0,0,0,48,275,1,0,
        0,0,50,281,1,0,0,0,52,289,1,0,0,0,54,293,1,0,0,0,56,295,1,0,0,0,
        58,300,1,0,0,0,60,309,1,0,0,0,62,311,1,0,0,0,64,322,1,0,0,0,66,333,
        1,0,0,0,68,344,1,0,0,0,70,355,1,0,0,0,72,366,1,0,0,0,74,380,1,0,
        0,0,76,385,1,0,0,0,78,387,1,0,0,0,80,402,1,0,0,0,82,412,1,0,0,0,
        84,416,1,0,0,0,86,423,1,0,0,0,88,425,1,0,0,0,90,93,3,4,2,0,91,93,
        3,18,9,0,92,90,1,0,0,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,
        94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,0,0,1,98,1,1,0,
        0,0,99,100,7,0,0,0,100,3,1,0,0,0,101,102,5,8,0,0,102,103,5,47,0,
        0,103,104,5,37,0,0,104,105,3,6,3,0,105,106,5,38,0,0,106,107,5,41,
        0,0,107,5,1,0,0,0,108,109,3,8,4,0,109,110,3,6,3,0,110,113,1,0,0,
        0,111,113,1,0,0,0,112,108,1,0,0,0,112,111,1,0,0,0,113,7,1,0,0,0,
        114,117,3,2,1,0,115,117,5,47,0,0,116,114,1,0,0,0,116,115,1,0,0,0,
        117,118,1,0,0,0,118,119,5,47,0,0,119,120,5,41,0,0,120,9,1,0,0,0,
        121,122,3,2,1,0,122,125,5,47,0,0,123,124,5,35,0,0,124,126,3,62,31,
        0,125,123,1,0,0,0,125,126,1,0,0,0,126,143,1,0,0,0,127,128,5,3,0,
        0,128,131,5,47,0,0,129,130,5,35,0,0,130,132,3,62,31,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,143,1,0,0,0,133,134,5,47,0,0,134,143,5,
        47,0,0,135,136,5,47,0,0,136,137,5,47,0,0,137,138,5,35,0,0,138,139,
        5,37,0,0,139,140,3,12,6,0,140,141,5,38,0,0,141,143,1,0,0,0,142,121,
        1,0,0,0,142,127,1,0,0,0,142,133,1,0,0,0,142,135,1,0,0,0,143,11,1,
        0,0,0,144,147,3,14,7,0,145,147,1,0,0,0,146,144,1,0,0,0,146,145,1,
        0,0,0,147,13,1,0,0,0,148,149,3,16,8,0,149,150,5,42,0,0,150,151,3,
        14,7,0,151,154,1,0,0,0,152,154,3,16,8,0,153,148,1,0,0,0,153,152,
        1,0,0,0,154,15,1,0,0,0,155,161,3,62,31,0,156,157,5,37,0,0,157,158,
        3,12,6,0,158,159,5,38,0,0,159,161,1,0,0,0,160,155,1,0,0,0,160,156,
        1,0,0,0,161,17,1,0,0,0,162,166,3,2,1,0,163,166,5,7,0,0,164,166,5,
        47,0,0,165,162,1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,165,166,1,
        0,0,0,166,167,1,0,0,0,167,168,5,47,0,0,168,169,5,39,0,0,169,170,
        3,20,10,0,170,171,5,40,0,0,171,172,3,26,13,0,172,19,1,0,0,0,173,
        176,3,22,11,0,174,176,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,
        21,1,0,0,0,177,178,3,24,12,0,178,179,5,42,0,0,179,180,3,22,11,0,
        180,183,1,0,0,0,181,183,3,24,12,0,182,177,1,0,0,0,182,181,1,0,0,
        0,183,23,1,0,0,0,184,187,3,2,1,0,185,187,5,47,0,0,186,184,1,0,0,
        0,186,185,1,0,0,0,187,188,1,0,0,0,188,189,5,47,0,0,189,25,1,0,0,
        0,190,191,5,37,0,0,191,192,3,28,14,0,192,193,5,38,0,0,193,27,1,0,
        0,0,194,197,3,30,15,0,195,197,1,0,0,0,196,194,1,0,0,0,196,195,1,
        0,0,0,197,29,1,0,0,0,198,199,3,32,16,0,199,200,3,30,15,0,200,203,
        1,0,0,0,201,203,1,0,0,0,202,198,1,0,0,0,202,201,1,0,0,0,203,31,1,
        0,0,0,204,205,3,10,5,0,205,206,5,41,0,0,206,217,1,0,0,0,207,217,
        3,34,17,0,208,217,3,26,13,0,209,217,3,36,18,0,210,217,3,38,19,0,
        211,217,3,40,20,0,212,217,3,48,24,0,213,217,3,42,21,0,214,217,3,
        44,22,0,215,217,3,46,23,0,216,204,1,0,0,0,216,207,1,0,0,0,216,208,
        1,0,0,0,216,209,1,0,0,0,216,210,1,0,0,0,216,211,1,0,0,0,216,212,
        1,0,0,0,216,213,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,0,217,33,1,
        0,0,0,218,219,3,60,30,0,219,220,5,41,0,0,220,35,1,0,0,0,221,222,
        5,15,0,0,222,223,5,39,0,0,223,224,3,60,30,0,224,225,5,40,0,0,225,
        226,3,32,16,0,226,227,5,13,0,0,227,228,3,32,16,0,228,236,1,0,0,0,
        229,230,5,15,0,0,230,231,5,39,0,0,231,232,3,60,30,0,232,233,5,40,
        0,0,233,234,3,32,16,0,234,236,1,0,0,0,235,221,1,0,0,0,235,229,1,
        0,0,0,236,37,1,0,0,0,237,238,5,18,0,0,238,239,5,39,0,0,239,240,3,
        60,30,0,240,241,5,40,0,0,241,242,3,32,16,0,242,39,1,0,0,0,243,244,
        5,14,0,0,244,247,5,39,0,0,245,248,3,10,5,0,246,248,3,60,30,0,247,
        245,1,0,0,0,247,246,1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,
        251,5,41,0,0,250,252,3,60,30,0,251,250,1,0,0,0,251,252,1,0,0,0,252,
        253,1,0,0,0,253,255,5,41,0,0,254,256,3,60,30,0,255,254,1,0,0,0,255,
        256,1,0,0,0,256,257,1,0,0,0,257,258,5,40,0,0,258,259,3,32,16,0,259,
        41,1,0,0,0,260,261,5,9,0,0,261,262,5,41,0,0,262,43,1,0,0,0,263,264,
        5,11,0,0,264,265,5,41,0,0,265,45,1,0,0,0,266,268,5,17,0,0,267,269,
        3,60,30,0,268,267,1,0,0,0,268,269,1,0,0,0,269,270,1,0,0,0,270,274,
        5,41,0,0,271,272,5,17,0,0,272,274,5,41,0,0,273,266,1,0,0,0,273,271,
        1,0,0,0,274,47,1,0,0,0,275,276,5,16,0,0,276,277,5,39,0,0,277,278,
        3,60,30,0,278,279,5,40,0,0,279,280,3,50,25,0,280,49,1,0,0,0,281,
        282,5,37,0,0,282,283,3,52,26,0,283,284,5,38,0,0,284,51,1,0,0,0,285,
        286,3,54,27,0,286,287,3,52,26,0,287,290,1,0,0,0,288,290,1,0,0,0,
        289,285,1,0,0,0,289,288,1,0,0,0,290,53,1,0,0,0,291,294,3,56,28,0,
        292,294,3,58,29,0,293,291,1,0,0,0,293,292,1,0,0,0,294,55,1,0,0,0,
        295,296,5,10,0,0,296,297,3,60,30,0,297,298,5,43,0,0,298,299,3,30,
        15,0,299,57,1,0,0,0,300,301,5,12,0,0,301,302,5,43,0,0,302,303,3,
        30,15,0,303,59,1,0,0,0,304,305,3,78,39,0,305,306,5,35,0,0,306,307,
        3,60,30,0,307,310,1,0,0,0,308,310,3,62,31,0,309,304,1,0,0,0,309,
        308,1,0,0,0,310,61,1,0,0,0,311,312,6,31,-1,0,312,313,3,64,32,0,313,
        319,1,0,0,0,314,315,10,2,0,0,315,316,5,30,0,0,316,318,3,64,32,0,
        317,314,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,
        320,63,1,0,0,0,321,319,1,0,0,0,322,323,6,32,-1,0,323,324,3,66,33,
        0,324,330,1,0,0,0,325,326,10,2,0,0,326,327,5,31,0,0,327,329,3,66,
        33,0,328,325,1,0,0,0,329,332,1,0,0,0,330,328,1,0,0,0,330,331,1,0,
        0,0,331,65,1,0,0,0,332,330,1,0,0,0,333,334,6,33,-1,0,334,335,3,68,
        34,0,335,341,1,0,0,0,336,337,10,2,0,0,337,338,7,1,0,0,338,340,3,
        68,34,0,339,336,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,341,342,
        1,0,0,0,342,67,1,0,0,0,343,341,1,0,0,0,344,345,6,34,-1,0,345,346,
        3,70,35,0,346,352,1,0,0,0,347,348,10,2,0,0,348,349,7,2,0,0,349,351,
        3,70,35,0,350,347,1,0,0,0,351,354,1,0,0,0,352,350,1,0,0,0,352,353,
        1,0,0,0,353,69,1,0,0,0,354,352,1,0,0,0,355,356,6,35,-1,0,356,357,
        3,72,36,0,357,363,1,0,0,0,358,359,10,2,0,0,359,360,7,3,0,0,360,362,
        3,72,36,0,361,358,1,0,0,0,362,365,1,0,0,0,363,361,1,0,0,0,363,364,
        1,0,0,0,364,71,1,0,0,0,365,363,1,0,0,0,366,367,6,36,-1,0,367,368,
        3,74,37,0,368,374,1,0,0,0,369,370,10,2,0,0,370,371,7,4,0,0,371,373,
        3,74,37,0,372,369,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,
        1,0,0,0,375,73,1,0,0,0,376,374,1,0,0,0,377,378,7,5,0,0,378,381,3,
        74,37,0,379,381,3,76,38,0,380,377,1,0,0,0,380,379,1,0,0,0,381,75,
        1,0,0,0,382,383,7,6,0,0,383,386,3,78,39,0,384,386,3,78,39,0,385,
        382,1,0,0,0,385,384,1,0,0,0,386,77,1,0,0,0,387,391,3,82,41,0,388,
        390,3,80,40,0,389,388,1,0,0,0,390,393,1,0,0,0,391,389,1,0,0,0,391,
        392,1,0,0,0,392,79,1,0,0,0,393,391,1,0,0,0,394,403,5,33,0,0,395,
        403,5,34,0,0,396,397,5,36,0,0,397,403,5,47,0,0,398,399,5,39,0,0,
        399,400,3,84,42,0,400,401,5,40,0,0,401,403,1,0,0,0,402,394,1,0,0,
        0,402,395,1,0,0,0,402,396,1,0,0,0,402,398,1,0,0,0,403,81,1,0,0,0,
        404,413,5,44,0,0,405,413,5,45,0,0,406,413,5,46,0,0,407,413,5,47,
        0,0,408,409,5,39,0,0,409,410,3,60,30,0,410,411,5,40,0,0,411,413,
        1,0,0,0,412,404,1,0,0,0,412,405,1,0,0,0,412,406,1,0,0,0,412,407,
        1,0,0,0,412,408,1,0,0,0,413,83,1,0,0,0,414,417,3,86,43,0,415,417,
        1,0,0,0,416,414,1,0,0,0,416,415,1,0,0,0,417,85,1,0,0,0,418,419,3,
        88,44,0,419,420,5,42,0,0,420,421,3,86,43,0,421,424,1,0,0,0,422,424,
        3,88,44,0,423,418,1,0,0,0,423,422,1,0,0,0,424,87,1,0,0,0,425,426,
        3,62,31,0,426,89,1,0,0,0,39,92,94,112,116,125,131,142,146,153,160,
        165,175,182,186,196,202,216,235,247,251,255,268,273,289,293,309,
        319,330,341,352,363,374,380,385,391,402,412,416,423
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
                      "LIT_INT", "LIT_FLOAT", "LIT_STRING", "ID", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_type = 1
    RULE_structdcl = 2
    RULE_member_list = 3
    RULE_member = 4
    RULE_vardecl = 5
    RULE_memberdcl_prime = 6
    RULE_memberdcl_list = 7
    RULE_memberdcl = 8
    RULE_funcdecl = 9
    RULE_parameter_prime = 10
    RULE_parameter_list = 11
    RULE_parameter = 12
    RULE_body = 13
    RULE_statement_prime = 14
    RULE_statement_list = 15
    RULE_statement = 16
    RULE_assignStmt = 17
    RULE_ifStmt = 18
    RULE_whileStmt = 19
    RULE_forStmt = 20
    RULE_breakStmt = 21
    RULE_continueStmt = 22
    RULE_returnStmt = 23
    RULE_switchStmt = 24
    RULE_switchBody = 25
    RULE_case_list = 26
    RULE_case = 27
    RULE_normal_case = 28
    RULE_default_case = 29
    RULE_assignment_expr = 30
    RULE_or_expr = 31
    RULE_and_expr = 32
    RULE_equality_expr = 33
    RULE_compare_expr = 34
    RULE_add_expr = 35
    RULE_mul_expr = 36
    RULE_unary_expr = 37
    RULE_prefix_expr = 38
    RULE_postfix_expr = 39
    RULE_postfix_op = 40
    RULE_primary_expr = 41
    RULE_argument_prime = 42
    RULE_argument_list = 43
    RULE_argument = 44

    ruleNames =  [ "program", "type", "structdcl", "member_list", "member", 
                   "vardecl", "memberdcl_prime", "memberdcl_list", "memberdcl", 
                   "funcdecl", "parameter_prime", "parameter_list", "parameter", 
                   "body", "statement_prime", "statement_list", "statement", 
                   "assignStmt", "ifStmt", "whileStmt", "forStmt", "breakStmt", 
                   "continueStmt", "returnStmt", "switchStmt", "switchBody", 
                   "case_list", "case", "normal_case", "default_case", "assignment_expr", 
                   "or_expr", "and_expr", "equality_expr", "compare_expr", 
                   "add_expr", "mul_expr", "unary_expr", "prefix_expr", 
                   "postfix_expr", "postfix_op", "primary_expr", "argument_prime", 
                   "argument_list", "argument" ]

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
    LIT_INT=44
    LIT_FLOAT=45
    LIT_STRING=46
    ID=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

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
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355824) != 0):
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 90
                    self.structdcl()
                    pass
                elif token in [4, 5, 6, 7, 47]:
                    self.state = 91
                    self.funcdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
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
            self.state = 101
            self.match(TyCParser.TYPE_STRUCT)
            self.state = 102
            self.match(TyCParser.ID)
            self.state = 103
            self.match(TyCParser.LBR)
            self.state = 104
            self.member_list()
            self.state = 105
            self.match(TyCParser.RBR)
            self.state = 106
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.member()
                self.state = 109
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.state = 114
                self.type_()
                pass
            elif token in [47]:
                self.state = 115
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 118
            self.match(TyCParser.ID)
            self.state = 119
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
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.type_()
                self.state = 122
                self.match(TyCParser.ID)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 123
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 124
                    self.or_expr(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(TyCParser.TYPE_AUTO)
                self.state = 128
                self.match(TyCParser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 129
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 130
                    self.or_expr(0)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(TyCParser.ID)
                self.state = 134
                self.match(TyCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(TyCParser.ID)
                self.state = 136
                self.match(TyCParser.ID)
                self.state = 137
                self.match(TyCParser.ASSIGNMENT)
                self.state = 138
                self.match(TyCParser.LBR)
                self.state = 139
                self.memberdcl_prime()
                self.state = 140
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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32, 33, 34, 37, 39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.memberdcl()
                self.state = 149
                self.match(TyCParser.COMMA)
                self.state = 150
                self.memberdcl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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


        def LBR(self):
            return self.getToken(TyCParser.LBR, 0)

        def memberdcl_prime(self):
            return self.getTypedRuleContext(TyCParser.Memberdcl_primeContext,0)


        def RBR(self):
            return self.getToken(TyCParser.RBR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_memberdcl




    def memberdcl(self):

        localctx = TyCParser.MemberdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_memberdcl)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32, 33, 34, 39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.or_expr(0)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(TyCParser.LBR)
                self.state = 157
                self.memberdcl_prime()
                self.state = 158
                self.match(TyCParser.RBR)
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
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 162
                self.type_()

            elif la_ == 2:
                self.state = 163
                self.match(TyCParser.TYPE_VOID)

            elif la_ == 3:
                self.state = 164
                self.match(TyCParser.ID)


            self.state = 167
            self.match(TyCParser.ID)
            self.state = 168
            self.match(TyCParser.LP)
            self.state = 169
            self.parameter_prime()
            self.state = 170
            self.match(TyCParser.RP)
            self.state = 171
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
        self.enterRule(localctx, 20, self.RULE_parameter_prime)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
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
        self.enterRule(localctx, 22, self.RULE_parameter_list)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.parameter()
                self.state = 178
                self.match(TyCParser.COMMA)
                self.state = 179
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.parameter()
                pass


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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_parameter




    def parameter(self):

        localctx = TyCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.state = 184
                self.type_()
                pass
            elif token in [47]:
                self.state = 185
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 188
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
        self.enterRule(localctx, 26, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(TyCParser.LBR)
            self.state = 191
            self.statement_prime()
            self.state = 192
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
        self.enterRule(localctx, 28, self.RULE_statement_prime)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_statement_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 9, 11, 14, 15, 16, 17, 18, 19, 20, 32, 33, 34, 37, 39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.statement()
                self.state = 199
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
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.vardecl()
                self.state = 205
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.body()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.switchStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.breakStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 214
                self.continueStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.assignment_expr()
            self.state = 219
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
        self.enterRule(localctx, 36, self.RULE_ifStmt)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(TyCParser.IF)
                self.state = 222
                self.match(TyCParser.LP)
                self.state = 223
                self.assignment_expr()
                self.state = 224
                self.match(TyCParser.RP)
                self.state = 225
                self.statement()
                self.state = 226
                self.match(TyCParser.ELSE)
                self.state = 227
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(TyCParser.IF)
                self.state = 230
                self.match(TyCParser.LP)
                self.state = 231
                self.assignment_expr()
                self.state = 232
                self.match(TyCParser.RP)
                self.state = 233
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
        self.enterRule(localctx, 38, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(TyCParser.WHILE)
            self.state = 238
            self.match(TyCParser.LP)
            self.state = 239
            self.assignment_expr()
            self.state = 240
            self.match(TyCParser.RP)
            self.state = 241
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
        self.enterRule(localctx, 40, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(TyCParser.FOR)
            self.state = 244
            self.match(TyCParser.LP)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 245
                self.vardecl()

            elif la_ == 2:
                self.state = 246
                self.assignment_expr()


            self.state = 249
            self.match(TyCParser.SEMI)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264462612824064) != 0):
                self.state = 250
                self.assignment_expr()


            self.state = 253
            self.match(TyCParser.SEMI)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264462612824064) != 0):
                self.state = 254
                self.assignment_expr()


            self.state = 257
            self.match(TyCParser.RP)
            self.state = 258
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
        self.enterRule(localctx, 42, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(TyCParser.BREAK)
            self.state = 261
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
        self.enterRule(localctx, 44, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(TyCParser.CONTINUE)
            self.state = 264
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
        self.enterRule(localctx, 46, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(TyCParser.RETURN)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264462612824064) != 0):
                    self.state = 267
                    self.assignment_expr()


                self.state = 270
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(TyCParser.RETURN)
                self.state = 272
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
        self.enterRule(localctx, 48, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(TyCParser.SWITCH)
            self.state = 276
            self.match(TyCParser.LP)
            self.state = 277
            self.assignment_expr()
            self.state = 278
            self.match(TyCParser.RP)
            self.state = 279
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
        self.enterRule(localctx, 50, self.RULE_switchBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(TyCParser.LBR)
            self.state = 282
            self.case_list()
            self.state = 283
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
        self.enterRule(localctx, 52, self.RULE_case_list)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.case()
                self.state = 286
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

        def normal_case(self):
            return self.getTypedRuleContext(TyCParser.Normal_caseContext,0)


        def default_case(self):
            return self.getTypedRuleContext(TyCParser.Default_caseContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_case




    def case(self):

        localctx = TyCParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 291
                self.normal_case()
                pass
            elif token in [12]:
                self.state = 292
                self.default_case()
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


    class Normal_caseContext(ParserRuleContext):
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

        def statement_list(self):
            return self.getTypedRuleContext(TyCParser.Statement_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_normal_case




    def normal_case(self):

        localctx = TyCParser.Normal_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_normal_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(TyCParser.CASE)
            self.state = 296
            self.assignment_expr()
            self.state = 297
            self.match(TyCParser.COLON)
            self.state = 298
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_caseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def statement_list(self):
            return self.getTypedRuleContext(TyCParser.Statement_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_default_case




    def default_case(self):

        localctx = TyCParser.Default_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_default_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(TyCParser.DEFAULT)
            self.state = 301
            self.match(TyCParser.COLON)
            self.state = 302
            self.statement_list()
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
        self.enterRule(localctx, 60, self.RULE_assignment_expr)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.postfix_expr()
                self.state = 305
                self.match(TyCParser.ASSIGNMENT)
                self.state = 306
                self.assignment_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    self.match(TyCParser.LOG_OR)
                    self.state = 316
                    self.and_expr(0) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.equality_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 330
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    self.match(TyCParser.LOG_AND)
                    self.state = 327
                    self.equality_expr(0) 
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_equality_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.compare_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Equality_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expr)
                    self.state = 336
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 338
                    self.compare_expr(0) 
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_compare_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Compare_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare_expr)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 349
                    self.add_expr(0) 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.mul_expr(0) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.unary_expr() 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4296540160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 378
                self.unary_expr()
                pass
            elif token in [33, 34, 39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
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
        self.enterRule(localctx, 76, self.RULE_prefix_expr)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 383
                self.postfix_expr()
                pass
            elif token in [39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
        self.enterRule(localctx, 78, self.RULE_postfix_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.primary_expr()
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 388
                    self.postfix_op() 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_postfix_op)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(TyCParser.INCREMENT)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(TyCParser.DECREMENT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 397
                self.match(TyCParser.ID)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 398
                self.match(TyCParser.LP)
                self.state = 399
                self.argument_prime()
                self.state = 400
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
        self.enterRule(localctx, 82, self.RULE_primary_expr)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(TyCParser.LIT_INT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(TyCParser.LIT_FLOAT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(TyCParser.LIT_STRING)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(TyCParser.ID)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.match(TyCParser.LP)
                self.state = 409
                self.assignment_expr()
                self.state = 410
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
        self.enterRule(localctx, 84, self.RULE_argument_prime)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32, 33, 34, 39, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
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
        self.enterRule(localctx, 86, self.RULE_argument_list)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.argument()
                self.state = 419
                self.match(TyCParser.COMMA)
                self.state = 420
                self.argument_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
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
        self.enterRule(localctx, 88, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.or_expr(0)
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
        self._predicates[31] = self.or_expr_sempred
        self._predicates[32] = self.and_expr_sempred
        self._predicates[33] = self.equality_expr_sempred
        self._predicates[34] = self.compare_expr_sempred
        self._predicates[35] = self.add_expr_sempred
        self._predicates[36] = self.mul_expr_sempred
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
         




