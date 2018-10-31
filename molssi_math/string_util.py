"""
string_util.py
Sample repository for MolSSI Workshop at SERMACS

Misc. string processing funtions
"""

def title_case(sentence):
	"""
	Convert string to title case

	Parameters
	------------
	sentence: string
	  Sentence to be converted to title case

	Returns:
	------------
	ret: string
	  Input string in title case

	Example
	-----------
	>>>> title_case('ThIs iS a StrIng tO be ConVerted')
	  This Is A String To Be Converted
	"""
	if not isinstance(sentence, str):
	   raise TypeError('Input must be type string')
	
	if len(sentence)==0:
	   raise IndexError('Cannot apply title function to empty string.')
	
	sentence.lower()
	small=sentence.split()
	small = [word.capitalize() for word in small]

	return ' '.join(small)
