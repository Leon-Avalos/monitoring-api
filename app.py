from flask import Flask, render_template, jsonify

from controllers import controller


app = Flask(__name__)

# Ruta bas y documentacion de la API
@app.route("/")
def main():
    return render_template('index.html')

# Ruta para datos de dioxido de nitrogeno


@app.route("/no2")
def nitrogen():
    data = controller.get_data("NO2")
    return jsonify({
        'count:': len(data),
        'data': data})


@app.route("/o3")
def ozone():
    data = controller.get_data("o3")
    return jsonify({
        'count:': len(data),
        'data': data})


@app.route("/pm10")
def pm():
    data = controller.get_data("pm10")
    return jsonify({
        'count:': len(data),
        'data': data})


@app.route("/pm25")
def pm25():
    data = controller.get_data("pm2.5")
    return jsonify({
        'count:': len(data),
        'data': data})


if __name__ == "__main__":
    app.run()
