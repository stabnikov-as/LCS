
import lcs
import transformation as tr
import string_matching as sm


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

def transform_strings(X, Y, costs, operations):
    '''
    A function to transform one string to another
    :param X: str, first work
    :param Y: str, second word
    :param cost: list of ints, cost of operations
    :param operations: list of strings, the names of operations
    :return: nothing
    '''

    # assemble transformation and operations tables
    cost, op = tr.compute_transformation_table(X, Y, costs)
    # Print the found table
    tr.print_transformation_table(cost, op, X, Y, operations)
    # Assemble the transformation
    # This doesn't really do anything
    # Since we already know what the transformed string is
    # Just constructs the sequence of operations that transform one string to another
    print(tr.assemble_transformation(X, Y, op))

X = 'CATCGA'
Y = 'GTACCGTCA'

#find_and_print_lcs(X, Y)

X = 'ACAAGC'
Y = 'CCGT'

operations = ['copy', 'rep', 'del', 'ins']
costs = [-1, 1, 2, 2]

#transform_strings(X, Y, costs, operations)

def finite_automaton_string_matching(string_to, string_in, alphabet):
    '''
    Realises string matching algorythm using finite automaton
    :param string_to: str, String to match
    :param string_in: str, String to match in
    :param alphabet: str, a collection of characters that may be found in strings
    can use string_in as an alphabet if it is not too long and not all the chars a present
    :return: no return, prints the results
    '''
    # Assemble next_state table
    next_state = sm.fill_next_state(string_to, string_in)#alphabet)
    # Print next_state table
    sm.print_next_state_table(next_state)
    # Find and print (if toPrint then it's more Verbose) positions in the string where the string_to can be found
    print(sm.match_strings(string_in, next_state, toPrint = False))

# alphabet = 'aenhokvyzPSVl., '
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'
string_to = 'popa'
string_in  = 'popa shlyopa popo pipa,. dasdlkasdna.,smdndspopa pipa popopopopaaapa'


finite_automaton_string_matching(string_to, string_in, alphabet)




