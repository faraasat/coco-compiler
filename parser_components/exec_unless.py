import re

class Exec:
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def S(self):
        is_br = False
        if not self.tk[0] == "exec":
            if not self.tk[0][::-1][0] == "{":
                self.raise_error("\"{\" Expected. Invalid Token Found")
            elif self.tk[0][::-1][0] == "{":
                is_br = True
                if not self.tk[0].split("{")[0] == "exec":
                    self.raise_error("\"exec\" Expected. Invalid Token Found")
        elif self.tk[0] == "exec":
            pass
        else:
            self.raise_error("Invalid Token Found")
        if not is_br:
            try:
                if not self.tk[1] == "{":
                    self.raise_error("\"{\" Expected. Invalid Token Found")
            except:
                self.raise_error("\"{\" Expected. Invalid Token Found")
        self.prsed = True

    def get_val(self):
        return self.prsed

class ExecUnless:
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def U(self, sp_tk):
        if not sp_tk[0].split("(")[0] == "unless": self.raise_error("\"unless\" Expected. Invalid Token Found")
        if "True" in sp_tk[0].split("(")[1]:
                if not sp_tk[0][::-1][0] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
        elif "False" in sp_tk[0].split("(")[1]:
                if not sp_tk[0][::-1][0] == ")":
                    self.raise_error("\")\" Expected. Invalid Token Found")
        elif (bool(re.match("[A-Za-z_]+[A-Za-z_0-9]*$", sp_tk[0].split("(")[1])) or bool(re.match("[0-9]+$", sp_tk[0].split("(")[1]))):
            if not (sp_tk[1] == "<" or sp_tk[1] == ">" or sp_tk[1] == "==" or sp_tk[1] == ">=" or sp_tk[1] == "<=" or sp_tk[1] == "!=" or sp_tk[1] == "<>"):
                self.raise_error("Comparison Operator Expected. Invalid Token Found")
            if not (bool(re.match("[A-Za-z_]+[A-Za-z_0-9]*$", sp_tk[2].split(")")[0])) or bool(re.match("[0-9]+$", sp_tk[2].split(")")[0]))):
                self.raise_error("Invalid Value or Identifier Found")
            if not sp_tk[2][::-1][0] == ")":
                self.raise_error("\")\" Expected. Invalid Token Found")
        else:
            self.raise_error("Invalid Token Found after ( <--")

    def S(self):
        is_br = False
        if self.tk[0] == "}":
            self.tk.pop(0)
            self.U(self.tk)
        elif self.tk[0][0] == "}":
            self.tk[0] = self.tk[0].split("}")[1]
            self.U(self.tk)
        else:
            self.raise_error("\"}\" Expected. Invalid Token Found")
        self.prsed = True

    def get_val(self):
        return self.prsed