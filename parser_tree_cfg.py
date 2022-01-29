import nltk

cfg = """
S -> func id "(" ")" "{" S "}" | R
R -> IF | ELIF | EL | IT | UN | EXUN | DISP | RE | WR | VAR | VARA | R R | ASO |
IF -> "if" "(" ID COMP ID ")" "{" R "}"
ELIF -> "else" "if" "(" ID COMP ID ")" "{" R "}"
EL -> "else" "{" R "}"
IT -> "iterate" ID "in" IOR "{" R "}"
UN -> "unless" "(" ID COMP ID ")" "{" R "}"
EXUN -> "exec" "{" R "}" "unless" "(" ID COMP ID ")"
DISP -> "display" ID
RE -> ID "=" "read" "("  ")"
WR -> "write" "("  ")"
VAR -> "str" ID "=" '"' ID '"' | "num" ID "=" NUM | "bool" ID "=" BO
VARA -> "str" ID "[" "]" "=" "{" ISC "}" | "num" ID "[" "]" "=" "{" IRC "}" | "bool" ID "=" "{" IBC "}"
ISC -> ID COM
INC -> NUM COM
IBC -> BO COM
COM -> "," | 
IOR -> ID | "range" "(" NUM ")"
ID ->  ID ID | NUM | SAL | CAL | BO | SYM |
NUM -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0"
SAL -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
CAL -> "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
BO -> "true" | "false"
SYM -> "_"
ASO -> ID AS | ID ASE ID
AS -> "++" "--"
ASE -> "+=" "-="
COMP -> "<" | ">" | "<=" | ">=" | "==" | "!=" | "<>"   
"""


def parse_missing(token):
    global cfg
    missing = [tok for tok in token if not nltk.CFG.fromstring(cfg)._lexical_index.get(tok)]
    for i in missing:
        i = i.replace('"', "'")
        i = i.replace('"', "'")
        loc = cfg.find("ID ->") + 6
        cfg = cfg[:705] + f"\"{i}\" | " + cfg[705:]
    return nltk.CFG.fromstring(cfg)

def ret_grammar():
    return nltk.CFG.fromstring(cfg)