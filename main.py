
import lcs
import transformation

X = 'CATCGA'
Y = 'GTACCGTCA'
# X = 'popa'
# Y = 'sholpya'

def find_and_print_lcs(X, Y):
    '''
    :param X: string, first  word
    :param Y: string, second word
    :return: LCS, string
    '''
    # Find LCS table - a table containing lengths of longest common substrings of Xi and Yj
    l = lcs.compute_lcs_table(X, Y)
    # Print the found table
    lcs.print_lcs_table(l, X, Y)
    # Assemble lcs using words and table
    LCS = lcs.assemble_lcs(X, Y, l)
    print('\nLCS = ' + LCS)
    return LCS

find_and_print_lcs(X, Y)