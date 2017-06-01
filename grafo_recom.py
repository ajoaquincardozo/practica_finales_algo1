def recomendaciones_para_v(matriz,pos_vertice):
	lista_de_recom = []
	for pos in range(len(matriz[pos_vertice]) ):
		if matriz[pos_vertice][pos] == 0 and matriz[pos][pos_vertice] == 0:
			for i in range(pos,len(matriz[pos_vertice]) ):
				if matriz[pos_vertice][i] == 1 and matriz[i][pos] == 1 :
						lista_de_recom.append(i)
	return lista_de_recom
