import sys
import os
import subprocess

import tokenizer as tkr
import util as ut
import symbol_table as st
import type_check as tc
import parser_coco as pc
import imcg as im
import generate_py as gp


if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     raise Exception("Expected 1 argument but found 0.")
    # log_path = ut.logger_dir()
    # working_path = os.path.join(os.getcwd(), sys.argv[1])
    # tkz = tkr.Tokenize(working_path, log_path).get_tk()
    # pc.Parse(tkz)
    # stt = st.SymbolTable(working_path, log_path).get_st()
    # tc.TypeCheck(working_path)
    # imc = im.IntermediateCode(working_path, log_path).get_imc_path()
    # gpp = gp.GeneratePy(os.path.join(log_path, "imc.txt"), log_path).get_path()
    # subprocess.call(["python", gpp])

    #  Only For Testing Puropses
    sys.argv.append('test.txt')
    working_path = os.path.join(os.getcwd(), sys.argv[1])
    tkz = tkr.Tokenize(working_path, os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_tk()
    pc.Parse(tkz)
    stt = st.SymbolTable(working_path, os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_st()
    tc.TypeCheck(working_path)
    imc = im.IntermediateCode(working_path, os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_imc_path()
    gpp = gp.GeneratePy(os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819", "imc.txt"), os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819")).get_path()
    # subprocess.call(["python", gpp])