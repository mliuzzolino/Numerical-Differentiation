# Numerical-Differentiation

## Introduction
This script will calculate the derivative of a desired function at a desired position, x. If the derivative does not exist at x, the script will catch it and return a DNE.

Additionally, two plots can be generated with this script. Given a function, e.g., y = tan(x), the script can generate a plot of the function along with the tangent line at point x. If the entered x produces a derivative of DNE, a thick, red line will be plotted vertically to indicate DNE.

The second plot that can be generated is one for all the x positions where the derivates of the given function over the given domain DNE. It will plot red horizontal lines at all of these positions.

The program runs until the user desires to quit. 

## Methods
Forward, reverse, and central finite difference methods are utilized to produce the derivative of a position, x, depending on where the x is within the domain set for the function. 

For example, if we are trying to find the derivative of x = 0 and our function y = x spans the domain [0, 5], then a forward finite different method must be utilized. Conversely, if we want the derivative at x = 5, we must use the reverse finite difference method. The reasoning for these choices should be obvious - to avoid index errors. E.g., if we want dy/dx at x = 0 in a domain of [0, 5], and we use reverse or central finite differences, then we need index -1 and 0 or -1 and 1, respectively. Although this is an "index error", since Python interprets x[-1] as the last element in x, the resulting derivative will be calculated incorrectly. Therefore, we must use a forward finite method in this case.

Due to a 2 point forward and reverse finite method coming with errors on the order of O(h), and the central method with O(h^2), we desire to use the central method when possible. Therefore, when dy/dx is being sought for x != index 0 or x != last_index of domain, we use the central finite difference method to calculate the derivative. 
