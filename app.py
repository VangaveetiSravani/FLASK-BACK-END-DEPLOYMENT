from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    test_string = request.form['teststring']
    regex_pattern = request.form['regex_pattern']

    matches = find_matches(test_string, regex_pattern)

    return jsonify({'matches': matches})


def find_matches(test_string, regex_pattern):
    matches = re.findall(regex_pattern, test_string)
    return matches


@app.route('/email', methods=["POST"])
def email():
    return render_template("verifications.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
