import random
from datetime import date
from faker import Faker

# Inicializa o gerador de dados falsos com localização brasileira
fake = Faker('pt_BR')

def calcular_pace(distancia_km: float, tempo_minutos: float) -> str:
    if distancia_km <= 0 or tempo_minutos <= 0:
        return None
        
    pace_decimal = tempo_minutos / distancia_km
    minutos = int(pace_decimal)
    segundos = int((pace_decimal - minutos) * 60)
    
    return f"{minutos:02d}:{segundos:02d}"

def gerar_treino_cardio(id_usuario: int = 1, id_modalidade: int = 1) -> dict:
    distancia_km = round(random.uniform(3.0, 15.0), 2)
    
    # O tempo é calculado com base na distância para não gerar bizarrices 
    # (ex: 15km em 10 minutos). Pace simulado entre 4.5 e 7.5 min/km.
    fator_pace = random.uniform(4.5, 7.5)
    tempo_minutos = round(distancia_km * fator_pace, 2)
    
    # 2. Injeção de Caos Controlado (TDD 5% de falha)
    # random.random() gera um float de 0.000 a 1.000. 
    # Se o valor for menor que 0.05, simulamos a queda do sensor.
    if random.random() < 0.05:
        bpm = None # Sensor falhou
    else:
        # Sensor funcionou, gera batimento cardíaco normal para a atividade
        bpm = random.randint(130, 185)
        
    # 3. Montagem da linha de dados (Dicionário)
    treino = {
        "id_usuario": id_usuario,
        "id_modalidade": id_modalidade,
        "data": fake.date_between(start_date='-1y', end_date='today'),
        "distancia_km": distancia_km,
        "tempo_minutos": tempo_minutos,
        "pace_medio": calcular_pace(distancia_km, tempo_minutos),
        "bpm_medio": bpm
    }
    
    return treino

def gerar_treino_forca(id_usuario: int = 1, perfil_avancado: bool = False) -> dict:
    exercicios = ['Agachamento', 'Supino', 'Levantamento Terra', 'Remada Curvada', 'Desenvolvimento']
    
    if perfil_avancado:
        # Microciclo Avançado: Volume estrito, Falha mecânica
        series = random.randint(3, 4)
        repeticoes = random.randint(4, 10)
        rir = 0
        carga_kg = round(random.uniform(80.0, 160.0), 1)
    else:
        # Usuário Comum: Treino hipertrófico padrão, margem de segurança
        series = random.randint(3, 5)
        repeticoes = random.randint(8, 15)
        rir = random.randint(0, 3)
        carga_kg = round(random.uniform(20.0, 90.0), 1)

    # Injeção de Caos (5% de chance do usuário esquecer de registrar as séries)
    if random.random() < 0.05:
        series = None

    return {
        "id_usuario": id_usuario,
        "data": fake.date_between(start_date='-1y', end_date='today'),
        "exercicio": random.choice(exercicios),
        "series": series,
        "repeticoes": repeticoes,
        "carga_kg": carga_kg,
        "rir": rir
    }