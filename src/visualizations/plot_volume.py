import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from src.database import engine 

def get_data_from_db():
    """Busca dados e calcula a tonelagem diretamente no MySQL"""
    query = """
    SELECT 
        u.nome, 
        (f.series * f.repeticoes * f.carga_kg) AS tonelagem, 
        f.rir 
    FROM registro_treino_forca f
    JOIN usuario u ON f.id_usuario = u.id
    WHERE f.series IS NOT NULL 
      AND f.repeticoes IS NOT NULL 
      AND f.carga_kg IS NOT NULL
    """
    df = pd.read_sql(query, engine)
    
    
    df['perfil'] = df['nome'].apply(
        lambda x: 'Avançado (Rotina)' if x == 'Hiuri Selzler' else 'Recreativo (Faker)'
    )
    
    return df

def generate_plot():
    try:
        df = get_data_from_db()
    except Exception as e:
        print(f"Falha na extração de dados: {e}")
        return

    # Estilização visual Dark Mode
    plt.style.use('dark_background')
    sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#111111", "figure.facecolor": "#111111", "grid.color": "#333333", "text.color": "white"})

    fig, ax = plt.subplots(figsize=(12, 7))
    
    sns.violinplot(data=df, x='perfil', y='tonelagem', palette=["#00ffcc", "#ff3366"], inner=None, alpha=0.3, ax=ax)
    sns.swarmplot(data=df, x='perfil', y='tonelagem', color="white", size=4, alpha=0.7, ax=ax)

    ax.set_title('Distribuição de Tonelagem: Real vs. Simulado', fontsize=16, fontweight='bold')
    
    os.makedirs('outputs', exist_ok=True)
    plt.tight_layout()
    plt.savefig('outputs/distribuicao_volume_db.png', dpi=300)
    print("Visualização gerada com sucesso: outputs/distribuicao_volume_db.png")

if __name__ == "__main__":
    generate_plot()