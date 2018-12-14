import sys, random
from Tweet_Generator import sample
from Tweet_Generator import dictionary_words

from flask import Flask, render_template
from Code import markov_chain_v2

app = Flask(__name__)

markov = markov_chain_v2.main()

@app.route("/")
def main():

    sentence_string = markov.generate_sentence(30)

    return render_template("main.html", sentence = sentence_string)
