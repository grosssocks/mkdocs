# project/calculator.py

"""
This module discusses several arithmetic calculation techniques.

It allows the user to make mathematical calulations.

Examples:
	>>> from project import calculator
	>>> calculator.add(2, 4)
	6.0
	>>> calculator.multiply(2.0, 4.0)
	8.0
	>>> from project.calculator import divide
	>>> divide(4.0, 2)
	2.0

This module contains the following mathematical functions:
- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""
# importing Union from the built-in typing module
from typing import Union 
 
def add(a:Union[float, int], b: Union[float, int]) -> float:	
		"""Compute and return the sum of two numbers.

    Examples:
      >>> add(4.0, 2.0)
      6.0
    	>>> add(4, 2)
      6.0
    Args:
      a : A number representing the first addend in the addition.
      b : A number representing the second addend in the addition.
    Returns:
      A number representing the arithmetic sum of `a` and `b`.
    """
		return float(a + b)

def subtract(a:Union[float, int], b: Union[float, int]) -> float:
		"""Compute and return the difference of two numbers.

		Examples:
			>>> subtract(4.0, 2.0)
			2.0
			>>> subtract(4, 2)
			2.0
		Args: 
			a : A number representing the first subtracting integer in the substaction.
			b : A number representing the second subtracting integer in the subtraction.
		Returns:
			A number representing the arithmetic difference of 'a' and 'b'.
		"""
		return float (a - b)

def multiply(a:Union[float, int], b: Union[float, int]) -> float:
		"""Compute and return the multiplication of two numbers.

		Examples:
			>>> multiply(4.0, 2.0)
			8.0
			>>> multiply(4, 2)
			8.0
		Args: 
			a : A number representing the first multiplying integer in the multiplication.
			b : A number representing the second multiplying integer in the multiplication.
		Returns:
	  	A number representing the product of 'a' and 'b'.
	"""	
		return float (a * b)

def divide(a:Union[float, int], b: Union[float, int]) -> float:
	"""Compute and return the quotient of two numbers.

		Examples:
			>>> divide(4.0, 2.0)
			2.0
			>>> divide(4, 2)
			2.0
			>>> divide(4, 0)
			Traceback (most recent call last):
			...
			ZeroDivisionError: division by zero is invalid
		Args: 
			a : A number representing the dividend in the division.
			b : A number representing the divisor in the division.
		Returns:
			A number representing the quotient of 'a' and 'b'.
		Raises:
			ZeroDivisionError: An error occurs when divisor is '0'.
		"""
	if b == 0:
		raise ZeroDivisionError("division by zero is invalid")
	return float(a / b)


