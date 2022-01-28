import os

import util as ut

class GeneratePy:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        self.convert_file()

    def convert_file(self):
        f = open(self.filename)
        f = f.read()
        open(os.path.join(self.log_path, "imc.py"), "w+").close()
        fw = open(os.path.join(self.log_path, "imc.py"), "a")
        fw.write(f)
    
    def get_path(self):
        return os.path.join(self.log_path, "imc.py")

# For Testing Purpose
if __name__ == "__main__":
    if ut.get_config()["env"] == "testing":
        GeneratePy(os.path.join(ut.get_test_log_path(), "imc.txt"), ut.get_test_log_path())