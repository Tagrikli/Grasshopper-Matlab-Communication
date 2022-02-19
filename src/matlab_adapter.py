import matlab.engine
import os

class MatlabAdapter:
    def __init__(self):
        self.engine = matlab.engine.start_matlab()
        self.fis = None

    @classmethod
    def findFis(cls):
        for file in os.listdir('.'):
            if file.endswith('.fis'):
                return os.path.abspath(file)

    def loadFis(self):
        fis_file = MatlabAdapter.findFis()
        self.fis = self.engine.readfis(fis_file)

    def evalFis(self,inps):
        return self.engine.evalfis(self.fis,inps)

    def __del__(self):
        self.engine.quit()