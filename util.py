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