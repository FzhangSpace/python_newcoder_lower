# -*- encoding=UTF8 -*-

from nowstagram import app
from flask import render_template
from models import Image, User

@app.route('/')
def index():
    images = Image.query.order_by('id desc').limit(10).all()
    return render_template('index.html', images=images)