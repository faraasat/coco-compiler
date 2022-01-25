from datetime import datetime
import os

def absolute_path(dn):
    return os.path.join(os.path.dirname(__file__), dn)

def is_path_valid():
    cache_path = absolute_path("_logs")
    if not os.path.isdir(cache_path):
        os.mkdir(cache_path)

def logger_dir():
    dt = datetime.now()
    dt_name = dt.strftime("%Y-%m-%d_%H-%M-%S-%f")
    is_path_valid()
    os.mkdir(absolute_path(os.path.join("_logs", dt_name)))
    return absolute_path(os.path.join("_logs", dt_name))

def remove_comments(i, is_m_comment):
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

def clear_file(fn, imc):
    pre_tokens = []
    f = open(fn)
    f = f.readlines()
    for i in f:
        h = (remove_comments(i, imc)).strip()
        if h:
            pre_tokens.append(h.rstrip('\n').split(' '))
    return pre_tokens