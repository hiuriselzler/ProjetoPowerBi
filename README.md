O projeto Sanguine Performance estabelece uma infraestrutura completa para o monitoramento de performance física ao integrar a coleta de dados via Python, gerenciando dependências através do Poetry e persistindo informações em um banco de dados relacional MySQL 8.0 por meio do ORM SQLAlchemy.


A arquitetura do backend foi construída sob os pilares do Clean Code e do Princípio da Responsabilidade Única, empregando scripts de povoamento que utilizam transações atômicas com gestão de erros para assegurar a integridade dos dados durante a aplicação de regras de negócio complexas.


Estas regras diferenciam o perfil de atleta avançado(no caso a função foi criada com base na minha rotina😁), que opera em microciclos de oito dias com intensidade máxima e repetições limitadas, de uma população recreativa simulada pela biblioteca Faker para validação estatística. 

Na camada de Business Intelligence, o Power BI realiza o processo de extração e transformação via Power Query, onde a tipagem rigorosa e a imputação de valores nulos em métricas de telemetria garantem a confiabilidade da análise. A modelagem de dados segue o padrão de esquema estrela com relacionamentos otimizados entre dimensões e tabelas fato, permitindo que fórmulas DAX sofisticadas calculem dinamicamente o volume total de tonelagem, o ritmo médio de cardio e a intensidade média de esforço.

O ecossistema culmina em um dashboard analítico equipado com filtros cruzados e visualizações de tendência que permitem a consulta granular de recordes pessoais e evolução de carga, transformando dados brutos do MySQL em insights estratégicos de performance através de uma conexão de alta performance via driver ODBC.

obs: a taxa de evolução será insignificante devido a aleatoriedade proposta na criação dos treinos
