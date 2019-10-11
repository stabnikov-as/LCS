import numpy as np

def compute_transformation_table(X, Y, costs):
    '''
    A function to assemble tables of cost and operations to transform one word into another
    :param X: str, first word
    :param Y: str, second word
    :param costs: a list of costs for operations
    :return: two numpy 2d arrays of integers:
    cost - a table of costs to transform Xi to Yj
    op - a table of operations performed
    '''

    # initialize table
    cost = np.zeros((len(X) + 1, len(Y) + 1), dtype = int)
    op   = np.zeros((len(X) + 1, len(Y) + 1), dtype = int)
    op[0, 0] = -1
    for i in range(1, len(X) + 1):
        op[i, 0] = 2
        cost[i, 0] = cost[i-1, 0] + costs[op[i, 0]]
    for j in range(1, len(Y) + 1):
        op[0, j] = 3
        cost[0, j] = cost[0, j-1] + costs[op[0, j]]

    # go through each word filling the table
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):

            if X[i-1] == Y[j-1]:
                op[i, j] = 0
            else:
                op[i, j] = 1
            cost[i, j] = cost[i-1, j-1] + costs[op[i, j]]

            if cost[i, j - 1] + 2 < cost[i, j]:
                op[i, j] = 3
                cost[i, j] = cost[i, j - 1] + costs[op[i, j]]

            if cost[i - 1, j] + 2 < cost[i, j]:
                op[i, j] = 2
                cost[i, j] = cost[i - 1, j] + costs[op[i, j]]

    return cost, op

def print_transformation_table(cost, op, X, Y, operations):
    '''
    A function to print the table for string transformation and operations
    :param cost: numpy 2d array, table of costs
    :param op: numpy 2d array of integers, the code of operation
    :param X: str, first word
    :param Y: str, second word
    :param operations: a list str, operations with index equal to code
    :return: returns nothing, just prints the table
    '''
    # print headers
    print('       |  j{a}'.format(a=''.join(['{0:^12d}'.format(i) for i in range(cost.shape[1])])))
    print('       |  yj                {a}'.format(a='           '.join([i for i in Y])))
    print('i  xi  |')

    # print first rows, since they're special
    print('0      |               ', end='')
    for j in range (1, cost.shape[1]):
        print('{0:^12d}'.format(cost[0,j]), end = '')
    print('\n       |               ', end='')
    for j in range (1, cost.shape[1]):
        print('{0:^12s}'.format(operations[op[0,j]] + ' ' + Y[j-1]), end = '')

    # print the table row by row
    for i in range(1, cost.shape[0]):
        print('\n{0:<3d}  {1} |   '.format(i, X[i-1]), end='')

        # column by column
        for j in range(cost.shape[1]):
            print('{0:^12d}'.format(cost[i, j]), end='')
        print('\n       |   ', end='')

        for j in range(cost.shape[1]):
            # choose correct output for operation
            if op[i, j] in [0, 3]:
                add = ' ' + Y[j-1]
            elif op[i, j] == 1:
                add = ' ' + X[i-1] +  ' by ' + Y[j-1]
            elif op[i,j] == 2:
                add = ' ' + X[i-1]
            print('{0:^12s}'.format(operations[op[i, j]] + add), end='')

def assemble_transformation(X, Y, op):
    '''
    Procedure that transforms one string to another
    :param X: first word
    :param Y: second word
    :param op: a 2d numpy array with steps to convert all the Xi to all the Yj
    :return: a current transformation state, in a form of a string
    '''

    # Find the lengths of words
    i, j = op.shape
    # Set current indeces to the last characters in strings
    i -= 1
    j -= 1

    # If the current table element is minus one, that means that we are trying to convert two transform one empty string to another
    if op[i,j] == -1:
        return ''

    # Based on the current table element, decide which operation was last
    # and recursively call the procedure accordingly

    # Last character was copied from X to Y, it was teh same
    elif op[i, j] == 0:
        return assemble_transformation(X, Y, op[:-1, :-1]) + X[i - 1]
    # One character replaced by another
    elif op[i, j] == 1:
        return assemble_transformation(X, Y, op[:-1, :-1]) + Y[j - 1]
    # Deleted character
    elif op[i, j] == 2:
        return assemble_transformation(X, Y, op[:-1, :])
    # Inserted character
    else:
        return assemble_transformation(X, Y, op[:, :-1])   + Y[j - 1]
