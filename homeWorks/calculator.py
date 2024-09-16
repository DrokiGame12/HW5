class Calculator:
	def __add__(self, *numbers: int) -> int:
		"""
		returns sum of any count of numbers
		:param numbers:
		:return summ:
		"""
		return sum(numbers)

	def __sub__(self, first_num: int, *numbers: int) -> int:
		"""
		return difference between the first number and any other numbers
		:param first_num:
		:param numbers:
		:return difference:
		"""
		return first_num - sum(numbers)

	def __mul__(self, *numbers: int) -> int:
		"""
		return mult of any count numbers
		:param numbers:
		:return mult:
		"""
		mult = 1
		for number in numbers:
			mult *= number
		return mult

	def __truediv__(self, first_number: int, second_number: int) -> int | float:
		"""
		return division of first and second numbers
		:param first_number:
		:param second_number:
		:return :
		"""
		return first_number / second_number

calc = Calculator()
print(calc.__add__(5, 5, 10))	# 20
print(calc.__sub__(20, 5, 5))	# 10
print(calc.__mul__(10, 2, 5))	# 100
print(calc.__truediv__(60, 2))	# 20