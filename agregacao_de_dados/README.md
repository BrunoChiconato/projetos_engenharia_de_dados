# Agregação de Dados

Bem-vindo(a) ao projeto de **Agregação de Dados** do conjunto de projetos em Python voltados para a Engenharia de Dados. Neste projeto, foi desenvolvido um programa que gera um conjunto de dados aleatórios e implementa funções para calcular agregações como soma, média, mínimo e máximo para campos específicos. O objetivo é praticar a geração de dados sintéticos, manipulação de estruturas de dados em Python e implementação de funções de agregação eficientes.

## Sumário

- [Agregação de Dados](#agregação-de-dados)
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

1. **Gera um conjunto de dados aleatórios**: Utiliza o script `gerar_dados.py` para criar uma lista de dicionários contendo informações fictícias de funcionários, como nome, idade, salário e anos de experiência.

2. **Implementa funções de agregação**: No módulo `utils.py`, são implementadas as funções `soma`, `media`, `minimo` e `maximo`, que calculam a soma, média, mínimo e máximo dos valores de um campo específico do conjunto de dados.

3. **Executa as operações de agregação**: O script `main.py` utiliza as funções de agregação para calcular e exibir os resultados para um campo especificado, como `salario` ou `idade`.

**Objetivos de Aprendizado**:

- Geração de dados sintéticos utilizando a biblioteca `Faker`.
- Manipulação de listas e dicionários em Python.
- Implementação de funções de agregação básicas.
- Tratamento de exceções e validação de dados.
- Estruturação e organização de projetos em Python.
- Gerenciamento de ambientes virtuais e dependências com `pyenv` e `Poetry`.

## Estrutura do Projeto

```
agregacao_de_dados/
├── src/
│   ├── __init__.py
│   ├── gerar_dados.py
│   ├── main.py
│   └── utils.py
├── .python-version
├── poetry.lock
├── pyproject.toml
└── README.md
```

- **src/**: Diretório que contém os arquivos Python do projeto.
  - **gerar_dados.py**: Script responsável por gerar o conjunto de dados aleatórios.
  - **utils.py**: Contém as funções de agregação (`soma`, `media`, `minimo`, `maximo`).
  - **main.py**: Arquivo principal que executa a geração de dados e realiza as agregações.
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
git clone https://github.com/BrunoChiconato/projetos_engenharia_de_dados.git
cd projetos_engenharia_de_dados/agregacao_de_dados
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

Como os arquivos `pyproject.toml` e `poetry.lock` já estão presentes, basta instalar as dependências:

```bash
poetry install
```

Isso criará um ambiente virtual e instalará quaisquer dependências especificadas, incluindo a biblioteca `Faker`.

## Como Executar o Programa

Siga os passos abaixo para executar o programa:

1. **Ative o ambiente virtual do Poetry**:

   ```bash
   poetry shell
   ```

2. **Execute o Script Principal**:

   Navegue até a pasta `src/`:

   ```bash
   cd src
   ```

   Execute o script `main.py` para gerar o conjunto de dados e realizar as agregações:

   ```bash
   python main.py
   ```

### Observações

- **Personalização**: Você pode alterar o número de registros gerados e o campo a ser analisado modificando os parâmetros no arquivo `main.py`:

  ```python
  def main():
      conjunto_dados = gerar_dados_aleatorios(1000)  # Altere o número de registros aqui
      campo = "salario"  # Altere o campo de interesse aqui
      # ...
  ```

- **Dependências Adicionais**: Certifique-se de que a biblioteca `Faker` está instalada. O `Poetry` deve cuidar disso automaticamente ao executar `poetry install`.

- **Importação de Módulos**: Se encontrar problemas de importação, verifique se o diretório atual está correto e se o arquivo `__init__.py` está presente na pasta `src/`.

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
