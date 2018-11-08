import sys, random
from flask import Flask
from sample import get_random_word
from dictionary_words import read_in_txtfile, convert_to_list
from word_frequency_dict import histogram
app = Flask(__name__)

@app.route("/")
def main():
    #read in text file, store as list
    txt = read_in_txtfile("short_story.txt")
    txt_list = convert_to_list(txt)

    #create histogram based on list
    my_histogram = histogram(txt_list)

    sentence_string = ""

    random_number = random.randint(0, 20)
    for i in range(random_number):
        rand_word = get_random_word(my_histogram)
        sentence_string = sentence_string + " " + rand_word

    return sentence_string
