#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>

//funcion auxiliar
bool es_heap_aux(int arreglo[],size_t tam_arreglo,size_t pos){
	size_t pos_hijo_izq = pos*2 + 1; 
	if (pos_hijo_izq > tam_arreglo-1) return true;
	if ( arreglo[pos] < arreglo[pos_hijo_izq] ) return false;

	bool exito1 = es_heap_aux(arreglo,tam_arreglo,pos_hijo_izq);
	if( !exito1 ) return false;

	size_t pos_hijo_der = pos*2 + 2; 
	if (pos_hijo_der > tam_arreglo-1) return true;
	if ( arreglo[pos] < arreglo[pos_hijo_der] ) return false;

	bool exito2 = es_heap_aux(arreglo,tam_arreglo,pos_hijo_der);
	if( !exito2 ) return false;

	return exito1 && exito2;
}



/*El arreglo necesariamemnte debe ser de numero enteros y se debe pasar el tam del arreglo*/
bool es_heap(int arreglo[],size_t tam_arreglo){
	size_t pos_inicial = 0; 
	return es_heap_aux(arreglo,tam_arreglo,pos_inicial);
}

int main(){
	int arreglo[] = {8,7,6,5,4,3,2,0,1};
	size_t tam_arreglo = 9 ;
	bool exito = es_heap(arreglo,tam_arreglo);
	if ( exito ){
		printf("El arreglo, en efecto, es un Heap\n");
	} else {
		printf("El arreglo no es un Heap\n");
	}
	return 0;
}