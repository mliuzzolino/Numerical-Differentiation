import sys
import matplotlib.pyplot as plt
from modules.derivatives import *


def plot_dne(x_of_interest, X, Y):
	print("df/dx at x={:.3f} Does Not Exist".format(x_of_interest))
	plt.scatter(X, Y, marker='.')
	x_asymptote = np.ones(50) * x_of_interest
	y_asymptote = np.linspace(min(Y), max(Y), 50)
	plt.plot(x_asymptote, y_asymptote, 'r--', linewidth=4)
	plt.axis([min(X)-2, max(X)+2, -10.0, 10])
	plt.show()


def find_dne(X, Y):
	DNE = []
	for index, x in enumerate(X):
		success, df_dx = derivative(x, X, Y, 'first')
		if not success and df_dx == 0:
			DNE.append(x)

	plt.scatter(X, Y, marker='.')
	
	for dne in DNE:
		x_asymptote = np.ones(50) * dne
		y_asymptote = np.linspace(min(Y), max(Y), 50)
		plt.plot(x_asymptote, y_asymptote, 'r--', linewidth=4)
		

	plt.axis([min(X)-2, max(X)+2, -10.0, 10])
	plt.show()


def plot_it(x_of_interest, X, Y, Y_1):
	plt.scatter(X, Y, marker='.')
	plt.plot(X, Y_1, 'r--')
	plt.plot(x_of_interest, function(x_of_interest), 'ro')
	plt.axis([min(X)-2, max(X)+2, -10.0, 10])
	plt.show()


def display_dne_prompt():
	dne_input = raw_input("Show asmyptotes where df/dx DNE (y/n)? ")
	if dne_input == 'y':
		dne = True
	else:
		dne = False
	return dne


def check_input(x_of_interest, a, b):
	while True:
		if x_of_interest == 'pi':
			x_of_interest = float("{:.3f}".format(np.pi))
			get_multiple = float(raw_input("Multiple of pi: "))
			x_of_interest *= get_multiple
			x_of_interest = float("{:.3f}".format(x_of_interest))

		elif float(x_of_interest) < a or float(x_of_interest) >= b:
			x_of_interest = raw_input("{} is invalid. Enter xoi in range [{}, {}): ".format(x_of_interest, a, b))

		else:
			x_of_interest = float(x_of_interest)
			break

	return x_of_interest


def display_plot_prompt():
	plot_input = raw_input("Show plot with tangent line of df/dx (y/n)? ")
	if plot_input == 'y':
		plot_it = True
	else:
		plot_it = False
	return plot_it


def get_input(a, b):
	user_input = raw_input("Enter new xoi, or q to quit: ")
	if user_input == 'q':
		sys.exit()
	elif 'pi' in user_input:
		x_of_interest = float("{:.2f}".format(np.pi))
		get_multiple = float(raw_input("Multiple of pi: "))
		x_of_interest *= get_multiple
		x_of_interest = float("{:.2f}".format(x_of_interest))
	else:
		x_of_interest = float(user_input)

	while True:
		if x_of_interest < a or x_of_interest >= b:
			x_of_interest = float(raw_input("{} is invalid. Enter xoi in range [{}, {}): ".format(x_of_interest, a, b)))
		else:
			break

	return x_of_interest