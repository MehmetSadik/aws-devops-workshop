from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return('hello world')

@app.route("/second")
def second():
    return "This is second page"

@app.route("/third/subthird")
def third():
    return "This is subthird of third"

@app.route("/forth/<string:id>")
def forth(id):
    return f"This is subthird of third {id}"




if __name__== "__main__":
    app.run(debug=True)
    
    
    