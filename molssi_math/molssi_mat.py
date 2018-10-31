"""
molssi_mat.py
Sample repository for MolSSI Workshop

Misc. math functions
This is where you write a description
"""

def mean(num_list):
	"""
	Computes the mean of a list

	Parameters
	-------------
	num_lists: list
	   list to calculate mean of 

	Returns
	-------------
	mean: float
	   Mean of list of numbers
	"""
	# Check that input is a type list
	if not isinstance(num_list, list):
		raise TypeError('Input must be type list')

	# Check that list has length
	if len(num_list) == 0:
		raise ZeroDivisionError('Cannot calculate mean of empty list')

	# Check that values in list are numeric
	try:
		list_mean=sum(num_list)/len(num_list)
	except TypeError:
		raise TypeError('Values of list must be type int or float')

	return list_mean

