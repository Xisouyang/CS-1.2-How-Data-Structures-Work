'''This program takes in a textfile as an argument and returns a random sentence
generated through a markov chain'''

import sys, random, string
from dictogram import Dictogram
sys.path.insert(0, '../Tweet_Generator')
from sample import weighted_random_choice

def read_in_txtfile(text):
    '''reads in from text file and saves to an array'''
    with open(text) as f:
        word_data = f.read()
    return word_data

def convert_to_list(text_string):
    '''Takes in string of text, converts to and returns a list'''
    word_bank = text_string.split()
    return word_bank

def make_histogram_dict(txt_list):
    '''Iterates through your text file in form of a list, returns a dictionary
    containing the histograms of all words after a unique word'''

    histogram_dict = {}

    for i in range(len(txt_list) - 1):
        if txt_list[i] not in histogram_dict:
            histogram_dict[txt_list[i]] = Dictogram()
        histogram_dict[txt_list[i]].add_count(txt_list[i + 1])

    return histogram_dict

def random_walk(histogram_dict, txt_list):
    '''returns a random key inside the dictionary of histograms,
    and a random word that follows that random key based on weight'''
    rand_string = ""
    random_word = random.choice(list(histogram_dict))
    rand_string = rand_string + random_word + " "

    for i in range(len(txt_list) - 1):
        if random_word == txt_list[i]:
            rand_followup = weighted_random_choice(histogram_dict[txt_list[i]])
            rand_string = rand_string + rand_followup + " "
            return rand_string

def main():
    txtfile = read_in_txtfile("story.txt")
    txt_list = convert_to_list(txtfile)
    my_histogram_dict = make_histogram_dict(txt_list)
    print(my_histogram_dict)

    full_string = ""

    for i in range(20):
        test_string = random_walk(my_histogram_dict, txt_list)
        full_string += test_string
    print(full_string)


if __name__ == '__main__':
    main()
