from flask import Flask, render_template, request
from app import urlchkk


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def posts():
    try:
        if (request.method == 'POST'):
            msg = urlchkk(request.form.get("text"))
            # print(msg)
            return render_template('index.html', post=msg)
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(debug=True)