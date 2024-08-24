from app import app

@app.route('/')
def index():
    return "Hola, Equipo!"

@app.route('/yeison')
def yeison():
    return "Hola, Equipo, este es mi aporte!"