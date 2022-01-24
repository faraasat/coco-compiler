import re

class Func:
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def S(self):
        is_br = False
        # print(self.tk)
        if not self.tk[0].split("(")[0] == "func": self.raise_error("\"func\" Expected. Invalid Token Found")
        if self.tk[1][::-1][0] == "{":
            is_br = True
            if not (self.tk[1].split("{")[0])[::-1][1] == "(": self.raise_error("\")\" Expected. Invalid Token Found")
            if not (self.tk[1].split("{")[0])[::-1][0] == ")": self.raise_error("\")\" Expected. Invalid Token Found")
            if not bool(re.match("[a-zA-z_]+[a-zA-Z_0-9]*$",self.tk[1].split("(")[0])): self.raise_error("Illegal Character in function name")
        elif not self.tk[1][::-1][0] == "{":
            if not (self.tk[1].split("{")[0])[::-1][1] == "(": self.raise_error("\")\" Expected. Invalid Token Found")
            if not (self.tk[1].split("{")[0])[::-1][0] == ")": self.raise_error("\")\" Expected. Invalid Token Found")
            if not bool(re.match("[a-zA-z_]+[a-zA-Z_0-9]*$",self.tk[1].split("(")[0])): self.raise_error("Illegal Character in function name")
        if not is_br:
            if not self.tk[::-1][0] == "{":
                self.raise_error("\"{\" Expected. Invalid Token Found")
        self.prsed = True

    def get_val(self):
        return self.prsed