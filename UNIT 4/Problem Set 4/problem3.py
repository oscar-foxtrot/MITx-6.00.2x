# What is the R^2 value? (use 3 decimal places)
# ANSWER --> 0.005

# The code:
# Problem 3
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    pylab.figure(0)
    pylab.clf()
    pylab.title('Temperature throughout the recent years')
    pylab.plot(x, y, 'bo')
    pylab.xlabel('Year')
    pylab.ylabel('Temperature recorded')
    
    for model in models:
        yvals = []
        for elem in x:
            ycurr = 0
            for i in range(len(model)):
                 ycurr += model[-i - 1] * elem**i
            yvals += [ycurr]
        pylab.plot(x, yvals, label='degree ' + str(len(model - 1)) \
            + ' (R2 = ' + str(round(r_squared(y, yvals), 4)) + ')')
    pylab.legend(loc='lower left', fontsize = 'x-small')
