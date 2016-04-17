from __future__ import division
import sys
import modules.utilities as ut
import numpy as np
from modules.derivatives import *


def main(x_of_interest, X, Y, dne=False, display_plot=True):

	success, df_dx = derivative(x_of_interest, X, Y, 'first')

	if success:
		print("df/dx at x={:.3f}: {:.3f}".format(x_of_interest, df_dx))
		print("Tangent line equation: \t y(x) = {:0.3f}(x - {:.3f}) + {:.3f}".format(df_dx, x_of_interest, function(x_of_interest)))

	elif not success and df_dx == 0:
		ut.plot_dne(x_of_interest, X, Y)
		return

	elif not success and df_dx == 1:
		print("Error calculating derivative.")
		return


	# First derivative
	Y_1 = [derivative_function(x, df_dx, x_of_interest) for x in X]
	
	if dne:
		ut.find_dne(X, Y)
	
	if display_plot:
		ut.plot_it(x_of_interest, X, Y, Y_1)

	


if __name__ == '__main__':
	# Set bounds
	a = -5
	b = 5

	# Create X and Y for function
	X = np.arange(a, b, 5e-3)
	Y = [function(x) for x in X]

	# Check if command line input
	if len(sys.argv) > 1:
		x_of_interest = float(sys.argv[1])
	else:
		x_of_interest = raw_input("Find derivative of tan(x) at x = ")

	# Make sure correct input
	x_of_interest = ut.check_input(x_of_interest, a, b)

	# Check for plotting
	display_plot = ut.display_plot_prompt()
	dne = ut.display_dne_prompt()

	# Run program until user quits
	while True:
		main(x_of_interest, X, Y, dne, display_plot)
		x_of_interest = ut.get_input(a, b)
		display_plot = ut.display_plot_prompt()
		dne = ut.display_dne_prompt()

		




		
		


