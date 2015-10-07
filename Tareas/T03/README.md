#EL BATTLESHIP


### FUNCIONAMIENTO JUEGO
------------------------

Para iniciar el juego, se debe indicar la cantidad de jugadores e ingresar los nombres.
Si se elije [1] uno, se juega contra el computador.
Si no, se juega entre dos personas.

Para posicionar las piezas hay dos opciones: random y manual

El desarrollo del juego es bastante intuitivo. Van apareciendo en la consola las opciones a seguir. Si se quiere atacar
o revisar el radar. Luego, elegir un vehiculo del mapa y realizar la acción correspondiente.
Se puede realizar una acción por turno.

Se van alternando los jugadores hasta que uno haya perdido todos barcos y el puerto.

Cuando se piden coordenadas, se pide la esquina superior izquierda del elemento, ataque, o posicion.


### FUNCIONES
--------------------------

#### Interfaz
Principalmente es la encargada de recibir los inputs y ejecutar las funciones de las otras clases.

#### Mapa
*posicionar_random()*: posiciona los vehiculos correspondientes a un mapa de forma aleatoria

*ubicar_elemento(elemento, posicion)*: guarda un elemento en una nueva posicion en el mapa. Se registra en la lista de
vehiculos del mapa.

*borrar_elemento(elemento):* elimina un elemento del mapa

*mover_elemento(vehiculo):* muestra las opciones para mover un determinado vehiculo. Para las lanchas, pide una coordenada.
 Para el resto, una dirección en el teclado con S al centro.

*check_espacio(elemento, posicion):* revisa si la posicion es válida. Si está dentro del mapa y si tiene o no tiene
 elementos en ese espacio.

*get_elemento(coordenada, espacio=(1, 1)):* retorna una tupla con un elemento si tiene alguna parte dentro de la
coordenada ingresada y un booleano que indica si todas las coordenadas le dieron al vehiculo.


#### Jugadores
Se define un jugador y el computador que hereda de jugador.

**Jugador** tiene finalizar_turno(): que cierra(guarda) todos los mapas abiertos en el turno y pasa el turno para ver si
los ataques estarán disponibles la jugada siguiente.

**Computador** tiene las funciones para jugar solo. Decide entre explorar, atacar a cualquier parte o mover una pieza.
Si el turno anterior descubrió un vehículo, atacará en el lugar que se supo.


#### Vehiculos
Tienen un menú de opciones para cada uno según sus funcionalidades.
*atacado(ataque)*: le quita la resistencia correspondiente al ataque recibido (suma si es reparado por los ingenieros).
En el caso del explorador, se paraliza.


#### Ataques
Tienen dos funciones: usar() y actualizar estado(). La primera cambia el estado de uso a no disponible y la siguiente va contando
según los turnos pasados hasta que se cumple la espera correspondiente y vuelve a estar disponible el ataque.


#### Celdas
*coord_to_index(coordenada_ingresada)*: recibe una coordenada ingresada por el usario de la forma LetraNumero y retorna
una tupla con los índices correspondientes para el mapa.

*index_to_coord(posicion_tupla)*: hace el proceso contrario. Recibe indices y los transforma a coordenadas LetraNumero

*celdas_ocupadas(posicion, size)*: retorna una lista con las celdas ocupadas por un área dado por la posición y el
tamaño de ésta.





