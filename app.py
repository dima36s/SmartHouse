from flask import Flask, render_template, request

app = Flask(__name__)


# Главный экран
@app.route('/')
def home():
    return render_template('index.html')


# Управление освещением
@app.route('/lighting', methods=['GET', 'POST'])
def lighting():
    if request.method == 'POST':
        # Логика для управления освещением
        light_status = request.form['light_status']
        # Обработка команды включения/выключения освещения
        if light_status == 'on':
            # Включить освещение
            pass
        elif light_status == 'off':
            # Выключить освещение
            pass
    return render_template('lighting.html')


# Управление температурой
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        # Логика для управления температурой
        temperature = request.form['temperature']
        # Обработка установки желаемой температуры
        pass
    return render_template('temperature.html')


# Управление безопасностью
@app.route('/security', methods=['GET', 'POST'])
def security():
    if request.method == 'POST':
        # Логика для управления безопасностью
        security_status = request.form['security_status']
        # Обработка команды включения/выключения безопасности
        if security_status == 'on':
            # Включить безопасность
            pass
        elif security_status == 'off':
            # Выключить безопасность
            pass
    return render_template('security.html')


if __name__ == '__main__':
    app.run(debug=True)
