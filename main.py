# Importar
from flask import Flask, render_template, request
import jinja2
from Modelo import C_F

app = Flask(__name__)

Extensiones = {"png", "jpg", "jpeg"}

def allowed_file(filename):

    return "." in filename and \
    filename.rsplit("." , 1)[1].lower() in Extensiones
# La primera página
@app.route('/')
def index():


    return render_template('index.html')

@app.route('/Upload', methods=["POST"])
def UploadImage():
    #if "file-button" not in request.files:
    #    return "No hay ningun archivo ", 400
    file = request.files["file-button"]
    if file.filename == "":
        return "No se encontro el archivo ", 400
    if file and allowed_file(file.filename):
        file.save(f"./static/img/{file.filename}")
        return render_template('index.html', T_F = C_F(file), ruta_img = f"./static/img/{file.filename}", S = True) 
    else:
        return "Formato no permitido ", 400

app.run(debug=True)
