# Leitura, Processamento e Escrita de Arquivo de Texto

Bem-vindo(a) ao projeto de **Leitura, Processamento e Escrita de Arquivo de Texto** do conjunto de projetos em Python voltados para a Engenharia de Dados. Neste projeto, foi desenvolvido um programa que lê dados de um arquivo de texto, processa esses dados e escreve os resultados em um novo arquivo. O objetivo é praticar manipulação de arquivos, processamento de strings e escrita de arquivos em Python.

## Sumário

- [Leitura, Processamento e Escrita de Arquivo de Texto](#leitura-processamento-e-escrita-de-arquivo-de-texto)
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

Escreva um programa em Python que:

1. **Leia dados de um arquivo de texto**: O arquivo contém informações estruturadas, como nomes, idades e cidades, separados por vírgulas.
2. **Processe os dados**: Organize os dados em uma estrutura apropriada (por exemplo, um dicionário ou lista) e realize qualquer limpeza ou transformação necessária.
3. **Escreva os resultados em um novo arquivo**: Salve os dados processados em um novo arquivo de texto, mantendo um formato consistente e legível.

**Objetivos de Aprendizado**:

- Manipulação de arquivos em Python usando `open`, `read`, `write`.
- Processamento e limpeza de strings.
- Organização de dados em estruturas como listas e dicionários.
- Tratamento de erros e boas práticas de programação.

## Estrutura do Projeto

```
leitura_escrita_txt/
│
├── data/
│   ├── processed/
│   │   └── dados_processados.txt
│   └── raw/
│       └── base_dados.txt
├── notebooks/
│   └── exploracao_dados.ipynb
├── src/
│   └── __init__.py
│   └── main.py
│   └── utils.py
├── .python-version
├── poetry.lock
├── pyproject.toml
└── README.md
```

- **data/**: Diretório que contém os dados brutos e processados.
  - **raw/**: Contém o arquivo de entrada `base_dados.txt`.
  - **processed/**: Onde será salvo o arquivo de saída `dados_processados.txt`.
-  **notebooks/**: Diretório que contém arquivos do tipo Notebook
   - **exploracao_dados.ipynb**: Arquivo utilizado para realizar testes antes de inserir nas próprias funções.
- **src/**: Diretório que contém os arquivos Python utilizados, como funções e o arquivo principal.
  - **utils.py**: Arquivo que contém as funções utilizadas para o projeto em questão.
  - **main.py**: Arquivo principal que executa o programa.
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
cd projetos_engenharia_de_dados/leitura_escrita_txt
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

2. **Execute o script principal**:

   ```bash
   python main.py
   ```

3. **Saia do ambiente virtual após terminar**:

   ```bash
   exit
   ```

### Observações

- Certifique-se de que o arquivo de entrada `base_dados.txt` está presente no diretório `data/raw/`.
- O arquivo de saída `dados_processados.txt` será gerado no diretório `data/processed/`.

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
