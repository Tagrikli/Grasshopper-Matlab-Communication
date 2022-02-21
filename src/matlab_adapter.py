import matlab.engine
from os import listdir, path

class MatlabAdapter:
    def __init__(self):
        self.engine = matlab.engine.start_matlab()
        self.fis = None

    @classmethod
    def findFis(cls):
        for file in listdir(path.dirname(__file__)):
            if file.endswith('.fis'):
                return path.abspath(file)

    def loadFis(self):
        fis_file = MatlabAdapter.findFis()
        print(fis_file)
        self.fis = self.engine.readfis(fis_file)

    def evalFis(self,inps):
        inps_int = []
        for inp in inps:
            inps_int.append(float(inp))

        return self.engine.evalfis(self.fis,matlab.double(inps))

    def __del__(self):
        self.engine.quit()