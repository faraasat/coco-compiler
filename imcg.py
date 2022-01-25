import os
import re

import util as ut

class IntermediateCode:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        self.py_imc = []
        self.is_m_comment = False
        self.scope = 0
        self.__tokenize_text()
        self.__write_imc()

    def check_arr(self, i):
        is_arr = False
        is_in = False
        trimmed_val = []
        for j in i:
            if "{" in j and is_in == False:
                is_in = True
                trimmed_val.append((j.split("{")[1]).split(",")[0])
            elif "}" in j and is_in == True:
                is_in = False
                trimmed_val.append(j.split("}")[0])
            elif is_in == True:
                trimmed_val.append(j.split(",")[0])
        return trimmed_val
    
    def __tokenize_text(self):
        for i in ut.clear_file(self.filename, self.is_m_comment):
            if "}" in i[0]:
                self.scope -= 1
            elif (i[0] == "bool" or i[0] == "num" or i[0] == "str") and not ('[' in i[1] or ']' in i[1]):
                i.pop(0)
                i.insert(0, "\t"*self.scope)
                self.py_imc.append(i)
            elif (i[0] == "bool" or i[0] == "num" or i[0] == "str") and ('[' in i[1] or ']' in i[1]):
                n_arr = []
                i.pop(0)
                n_arr.append("\t"*self.scope)
                n_arr.append(i[0].split("[")[0])
                n_arr.append(i[1])
                n_arr.append("[")
                arr_val = self.check_arr(i)
                for index, i in enumerate(arr_val):
                    if not index == len(arr_val) - 1:
                        n_arr.append(f"{i}, ")
                    else:
                        n_arr.append(i)
                n_arr.append("]")
                self.py_imc.append(n_arr)
            elif "iterate" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                iter_val.append("for")
                iter_val.append(i[1])
                iter_val.append(i[2])
                iter_val.append(f"{i[3]}:")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "exec" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                iter_val.append("while(True):")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "}" in i[0]:
                try:
                    if "unless" in i[1]:
                        iter_val = []
                        iter_val.append("\t"*self.scope)
                        iter_val.append("if")
                        if len(i) > 1:
                            iter_val.append(i[0].split("(")[1])
                            iter_val.append(i[1])
                            iter_val.append(i[2].split(")")[0] + ":")
                            iter_val.append(" break")
                        self.scope -= 1
                        self.py_imc.append(iter_val)
                except:
                    pass
            elif "unless" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                if len(i) > 1:
                    iter_val.append("while(" + i[0].split("(")[1])
                    iter_val.append(i[1])
                    iter_val.append(i[2].split(")")[0] + "):")
                else:
                    bool_f = False
                    if "true" in i[0]:
                        bool_f = True
                    iter_val.append(f"while({bool_f}):")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "func" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                iter_val.append("def")
                iter_val.append(i[1].split("{")[0] + ":")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "if" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                if len(i) > 1:
                    iter_val.append("if(" + i[0].split("(")[1])
                    iter_val.append(i[1])
                    iter_val.append(i[2].split(")")[0] + "):")
                else:
                    bool_f = False
                    if "true" in i[0]:
                        bool_f = True
                        iter_val.append(f"if({bool_f}):")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "else" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                try:
                    if i[1] == "if":    
                        if len(i) > 1:
                            iter_val.append("elif(" + i[0].split("(")[1])
                            iter_val.append(i[1])
                            iter_val.append(i[2].split(")")[0] + "):")
                        else:
                            bool_f = False
                            if "true" in i[0]:
                                bool_f = True
                                iter_val.append(f"elif({bool_f}):")
                except:
                    iter_val.append("else:")
                self.scope += 1
                self.py_imc.append(iter_val)
            elif "display" in i[0]:
                iter_val = []
                iter_val.append("\t"*self.scope)
                iter_val.append(f"print({i[1]})")
                self.py_imc.append(iter_val)

    def __write_imc(self):
        open(os.path.join(self.log_path, "imc.txt"), "w+").close()
        fw = open(os.path.join(self.log_path, "imc.txt"), "a")
        for i in self.py_imc:
            for j in i:
                if j:
                    fw.write(str(str(j) + ' '))
            fw.write("\n")
    
    def get_imc_path(self):
        return os.path.join(self.log_path, "imc.txt")

# For Testing Purpose
if __name__ == "__main__":
    IntermediateCode("test.txt", os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819"))