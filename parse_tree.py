import nltk
from nltk.draw.tree import TreeView
from PIL import Image
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.55.0\bin\gswin64c.exe'
import os
import re
import subprocess

import util as ut
import parser_tree_cfg as ptc

class GeneratePTTokens:
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
        pass_count = 0
        for i in range(len(ntk)):
            if pass_count > 0:
                pass_count -= 1
            elif (ntk[i] in ["\'", '\"'] or bool(re.match('[_a-zA-Z]+[_a-zA-Z0-9]*$', ntk[i]))) and not is_lt:
                is_lt = True
                lt += ntk[i]
            elif (ntk[i] in ["\'", '\"'] or bool(re.match('[_a-zA-Z]+[_a-zA-Z0-9]*$', ntk[i]))) and is_lt:
                is_lt = False
                lt += ntk[i]
                self._lexemes.append(lt)
                lt = ''
            elif is_lt:
                lt += ntk[i]
            elif re.search('[0-9]+$', ntk[i]):
                alpha += ntk[i]
            else:
                if(len(alpha) > 0):
                    self._lexemes.append(alpha)
                    alpha = ''
                if ntk[i] in self._m_op:
                    if ntk[i] in ['+', '-']:
                        try:
                            if ntk[i + 1] in ['+', '-', '=']:
                                self._lexemes.append(f"{ntk[i]}{ntk[i + 1]}")
                                pass_count += 1
                        except:
                            self._lexemes.append(ntk[i])
                    else:
                        self._lexemes.append(ntk[i])
                elif ntk[i] in ['>', '<', '=']:
                    if ntk[i] in ['>', '<', '=']:
                        try:
                            if ntk[i + 1] in ['>', '=']:
                                self._lexemes.append(f"{ntk[i]}{ntk[i + 1]}")
                                pass_count += 1
                        except:
                            if ntk[i] == '=':
                                self._lexemes.append(ntk[i])
                            else:
                                self._lexemes.append(ntk[i])
                    else:
                        if ntk[i] == '=':
                            self._lexemes.append(ntk[i])
                        else:
                            self._lexemes.append(ntk[i])
                elif bool(re.search(self._punc, ntk[i])):
                    self._lexemes.append(ntk[i])

    def iter_pre_token(self):
        for i in self._pre_tokens:
            for next_token in i:
                if(re.search(self._is_op, next_token)):
                    self.__check_op(next_token)
                else:
                    self._lexemes.append(next_token)
        return self._lexemes

class ParseTree:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        self.cleaned_tokens = []
        self.nl_len = 0
        self.parse_tree = []
        self.clean()
        self.parse_tree_gen()
    
    def clean(self):
        gt = ut.clear_file(self.filename)
        nl = []
        for index, i in enumerate(gt):
            try:
                if not ("bool" in i or "num" in i or "str" in i or "display" in i or "write" in i[0] or "+-" in i or "-=" in i or "+=" in i or "--" in i or "read" in i[2]):
                    nl.append(i)
            except:
                nl.append(i)
        self.nl_len = len(nl)
        self.cleaned_tokens = GeneratePTTokens(nl).iter_pre_token()

    def parse_tree_gen(self):
        grammar = ptc.parse_missing(self.cleaned_tokens)
        a = []
        parser = nltk.ChartParser(grammar)
        for tree in parser.parse(self.cleaned_tokens):
            a.append(tree)
        self.parse_tree.append(a)
        open(os.path.join(self.log_path, "parse_tree.txt"), "w+").close()
        fw = open(os.path.join(self.log_path, "parse_tree.txt"), "w")
        for i in self.parse_tree[0]:
            fw.write(str(str(i) + ' '))
        if ut.get_config()["generate_parse_tree_img"] == 1:
            self.parse_tree_img_gen(a[0])

    def parse_tree_img_gen(self, prse_tree):
        print("Converting Parse Tree...")
        TreeView(prse_tree)._cframe.print_to_file(os.path.join(self.log_path, "ptimg.ps"))
        print("Converting Parse Tree Into PS...")
        psimage=Image.open(os.path.join(self.log_path, "ptimg.ps"))
        print("Converting Parse Tree Into PNG...")
        psimage.save(os.path.join(self.log_path, "ptimg.png"))

# For Testing Purpose
if __name__ == "__main__":
    if ut.get_config()["env"] == "testing":
        ParseTree("test.txt", ut.get_test_log_path())