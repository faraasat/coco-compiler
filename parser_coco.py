from parser_components import iterate
from parser_components import unless

class Parse:
    def __init__(self, tk):
        self.tokens = tk
        self.scope = 0
        self.prse()

    def raise_error(self, msg):
        raise Exception(msg)

    def prse(self):
        for token in self.tokens:
            if "}" in token:
                self.scope -= 1
            elif token[0] == "iterate":
                if not iterate.Iterate(token).get_val():
                    self.raise_error("Error While Parsing!")
                else:
                    self.scope += 1
            elif token[0] == "unless":
                if not unless.Unless(token).get_val():
                    self.raise_error("Error While Parsing!")
                else:
                    self.scope += 1
            