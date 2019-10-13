import numpy as np

def fill_next_state(string, alphabet):
    next_state = {char: np.zeros((len(string) + 1), dtype=int) for char in alphabet}

    for i in range(len(string)+1):
        for char in next_state.keys():
            Pia = string[0:i] + char
            for j in range(i+1, 0, -1):
                if Pia[-j:] == string[:j]:
                    next_state[char][i] = j
                    break

    return next_state

def print_next_state_table(next_state):
    column_width = 3
    header_len = len(next_state) * column_width
    print('       |{word:^{header_len}s}'.format(word = 'character', header_len = header_len))
    print('{0:^7s}|'.format('state'), end = '')
    for key in next_state.keys():
        print('{0:^{column_width}s}'.format(key, column_width = column_width), end='')
    for i in range(len(next_state[key])):
        print('\n{0:^7d}|'.format(i), end = '')
        for key in next_state.keys():
            print('{0:^{column_width}d}'.format(next_state[key][i], column_width = column_width), end='')