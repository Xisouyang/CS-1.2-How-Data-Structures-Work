import sys
from dictionary_words import read_in_txtfile, convert_to_list

'''Takes in a list of text, returns a histogram as a list of tuples'''
def histogram(source_text):

    tuple_list = []
    tuple_list.append((source_text[0], 1))

    for word in source_text:
        found_word = False
        for index, item in enumerate(tuple_list):
            if item[0] == word:
                found_word = True
                temp_count = item[1] + 1
                temp_tuple = (word, temp_count)
                item, temp_tuple = temp_tuple, item
                tuple_list[index] = item
        if found_word == False:
            tuple_list.append((word, 1))

    return tuple_list

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
    tuple_list = histogram(txt_list)
    print(tuple_list)

    word_freq = frequency("The", tuple_list)
    print(word_freq)

    unique_words_count = unique_words(tuple_list)
    print(unique_words_count)

if __name__ == '__main__':
    main()
