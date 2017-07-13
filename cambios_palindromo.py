import sys

# Un cambio en una cadena lo representaremos como q = (i,j,ch) que significa cambiar el caracter i-esimo y el 
# j-esimo de la cadena por el caracter ch. Proponer un algoritmo eficiente O(M+N) que permita resolver
# Sea S una cadena de longitud N y q1,q2....qM cambios consecutivos. Informar después de cada cambio si la cadena
# resultante es palindromo o no. Por ejemplo: si S = "abbc" entonces después de (0,3,"x") tenemos "xbbx" y
# después de (2,3,"a") tenemos "xbaa".En ese caso informar 1 - True, 2 - False: Los cambios se hacen sobre la
# cadena resultante en el paso anterior.

#Las cadenas no son mutables. 

def realizar_cambios(cadena,cambios):
	"""Suponemos que como minimo se va a realizar un cambio"""
	pos_cambio = 0
	elem_cambio = cambios[ len(cambios) - 1]
	l_cad = [letra for letra in cadena]
	for pos_cad in range( len(cadena) ):
		if pos_cad == cambios[pos_cambio] and pos_cambio < len(cambios) - 1:
			l_cad[ pos_cad ] = elem_cambio 
			pos_cambio += 1
	return "".join(l_cad) 
#realizo el cambio en O(N+M) porque no estoy recorriendo del todo M ya que solo cambia cuando encuentra una
# letra, con lo cual se suma y no se multiplica a N.

def obtener_cambios(cambios):
	cambios_aux = cambios.split(" ")
	for pos in range( len(cambios_aux) ):
		if pos < len(cambios_aux) - 1:
			cambios_aux[pos] = int( cambios_aux[pos] )
	return tuple(cambios_aux)

def es_palindromo(cadena):
	cadena_aux = cadena.replace(" ","")
	fin = ( len(cadena_aux) // 2 ) - 1
	pos_aux = fin + 1
	palindromo = True 
	for pos in range(fin,-1,-1):
		if cadena_aux[pos] != cadena_aux[pos_aux]:
			palindromo = False
		pos_aux += 1
	return palindromo

def es_palindromo_con_cambios( cadena ):
	"""Realiza cambios y en base a eso te dice si hay palindromos o no"""
	cambios = sys.stdin.readline().rstrip("\n").replace(",","")
	while cambios:
		cambios = obtener	_cambios(cambios)
		cadena = realizar_cambios(cadena,cambios)
		print(cadena," Es palindromo: ",es_palindromo( cadena ) )
		print("Desea continuar: [S/N]",end = " ")
		cambios = sys.stdin.readline().rstrip("\n").replace(",","")
		if cambios.upper() == "N":
			break
		print()
es_palindromo_con_cambios("abbc")