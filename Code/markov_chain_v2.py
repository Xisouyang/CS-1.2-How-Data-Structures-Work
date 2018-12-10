import sys, random, string
from dictogram import Dictogram
sys.path.insert(0, '../Tweet_Generator')
from Tweet_Generator.sample import weighted_random_choice

class markov(dict):

    def __init__(self, word_list=None, order=1):
        ''' markov class initialization'''
        super(markov, self).__init__()

        self.order = order

    def create_markov_model(self, word_list):

        order = self.order

        #iterate through the word list
        for i in range(len(word_list) - self.order):
            key = tuple(word_list[i: i + order])
            value = word_list[i + order]
            self.check_key(key, value)

    def check_key(self, key, value):
        if key in self:
            self[key].add_count(value)
        else:
            self[key] = Dictogram([value])

    def generate_sentence(self, txt_list, count=10):

        # Find random key
        rand_string = ""
        rand_key = random.choice(list(self))
        rand_followup = weighted_random_choice(self[rand_key])
        rand_string = rand_string + ' '.join(rand_key) + ' ' + rand_followup

        # add follow-up word to tuple, chop off head
        for i in range(count - self.order - 1):

            tmp_list = list(rand_key)
            tmp_list.append(rand_followup)
            tmp_list = tmp_list[1:]
            rand_key = tuple(tmp_list)

            try:
                rand_followup = weighted_random_choice(self[rand_key])
            except KeyError:
                rand_key = random.choice(list(self))
                rand_followup = weighted_random_choice(self[rand_key])

            while rand_followup == None:
                rand_followup = weighted_random_choice(self[rand_key])
                print(rand_followup)

            rand_string = rand_string + " " + rand_followup

        return rand_string

def read_in_txtfile(text):
    '''reads in from text file and saves to an array'''
    with open(text) as f:
        word_data = f.read()
    return word_data

def convert_to_list(text_string):
    '''Takes in string of text, converts to and returns a list'''
    word_list = text_string.split()
    return word_list

def main():
    txtfile = read_in_txtfile("./Tweet_Generator/lord.txt")
    txt_list = convert_to_list(txtfile)
    markov_chain = markov(txt_list, 3)
    markov_chain.create_markov_model(txt_list)
    string = markov_chain.generate_sentence(txt_list, 30)

    return string

if __name__ == '__main__':
    main()
