from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():

    nombre = request.form["nombre"]
    email = request.form["email"]
    mensaje = request.form["mensaje"]

    with open("mensajes.txt", "a") as archivo:
        archivo.write(f"{nombre} | {email} | {mensaje}\n")

    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)