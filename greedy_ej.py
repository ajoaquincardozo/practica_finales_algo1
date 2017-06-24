def obtener_mayor_cantidad_prog(lista_horarios):

	lista_horarios = lista_horarios.sort() # ordenado por el fin de cada una de < a >

	horario_act  = lista_horarios[0]
	lista_sol = [ horario_act ] #agarre el primer programa
	for prog in lista_horarios:
		if not horarios_colisionan(horario_act.inicio,horario_act.fin,prog.inicio,prog.fin):
			lista_sol.append(prog)
			horario_act = prog


def obtener_mayor_cantidad_prog(lista_horarios):

	lista_horarios = lista_horarios.sort() # ordenado por el tam de duracion de cada programa de < a >

	horario_act  = lista_horarios[0]
	lista_sol = [ horario_act ] #agarre el primer programa
	for prog in lista_horarios:
		if not horarios_colisionan(horario_act.inicio,horario_act.fin,prog.inicio,prog.fin) and horario_compatible(lista_sol,prog):
			
			lista_sol.append(prog)
			horario_act = prog

#horario_compatible se fija si los el horario si el programa se superpone con algo que ya tenias
#horarios_colisionan te devueleve si los horarios son compatibles,es decir, que no se superponen