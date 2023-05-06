# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    mean = 0
    for elem in y:
        mean += elem
    mean /= len(y)
    
    err = 0
    meanerr = 0
    for i in range(len(y)):
        err += (y[i] - estimated[i])**2
        meanerr += (y[i] - mean)**2
    
    return 1 - err / meanerr
