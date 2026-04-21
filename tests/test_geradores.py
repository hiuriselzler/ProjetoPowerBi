from src.generate_fact import gerar_treino_cardio , gerar_treino_forca



def test_deve_injetar_5_porcento_de_valores_nulos_no_bpm():
    amostra = 1000
    nulos_gerados = 0
    
    for _ in range(amostra):
        # A função vai retornar um dicionário com os dados do treino
        treino = gerar_treino_cardio() 
        
        # Verificamos se o sensor "falhou" (veio None)
        if treino.get('bpm_medio') is None:
            nulos_gerados += 1
            
    # Calculamos a taxa real de falhas gerada
    taxa_erro = nulos_gerados / amostra
    
    # Afirmamos que a taxa de erro deve estar entre 4% e 6% 
    # (damos uma margem de 1% para a aleatoriedade estatística)
    assert 0.04 <= taxa_erro <= 0.06

ID_HIURI = 1

def test_deve_aplicar_restricoes_para_perfil_avancado():
    treino = gerar_treino_forca(id_usuario=ID_HIURI, perfil_avancado=True)
    
    # Assert: Treino avançado sempre tem RIR 0 e repetições controladas
    assert treino['rir'] == 0
    assert 4 <= treino['repeticoes'] <= 10

def test_deve_permitir_variacao_para_usuarios_comuns():
    treino = gerar_treino_forca(id_usuario=2, perfil_avancado=False)
    
    # Assert: Usuários comuns podem ter repetições em reserva maiores que 0
    assert treino['rir'] >= 0

def test_deve_injetar_valores_nulos_nas_series_de_forca():
    amostra = 1000
    nulos = sum(1 for _ in range(amostra) if gerar_treino_forca().get('series') is None)
    taxa = nulos / amostra
    
    # Assert: ~5% dos treinos de força devem vir sem a contagem de séries preenchida
    assert 0.04 <= taxa <= 0.06