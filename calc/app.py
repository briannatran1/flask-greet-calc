# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get("/add")
def query_add():
    """returns addition result from query"""
    queries = process_query_to_int(request)
    result = add(queries[0], queries[1])
    return str(result)


@app.get("/sub")
def query_sub():
    """returns subtraction result from query"""
    queries = process_query_to_int(request)
    result = sub(queries[0], queries[1])
    return str(result)


@app.get("/mult")
def query_multiply():
    """returns multiplication result from query"""
    queries = process_query_to_int(request)
    result = mult(queries[0], queries[1])
    return str(result)


@app.get("/div")
def query_division():
    """returns division result from query"""
    queries = process_query_to_int(request)
    result = int(div(queries[0], queries[1]))
    return str(result)


def process_query_to_int(request):
    """returns query params as integer tuple"""
    return (int(request.args["a"]), int(request.args["b"]))


# further study...

# OPERATIONS: {"add": add, "sub": sub, "mult": mult, "div": div}

# @app.get("/<operation>")
# def query_math(operation):
