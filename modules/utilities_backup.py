from modules.derivatives import *
import matplotlib.pyplot as plt



def plot(x, y):
	plt.plot(x, y)
	plt.axis([min(x)-2, max(x)+2, min(y)-2, max(y)+2])
	plt.show()


def function(x):
	y = x**2
	return y


def known_derivative(x, first=True):
	if first:
		df_dx = 2 * x
	else:
		df_dx = 2
	return df_dx


def derivative_function(x, df_dx, number, xoi):
	if number == 'first':
		f_1 = df_dx * (x - xoi) + function(xoi)
	elif number == 'second':
		f_1 = df_dx
	return f_1


def relative_error(df_dx, x_of_interest, first=True):
	known = known_derivative(x_of_interest, first)
	rel_error = np.abs( (df_dx - known) / known )
	return rel_error


def print_info(X, Y, x_of_interest):
	print("First Derivative: Forward")
	df_dx = derivative(x_of_interest, X, Y, 'first', 'forward')
	print("df/dx = {}".format(df_dx))
	rel_error = relative_error(df_dx, x_of_interest)
	print("Error: {}".format(rel_error))
	print

	print("First Derivative: Central")
	df_dx = derivative(x_of_interest, X, Y, 'first', 'central')
	print("df/dx = {}".format(df_dx))
	rel_error = relative_error(df_dx, x_of_interest)
	print("Error: {}".format(rel_error))
	print
	
	print("Second Derivative: Forward")
	df_dx = derivative(x_of_interest, X, Y, 'second', 'forward')
	print("df/dx = {}".format(df_dx))
	rel_error = relative_error(df_dx, x_of_interest, False)
	print("Error: {}".format(rel_error))
	print

	print("Second Derivative: Central")
	df_dx = derivative(x_of_interest, X, Y, 'second', 'central')
	print("df/dx = {}".format(df_dx))
	rel_error = relative_error(df_dx, x_of_interest, False)
	print("Error: {}".format(rel_error))
	print