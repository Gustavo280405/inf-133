from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error": "Se requiere un nombre en os parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"Hola, {nombre}"})

@app.route('/')
def hello_world():
    return 'Hola mundillo'

@app.route('/sumar', methods=['GET'])
def sumar():
    a=int(request.args.get("a")) 
    b=int(request.args.get("b"))
    if not a or not b:
        return(
            jsonify({"error":"Se requiere un valor en los parámetros de la URL."}),
            400,
        )
    resultado=a+b
    return jsonify({"respuesta": f"{resultado}={a}+{b}"})

@app.route('/palin', methods=['GET'])
def palin():
    pal=request.args.get("pal")
    if not pal:
        return(
            jsonify({"error":"Se requiere una cadena para los parámetros de la URL."})
        )
    if(pal[::-1]==pal):
        return jsonify({"palin": "es palindromo"})
    else:
        return jsonify({"palin": "no es palindromo"})

@app.route('/cont', methods=['GET'])
def cont():
    pal=request.args.get("pal")
    voc=request.args.get("voc")
    c=0
    if not pal or not voc:
        return(
            jsonify({"error":"Se requiere una cadena para los parámetros de la URL."})
        )
    for i in range (len(pal)):
        if(pal[i]==voc):
            c=c+1
    return jsonify({"cont": f"{c} veces se repite la vocal"})
if __name__ == '__main__':
    app.run()