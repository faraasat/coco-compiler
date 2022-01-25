import os

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

if __name__ == "__main__":
    GeneratePy(os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819", "imc.txt"), os.path.join(os.path.dirname(__file__), "_logs", "2022-01-18_22-22-06-487819"))