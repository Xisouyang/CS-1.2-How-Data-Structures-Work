import sys, random
from sample import weighted_random_choice
from dictionary_words import read_in_txtfile, convert_to_list

from flask import Flask, render_template
sys.path.insert(0, '../Code')
import markov_chain_v2
app = Flask(__name__)

@app.route("/")
def main():
    
    sentence_string = markov_chain_v2.main()

    return render_template("main.html", sentence=sentence_string)
