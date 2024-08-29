import sys

def distribute(y_axis, x_axis, arr2D, figures, no_stack):
    # index testing on boundaries
    if x_axis >= -1 and y_axis == figures:
        return 1

    # objects/balls/robots validation
    if y_axis > figures:
        return 0

    # verify the boundary
    if x_axis < 0:
        return 0

    # optimisation by reusing the calcualted values
    if arr2D[y_axis][x_axis] != -1:
        return arr2D[y_axis][x_axis]

    summation = 0

    for i in range(0, no_stack + 1):
        summation += distribute(y_axis + i, x_axis - 1, arr2D, figures, no_stack)

    arr2D[y_axis][x_axis] = summation
    return arr2D[y_axis][x_axis]



#calling block
with open(sys.argv[0], 'r') as rows:
    for line in rows:
        arr2D = [[-1 for i in range(0, 1004)] for j in range(0, 1004)]
        # no_stack contains the limit upto which robots can pile up
        figures, n, no_stack = map(int, line.split(","))
        print('({0},{1},{2})={3}'.format(figures, n, no_stack, distribute(0, n - 1, arr2D, figures, no_stack)))

