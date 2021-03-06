from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<word>')
def jinja_usage(word):
    return render_template('jinja_usage.html', item=word)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)

