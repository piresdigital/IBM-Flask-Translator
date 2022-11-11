from translator import translator
from flask import Flask, render_template, request
import json

app = Flask("Flask Translator")

@app.route("/englishToPortuguese")
def englishToPortuguese():
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_portuguese(textToTranslate)

@app.route("/portugueseToEnglish")
def portugueseToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.portuguese_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
