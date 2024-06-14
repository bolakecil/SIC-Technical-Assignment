from flask import Flask, request, render_template_string

app=Flask(__name__)

latest_temperature=None

@app.route('/update_temperature', methods=['POST'])
def update_temperature():
    global latest_temperature
    latest_temperature = request.form['temperature']
    return 'OK', 200

@app.route('/')
def index():
    temp = latest_temperature or "No data yet"
    return render_template_string('''
        <!doctype html>
        <html>
        <head>
            <title>Temperature Monitor</title>
            <meta http-equiv="refresh" content="5">
        </head>
        <body>
            <h1>Current Temperature: {{ temp }} °C</h1>
        </body>
        </html>
    ''', temp=temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)