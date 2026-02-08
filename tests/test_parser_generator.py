import pandas as pd

INPUT_EXCEL = "testcase_parser.xlsx"
OUTPUT_PY = "test_parser.py"
NUM_TESTS = 100   # muốn bao nhiêu test thì chỉnh ở đây

df = pd.read_excel(INPUT_EXCEL)

with open(OUTPUT_PY, "w", encoding="utf-8") as f:
    # Header
    f.write('"""\nParser test cases for TyC compiler\nImplement 100 test cases for parser\n"""\n')
    f.write("import pytest\n")
    f.write("from tests.utils import Parser\n\n\n")
    f.write("# ========== Simple Test Cases (10 types) ==========")
    f.write("# removed\n\n");
    f.write("# testcases submission:\n")
    for i, row in df.head(NUM_TESTS).iterrows():
        name = row["name"]
        structDcl = row["structDcl"]
        programBody = row["programBody"]
        expected = row["expected"]

        # Handle NaN / empty cell
        structDcl = "" if pd.isna(structDcl) else structDcl
        programBody = "" if pd.isna(programBody) else programBody
        expected = "" if pd.isna(expected) else expected

        f.write(f"def test_{name}():\n")
        f.write(f'    """Testcase {i + 1}: {name}"""\n')
        f.write('    source = """\n')
        f.write(f"{structDcl}\n\n")
        f.write(f"{programBody}\n")
        f.write('    """\n')
        f.write(f'    expected = "{expected}"\n')
        f.write("    assert Parser(source).parse() == expected\n\n")
