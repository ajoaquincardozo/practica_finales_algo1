def obtener_valor_maximo_cable(n,array_de_precios):
	"""Obtiene una valor maximo de un cable """
	#la tabla de precios la represento en un array, ya que es mas representativo en este caso.

	divisible = es_divisible(n,array_de_precios) #devuelve si es posible dividirlo para maximar ganancias

	if not divisible:
		return array_de_precios[n]

	valor = buscar_mejor_combinacion(n,array_de_precios)
	return max(array_de_precios[n],valor)


def buscar_mejor_solucion(n,array_de_precios):
	"""Se considera que los primeros 3 valores son los casos base"""
	l_comb_posible = []
	for i in range( n, (n//2) -1 ):
		pos1 = n - i
		pos2 = n - valor1
		if pos1 + pos2 != n :
			continue 
		suma = array_de_precios[pos1] + array_de_precios[pos2]
		l_comb_posible.append(suma)

	return max(l_comb_posible)