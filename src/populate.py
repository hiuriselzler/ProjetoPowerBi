import random
from faker import Faker
from sqlalchemy.orm import Session
from src.database import engine
from src.models import Usuario, Modalidade, RegistroTreinoForca, RegistroTreinoCardio
from src.generate_fact import gerar_treino_forca, gerar_treino_cardio

fake = Faker('pt_BR')



def criar_modalidades(session: Session):
    """Responsável única e exclusivamente por criar as modalidades."""
    nomes_modalidades = ['Musculação', 'Corrida', 'Ciclismo', 'Natação']
    modalidades = [Modalidade(nome_modalidade=nome) for nome in nomes_modalidades]
    session.add_all(modalidades)
    session.flush() # O flush envia pro banco para gerar os IDs, mas não encerra a transação

def criar_usuarios(session: Session, qtd_usuarios: int = 50) -> tuple:
    """Responsável por gerar a população e retornar os IDs criados."""
    hiuri = Usuario(nome="Hiuri Selzler", idade=25, peso=82.5)
    session.add(hiuri)
    
    usuarios_comuns = []
    for _ in range(qtd_usuarios):
        novo_usuario = Usuario(
            nome=fake.name(),
            idade=random.randint(18, 65),
            peso=round(random.uniform(50.0, 115.0), 1)
        )
        usuarios_comuns.append(novo_usuario)
        
    session.add_all(usuarios_comuns)
    session.flush() 

    # Separação de IDs para a lógica de treinos
    ids_comuns = [u.id for u in usuarios_comuns]
    todos_ids = [hiuri.id] + ids_comuns
    
    return hiuri.id, ids_comuns, todos_ids

def criar_treinos_forca(session: Session, id_hiuri: int, ids_comuns: list):
    treinos_forca = []
    
    # 150 treinos avançados (Seus)
    for _ in range(150):
        dados = gerar_treino_forca(id_usuario=id_hiuri, perfil_avancado=True)
        treinos_forca.append(RegistroTreinoForca(**dados))

    # 1000 treinos comuns (Outros)
    for _ in range(1000):
        id_random = random.choice(ids_comuns)
        dados = gerar_treino_forca(id_usuario=id_random, perfil_avancado=False)
        treinos_forca.append(RegistroTreinoForca(**dados))

    session.add_all(treinos_forca)

def criar_treinos_cardio(session: Session, todos_ids: list):
    """Responsável por gerar o volume de treinamento aeróbico."""
    treinos_cardio = []
    
    # 500 treinos de cardio distribuídos
    for _ in range(500):
        id_user_random = random.choice(todos_ids)
        id_mod_random = random.choice([2, 3, 4]) # 2=Corrida, 3=Ciclismo, 4=Natação
        dados = gerar_treino_cardio(id_usuario=id_user_random, id_modalidade=id_mod_random)
        treinos_cardio.append(RegistroTreinoCardio(**dados))

    session.add_all(treinos_cardio)


def popular_banco():
    """Gerencia a sessão e chama os especialistas na ordem correta."""
    with Session(engine) as session:
        try:
            print("Iniciando a esteira de dados (ETL)...")

            criar_modalidades(session)
            print(" ✓ Modalidades criadas.")

            id_hiuri, ids_comuns, todos_ids = criar_usuarios(session, qtd_usuarios=50)
            print(f" ✓ {len(todos_ids)} Usuários criados.")

            criar_treinos_forca(session, id_hiuri, ids_comuns)
            print(" ✓ Treinos de força gerados.")

            criar_treinos_cardio(session, todos_ids)
            print(" ✓ Treinos de cardio gerados.")

            # O Commit acontece uma única vez, no final. Se tudo deu certo, ele salva no MySQL.
            session.commit()
            print("\nSUCESSO: Transação finalizada. Banco alimentado e pronto para o Power BI!")
            
        except Exception as e:
            # Se QUALQUER função der erro, ele desfaz tudo e o banco fica intacto
            session.rollback()
            print(f"\n[ERRO CRÍTICO] A carga falhou e as alterações foram desfeitas. Detalhes: {e}")

if __name__ == "__main__":
    popular_banco()