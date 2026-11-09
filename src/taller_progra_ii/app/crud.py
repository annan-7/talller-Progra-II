from sqlalchemy import select
from sqlalchemy.orm import Session
from app.modelos import Sala, Reserva

def insertar_sala(db: Session, nombre: str, capacidad: int):
    if not nombre or not nombre.strip():
        return "Error: el nombre de la sala no puede estar vacío."
    if not isinstance(capacidad, int) or capacidad <= 0:
        return "Error: la capacidad debe ser un número mayor que cero."
    
    try:
        nueva_sala = Sala(nombre=nombre.strip(), capacidad=capacidad, disponible=True)
        db.add(nueva_sala)
        db.commit()
        db.refresh(nueva_sala)
        return f"Sala '{nueva_sala.nombre}' registrada con éxito (ID: {nueva_sala.id})."
    except Exception as e:
        db.rollback()
        return f"Error al insertar sala: {e}"

def consultar_salas(db: Session):
    consulta = select(Sala)
    salas = db.execute(consulta).scalars().all()

    if not salas:
        return "No hay salas registradas."
    
    resultado = "\n LISTADO DE SALAS \n"
    resultado += f"{'ID':<5} | {'Nombre':<20} | {'Capacidad':<10} | {'Disponible'}\n"
    resultado += "-" * 55 + "\n"
    for sala in salas:
        disp = "Sí" if sala.disponible else "No"
        resultado += f"{sala.id:<5} | {sala.nombre:<20} | {sala.capacidad:<10} | {disp}\n"
    return resultado

def registrar_reversa(db: Session, estudiante: str, sala_id: int, fecha: str):
    if not estudiante or not estudiante.strip():
        return "Error: el nombre del estudiante no puede estar vacío."
    if not fecha or len(fecha) != 10:
        return "Error: La fecha debe tener formato AAAA-MM-DD."

    try:
        sala = db.get(Sala, sala_id)
        if sala is None:
            return f"Error: no existe una sala con ID {sala_id}."
        if not sala.disponible:
            return f"Error: la sala '{sala.nombre}' no está disponible actualmente."

        # CORREGIDO: Todo normalizado a 'nueva_reserva'
        nueva_reserva = Reserva(
            estudiante=estudiante.strip(), 
            sala_id=sala_id, 
            fecha=fecha
        )
        db.add(nueva_reserva)
        
        # CORREGIDO: Cambiamos la disponibilidad en el objeto de la sala
        sala.disponible = False 
        
        db.commit()
        db.refresh(nueva_reserva)
        return f"Reserva realizada con éxito (ID Reserva: {nueva_reserva.id})."
    except Exception as e:
        db.rollback()
        return f"Error al registrar reserva: {e}"

def consultar_reservas(db: Session):
    try:
        consulta = select(Reserva)
        reservas = db.execute(consulta).scalars().all()
    
        if not reservas:
            return "No hay reservas en la base de datos."
        
        resultado = "\n LISTADO DE RESERVAS \n"
        resultado += f"{'ID':<5} | {'Estudiante':<20} | {'Sala':<20} | {'Fecha'}\n"
        resultado += "-" * 65 + "\n"
        for reserva in reservas:
            resultado += f"{reserva.id:<5} | {reserva.estudiante:<20} | {reserva.sala.nombre:<20} | {reserva.fecha}\n"
        return resultado
    except Exception as e:
        return f"Hubo un error al consultar reservas: {e}"

def cancelar_reversa(db: Session, id_reserva: int):
    try:
        # CORREGIDO: El parámetro se llama exactamente 'id_reserva'
        reserva = db.get(Reserva, id_reserva)
        if reserva is None:
            return f"Error: no existe una reserva con ID {id_reserva}."

        sala = reserva.sala  
        db.delete(reserva)
        
        if sala:
            sala.disponible = True 
            
        db.commit()
        return f"Reserva ID {id_reserva} cancelada. La sala '{sala.nombre}' vuelve a estar disponible."
    except Exception as e:
        db.rollback()
        return f"Error al cancelar la reserva: {e}"
