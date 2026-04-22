O projeto Sanguine Performance estabelece uma infraestrutura completa para o monitoramento de performance física ao integrar a coleta de dados via Python, gerenciando dependências através do Poetry e persistindo informações em um banco de dados relacional MySQL 8.0 por meio do ORM SQLAlchemy.

Atenção: No desenvolvimento deste pipeline, o conceito de TDD foi aplicado na técnica de Failure Injection (Injeção de Falhas). Em vez de escrever um código que gera dados perfeitos, o "teste" aqui era verificar se o dashboard de Business Intelligence (BI) seria capaz de manter a integridade analítica diante de dados corrompidos. O ciclo "Red-Green-Refactor" foi transposto para o fluxo de dados: gerei o erro no Python (Red), identificamos a quebra no Power BI e apliquei a limpeza no Power Query (Green).

Embora o processo de tratamento de dados e ETL seja comumente realizado em ambiente Python através da biblioteca Pandas, que oferece alto controle programático sobre a higienização das informações, este projeto adotou deliberadamente a execução dessas transformações dentro do Power Query do Power BI. Essa decisão estratégica visou testar e demonstrar proficiência técnica nas ferramentas nativas de Business Intelligence, validando competências em limpeza de dados, gestão de valores nulos e tipagem de colunas diretamente nos dados da visualização.

A arquitetura do backend foi construída sob os pilares do Clean Code e do Princípio da Responsabilidade Única, empregando scripts de povoamento que utilizam transações atômicas com gestão de erros para assegurar a integridade dos dados durante a aplicação de regras de negócio complexas.


Estas regras diferenciam o perfil de atleta avançado(no caso a função foi criada com base na minha rotina😁), que opera em microciclos de oito dias com intensidade máxima e repetições limitadas, de uma população recreativa simulada pela biblioteca Faker para validação estatística. 

Na camada de Business Intelligence, o Power BI realiza o processo de extração e transformação via Power Query, onde a tipagem rigorosa e a imputação de valores nulos em métricas de telemetria garantem a confiabilidade da análise. A modelagem de dados segue o padrão de esquema estrela com relacionamentos otimizados entre dimensões e tabelas fato, permitindo que fórmulas DAX sofisticadas calculem dinamicamente o volume total de tonelagem, o ritmo médio de cardio e a intensidade média de esforço.

O ecossistema culmina em um dashboard analítico equipado com filtros cruzados e visualizações de tendência que permitem a consulta granular de recordes pessoais e evolução de carga, transformando dados brutos do MySQL em insights estratégicos de performance através de uma conexão de alta performance via driver ODBC.

obs: a taxa de evolução será insignificante devido a aleatoriedade proposta na criação dos treinos.

