from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def add_handler():
    """Returns a + b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(add(a, b))

@app.get("/sub")
def sub_handler():
    """Returns a - b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a, b))

@app.get("/mult")
def mult_handler():
    """Returns a * b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a, b))

@app.get("/div")
def div_handler():
    """Returns a / b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a, b))

@app.get("/math/<operation>")
def math_handler(operation):
    """Return result of math operation of a and b"""
    operations = {"add": add, "sub": sub,
                  "mult": mult, "div": div}

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    funct = operations.get(operation)
    return str(funct(a,b))
