from flask import Flask, url_for, redirect, request, make_response, render_template, session
import jinja2

app = Flask('Prva flask aplikacija')

podaci_temperatura = [
    {'datum': '21.11.2023', 'vrijednost': 19},
    {'datum': '22.11.2023', 'vrijednost': 18},
    {'datum': '23.11.2023', 'vrijednost': 17},
    {'datum': '24.11.2023', 'vrijednost': 16}
]

podaci_vlaga = [
    {'datum': '21.11.2023', 'vrijednost': 50},
    {'datum': '22.11.2023', 'vrijednost': 48},
    {'datum': '23.11.2023', 'vrijednost': 45},
    {'datum': '24.11.2023', 'vrijednost': 47}
]

app.secret_key = '_de5jRRR83x'

@app.before_request
def before_request_func():
    if request.path.startswith('/static'):
        return  
    if request.path == '/login':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))

@app.get('/')
def index():
    global podaci_vlaga, podaci_temperatura
    id_param = request.args.get('id')
    if id_param == '1' or id_param == None:
        response = render_template('index.html', naslov = 'Pocetna stranica', tip = 'Temperatura', username = session.get('username').capitalize(), podaci = podaci_temperatura)
        return response, 200
    if id_param == '2':
        response2 = render_template('index.html', naslov = 'Pocetna stranica', tip = 'Vlaga', username = session.get('username').capitalize(), podaci = podaci_vlaga)
        return response2, 200

@app.get('/login')
def login():
    response = render_template('login.html',  naslov = 'Stranica za prijavu')
    return response

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.post('/login')
def check():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template('login.html', naslov='Stranica za prijavu', poruka='Uneseni su pogresni podaci')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)