from flask import Flask, request, render_template
import test

app = Flask(__name__)

@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    if request.method == 'POST':
        read_time = int(request.form.get('read_time', 1))
        summaries = test.get_summaries(read_time)
        return render_template('index.html', summaries=summaries)
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
