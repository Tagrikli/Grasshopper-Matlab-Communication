from flask import Flask
import logging
import ghhops_server as hs
import rhino3dm
from matlab_adapter import MatlabAdapter
from os import path
icon_path = path.join(path.dirname(__file__),'icon.png')

app = Flask(__name__)
app.logger.disabled = True
logging.getLogger('werkzeug').disabled = True

hops = hs.Hops(app)
matlab_adapter = MatlabAdapter()
matlab_adapter.loadFis()


@hops.component(
    "/matlab_fis",
    name="Matlab FIS Calculator",
    description="Runs the FIS function in matlab and returns the result.",
    icon=icon_path,
    inputs=[
        hs.HopsNumber("Extrude", "Extrude", "Extrude variable"),
        hs.HopsNumber("Color", "Color", "Color variable"),
        hs.HopsNumber("Shape", "Shape", "Shape variable"),
        hs.HopsNumber("Isolation", "Isolation", "Isolation variable"),
    ],
    outputs=[
        hs.HopsNumber("Output", "Output", "Output from the FIS")
    ]
)
def calculator(extrude, color, shape, isolation):
    return matlab_adapter.evalFis([extrude, color, shape, isolation])


if __name__ == "__main__":
    app.run()