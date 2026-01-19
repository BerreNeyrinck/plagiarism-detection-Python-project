
from pathlib import Path
import ast

p = Path(input())

parse = ast.parse(p.read_text())
AParse = ast.unparse(parse)
print(AParse)