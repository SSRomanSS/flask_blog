from flask import render_template, flash, redirect, url_for
from blog import app
from blog.forms import LoginForm
from blog.models import *


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='HOME', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        remember_me = form.remember_me.data
        flash(f'Login requested for {user}, remember me - {remember_me}', 'info')
        redirect(url_for('index'))
    return render_template('login.html', title='LOG IN', form=form)