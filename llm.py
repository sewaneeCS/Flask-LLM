from flask import Flask, render_template, redirect, url_for, request #type: ignore
from flask_bootstrap import Bootstrap5 #type: ignore

from flask_wtf import FlaskForm, CSRFProtect #type: ignore
from wtforms import StringField, SubmitField #type: ignore

from functions import prompt #type: ignore

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$I'

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

class AskForm(FlaskForm):
    p = StringField('Ask me anything! Or tell me to do something.')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def ppt():
    form = AskForm()
    return render_template('index.html', form=form)

@app.route('/answer', methods=['POST'])
def answer():
    if request.method == 'POST':
        pt = request.form['p']
        answer = prompt(pt)
    return render_template('answer.html', pt=pt, answer=answer)

@app.route('/model', methods=['GET', 'POST'])
def model():
    return render_template('model.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
