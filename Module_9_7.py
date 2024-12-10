def is_prime(func):
	def wrapper(*args, **kwargs):
		x = func(*args, **kwargs)
		if x <= 1:
			return f'Составное {x}'
		elif x == 2 or x == 3:
			return f'Простое {x}'
		elif x % 2 == 0 or x % 3 == 0:
			return f'Составное {x}'
		else:
			i = 5
			while i * i <= x:
				if x % i == 0 or x % (i + 2) == 0:
					return f'Составное {x}'
				i += 6
			return f'Простое {x}'
	return wrapper

@is_prime
def sum_three(a, b, c):
	return a + b + c

result = sum_three(2, 3, 6)
print(result)
