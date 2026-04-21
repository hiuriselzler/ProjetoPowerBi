from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100)) # Permitido ser nulo (erro de cadastro)
    idade = Column(Integer)
    peso = Column(Float)

    forca = relationship("RegistroTreinoForca", back_populates="usuario")
    cardio = relationship("RegistroTreinoCardio", back_populates="usuario")

class Modalidade(Base):
    __tablename__ = 'modalidade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_modalidade = Column(String(50)) # Permitido ser nulo ou ter erros de digitação

    cardios = relationship("RegistroTreinoCardio", back_populates="modalidade")

class RegistroTreinoForca(Base):
    __tablename__ = 'registro_treino_forca'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False) # BLINDADO: Chave Estrangeira
    data = Column(Date, nullable=False) # BLINDADO: Sem data, não há análise de tempo
    exercicio = Column(String(100)) # Permitido ser nulo
    series = Column(Integer) # Permitido ser nulo
    repeticoes = Column(Integer)
    carga_kg = Column(Float)
    rir = Column(Integer)

    usuario = relationship("Usuario", back_populates="forca")

class RegistroTreinoCardio(Base):
    __tablename__ = 'registro_treino_cardio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False) # BLINDADO
    id_modalidade = Column(Integer, ForeignKey('modalidade.id'), nullable=False) # BLINDADO
    data = Column(Date, nullable=False) # BLINDADO
    distancia_km = Column(Float) # Permitido ser nulo (falha de GPS)
    tempo_minutos = Column(Float) # Permitido ser nulo (falha de cronômetro)
    pace_medio = Column(String(10))
    bpm_medio = Column(Integer)

    usuario = relationship("Usuario", back_populates="cardio")
    modalidade = relationship("Modalidade", back_populates="cardios")