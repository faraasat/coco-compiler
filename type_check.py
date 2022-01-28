import os

import util as ut

class TypeCheck:
    def __init__(self, fn):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.sbt = []
        self.is_m_comment = False
        self.__check_type()

    def __error(self, msg):
        raise Exception(f"Datatype Error in \"{msg[0]} {msg[1]}\", Value and Datatype do not match!")

    def __check_arr(self, i):
        is_arr = False
        is_in = False
        trimmed_val = ""
        if i[0] == "bool":
            for j in i:
                if "{" in j and is_in == False:
                    is_in = True
                    trimmed_val = (j.split("{")[1]).split(",")[0]
                    if not (trimmed_val == "true" or trimmed_val == "false"):
                        self.__error(i)
                elif "}" in j and is_in == True:
                    is_in = False
                    trimmed_val = j.split("}")[0]
                    if not (trimmed_val == "true" or trimmed_val == "false"):
                        self.__error(i)
                elif is_in == True:
                    trimmed_val = j.split(",")[0]
                    if not (trimmed_val == "true" or trimmed_val == "false"):
                        self.__error(i)
        elif i[0] == "num":
            for j in i:
                if "{" in j and is_in == False:
                    is_in = True
                    trimmed_val = (j.split("{")[1]).split(",")[0]
                    try:
                        int(trimmed_val)
                    except (TypeError, ValueError):
                        self.__error(i)
                elif "}" in j and is_in == True:
                    is_in = False
                    trimmed_val = j.split("}")[0]
                    try:
                        int(trimmed_val)
                    except (TypeError, ValueError):
                        self.__error(i)
                elif is_in == True:
                    trimmed_val = j.split(",")[0]
                    try:
                        int(trimmed_val)
                    except (TypeError, ValueError):
                        self.__error(i)


    def __check_non_arr(self, i):
        if i[0] == "num":
            try:
                int(i[3])
            except (TypeError, ValueError):
                self.__error(i)
        elif i[0] == "bool":
            if not (i[3] == "true" or i[3] == "false"):
                self.__error(i)
        elif i[0] == "str":
            if not ((i[3][0]) in "\'" or (i[3][0]) in '\"'):
                self.__error(i)
            if not ((i[3][-1]) in "\'" or (i[3][-1]) in '\"'):
                self.__error(i)

    def __check_type(self):
        self.sbt = ut.clear_file(self.filename, self.is_m_comment)
        count = 0
        try:
            for i in self.sbt:
                count += 1
                if i[0] in ["num", "str", "bool"]:
                    if "[" in i[1]:
                        self.__check_arr(i)
                    else:
                        self.__check_non_arr(i)
        except IndexError:
            raise Exception(f"Variable not Initialized Correctly at \"{self.sbt[count - 1][0]} {self.sbt[count - 1][1]}\"")

# For Testing Purpose
if __name__ == "__main__":
    if ut.get_config()["env"] == "testing":
        TypeCheck("test.txt")