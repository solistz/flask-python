from app import app

counter = 0

@app.route('/')
@app.route('/index')
def index():
    return 'Hay WORLD'

@app.route('/info')
def info():
    global counter
    counter += 1
    return 'hellow, times: {}'.format(counter)


