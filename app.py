from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

@app.route('/convert/celsius-to-fahrenheit')
def convert_celsius_fahrenheit():
    value = request.args.get('value', type=float)
    if value is None:
        return jsonify({'error': '"value" parameter is required'}), 400
    return jsonify({'celsius': value, 'fahrenheit': celsius_to_fahrenheit(value)})

@app.route('/convert/fahrenheit-to-celsius')
def convert_fahrenheit_celsius():
    value = request.args.get('value', type=float)
    if value is None:
        return jsonify({'error': '"value" parameter is required'}), 400
    return jsonify({'fahrenheit': value, 'celsius': fahrenheit_to_celsius(value)})

@app.route('/convert/km-to-miles')
def convert_km_miles():
    value = request.args.get('value', type=float)
    if value is None:
        return jsonify({'error': '"value" parameter is required'}), 400
    return jsonify({'km': value, 'miles': km_to_miles(value)})

@app.route('/convert/miles-to-km')
def convert_miles_km():
    value = request.args.get('value', type=float)
    if value is None:
        return jsonify({'error': '"value" parameter is required'}), 400
    return jsonify({'miles': value, 'km': miles_to_km(value)})

if __name__ == '__main__':
    app.run(debug=True)