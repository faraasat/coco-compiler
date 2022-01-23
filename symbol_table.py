import os

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
        self.__clear_file()
        self.__gen_tk()
        self.__gen_symbol_table()
        self.__write_table()

    def __remove_comments(self, i):
        i = i.split('*@*')[0]
        if '/@' in i and '@/' in i:
            i = i.split('/@')[0]
        if '/@' in i:
            self.is_m_comment = True
            return ''
        elif '@/' in i:
            self.is_m_comment = False
            return ''
        elif self.is_m_comment:
            return ''
        return i

    def __clear_file(self):
        f = open(self.filename)
        f = f.readlines()
        for i in f:
            h = (self.__remove_comments(i)).strip()
            if h:
                self.sbt.append(h.rstrip('\n').split(' '))

    def __gen_tk(self):
        for i in self.sbt:
            if '{' in i:
                self.scope += 1
            elif '}' in i:
                self.scope -= 1
            else:
                i.insert(0, f"{self.scope - 1}")
                self.tokens.append(i)

    def __gen_symbol_table(self):
        for i in self.tokens:
            if i[1] in ["num", "str", "bool"]:
                i[2] = i[2].split("[")[0]
                if len(self.table) == 0:
                    self.__insert(i[2], i[1], i[0])
                else:
                    fl = self.__lookup(i[2], i[0])
                    if not fl:
                        raise Exception("Variable Already Defined in the Same Scope")
                    else:
                        self.__insert(i[2], i[1], i[0])
    
    def __lookup(self, n, s):
        for i in self.table:
            if n in i and s in i:
                return False
        return True

    def __insert(self, n, d, s):
        self.table.append([n, d, s])

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

# For Testing Purpose
if __name__ == "__main__":
    SymbolTable("test.txt", os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819"))