from app import app

from flask import render_template

counter = 0

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Solist'}
    posts = [
        {
            'title':'art 1',
            'body':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
        },
        {
            'title':'art 2',
            'body':'New Site'
        }
    ]

    return render_template('index.html', title='Test Pages', user=user, posts=posts)



@app.route('/info')
def info():
    global counter
    counter += 1
    return render_template('info.html', title='INFO Pages', counter = counter)


