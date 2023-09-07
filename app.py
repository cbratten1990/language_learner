from flask import Flask, render_template

app = Flask(__name__)

# Define routes and views here

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/page")
def page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
