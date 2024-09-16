class Bank:
	def __init__(self, name, balance):
		self._name = name
		self._balance = balance
	def moneyX(self):
		self._balance += int(input('Введите сумму которую хотите положить: '))

	def _kill(self):
		money = int(input('Введите сумму которую хотите взять: '))
		if money <= self._balance:
			self._balance -= money
		else:
			print(f'У вас нет столько денег.\nУ вас на балансе {self._balance} денег.')
	def __jackpot(self):
		self._balance *= 10

	def _copy(self, target):
		self._balance += target._balance

akel = Bank('Akel', 10)
akel._Bank__jackpot()
beka = Bank('Bekbolot', 100)
beka._copy(akel)
print(beka._balance)