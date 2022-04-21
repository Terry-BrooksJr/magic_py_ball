from crypt import methods
from flask import Flask, redirect, url_for, request, session, render_template, current_app as app 
from forms import Question, Wisdom 



@app.route('/', methods=['GET','POST'])
def home ():
    form = Question()
    if request.method == 'GET':
        return render_template('index.html.jinja', form=form)
    else: 
        recent_question = []
        
        
        
