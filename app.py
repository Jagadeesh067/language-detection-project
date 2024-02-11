from flask import Flask, request,jsonify, render_template
import algorithm 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def test():
    getint = request.json.get('text')
    if getint is not None:
        return algorithm.text(getint)
        # return getint
    else:
        return "No 'text' field found in the form data"

if __name__ == '__main__':
    app.run(debug=True)
