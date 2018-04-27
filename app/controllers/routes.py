from app import app

@app.route('/index')
@app.route('/')
def index():
    return 'Hello world!'

@app.route('/test', defaults={'name': None})
@app.route('/test/<name>')
def teste(name):
    if name:
        return 'Olá {}!'.format(name)
    else:
        return 'Olá!'
