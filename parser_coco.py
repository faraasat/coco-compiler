from parser_components import iterate
from parser_components import unless
from parser_components import exec_unless
from parser_components import if_else

class Parse:
    def __init__(self, tk):
        self.tokens = tk
        self.scope = 0
        self.unless = 0
        self.prse()

    def raise_error(self):
        raise Exception("Error While Parsing")

    def prse(self):
        for token in self.tokens:
            print(self.scope)
            if "}" in token and not "unless" in token:
                self.scope -= 1
            if "}" in token and "unless" in token:
                if not exec_unless.ExecUnless(token).get_val():
                    self.raise_error()
                else:
                    self.scope -= 1
                    self.unless -= 1
            elif token[0] == "iterate":
                if not iterate.Iterate(token).get_val():
                    self.raise_error()
                else:
                    self.scope += 1
            elif token[0] == "unless":
                if not unless.Unless(token).get_val():
                    self.raise_error()
                else:
                    self.scope += 1
            elif token[0] == "exec":
                if not exec_unless.Exec(token).get_val():
                    self.raise_error()
                else:
                    self.scope += 1
                    self.unless += 1
            elif token[0] == "if":
                if not if_else.If(token).get_val():
                    self.raise_error()
                else:
                    self.scope += 1
                    self.unless += 1
            elif token[0] == "else":
                if not if_else.Else(token).get_val():
                    self.raise_error()
                else:
                    self.scope += 1
                    self.unless += 1
        # if self.scope > 0 or self.unless > 0:
        #     raise Exception("Missing token(s) \"}\"") 