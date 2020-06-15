from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from converter import convertHtmlfile
from add_to_db import addToDatabase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


class SubmitHtmlForm(FlaskForm):
    name = StringField('HTML file name: ')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SubmitHtmlForm()
    if form.validate_on_submit():
        name = form.name.data
        convertHtmlfile(name)
        addToDatabase(name)

        return redirect(url_for('home'))

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
