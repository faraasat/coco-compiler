import os

import util as ut

class SymbolTable:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        self.is_m_comment = False
        self.sbt = []
        self.tokens = []
        self.scope = 0
        self.table = []
        self.__set_scope()
        self.__gen_symbol_table()
        self.__write_table()

    def __set_scope(self):
        self.sbt = ut.clear_file(self.filename, self.is_m_comment)
        for i in self.sbt:
            if '{' in i:
                self.scope += 1
            elif '}' in i:
                self.scope -= 1
            else:
                i.insert(0, f"{self.scope}")
                self.tokens.append(i)

    def __gen_symbol_table(self):
        for i in self.tokens:
            if i[1] in ["num", "str", "bool"]:
                if len(self.table) == 0:
                    self.__insert(i[2], i[1], i[0], i[4])
                else:
                    fl = self.__lookup(i[2], i[0])
                    if not fl:
                        raise Exception("Variable Already Defined in the Same Scope")
                    else:
                        self.__insert(i[2], i[1], i[0], i[4])
    
    def __lookup(self, n, s):
        for i in self.table:
            if n in i and s in i:
                return False
        return True

    def __insert(self, n, d, s, v):
        self.table.append([n, d, s, v])

    def __write_table(self):
        open(os.path.join(self.log_path, "symbol_table.txt"), "w+").close()
        fw = open(os.path.join(self.log_path, "symbol_table.txt"), "a")
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("\n")
        fw.write("|")
        fw.write(f"{'Name':>10}")
        fw.write(f"{'|':>10}")
        fw.write(f"{'Datatype':>10}")
        fw.write(f"{'|':>10}")
        fw.write(f"{'Scope':>10}")
        fw.write(f"{'|':>10}")
        fw.write("\n")
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("-"*19)
        fw.write("+")
        fw.write("\n")
        for i in self.table:
            fw.write("|")
            fw.write(f"{i[0]:>10}")
            fw.write(f"{'|':>10}")
            fw.write(f"{i[1]:>10}")
            fw.write(f"{'|':>10}")
            fw.write(f"{i[2]:>10}")
            fw.write(f"{'|':>10}")
            fw.write("\n")
            fw.write("+")
            fw.write("-"*19)
            fw.write("+")
            fw.write("-"*19)
            fw.write("+")
            fw.write("-"*19)
            fw.write("+")
            fw.write("\n")

    def get_st(self):
        valid_tk = []
        for i in self.tokens:
            if ("num" in i or "bool" in i or "str" in i):
                valid_tk.append(i)
        return valid_tk

# For Testing Purpose
if __name__ == "__main__":
    if ut.get_config()["env"] == "testing":
        SymbolTable("test.txt", ut.get_test_log_path())