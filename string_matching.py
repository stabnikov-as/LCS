import numpy as np

def fill_next_state(string, alphabet):
    a_i = np.array([i for i in range(len(alphabet))], dtype=int)
    next_state = np.zeros((len(string) + 1, len(alphabet)), dtype=int)

    for i in range(next_state.shape[0]):
        for j in range(next_state.shape[1]):
            Pia = string[0:i] + alphabet[a_i[j]]
            print(Pia)

