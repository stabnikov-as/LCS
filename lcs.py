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
            # If current characters match, increment previous (i-1, j-1) table element
            # Else take the previous one, the LCS hasn't changed
            if X[i - 1] == Y[j - 1]:
                l[i, j] = l[i - 1, j - 1] + 1
            else:
                l[i, j] = max(l[i - 1, j], l[i, j - 1])
    return l

def print_lcs_table(l, X, Y):
    '''
    Prints LCS table
    :param l: table, a numpy 2d array
    :param X: word 1
    :param Y: word 2
    :return: none
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

def assemble_lcs(X, Y, l):
    '''
    Assembles longest common subsequence of 2 words, using LCS table
    :param X: First word, string
    :param Y: Second word, string
    :param l: LCS table, numpy array with dimensions len(X) x len(Y)
    :param i: current index in first word (in the table, since it has len(X) + 1 rows), int
    :param j: current index in second word (in the table, since it has len(X) + 1 rows), int
    :return: LCS, string Longest common subsequence
    '''
    # Find the lengths of words
    i, j = l.shape
    # Set current indeces to the last characters
    i -= 1
    j -= 1
    # If the current table element is zero, that means that the longest common subsequence is an empty string
    if l[i,j] == 0:
        return ''
    # Else if the last characters are equal means that it is the last character in the LCS
    # Add it to the end and call the same procedure with words without last characters
    elif X[i-1] == Y[j-1]:
        return assemble_lcs(X, Y, l[:-1, :-1]) + X[i-1]
    # else, if the characters are not the same, call the procedure with one of the words reduced by one character
    # whichever LCS is going to be longer
    elif l[i,j-1] < l[i-1, j]:
        return assemble_lcs(X, Y, l[:-1, :])
    else:
        return assemble_lcs(X, Y, l[:, :-1])

