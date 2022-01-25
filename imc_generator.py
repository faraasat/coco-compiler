class Parse:
    def __init__(self, tk, st):
        self.tokens = tk
        self.symbol_table = st
        self.scope = 0
        self.vars = []
        self.prse()

    def raise_error(self, msg):
        raise Exception(msg)

    def add_symbols(self):
        for i in self.symbol_table:
            if int(i[0]) == self.scope:
                self.vars.append(i)

    def remove_symbols(self):
        temp_var = []
        for i in self.vars:
            if int(i[0]) <= self.scope:
                temp_var = i
        self.vars = temp_var
    
    def search_vars(self, tk):
        for i in self.vars:
            if tk in i[2]:
                if not ('[' in i[2] and ']' in i[2]): self.raise_error(f"Variable {tk} is not iterateable.")
                return {"values": i[4:], "is_arr": True}
        return None

    def prse(self):
        self.add_symbols()
        
        for token in self.tokens:
            fl = {}
            if "iterate" == token[0]:
                self.scope += 1
                if not token[2] == "in": self.raise_error("\"in\" Expected. Invalid Token Found")
                if "range" == token[3]:
                    pass
                elif not "range" == token[3]:
                    fl = self.search_vars(token[3].split("{")[0])
                    print(fl)
                    if not fl: self.raise_error(f"Variable {token[3]} not Found Scope")
                else: self.raise_error("\"range\" or iterable value Expected. Invalid Token Found")
                if not ("{" in token[3] or "{" == token[4]): self.raise_error("\"{\" Expected. Invalid Token Found")
                self.scope += 1
                self.add_symbols()
                
                self.scope -= 1
                self.remove_symbols()