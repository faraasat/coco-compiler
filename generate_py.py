import os

import util as ut

class GeneratePy:
    def __init__(self, fn, lp):
        if not os.path.exists(fn):
            raise Exception("Invalid Path Provided!")
        self.filename = fn
        self.log_path = lp
        ut.check_verbosity(f"{ut.bcolors.BOLD}---  Python Executable File Generator  ---{ut.bcolors.ENDC}")
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Starting Python File Genration...{ut.bcolors.ENDC}")
        self.convert_file()
        ut.check_verbosity(f"{ut.bcolors.OKBLUE}\t*  Python Executable File Generated At:{ut.bcolors.ENDC}")
        ut.check_verbosity(f"{ut.bcolors.CYELLOW}\t   -   {os.path.join(self.log_path, 'imc.py')}{ut.bcolors.ENDC}")
        ut.check_verbosity()

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