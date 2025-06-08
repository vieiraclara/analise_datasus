# analise_datasus

# Análise de Dados da Qualidade da Água no Brasil (DATASUS)

## Sobre o Projeto

Este projeto realiza uma análise exploratória, de probabilidade e inferência estatística de dois conjuntos de dados públicos do **Sistema de Informação de Vigilância da Qualidade da Água para Consumo Humano (Sisagua)**, disponibilizados na plataforma OpenDataSUS.

O objetivo principal é investigar a qualidade da água e a infraestrutura de tratamento no Brasil, buscando responder a perguntas e testar hipóteses sobre a relação entre a presença de cianobactérias e a capacidade de tratamento de água nas diferentes regiões do país.

Este trabalho foi desenvolvido como projeto final da disciplina de **Estatística e Probabilidade** do curso de Análise e Desenvolvimento de Sistemas do IFSP.

## Datasets Utilizados

Foram utilizados dois conjuntos de dados do grupo **Vigilância e Meio Ambiente** do DATASUS. Para executar a análise, é necessário baixar os arquivos e colocá-los em uma pasta chamada `dados/` na raiz do projeto.

1.  **Vigilância de Cianobactérias e cianotoxinas**: Contém registros de análises de cianobactérias e cianotoxinas em amostras de água.
    * *Arquivo*: `vigilancia_cianobacterias_cianotoxinas.csv`
2.  **Cadastro de Tratamento de água**: Contém informações cadastrais sobre as Estações de Tratamento de Água (ETAs) e Unidades de Tratamento Simplificado (UTAs).
    * *Arquivo*: `cadastro_tratamento_de_agua.csv`

## Principais Análises Realizadas

A análise buscou responder a diversas perguntas, entre elas:
- Qual a distribuição geográfica das amostras de cianobactérias e dos cadastros de tratamento de água no Brasil?
- Como se comportam as distribuições de concentração de cianobactérias e da vazão de água tratada?
- Qual a probabilidade de certos eventos, como a detecção de cianobactérias em uma amostra?
- Existe uma relação estatisticamente significativa entre a média de detecção de cianobactérias e a vazão de água tratada em nível regional?

## Estrutura do Repositório

O projeto está organizado da seguinte forma:
```
/
|-- README.md                     # Este arquivo
|-- codigos/                      # Contém os scripts Python da análise
|   |-- data_cleaning.py          # Limpeza e pré-processamento dos dados
|   |-- statistical_analysis.py   # Análise de estatística descritiva
|   |-- probability_analysis.py   # Análise de probabilidade
|   |-- inference_analysis.py     # Análise de inferência e testes de hipótese
|   |-- relationship_analysis.py  # Análise do relacionamento entre os datasets
|   |-- visualization_analysis.py # Geração dos gráficos
|-- dados/                        # Pasta para os arquivos CSV (requer download)
|-- docs/                         # Documentação do projeto
|   |-- relatorio_final.pdf       # Relatório final completo com as análises
|-- graficos/                     # Gráficos gerados pelos scripts
```

## Tecnologias Utilizadas
* **Python 3**
* **Pandas** para manipulação e análise de dados.
* **NumPy** para operações numéricas.
* **Matplotlib** e **Seaborn** para visualização de dados.
* **SciPy** para cálculos estatísticos e de inferência.

## Como Executar o Projeto

1.  **Clone o repositório:**
2.  **Crie e ative um ambiente virtual (recomendado):**
3.  **Instale as dependências:** execute `pip install -r requirements.txt`.
4.  **Baixe os dados:** Faça o download dos arquivos CSV da plataforma OpenDataSUS e coloque-os na pasta `dados/`.
5.  **Execute os scripts de análise:** Os scripts podem ser executados individualmente a partir da raiz do projeto.
    # Exemplo de execução
    ```
    # Exemplo de execução
    python3 codigos/statistical_analysis.py
    python3 codigos/visualization_analysis.py
   
6.  **Consulte o relatório final:** Para uma visão completa dos resultados e conclusões, consulte o arquivo `docs/relatorio_final.pdf`.


