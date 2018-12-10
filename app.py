import sys, random
from Tweet_Generator import sample
from Tweet_Generator import dictionary_words

from flask import Flask, render_template
from Code import markov_chain_v2

app = Flask(__name__)

@app.route("/")

def main():

    sentence_string = markov_chain_v2.main()

    return render_template("main.html", sentence = sentence_string)
