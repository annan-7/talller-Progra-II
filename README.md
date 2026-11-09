
## Cómo ejecutarlo


Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

``` 
uv run src/taller_progra_ii/main.py

```
-----


## Pruebas


SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 1

--- Registrar Sala ---
Nombre de la sala: Sala A
Capacidad (número de cupos): 6
Sala 'Sala A' registrada con éxito (ID: 1).

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 1

--- Registrar Sala ---
Nombre de la sala: Sala B
Capacidad (número de cupos): 4
Sala 'Sala B' registrada con éxito (ID: 2).

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 3

--- Registrar Reserva ---
Nombre del estudiante: Ana
ID de la sala: 1
Fecha de reserva (AAAA-MM-DD): 2003-09-23
Reserva realizada con éxito (ID Reserva: 1).

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 3

--- Registrar Reserva ---
Nombre del estudiante: Pedro
ID de la sala: 1
Fecha de reserva (AAAA-MM-DD): 2004-08-23
Error: la sala 'Sala A' no está disponible actualmente.

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 4

 LISTADO DE RESERVAS 
ID    | Estudiante           | Sala  | Fecha
-----------------------------------------------------------------
1     | Ana                  | Sala A  | 2003-09-23

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 5

--- Cancelar Reserva ---
ID de la reserva a cancelar: 1
Reserva ID 1 cancelada. La sala 'Sala A' vuelve a estar disponible.

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 3

--- Registrar Reserva ---
Nombre del estudiante: Pedro
ID de la sala: 1
Fecha de reserva (AAAA-MM-DD): 2003-08-12
Reserva realizada con éxito (ID Reserva: 1).

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 4

 LISTADO DE RESERVAS 
ID    | Estudiante           | Sala  | Fecha
-----------------------------------------------------------------
1     | Pedro                | Sala A  | 2003-08-12

SISTEMA DE RESERVAS DE SALAS UCT
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
----------------------------------------
Seleccione una opción: 0
Saliendo del sistema...!

