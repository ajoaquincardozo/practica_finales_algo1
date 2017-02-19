def max_comun_divisor(num,dem):
	m_c_d = 0
	if (num == 0 and dem == 0) or num == 0:
		return m_c_d 
	elif dem == 0:
		raise ValueError("Es division por cero con lo cual es indefinido")
	if num > dem :
		min_num = dem
	else:
		min_num = num
	for i in range(1,min_num+1):
		if  num % i == 0 and dem % i == 0 :
			m_c_d = i 
	return m_c_d

#print(max_comun_divisor(18,27))

class NumeroRacional:
	"""docstring for """
	def __init__(self,num,dem):
		try:
			if type(num) is int and (type(dem) is int and dem != 0):
				self.num = num 
				self.dem = dem
		except ValueError:
			raise ValueError("Los parametros que ingreso no son un numero racional")

	def suma(self,otro):
		if abs(self.dem) != abs(otro.num): 
			return "{}/{}".format((otro.dem *self.num + self.dem * otro.num),(self.dem * otro.dem))

	def multiplica(self,otro):
		return "{}/{}".format((self.num * otro.num),(self.dem * otro.dem))

	def simplifica(self):
		m_c_divisor = max_comun_divisor(self.num,self.dem)
		return "{}/{}".format(int((self.num / m_c_divisor)),int((self.dem / m_c_divisor)))


	def __float__(self):
		return self.num / self.dem 
	
	def __str__(self):
		return "{}/{}".format(self.num,self.dem)

def main():
	num_rac_1 = NumeroRacional(2,4)
	num_rac_2 = NumeroRacional(16,8)
	print(num_rac_1.suma(num_rac_2))
	print(num_rac_1.multiplica(num_rac_2))
	print(num_rac_1.simplifica())
	print(num_rac_2.simplifica())
	print(str(num_rac_1))
	print(float(num_rac_1))
main()
