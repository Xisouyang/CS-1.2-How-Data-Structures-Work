#rearrange.py
'''This program takes in all command line arguments
 and returns those arguments in a different ordering'''

import sys, random

'''print out number of arguments'''
def start_message():
    if len(arg_list) == 1:
        print("Number of arguments: {} argument".format(len(arg_list)))
    else:
        print("Number of arguments: {} arguments".format(len(arg_list)))

'''add command line arguments into a list'''
def add_list(list):
    for argument in sys.argv[1: ]:
        arg_list.append(argument)

'''randomize the list of command line arguments'''
def randomize_list(list):
    if len(list) == 0:
        print("No arguments")
        return
    for index in range(0, len(sys.argv) - 1):
        rand_item = arg_list.pop(random.randint(0, len(arg_list) - 1))
        arg_list.append(rand_item)

def print_list(list):
    if len(list) == 0:
        print("No arguments")
        return
    print(" ".join(list))

if __name__ == '__main__':
    arg_list = []
    add_list(arg_list)
    start_message()
    print_list(arg_list)
    randomize_list(arg_list)
    print_list(arg_list)

# string = sys.argv[1:]
# shuffle(string)
# print(" ".join(string))
