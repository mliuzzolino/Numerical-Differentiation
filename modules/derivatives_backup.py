from __future__ import division
import numpy as np


def derivative(x_, X, Y, deriv_number, method):
	
	for index, x in enumerate(X):
		if np.abs(x_ - x) < 1e-6:
			
			xi_neg1 	= X[index-1]
			xi 			= X[index]

			f_xi_neg1 	= Y[index-1]
			f_xi 		= Y[index]
			
			
			try:
				xi_1 		= X[index+1]
				xi_2 		= X[index+2]
				f_xi_1 		= Y[index+1]
				f_xi_2		= Y[index+2]
			except:
				return None
			break

	h = xi_1 - xi

	if deriv_number == 'first':
		if method == 'forward':
			ddx = (f_xi_1 - f_xi) / h
		elif method == 'central':
			ddx = (f_xi_1 - f_xi_neg1) / (2*h)
			
	elif deriv_number == 'second':
		if method == 'forward':
			ddx = (f_xi_2 - 2*f_xi_1 + f_xi) / (h**2)
		elif method == 'central':
			ddx = (f_xi_1 + f_xi_neg1 - 2*f_xi) / (h**2)

	return ddx

