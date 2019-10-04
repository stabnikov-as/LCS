import numpy as np
def compute_lcs_table(X, Y):
    '''
    Procedure to compute the LCS table
    :param X: word 1
    :param Y: word 2
    :return: returns lcs table for two words as a 2d numpy array
    '''
    # initialize table
    l = np.zeros((len(X) + 1, len(Y) + 1))

    # go through each word filling the table
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            # If current letters match, increment previous (i-1, j-1) table element
            # Else take the previous one, the LCS hasn't changed
            if X[i - 1] == Y[j - 1]:
                l[i, j] = l[i - 1, j - 1] + 1
            else:
                l[i, j] = max(l[i - 1, j], l[i, j - 1])
    return l


def print_table(l, X, Y):
    '''
    :param l: table, a numpy 2d array
    :param X: word 1
    :param Y: word 2
    :return: prints lcs table with headers and legend
    '''
    # print headers
    print('      |   j {a}'.format(a=' '.join([str(i) for i in range(l.shape[1])])))
    print('      |  yj   {a}'.format(a=' '.join([i for i in Y])))
    print('i  xi |l[i,j]')
    # print first row, since it's special
    print('0     |     {a}'.format(a=' '.join([str(int(i)) for i in l[0, ...]])))
    # print the table row by row
    for i in range(1, l.shape[0]):
        print('{i}  {b}  |     {a}'.format(a=' '.join([str(int(i)) for i in l[i, ...]]), i=i, b=X[i - 1]))