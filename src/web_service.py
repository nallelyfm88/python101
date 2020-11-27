from flask import Flask, jsonify

app = Flask(__name__,static_url_path="")

@app.route('/json',methods=['GET'])
def ejemplo_json():
    contenido = {"id": 1, "nombre": "Juan", "apellido": "flores"}
    segundo = {"id": 2, "nombre": "Nallely", "apellido": "Martinez"}
    lista = [contenido,segundo]
    return jsonify(lista)



@app.route('/',methods=['GET'])
def hola_mundo_flask():
    return 'hola mundo'





if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
 

