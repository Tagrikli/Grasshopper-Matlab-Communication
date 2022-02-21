from flask import Flask
import ghhops_server as hs
import rhino3dm

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/test/echo",
    name="Hops Server Test",
    description="Test server.",
    inputs=[
        hs.HopsNumber("Input")
    ],
    outputs=[
        hs.HopsNumber("Output")
    ]
)
def echo(input_number):
    return input_number


if __name__ == "__main__":
    app.run()