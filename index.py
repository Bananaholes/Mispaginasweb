from flask import Flask, render_template

app=Flask(__name__)



@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/servicios")
def mostrarLenguajes():
    return render_template("servicios.html")


@app.route('/')
def principio():
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True, port=5017)


import os

print(os.getcwd())  # Te dice en qué carpeta estás ejecutando el script
print(os.listdir('templates'))  # Lista los archivos dentro de /templates
