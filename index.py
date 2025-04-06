from flask import Flask, render_template

app=Flask(__name__)


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/lenguajes")
def mostrarLenguajes():
    mislenguajes=("PHP", "Python", "Java", "C#", "JavaScript", "Perl", "Ruby", "Rust")
    return render_template("lenguajes.html", lenguajes=mislenguajes)


@app.route('/')
def principio():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True, port=5017)
