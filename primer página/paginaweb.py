from flask import Flask,render_template

app = Flask("Página-Conta")

@app.route("/")
def hello_world():
    return render_template("Index.html")

@app.route("/example")
def example_route():
    return "esto es una pagina de ejemplo"

@app.route("/<name>")
def return_with_dynamic_content(name):
    return render_template("name.html",contenido=name,Lorem = "Todo se actualiza perfecto")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port="5000")
