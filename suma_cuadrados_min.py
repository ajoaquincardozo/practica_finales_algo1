from math import sqrt

CASOS_BASE = 4

def inicializar_casos_base(lista_pd):
	for i in range(CASOS_BASE):
		lista_pd[i] = i 


def buscar_mejor_solucion(num_corte):
	"""Se considera que los primeros 3 valores son los casos base"""
	div_aux = int( sqrt(num_corte) )
	num_aux = num_corte
	l_comb_posible = []
	l_aux = []
	for div in range( div_aux , 1 ,-1):
		cantidad = 0
		l = []
		while num_aux > 0 and True:
			if div * div <= num_aux:
				num_aux -= div * div
				l.append( div )
				cantidad += 1
			else:
				div -= 1
		l_aux.append(l)
		l_comb_posible.append(cantidad)		
		num_aux = num_corte

	# print("soy",num_corte, l_comb_posible," y la lista combinacion es ",l_aux)
	return min(l_comb_posible)	

def suma_de_cuadrados_min(num):
	"""Debe pasarse un numero entero,ya que no funcion con numeros negativos"""
	lista_pd = [0 for i in range(num+1)]
	inicializar_casos_base( lista_pd )
	if num == 0:
		return 0

	if num < 5:
		return lista_pd[num-1]
	
	for pos in range(CASOS_BASE,num+1): # va desde 3 hasta el numero en cuestion. 
		if int(sqrt(pos)) == sqrt(pos):
			lista_pd[pos] = 1
		else:
			lista_pd[pos] = min( lista_pd[pos-1] + 1 , buscar_mejor_solucion(pos) )
			
	# Para imprimir
	for i in range( len(lista_pd) ):
		print(i,end = "  ")
	print()
	for pos,elem in enumerate(lista_pd):
		if pos < 9:
			print(elem,end = "  ")
		else:
			print(elem,end = "   ")
	print()
	return lista_pd[num]

num = 25
suma_de_cuadrados_min(num)
# print(suma_de_cuadrados_min(num))
