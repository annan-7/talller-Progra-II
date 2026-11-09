from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base_datos import Base

class Sala(Base):
    __tablename__ = 'salas'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int]
    disponible: Mapped[bool] = mapped_column(default=False)
    
    # Relación 1:N con Reserva
    reservas: Mapped[list["Reserva"]] = relationship("Reserva", back_populates="sala", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"Sala(id={self.id}, nombre='{self.nombre}', capacidad={self.capacidad}, disponible={self.disponible})"


class Reserva(Base):
    __tablename__ = 'reservas'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey('salas.id'), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)  # Formato AAAA-MM-DD
    
    # Relación N:1 con Sala
    sala: Mapped["Sala"] = relationship("Sala", back_populates="reservas")
    
    def __repr__(self) -> str:
        return f"Reserva(id={self.id}, estudiante='{self.estudiante}', sala_id={self.sala_id}, fecha='{self.fecha}')"

    



