# packages
from flask import Flask, render_template, request, redirect, url_for, abort, session
import data
import random

# globals
previous_pointer = 0

# helper function
def get_pointer():
    global previous_pointer
    while(1):
        i = random.randint(0,48)
        if i != previous_pointer:
            previous_pointer = i
            return i

# app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    session['tense'] = request.form['tense']
    session['mode'] = request.form['mode']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    global previous_pointer
    if not 'tense' in session:
        return abort(403)
    #i = get_pointer()
    #while(1):
    #    i = random.randint(0,48)
    #    if i != previous_pointer:
    #        previous_pointer = i
    #        break
    #for x in range(20):
    #    i = random.randint(0,48)
    #words = data.present_tense[i]
    #session['myword'] = words

    if session['tense'] == 'present':
        i = get_pointer()
        words = data.present_tense[i]
    elif session['tense'] == 'preterit':
        i = get_pointer()
        words = data.preterit_tense[i]
    elif session['tense'] == 'imperfect':
        old_pointer = previous_pointer
        flag = 1
        xverb = [0, 1, 2, 3, 22, 41, 46]
        while(flag):

            i = get_pointer()
            for x in xverb:
                if x == i:
                    words = data.imperfect_tense[i]
                    flag = 0
                    break
                else:
                    previous_pointer = old_pointer
    else:
        i = get_pointer()
        words = data.future_tense[i]
    session['myword'] = words
    """
    newwords=list()
    for words in data.preterit_tense[i]:
        newwords.append( words )
    morenewwords=data.imperfect_tense[i]
    futurewords=data.future_tense[i]
    """
    mode=session['mode']
    if mode == 'refresh':
        return render_template('refresh_message.html')
    else:
        return render_template('test_message.html')

@app.route('/answer')
def answer():
    session['mode'] = 'refresh'
    return render_template('refresh_message.html')

if __name__ == '__main__':
    app.run()
