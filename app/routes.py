from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'Username': 'Elisha'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in San Fransico'
        },
        {
            'author': {'username': 'AY comedian'},
            'body': '40 days in Atlanta'
        },
        {
            'author': {'username': 'Longrich'},
            'body': 'Longrich Trip to Johnnersburg South Africa'
        }
    ]
    return render_template('index.html', title='Homepage - Microblog', user=user, posts=posts)