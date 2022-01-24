import re

class Else:
    pass
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def S(self):
        is_br = False
        if not "else" in self.tk[0]:
            self.raise_error("\"else\" Expected. Invalid Token Found")
        else:
            if "else" in self.tk[0]:
                if self.tk[0][::-1][0] == "{":
                    if self.tk[0].split("{")[0] == "else":
                        pass
                elif self.tk[1] == "{":
                    pass
                else:
                    self.tk.pop(0)
                    If(self.tk)
        self.prsed = True

    def get_val(self):
        return self.prsed

class If:
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def S(self):
        is_br = False
        if not self.tk[0].split("(")[0] == "if": self.raise_error("\"if\" Expected. Invalid Token Found")
        if "True" in self.tk[0].split("(")[1]:
            if not self.tk[0][::-1][0] == "{":
                if not self.tk[0][::-1][0] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
            elif self.tk[0][::-1][0] == "{": 
                is_br = True
                if not self.tk[0][::-1][1] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
        elif "False" in self.tk[0].split("(")[1]:
            if not self.tk[0][::-1][0] == "{":
                if not self.tk[0][::-1][0] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
            elif self.tk[0][::-1][0] == "{": 
                is_br = True
                if not self.tk[0][::-1][1] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
        elif (bool(re.match("[A-Za-z_]+[A-Za-z_0-9]*$", self.tk[0].split("(")[1])) or bool(re.match("[0-9]+$", self.tk[0].split("(")[1]))):
            if not (self.tk[1] == "<" or self.tk[1] == ">" or self.tk[1] == "==" or self.tk[1] == ">=" or self.tk[1] == "<=" or self.tk[1] == "!=" or self.tk[1] == "<>"):
                self.raise_error("Comparison Operator Expected. Invalid Token Found")
            if not (bool(re.match("[A-Za-z_]+[A-Za-z_0-9]*$", self.tk[2].split(")")[0])) or bool(re.match("[0-9]+$", self.tk[2].split(")")[0]))):
                self.raise_error("Invalid Value or Identifier Found")
            if self.tk[2].split(")")[1] == "{":
                is_br = True
        else:
            self.raise_error("Invalid Token Found after ( <--")
        if not is_br:
            try:
                if not self.tk[::-1][0] == "{":
                    self.raise_error("\"{\" Expected. Invalid Token Found")
            except:
                self.raise_error("\"{\" Expected. Invalid Token Found")
        self.prsed = True