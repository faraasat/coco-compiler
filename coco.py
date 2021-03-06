import traceback
import sys
import os
import subprocess

import util as ut
import tokenizer as tkr
import symbol_table as st
import type_check as tc
import parser_coco as pc
import imcg as im
import generate_py as gp
import parse_tree as pt

def main():
    conf = ut.get_config()
    if conf["env"] == "testing":
        #  Only For Testing Puropses
        ut.check_verbosity(f"{ut.bcolors.BOLD}{ut.bcolors.CITALIC}{ut.bcolors.UNDERLINE}{ut.bcolors.CBLINK}*************** Running in Test Environment ***************\n{ut.bcolors.ENDC}")
        test_path = ut.get_test_log_path()
        working_path = os.path.join(os.getcwd(), "test.txt")
        tkz = tkr.Tokenize(working_path, test_path).get_tk()
        pc.Parse(tkz)
        if ut.get_config()["generate_parse_tree"] == 1: pt.ParseTree("test.txt", ut.get_test_log_path())
        st.SymbolTable(working_path, test_path)
        tc.TypeCheck(working_path)
        im.IntermediateCode(working_path, test_path)
        gpp = gp.GeneratePy(os.path.join(test_path, "imc.txt"), test_path).get_path()
        if conf["execute"] == 1:
            ut.check_verbosity(f"{ut.bcolors.BOLD}---  Code Execution  ---{ut.bcolors.ENDC}")
            ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Executing Code from: {gpp}{ut.bcolors.ENDC}")
            ut.check_verbosity(f"{ut.bcolors.CYELLOW}\t   -   {gpp}{ut.bcolors.ENDC}")
            subprocess.call(["python", gpp])
    else:
        if len(sys.argv) == 1:
            raise Exception("Expected 1 argument but found 0! Please provide file path.")
        ut.check_verbosity(f"{ut.bcolors.BOLD}{ut.bcolors.CITALIC}{ut.bcolors.UNDERLINE}{ut.bcolors.CBLINK}*************** Running in Production ***************\n{ut.bcolors.ENDC}")
        log_path = ut.logger_dir()
        working_path = os.path.join(os.getcwd(), sys.argv[1])
        tkz = tkr.Tokenize(working_path, log_path).get_tk()
        pc.Parse(tkz)
        if ut.get_config()["generate_parse_tree"] == 1: pt.ParseTree(working_path, log_path)
        stt = st.SymbolTable(working_path, log_path).get_st()
        tc.TypeCheck(working_path)
        imc = im.IntermediateCode(working_path, log_path).get_imc_path()
        gpp = gp.GeneratePy(os.path.join(log_path, "imc.txt"), log_path).get_path()
        if conf["execute"] == 1:
            ut.check_verbosity(f"{ut.bcolors.BOLD}---  Code Execution  ---{ut.bcolors.ENDC}")
            ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Executing Code from: {gpp}{ut.bcolors.ENDC}")
            subprocess.call(["python", gpp])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{ut.bcolors.BOLD}\n---   Traceback   ---{ut.bcolors.ENDC}")
        print(f"{ut.bcolors.FAIL}{traceback.format_exc()}{ut.bcolors.ENDC}")
        print(f"{ut.bcolors.BOLD}---   Message   ---{ut.bcolors.ENDC}")
        print(f"{ut.bcolors.FAIL}{e}{ut.bcolors.ENDC}")