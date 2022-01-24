import re

class Unless:
    def __init__(self, tk):
        self.tk = tk
        self.prsed = False
        self.S()

    def raise_error(self, msg):
        raise Exception(msg)

    def S(self):
        print("Here")
        self.tk.append("$")
        is_br = False
        if not self.tk[0] == "iterate": self.raise_error("\"iterate\" Expected. Invalid Token Found")
        if not bool(re.match("[a-zA-Z_]+[a-zA-Z_0-9]*$", self.tk[1])): self.raise_error(f"Got {tk[1]}. Invalid Identifier Found")
        if not self.tk[2] == "in": self.raise_error("\"in\" Expected. Invalid Token Found")
        if not ("range" in self.tk[3]):
            if not bool(re.match("[a-zA-Z_]+[a-zA-Z_0-9]*$", self.tk[3])):
                if not self.tk[3][len(self.tk[3]) - 1] == "{": self.raise_error(f"Got {tk[3]}. Invalid Identifier Found")
                else: is_br = True
                if not re.match("[a-zA-Z_]+[a-zA-Z_0-9]*$", self.tk[3][0: len(self.tk[3]) - 1]): self.raise_error(f"Got {tk[3]}. Invalid Identifier Found")
        elif "range" in self.tk[3]:
            if self.tk[3][len(self.tk[3]) - 1] == "{": is_br = True
            if not (self.tk[3][0: len(self.tk[3]) - 1]).split("(")[0] == "range": self.raise_error("\"range\" Expected. Invalid Token Found")
            if not bool(re.match("[0-9]+$",((self.tk[3][0: len(self.tk[3]) - 1]).split("(")[1]).split(")")[0])):  self.raise_error("Integer Expected. Invalid Token Found")
        if not is_br:
            try:
                if not self.tk[4] == "{":
                    self.raise_error("\"{\" Expected. Invalid Token Found")
            except:
                self.raise_error("\"{\" Expected. Invalid Token Found")
        self.prsed = True

    def get_val(self):
        return self.prsed