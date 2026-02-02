import pandas as pd

INPUT_EXCEL = "testcase_lexer.xlsx"
OUTPUT_PY = "test_lexer_generated.py"
NUM_TESTS = 90

df = pd.read_excel(INPUT_EXCEL)

with open(OUTPUT_PY, "w", encoding="utf-8") as f:
    # Header
    f.write("import pytest\n")
    f.write("from tests.utils import Tokenizer\n\n\n")

    for i, row in df.head(NUM_TESTS).iterrows():
        name = row["Testcase"]
        program = row["Program"]
        expected = row["Expected"]

        # Escape for Python string literal
        # program = program.replace("\\", "\\\\").replace('"', '\\"')
        # expected = expected.replace("\\", "\\\\").replace('"', '\\"')

        f.write(f"def test_{name}():\n")
        f.write(f'    """ Testcase: {i + 1} """\n')
        f.write(f'    source = "{program}"\n')
        f.write(f'    expected = "{expected}"\n')
        f.write(f"    tokenizer = Tokenizer(source)\n")
        f.write(f"    assert tokenizer.get_tokens_as_string() == expected\n\n")