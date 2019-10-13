import numpy as np

def fill_next_state(string, alphabet):
    '''
    Function fo assemble next_state table according to Finite Automaton
    :param string: str, string to match
    :param alphabet: str, a set of characters that strings consist of
    :return:
    '''
    # Assembling a dictionary, with keys are characters from the alphabet
    # and indices in the lists are the states of the Finite Automaton
    next_state = {char: np.zeros((len(string) + 1), dtype=int) for char in alphabet} # a dict of 1d numpy arrays

    # cycles through each element of the table
    for i in range(len(string)+1):
        for char in next_state.keys():
            # Pia is a string consisting of Pi - a prefix of sting to march
            # and current char from the alphabet
            Pia = string[0:i] + char
            # check if Pia suffixes match sting prefixes
            # the length of such match is the next state magnitude
            for j in range(i+1, 0, -1):
                if Pia[-j:] == string[:j]:
                    next_state[char][i] = j
                    break

    return next_state

def print_next_state_table(next_state):
    '''
    Function pretty prints the next_state table
    :param next_state: dict of np 1d arrays of integers. keys are characters from the alphabet. Next_state table
    :return: no return, just prints
    '''
    # Parameters for pretty outputs to match the widths of columns
    column_width = 2
    header_len = len(next_state) * column_width
    # print header
    print('       |{word:^{header_len}s}'.format(word = 'character', header_len = header_len))
    print('{0:^7s}|'.format('state'), end = '')
    for key in next_state.keys():
        print('{0:>{column_width}s}'.format(key, column_width = column_width), end='')
    # print main content
    for i in range(len(next_state[key])):
        print('\n{0:^7d}|'.format(i), end = '')
        for key in next_state.keys():
            print('{0:>{column_width}d}'.format(next_state[key][i], column_width = column_width), end='')
    print('\n')

def match_strings(string_in, next_state, toPrint = False):
    '''
    A function that returns positions of string_to in string_in
    doesn't require string_ro since all the information is already in the table
    :param string_in: str, a string to search string_to in
    :param next_state: a table of next_state according to Finite Automaton
    :param toPrint: bool, if you want the procedure to be Verbose
    :return: a list of indices where string_to starts if there are any matches
              empty list if no matches
    '''
    # initialize variables
    i = 1
    state = 0
    matches = []

    len_str_to = len(next_state[string_in[0]])-1 # get length of string to match

    # Go through every character in string_in and define state of Finite Automaton
    # If FA reaches max value (len_str_to) then there is a match and append the
    # index of where the match starts to the list to be returned
    for ch in string_in:
        state = next_state[ch][state] # defines the next state using current state and current character
        if state == len_str_to:
            if toPrint: print('String matches at position {}'.format(i-len_str_to+1))
            matches.append(i-len_str_to)
        i += 1
    return matches