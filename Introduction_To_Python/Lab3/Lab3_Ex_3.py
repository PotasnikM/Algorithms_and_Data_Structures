import numpy as np


# Defining a function sine
def func(x):
    return np.sin(x)


# Defining a function to approximately calculate definite integral
def monte_carlo(low_limit_of_integral, up_limit_of_integral, up_limit_of_y, low_limit_of_y, n):
    # under_plot will store hit score
    under_plot = 0
    for _ in range(n):
        # Randomly choosing x value from range
        x = np.random.uniform(low=low_limit_of_integral, high=up_limit_of_integral)
        # Randomly choosing y value from range
        y = np.random.uniform(low=low_limit_of_y, high=up_limit_of_y)
        # Checking if point (x,y) is under or on plot of sine
        if func(x) >= y:
            under_plot += 1
    # Calculating the approximate value of the integral
    return (up_limit_of_integral - low_limit_of_integral) * (up_limit_of_y - low_limit_of_y) * under_plot/n


if __name__ == '__main__':
    # Calculating the approximate value of the definite integral of sine within the limits <0,2>
    print('Definite integral of the sine within the limits <0,2> is approximately', monte_carlo(0, 2, 1, 0, 100000))
