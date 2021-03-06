from datetime import datetime
import os
import json

is_m_comment = False

def absolute_path(dn):
    return os.path.join(os.path.dirname(__file__), dn)

def is_path_valid():
    cache_path = absolute_path(get_config()["log_path"])
    if not os.path.isdir(cache_path):
        os.mkdir(cache_path)

def logger_dir():
    dt = datetime.now()
    dt_name = dt.strftime("%Y-%m-%d_%H-%M-%S-%f")
    is_path_valid()
    os.mkdir(absolute_path(os.path.join(get_config()["log_path"], dt_name)))
    return absolute_path(os.path.join(get_config()["log_path"], dt_name))

def remove_comments(i):
    global is_m_comment
    i = i.split('*@*')[0]
    if '/@' in i and '@/' in i:
        i = i.split('/@')[0]
    if '/@' in i:
        is_m_comment = True
        return ''
    elif '@/' in i:
        is_m_comment = False
        return ''
    elif is_m_comment:
        return ''
    return i

def clear_file(fn):
    pre_tokens = []
    f = open(fn)
    f = f.readlines()
    for i in f:
        h = (remove_comments(i)).strip()
        if h:
            pre_tokens.append(h.rstrip('\n').split(' '))
    return pre_tokens

def get_config():
    f = open('coco.config.json')
    return json.load(f)

def get_test_log_path():
    f = open('coco.config.json')
    is_path_valid()
    test_log_path = os.path.join(os.path.dirname(__file__), get_config()["log_path"], json.load(f)["test_log_path"])
    if not os.path.isdir(test_log_path):
        os.mkdir(test_log_path)
    return test_log_path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYELLOW = '\33[33m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    UNDERLINE = '\033[4m'

def check_verbosity(msg=""):
    if get_config()["verbosity"] == 1:
        print(msg)