from flask import Flask, render_template, url_for, request, redirect
from ner import *
from helpers import helper


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        inp = request.form['input']
        sentence = helper.prepare_sentence(inp)
        task = test_camel(sentence)
        # task = helper.final_result(task)
        return render_template('test.html', task=task, inp=inp)
    else:
        return render_template('test.html', task='', inp='')


if __name__ == '__main__':
    app.run(debug=True)
