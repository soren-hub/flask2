from flask import Flask, jsonify
from products import products

app = Flask(__name__) #servidor

#crear rutas

@app.route('/ping', methods =['GET'])
def ping():
    return jsonify({"message": "pong"})

#otra ruta
#SE USA METHODS SEGUN LA ACCION QUE QUERAMOS SOBRE EL SERVIDOR:
#GET VIENE POR DEFAULT
#POST: PARA GUARDAR DATOS EN EL SERVIDOR
#PUT: ACTUALIZAR DATOS
#DELETE: BORRAR DATOS

@app.route('/products', methods =['GET'])
def getProducts():
    return jsonify({"products": products, "message": "product's list"})

#creacion de errores:
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
