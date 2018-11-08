#word_frequency_list.py

'''This program takes in a word file, and then returns a histogram of all the words, the number of unique words within
   the text file, as well as the number of occurences of a particular word.

   USAGE: python3 ./word_frequency_list.py'''

import sys
from dictionary_words import read_in_txtfile, convert_to_list

'''Takes in a list of text, returns a histogram as a list of lists'''
def histogram(source_text):
    histogram_list = []

    if len(histogram_list) == 0:
        histogram_list.append([source_text[0], 1])

    for word in source_text:
        found_word = False
        for item in histogram_list:
            if item[0] == word:
                item[1] += 1
                found_word = True
                break
        if found_word == False:
            histogram_list.append([word, 1])

    return histogram_list

'''Take in a word and histogram, returns number of times that word occurs within the dictionary'''
def frequency(word, histogram):
    count = 0
    for item in histogram:
        if item[0] == word:
            count = item[1]
    return count

'''Takes in a histogram, returns number of unique words'''
def unique_words(histogram):
    count = 0
    for item in histogram:
        count += 1
    return count

def main():
    file_txt = read_in_txtfile('short_story.txt')
    txt_list = convert_to_list(file_txt)
    hist_list = histogram(txt_list)
    print(hist_list)

    unique_count = unique_words(hist_list)
    print("Number of unique words: {}".format(unique_count))


    word = "Troy"
    word_count = frequency(word, hist_list)
    print("Occurences of the word \'{}\': {}".format(word, word_count))


if __name__ == '__main__':
    main()
