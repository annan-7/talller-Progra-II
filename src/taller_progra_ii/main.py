from sqlalchemy.exc import IntegrityError

from app.base_datos import Base, engine, SessionLocal
from app import modelos, crud



def leer_int(mensaje: str) -> int | None:
   
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: debe ingresar un número entero válido.")
        return None


def menu():
    Base.metadata.create_all(bind=engine)

    while True:
        
        print("SISTEMA DE RESERVAS DE SALAS UCT")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")
        print("----------------------------------------")

        opcion = leer_int("Seleccione una opción: ")
        if opcion is None:
            continue

        with SessionLocal() as db:
            if opcion == 1:
                print("\n--- Registrar Sala ---")
                nombre = input("Nombre de la sala: ")
                capacidad = leer_int("Capacidad (número de cupos): ")
                if capacidad is not None:
                    print(crud.insertar_sala(db, nombre, capacidad))

            elif opcion == 2:
                print(crud.consultar_salas(db))

            elif opcion == 3:
                print("\n--- Registrar Reserva ---")
                estudiante = input("Nombre del estudiante: ")
                sala_id = leer_int("ID de la sala: ")
                if sala_id is not None:
                    fecha = input("Fecha de reserva (AAAA-MM-DD): ")
                    print(crud.registrar_reversa(db, estudiante, sala_id, fecha))

            elif opcion == 4:
                print(crud.consultar_reservas(db))

            elif opcion == 5:
                print("\n--- Cancelar Reserva ---")
                id_reserva = leer_int("ID de la reserva a cancelar: ")
                if id_reserva is not None:
                    print(crud.cancelar_reversa(db, id_reserva))

            elif opcion == 0:
                print("Saliendo del sistema...!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    menu()