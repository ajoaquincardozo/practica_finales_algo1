# Se desea planear la ejecucion de n trabajos de duraciones conocidas t[1] .....t[n]
# para ejecutar en un unico procesador. Los trabajos pueden ser ejecutados en cualquiern orden, uno por vez
# Queremos encontrar el orden que minimiza el tiempo total ultilizado por todos los trabajos. EL tiempo utilizado
# por un trabajo es la suma del tiempo de espera de ese trabajo y el tiempo de ejecucion

#Me parecio que tenia ordenar por tamaño de duracion ya que en el ultimo caso no hay tiempo de espera para poder 
#realizar el siguiente trabajo sino más bien solo el tiempo de ejecucion.

def obtener_menor_tiempo_total(lista_trabajos,procesador):
	lista_trabajos = lista_trabajos.sort() #ordenar de menor a mayor en relacion a la duracion
	tiempo_de_espera = 0
	tiempo_de_ejecucion = 0
	for trabajo in lista_trabajos:
		procesador.realizar_trabajo(trabajo)
		tiempo_de_espera = procesador.obtener_tiempo_espera(trabajo)
		tiempo_de_ejecucion = procesador.obtener_tiempo_ejecucion(trabajo)

	tiempo_total = tiempo_de_espera + tiempo_de_ejecucion
	return tiempo_total

#Orden del algoritmo: tiempo ---> O(nlogn), ya que se tuve que ordenar previamente
#Orden del algoritmo: memoria---> O(1), ya que solo se use 2 variables para obtener el resultado

