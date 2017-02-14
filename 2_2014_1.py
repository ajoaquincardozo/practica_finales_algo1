"""
Hacer una funcion que recibe dos listas de strings y comparen de la siguiente manera:
["A","B","C"] y ["C","B","C","A"] representan el mismo conjunto
["A","B","C"] y ["C","B","Z","A"] representan conjuntos diferentes
"""
def recorriendo_listas(lista_a_recorrer,lista_a_comp):
	"""doc"""
	for elem in lista_a_recorrer:
		if not elem in lista_a_comp:
			return False 
	return True

def comparacion_de_listas_de_strings(lista_cadena_1,lista_cadena_2):
	"""pre: dada das listas no vacias se procede a comparar los elementos que conforman cada lista
	post: devuelve un True en el caso de que sean los mismos y un False en el que sean diferentes"""
	misma_representacion = True
	misma_representacion = recorriendo_listas(lista_cadena_1,lista_cadena_2)
	misma_representacion = recorriendo_listas(lista_cadena_2,lista_cadena_1)
	return misma_representacion

lista_cadena_1 = ["A","B","C"]
lista_cadena_2 = ["C","B","C","A"]
print(comparacion_de_listas_de_strings(lista_cadena_1,lista_cadena_2))