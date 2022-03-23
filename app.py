from crypt import methods
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.get("/<int:numero>")
@app.post("/<int:numero>") #e se deixar esse caminho ativo ele também funciona
#@app.route("/", methods=['GET', 'POST']) pode ser feito dessa maneira também

def ola(numero):
    return f'Olá mundo.{numero}'

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True) se o debug ficar como True, o VS vai fazer o debug automatico, e bom, porém não e muito interessante deixar assim

