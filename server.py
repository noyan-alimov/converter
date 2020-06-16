from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from converter import convertHtmlfile
from db_utils import addToDatabase, queryData

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


class SubmitHtmlForm(FlaskForm):
    name = StringField('HTML file name: ')
    submit = SubmitField('Submit')


class ReadDataFromDB(FlaskForm):
    col_name = StringField('Enter collection name: ')
    filter_data = StringField('Enter filter data: ')
    submit = SubmitField('Filter')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SubmitHtmlForm()
    if form.validate_on_submit():
        name = form.name.data
        convertHtmlfile(name)
        addToDatabase(name)

        return redirect(url_for('home'))

    return render_template('home.html', form=form)


@app.route('/query', methods=['GET', 'POST'])
def query():
    docs = []
    form = ReadDataFromDB()
    if form.validate_on_submit():
        col_name = form.col_name.data
        filter_data = form.filter_data.data
        data = queryData(col_name, filter_data)
        docs.append(data)
        docs = docs[0]

    return render_template('query.html', form=form, docs=docs)


if __name__ == '__main__':
    app.run(debug=True)
