from flask import Flask, make_response
from flask import render_template
from flask import Flask, request
from summarization_utils import get_summaries

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers


from flask import Flask, make_response
from flask import render_template
from flask import Flask, request
from summarization_utils import get_summaries

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    if request.method == 'POST':
        read_time = int(request.form.get('read_time', 1))
        summaries = get_summaries(read_time)
        return render_template('index.html', summaries=summaries)
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
