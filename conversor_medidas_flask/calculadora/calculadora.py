from flask import Flask, render_template

calculadora = Flask(__name__)

@calculadora.route("/")
def inicial():
    return render_template("inicial.html")


@calculadora.route("/quadrado")
def Lado():
    return render_template("quadrado.html")

@calculadora.route("/circulo")
def Raio():
    return render_template("circulo.html")

@calculadora.route("/retangulo")
def Lado_re():
    return render_template("retangulo.html")

@calculadora.route("/triangulo")
def Lado_tri():
    return render_template("triangulo.html")



if __name__ == "__main__":
    calculadora.run(debug=True)