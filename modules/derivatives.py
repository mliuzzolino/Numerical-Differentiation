from __future__ import division
import numpy as np



def function(x):
	y = np.tan(x)
	return y


def derivative_function(x, df_dx, xoi):
	return df_dx * (x - xoi) + function(xoi)
	

def derivative(x_, X, Y, deriv_number):
	
	# Check for DNE
	try:
		function(x_)
	except ZeroDivisionError:
		return False, 0


	# Find x_of_interest in X and note index
	for index, x in enumerate(X):
		if np.abs(x_ - x) < 1e-6:
			xi = X[index]
			f_xi = Y[index]

			# Check for index = 0
			if index == 0:
				method = 'forward'
				xi_1 = X[index+1]
				xi_2 = X[index+2]

				f_xi_1 = Y[index+1]
				f_xi_2 = Y[index+2]

				h = xi_1 - xi
				
			# Check if xi last element in X
			elif index == len(X) - 1:
				method = 'reverse'
				xi_neg1 = X[index-1]
				xi_neg2 = X[index-2]

				f_xi_neg1 = Y[index-1]
				f_xi_neg2 = Y[index-2]

				h = xi - xi_neg1

			# Otherwise, use centarl method
			else:
				method = 'central'
				xi_1 = X[index+1]
				xi_neg1 = X[index-1]
				f_xi_1 = Y[index+1]
				f_xi_neg1 = Y[index-1]

				h = xi_1 - xi
	
			break
	

	# Method not found due to x_ exceeding tolerance
	try:
		method
	except UnboundLocalError:
		return False, 1


	# First derivative
	if deriv_number == 'first':
		# 2 point forward
		if method == 'forward':
			ddx = (f_xi_1 - f_xi) / h

		# 2 point central
		elif method == 'central':
			ddx = (f_xi_1 - f_xi_neg1) / (2*h)

		# 2 point reverse
		elif method == 'reverse':
			ddx = (f_xi - f_xi_neg1) / h

			
	# Second derivative
	elif deriv_number == 'second':

		# 3 point forward
		if method == 'forward':
			ddx = (f_xi_2 - 2*f_xi_1 + f_xi) / (h**2)

		# 3 point central
		elif method == 'central':
			ddx = (f_xi_1 + f_xi_neg1 - 2*f_xi) / (h**2)

		elif method == 'reverse':
			ddx = (f_xi_neg2 - 2*f_xi_neg1 + f_xi) / (h**2)	

	
	# Check between prev and current for DNE
	try:
		f_xi_neg2 = Y[index-2]
		f_xi = Y[index]
		ddx_prev = (f_xi - f_xi_neg2) / (2*h)

		#print("ddx: {:.4f} \t ddx_prev: {:.4f} \t ddx*ddx_prev: {:.4f}".format(ddx, ddx_prev, ddx*ddx_prev))

		#print("x: {} \t ddx_prev: {} \t ddx: {}".format(xi, ddx_prev, ddx))
		if ddx*ddx_prev < -1e4:
			return False, 0

	except:
		pass

	# Check between current and next for DNE
	try:
		f_xi_2 = Y[index+2]
		ddx_prev = (f_xi_2 - f_xi) / (2*h)

		#print("ddx: {:.4f} \t ddx_prev: {:.4f} \t ddx*ddx_prev: {:.4f}".format(ddx, ddx_prev, ddx*ddx_prev))

		#print("x: {} \t ddx_prev: {} \t ddx: {}".format(xi, ddx_prev, ddx))
		if ddx*ddx_prev < -1e4:
			return False, 0

	except:
		pass

	return True, ddx

