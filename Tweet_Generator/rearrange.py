#rearrange.py

import sys, random

def start_message(arg_list):
    '''print out number of arguments'''
    if len(arg_list) == 1:
        print("Number of arguments: {} argument".format(len(arg_list)))
    else:
        print("Number of arguments: {} arguments".format(len(arg_list)))

def add_list(arg_list):
    '''add command line arguments into a list'''
    for argument in sys.argv[1: ]:
        arg_list.append(argument)

def randomize_list(arg_list):
    '''randomize the list of command line arguments'''
    if len(arg_list) == 0:
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

def main():
    arg_list = []
    add_list(arg_list)
    start_message(arg_list)
    print_list(arg_list)
    randomize_list(arg_list)
    print_list(arg_list)

if __name__ == '__main__':
    '''This program takes in all command line arguments
     and returns those arguments in a different ordering'''
    main()


# string = sys.argv[1:]
# shuffle(string)
# print(" ".join(string))
