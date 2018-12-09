import sys, random, string
from dictogram import Dictogram

class markov(dict):

    def __init__(self, word_list=None, order=1):
        ''' markov class initialization'''
        super(markov, self).__init__()

        self.order = order

    #TODO: Create Markov Model

        # Create method to walk through word list, creating tuple of words based on order
        # Find every word that comes after that tuple sequence(our key) - save to Dictogram
        #
    def create_markov_model(self, word_list):

        order = self.order

        #iterate through the word list
        for i in range(len(word_list) - self.order):
            key = tuple(word_list[i: i + order])
            value = word_list[i + order]
            self.check_key(key, value)

        print(self)

    def check_key(self, key, value):
        if key in self:
            print("here")
            self[key].add_count(value)
        else:
            self[key] = Dictogram([value])


def read_in_txtfile(text):
    '''reads in from text file and saves to an array'''
    with open(text) as f:
        word_data = f.read()
    return word_data

def convert_to_list(text_string):
    '''Takes in string of text, converts to and returns a list'''
    word_bank = text_string.split()
    return word_bank

def main():
    txtfile = read_in_txtfile("story.txt")
    txt_list = convert_to_list(txtfile)
    markov_chain = markov(txt_list, 2)
    markov_chain.create_markov_model(txt_list)

if __name__ == '__main__':
    main()




    #TODO: Generate Sentence using Markov Model
