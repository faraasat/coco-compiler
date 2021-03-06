import os
import re

import util as ut

class Generate_Tokens:
    def __init__(self, tk):
        self._pre_tokens = tk
        self._keywords = ['unless', 'iterate', 'exec', 'display', 'if', 'else', 'struct', 'declare', 'return', 'func', 'read', 'write', 'in']
        self._is_op = '[\)\(\{\}\[\],\.\;\:\"\+\-\*\/%<>=]+'
        self._m_op = '[\+\-\*\/%]'
        self._l_op = ['and', 'or', 'not']
        self._punc = '[\)\(\{\}\[\],\.\;\:]'
        self._dtypes = ['num', 'str', 'bool']
        self._lexemes = []
    
    def __check_op(self, ntk):
        alpha = ''
        lt = ''
        is_lt = False
        dbl = ''
        for i in range(len(ntk)):
            if ntk[i] in ["\'", '\"'] and not is_lt:
                is_lt = True
                lt += ntk[i]
            elif ntk[i] in ["\'", '\"'] and is_lt:
                is_lt = False
                lt += ntk[i]
                self._lexemes.append(['Literal', lt])
                lt = ''
            elif is_lt:
                lt += ntk[i]
            if re.search('[A-Za-z0-9_]', ntk[i]):
                alpha += ntk[i]
            else:
                if(len(alpha) > 0):
                    self.__check_norm(alpha)
                    alpha = ''
                if ntk[i] in self._m_op:
                    if ntk[i] in ['+', '-']:
                        try:
                            if ntk[i + 1] in ['+', '-', '=']:
                                self._lexemes.append(['Increment Decrement', f"{ntk[i]}{ntk[i + 1]}"])
                                i += 1
                        except:
                            self._lexemes.append(['Mathematical Operator', ntk[i]])
                    else:
                        self._lexemes.append(['Mathematical Operator', ntk[i]])
                elif ntk[i] in ['>', '<', '=']:
                    if ntk[i] in ['>', '<', '=']:
                        try:
                            if ntk[i + 1] in ['>', '=']:
                                self._lexemes.append(['Relational Operator', f"{ntk[i]}{ntk[i + 1]}"])
                                i += 1
                        except:
                            if ntk[i] == '=':
                                self._lexemes.append(['Assignment Operator', ntk[i]])
                            else:
                                self._lexemes.append(['Relational Operator', ntk[i]])
                    else:
                        if ntk[i] == '=':
                            self._lexemes.append(['Assignment Operator', ntk[i]])
                        else:
                            self._lexemes.append(['Relational Operator', ntk[i]])
                elif bool(re.search(self._punc, ntk[i])):
                    self._lexemes.append(['Punctuation', ntk[i]])
    
    def __check_norm(self, ntk):
        if ntk in self._keywords:
            self._lexemes.append(['Keyword', ntk])
        elif ntk in self._l_op:
            self._lexemes.append(['Logical Operator', ntk])
        elif ntk in self._dtypes:
            self._lexemes.append(['Data Type', ntk])
        elif ntk in ['true', 'false']:
            self._lexemes.append(['Literal', ntk])
        elif (re.findall('[A-Za-z_]+$', ntk)):
            self._lexemes.append(['Identifier', ntk])
        elif (re.findall('[0-9]+$', ntk)):
            self._lexemes.append(['Literal', ntk])

    def iter_pre_token(self):
        for i in self._pre_tokens:
            for next_token in i:
                if(re.search(self._is_op, next_token)):
                    self.__check_op(next_token)
                else:
                    self.__check_norm(next_token)
        return self._lexemes

    def get_pre_tokens(self):
        return self._pre_tokens

class Tokenize:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        self.pre_tokens = []
        self.tokens = []
        ut.check_verbosity(f"{ut.bcolors.BOLD}---  Tokenizer  ---{ut.bcolors.ENDC}")
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Starting Token Generation...{ut.bcolors.ENDC}")
        self.__tokenize_text()
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Tokens Generated Successfully...{ut.bcolors.ENDC}")
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Writing Tokens...{ut.bcolors.ENDC}")
        self.__write_tokens()
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Tokens Written Successfully At:{ut.bcolors.ENDC}")
        ut.check_verbosity(f"{ut.bcolors.CYELLOW}\t   -   {os.path.join(self.log_path, 'test.txt')}{ut.bcolors.ENDC}")
        ut.check_verbosity()
    
    def __tokenize_text(self):
        gt = Generate_Tokens(ut.clear_file(self.filename))
        self.pre_tokens = gt.get_pre_tokens()
        lex = gt.iter_pre_token()
        self.tokens = lex

    def __write_tokens(self):
        open(os.path.join(self.log_path, "token.txt"), "w+").close()
        fw = open(os.path.join(self.log_path, "token.txt"), "a")
        for i in self.tokens:
            fw.write(str(str(i) + ' '))

    def get_tk(self):
        return self.pre_tokens

# For Testing Purpose
if __name__ == "__main__":
    if ut.get_config()["env"] == "testing":
        Tokenize("test.txt", ut.get_test_log_path())