from flask import render_template
from app import app
from random import randint


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# @app.route('/jokes')
# def jokes():
#    jokes = ["I invented a new word! ... Plagiarism!",
#              "Why do we tell actors to “break a leg? ... Because every play has a cast.",
#              "Knock! Knock! ... Who’s there? ... Control Freak. ... Con… ... OK, now you say, “Control Freak who?” "]
#    return jokes[randint(0, len(jokes) - 1)]
