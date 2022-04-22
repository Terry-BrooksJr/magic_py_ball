from flask import Flask, redirect, url_for, request, session, render_template 
from forms import Question, Wisdom 
from flask_sqlalchemy import SQLAlchemy
import os
from app import app 

@app.route('/', methods=['GET','POST'])
def home ():
    form = Question()
    if request.method == 'GET':
        return render_template('index.html.jinja', form=form)
    else: 
        recent_question = []
