# Manipulação de Arquivos CSV

Bem-vindo(a) ao projeto de **Manipulçaõ de Arquivos CSV** do conjunto de projetos em Python voltados para a Engenharia de Dados. Neste projeto, foi desenvolvido um programa que lê dados de um arquivo CSV, processa esses dados e realiza operações de filtragem com base em critérios específicos, salvando os resultados em um novo arquivo CSV. O objetivo é praticar manipulação de arquivos, processamento de dados e implementação de filtros eficientes em Python.

## Sumário

- [Manipulação de Arquivos CSV](#manipulação-de-arquivos-csv)
  - [Sumário](#sumário)
  - [Descrição do Projeto](#descrição-do-projeto)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Configuração do Ambiente](#configuração-do-ambiente)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
      - [1. Clonando o Repositório](#1-clonando-o-repositório)
      - [2. Configurando o Ambiente Python](#2-configurando-o-ambiente-python)
      - [3. Instalando Dependências com o Poetry](#3-instalando-dependências-com-o-poetry)
  - [Como Executar o Programa](#como-executar-o-programa)
    - [Observações](#observações)
  - [Contribuindo](#contribuindo)
    - [Passos para Contribuir](#passos-para-contribuir)

## Descrição do Projeto

Este projeto desenvolve um programa em Python que:

1. **Gera um arquivo CSV com dados fictícios**: Utiliza o script `gerar_csv.py` para criar um arquivo CSV com 100.000 linhas contendo informações sobre produtos eletrônicos.
2. **Lê dados de um arquivo CSV**: A função `ler_arquivo_csv` no `utils.py` lê os dados do arquivo CSV gerado.
3. **Processa os dados**: A função `tratar_datas_csv` converte as datas de adição dos produtos do formato "YYYY-MM-DD" para "DD/MM/YYYY".
4. **Filtra os dados**: A função `filtrar_produtos_pelo_preco` filtra os produtos que possuem preço acima de um determinado valor.
5. **Salva os resultados em um novo arquivo CSV**: A função `salvar_como_csv` escreve os dados filtrados em um novo arquivo CSV na pasta `data/processed/`.

**Objetivos de Aprendizado**:

- Manipulação de arquivos CSV em Python usando a biblioteca `csv`.
- Tipagem de variáveis utilizando a biblioteca `typing`.
- Processamento e transformação de dados com a biblioteca `datetime`.
- Implementação de filtros eficientes para grandes conjuntos de dados.
- Estruturação e organização de projetos em Python.

## Estrutura do Projeto

```
manipulacao_csv/
│
├── data/
│   ├── processed/
│   │   └── produtos_filtrados.csv
│   └── raw/
│       └── produtos_100k.csv
├── src/
│   ├── __init__.py
│   ├── gerar_csv.py
│   ├── main.py
│   └── utils.py
├── notebooks/
│   └── exploracao_dados.ipynb
├── .python-version
├── poetry.lock
├── pyproject.toml
└── README.md
```

- **data/**: Diretório que contém os dados brutos e processados.
  - **raw/**: Contém o arquivo de entrada `produtos_100k.csv` gerado pelo script `gerar_csv.py`.
  - **processed/**: Onde será salvo o arquivo de saída `produtos_filtrados.csv` após o processamento.
- **src/**: Diretório que contém os arquivos python (Arquivo de funções para manipulação de `csv`, arquivo para geração do arquivo `csv` utilizado e o arquivo principal).
  - **gerar_csv.py**: Script responsável por gerar o arquivo CSV com dados fictícios.
  - **main.py**: Arquivo principal que executa o fluxo de leitura, processamento, filtragem e escrita dos dados.
  - **utils.py**: Arquivo que contém as funções utilitárias para manipulação dos dados CSV.
-  **notebooks/**: Diretório que contém arquivos do tipo Notebook.
   - **exploracao_dados.ipynb**: Arquivo utilizado para realizar testes antes de inserir nas funções.
- **.python-version**, **poetry.lock**, **pyproject.toml**: Arquivos de configuração do ambiente Python com `pyenv` e `Poetry`.
- **README.md**: Este arquivo de documentação.
  
## Configuração do Ambiente

Para garantir a consistência do ambiente de desenvolvimento, foi utilizado o **pyenv** para gerenciar a versão do Python e o **Poetry** para gerenciamento de dependências e ambientes virtuais.

### Pré-requisitos

- **Git**: Para clonar o repositório e versionar seu código.
- **pyenv**: Para gerenciar múltiplas versões do Python.
- **Poetry**: Para gerenciamento de dependências e ambientes virtuais.

### Instalação

#### 1. Clonando o Repositório

```bash
git clone https://github.com/BrunoChiconato/projetos_engenharia_de_dados
cd projetos_engenharia_de_dados/manipulacao_csv
```

#### 2. Configurando o Ambiente Python

Verifique a versão do Python especificada em `.python-version`:

```bash
cat .python-version
```

Instale essa versão usando o **pyenv** (se ainda não estiver instalada):

```bash
pyenv install x.x.x  # Substitua x.x.x pela versão listada
pyenv local x.x.x
```

#### 3. Instalando Dependências com o Poetry

Como o `pyproject.toml` e o `poetry.lock` já estão presentes, basta instalar as dependências:

```bash
poetry install
```

Isso criará um ambiente virtual e instalará quaisquer dependências especificadas.

## Como Executar o Programa

Siga os passos abaixo para executar o programa:

1. **Ative o ambiente virtual do Poetry**:

   ```bash
   poetry shell
   ```

2. **Gerar o Arquivo CSV de 100k Linhas**:

   Execute o script `gerar_csv.py` para gerar o arquivo `produtos_100k.csv` na pasta `data/raw/`:

   ```bash
   python gerar_csv.py
   ```

   **Saída Esperada**:
   - O script imprimirá uma mensagem a cada 10.000 linhas geradas para monitorar o progresso.
   - Ao final, exibirá uma mensagem confirmando que o arquivo CSV foi gerado com sucesso.

3. **Processar e Filtrar os Dados CSV**:

   Execute o script `main.py` para ler, processar, filtrar os dados e salvar o resultado em `data/processed/produtos_filtrados.csv`:

   ```bash
   python main.py
   ```

### Observações

- **Estrutura de Pastas**: Certifique-se de que as pastas `data/raw/` e `data/processed/` existam. O script `gerar_csv.py` cria a pasta `data/raw/` automaticamente se não existir.
- **Desempenho**: A geração de 100.000 linhas pode levar alguns minutos dependendo do desempenho do seu hardware.
- **Personalização**: Você pode ajustar o número de linhas a serem geradas modificando o parâmetro `num_linhas` na função `gerar_produtos_csv` dentro de `gerar_csv.py`.

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou identificar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Passos para Contribuir

1. **Faça um fork do projeto**.

2. **Crie uma branch para sua feature ou correção**:

   ```bash
   git checkout -b feature/nova-feature
   ```

3. **Faça commit das suas alterações**:

   ```bash
   git commit -m 'Adiciona nova feature'
   ```

4. **Faça push para a branch**:

   ```bash
   git push origin feature/nova-feature
   ```

5. **Abra um Pull Request**.

**Observação**: Certifique-se de que os caminhos dos arquivos e módulos estão corretos em relação à estrutura do seu projeto. Ajuste os comandos e instruções conforme necessário para o seu ambiente.