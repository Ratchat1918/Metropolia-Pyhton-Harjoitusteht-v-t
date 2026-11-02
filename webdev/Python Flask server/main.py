from pathlib import Path

import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/check_number/<number>')
def check_number(number):
    number = int(number)
    numberIsPrime = True
    if number % 2 == 0 and number !=2:
        numberIsPrime = False
    response = {
        "Number": number,
        "isPrime": numberIsPrime
    }
    return response

dictionary_path = Path(__file__).parent / 'static' / 'dictionary.json'
with dictionary_path.open(encoding='utf-8') as dictionary_file:
    dictionary = json.load(dictionary_file)

@app.route('/translate/<word>')
def translate_word(word):
    translation = dictionary.get(word.lower())
    response = {"error": "Word not found"}
    if translation != None:
        response = {
            "English": word,
            "Finish": translation
            }
    return response

if __name__ == "__main__":
    app.run(use_reloader=True)