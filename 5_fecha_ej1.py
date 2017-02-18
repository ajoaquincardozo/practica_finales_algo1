"""Escribir una funcion que dadas dos lista K y S construya (y retorne) un diccionario D donde las claves
son los elementos de K  y sus significados son los elementos de S. Hay que prestar atencion a(al menos) los
siguientes casos de excepciones
(i): El tipo de algun elemento de K no puede ser clave // Nota: todo lo dinamico no puede ser clave
en este rango entran las listas, los tipo boolean tampoco puede ser clave
(ii) K se termina antes que S
(iii) S se termina antes que K
"""
def obtener_diccionario(lista_K,lista_S):
	ind_k,ind_s = 0,0
	excep_clave = [list,bool]
	dicc = {}
	while ind_k < len(lista_K) and ind_s < len(lista_S):
		if not type(lista_K[ind_k]) in excep_clave:
			clave = lista_K[ind_k]
			valor = lista_S[ind_s]
			dicc[clave] = valor
			ind_k +=1
			ind_s +=1
		else:
			ind_k +=1
	return dicc

#lista_K = [[1,2],True,2,"hola"]
#lista_S = [2,3,4,5]
lista_K = ["hola",3.5,(1,2)]
lista_S = [2]
print(obtener_diccionario(lista_K,lista_S))  
