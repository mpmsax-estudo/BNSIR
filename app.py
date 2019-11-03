from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teste.html", methods=["GET"])
def teste():
    return render_template("teste.html")

if __name__ == "__main__":
    app.run()

