import sys
import os

import tokenizer as tkr
import util as ut
import symbol_table as st
import type_check as tc
import parser_coco as pc


if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     raise Exception("Expected 1 argument but found 0.")
    # log_path = ut.logger_dir()
    sys.argv.append('test.txt')
    working_path = os.path.join(os.getcwd(), sys.argv[1])
    tkz = tkr.Tokenize(working_path, os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_tk()
    stt = st.SymbolTable(working_path, os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_st()
    tc.TypeCheck(working_path)
    pc.Parse(tkz, stt)
    