#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>


int buscar_primer_maximo(int costo_ganancias[],size_t tam_productos,size_t cant_maxima){
	int pos_max = 0;
	for (int i = 0; i < tam_productos; ++i){
		if ( costo_ganancias[i] <= cant_maxima ){
			pos_max = i;
			break;
		}
	}
	return pos_max;
}

void imprimir_arreglo(int arreglo_pd[],size_t tam_productos){
	printf("[ ");
	for (int i = 0; i < tam_productos; ++i){
		if ( i < tam_productos-1){
			printf(" %d,",arreglo_pd[i]);
		} else {
			printf(" %d ",arreglo_pd[i] );
		}
	}
	printf("]\n");
}

int buscar_max_ganancia(int arreglo_pd[],size_t tam_arreglo){
	int pos_max = tam_arreglo-1;
	for (int i = tam_arreglo-2; i >= 0; --i){
		if( arreglo_pd[pos_max] < arreglo_pd[i] ){
			pos_max = i;
		}
	}
	return arreglo_pd[pos_max];
}


int obtener_mayor_ganancia(int costo_ganancias[],size_t tam_productos,int arreglo_pd[],size_t cant_maxima){
	int pos_pri_max = buscar_primer_maximo(costo_ganancias,tam_productos,cant_maxima);
	arreglo_pd[ pos_pri_max ] = costo_ganancias[pos_pri_max];
	arreglo_pd[ pos_pri_max + 1] = arreglo_pd[ pos_pri_max ] + costo_ganancias[ pos_pri_max + 1 ];
	for (int i = pos_pri_max + 2; i < tam_productos-1; ++i){
		if( arreglo_pd[i-1] > cant_maxima ){
			arreglo_pd[i-1] = costo_ganancias[pos_pri_max];
		}
		if ( arreglo_pd[ i - 1] + costo_ganancias[ i ] > cant_maxima  && arreglo_pd[i-2] + costo_ganancias[i] + costo_ganancias[i+1] <= cant_maxima ){
			// Entonces conviene poner una mejor oferta ya que a futura va a ser mejor.
			arreglo_pd[ i ] = arreglo_pd[ i - 2 ] + costo_ganancias[i];
			if ( arreglo_pd[i-1] + costo_ganancias[i+1] < cant_maxima && arreglo_pd[i-1] + costo_ganancias[i+1] > arreglo_pd[i] + arreglo_pd[i+1] ){
				arreglo_pd[i] = arreglo_pd[i-1];
			}
		} else{
			if ( arreglo_pd[ i - 1 ] + costo_ganancias[ i ] > cant_maxima){
				arreglo_pd[i] = arreglo_pd[i-1];
			}else{
				arreglo_pd[ i ] = arreglo_pd[ i - 1 ] + costo_ganancias[ i ];
			}
		}
	}
	if(arreglo_pd[tam_productos-2] + costo_ganancias[tam_productos-1] <= cant_maxima ){
		arreglo_pd[tam_productos-1] = arreglo_pd[tam_productos-2] + costo_ganancias[tam_productos-1];
	}
	imprimir_arreglo(arreglo_pd,tam_productos);
	int max_ganancia = buscar_max_ganancia(arreglo_pd,tam_productos);  
	return max_ganancia;
}

int main(){
	int costo_ganancias[] = {87,25,14,9,8,7,2,1}; // hay que ordenar el arreglo previamente de mayor a menor.
	// int costo_ganancias2[] = { 50,30,20,15,10 };
	size_t tam_productos = 8;
	// size_t tam_productos2 = 5;
	int arreglo_pd[] = { 0,0,0,0,0,0,0,0 };
	// int arreglo_pd2[] ={ 0,0,0,0,0 };
	size_t cant_maxima = 45;
	// size_t cant_maxima2 = 70;
	int max_ganancia = obtener_mayor_ganancia(costo_ganancias,tam_productos,arreglo_pd,cant_maxima);
	printf("La mayor ganancia es %d\n",max_ganancia );
	return 0;
} 