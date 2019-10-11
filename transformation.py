import numpy as np

def compute_transformation_table(X, Y, costs):

    # initialize table
    cost = np.zeros((len(X) + 1, len(Y) + 1))
    op   = np.zeros((len(X) + 1, len(Y) + 1))
    op = op.astype(int)
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

def print_transformation_table(l, X, Y):
    # print headers
    print('      |   j {a}'.format(a=' '.join([str(i) for i in range(l.shape[1])])))
    print('      |  yj   {a}'.format(a=' '.join([i for i in Y])))
    print('i  xi |l[i,j]')
    # print first row, since it's special
    print('0     |     {a}'.format(a=' '.join([str(int(i)) for i in l[0, ...]])))
    # print the table row by row
    for i in range(1, l.shape[0]):
        print('{i}  {b}  |     {a}'.format(a=' '.join([str(int(i)) for i in l[i, ...]]), i=i, b=X[i - 1]))

def assemble_transformation(X, Y, l):
    # Find the lengths of words
    i, j = l.shape
    i -= 1
    j -= 1
    # If the current table element is zero, that means that the longest common subsequence is an empty string
    if l[i,j] == 0:
        return ''
    # Else if the last characters are equal means that it is the last character in the LCS
    # Add it to the end and call the same procedure with words without last characters
    elif X[i-1] == Y[j-1]:
        return assemble_lcs(X, Y, l[:-1, :-1]) + X[i-1]
    # else, if the letters are not the same, call the procedure with one of the words reduced by one letter
    # whichever LCS is going to be longer
    elif l[i,j-1] < l[i-1, j]:
        return assemble_lcs(X, Y, l[:-1, :])
    else:
        return assemble_lcs(X, Y, l[:, :-1])

