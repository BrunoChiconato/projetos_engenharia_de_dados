# Projetos em Python para Engenharia de Dados

Bem-vindo(a) ao repositório de projetos em Python voltados para a área de Engenharia de Dados. Este conjunto de projetos foi realizado para ajudar no desenvolvimento de habilidades fundamentais em Python, preparando para enfrentar problemas e projetos comuns na rotina de um engenheiro de dados.

## Índice

- [Projetos em Python para Engenharia de Dados](#projetos-em-python-para-engenharia-de-dados)
  - [Índice](#índice)
  - [Projetos](#projetos)
  - [Configuração do Ambiente](#configuração-do-ambiente)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
      - [1. Instalando o Git](#1-instalando-o-git)
      - [2. Instalando o pyenv](#2-instalando-o-pyenv)
      - [3. Instalando o Poetry](#3-instalando-o-poetry)
      - [4. Clonando o Repositório](#4-clonando-o-repositório)
      - [5. Configurando o Ambiente Python](#5-configurando-o-ambiente-python)
        - [Verificando a Versão do Python](#verificando-a-versão-do-python)
      - [6. Instalando Dependências com o Poetry](#6-instalando-dependências-com-o-poetry)
  - [Como Executar os Projetos](#como-executar-os-projetos)
  - [Contribuindo](#contribuindo)

## Projetos

| Nome do Projeto                               | Breve Descrição                                                                                                                                                                          |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Leitura e Escrita de Arquivos de Texto**    | Escreva um programa que leia dados de um arquivo de texto, processe-os e escreva os resultados em um novo arquivo.                                                                        |
| **Manipulação de Arquivos CSV**               | Implemente um script para ler dados de um arquivo CSV, parsear os dados e realizar operações básicas, como filtrar linhas com base em certos critérios.                                   |
| **Agregação de Dados**                        | Dado um conjunto de dados representado como uma lista de dicionários, escreva funções para calcular agregações como soma, média, mínimo e máximo para campos específicos.                 |
| **Análise de Logs**                           | Crie um programa para analisar um arquivo de log de servidor, extrair informações relevantes (como timestamps, mensagens de erro) e gerar um relatório resumido.                          |
| **Processo ETL Simples**                      | Simule um processo ETL (Extração, Transformação, Carregamento) lendo dados de um arquivo de texto, transformando-os (por exemplo, alterando formatos de data, normalizando texto) e escrevendo-os em outro arquivo. |
| **Validação e Limpeza de Dados**              | Crie funções para validar entradas de dados, lidar com dados ausentes ou malformados e limpar o conjunto de dados.                                                                        |
| **Argumentos de Linha de Comando**            | Desenvolva um script que aceite argumentos da linha de comando para especificar arquivos de entrada e saída ou parâmetros para processamento de dados.                                    |
| **Implementação de uma Fila**                 | Use listas Python para implementar uma estrutura de dados de fila básica, simulando dados sendo ingeridos e processados.                                                                  |
| **Noções Básicas de Multithreading**          | Escreva um programa que use threading para realizar múltiplas tarefas de processamento de dados simultaneamente.                                                                          |
| **Tratamento de Erros e Logging**             | Aprimore seus scripts com tratamento de erros usando blocos `try-except` e implemente logging para rastrear eventos e erros.                                                              |
| **Serialização de Dados**                     | Serialize estruturas de dados em JSON e deserialize-as de volta, sem usar o módulo `json`.                                                                                                |
| **Expressões Regulares**                      | Utilize o módulo `re` para encontrar padrões em strings, como extrair endereços de e-mail ou números de telefone de um texto.                                                             |
| **Compressão e Descompressão de Arquivos**    | Escreva scripts para comprimir e descomprimir arquivos usando módulos integrados como `gzip` ou `zipfile`.                                                                                |
| **Manipulação de Datas e Horários**           | Use o módulo `datetime` para manipular datas e horários, como calcular a diferença entre duas datas.                                                                                      |
| **Simulação de Fluxos de Dados**              | Gere um fluxo de dados (por exemplo, números aleatórios ou timestamps) e escreva um script para processar os dados em tempo real.                                                         |
| **Construção de uma Calculadora Simples**     | Crie uma calculadora de linha de comando que possa realizar operações aritméticas básicas e lidar graciosamente com entradas inválidas.                                                   |
| **Ordenação e Busca de Dados**                | Implemente algoritmos de ordenação (como bubble sort ou quicksort) e algoritmos de busca (como busca binária) em conjuntos de dados.                                                      |
| **Análise de Arquivos de Configuração**       | Parseie arquivos de configuração (como arquivos INI) e use as configurações em seu programa.                                                                                              |
| **Noções Básicas de Redes com Sockets**       | Utilize o módulo `socket` para enviar e receber dados através de uma conexão de rede.                                                                                                     |

## Configuração do Ambiente

Para garantir a consistência do ambiente de desenvolvimento e facilitar a execução dos projetos desenvolvidos, foi utilziado o **pyenv** para gerenciar as versões do Python e o **Poetry** para gerenciamento de dependências e ambientes virtuais.

### Pré-requisitos

- **Git**: Para clonar o repositório e versionar seu código.
- **pyenv**: Para gerenciar múltiplas versões do Python.
- **Poetry**: Para gerenciamento de dependências e ambientes virtuais.

### Instalação

#### 1. Instalando o Git

- **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install git
  ```

- **macOS**:

  ```bash
  brew install git
  ```

- **Windows**:

  Baixe e instale o Git for Windows: [gitforwindows.org](https://gitforwindows.org/)

#### 2. Instalando o pyenv

Siga as instruções oficiais no repositório do [pyenv](https://github.com/pyenv/pyenv#installation).

Exemplo para Ubuntu:

```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl https://pyenv.run | bash

echo -e '\n# Pyenv' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

exec "$SHELL"
```

#### 3. Instalando o Poetry

Siga as instruções oficiais no site do [Poetry](https://python-poetry.org/docs/#installation).

Usando o script de instalação:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Adicione o Poetry ao seu PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

#### 4. Clonando o Repositório

```bash
git clone git@github.com:BrunoChiconato/projetos_engenharia_de_dados.git
```

#### 5. Configurando o Ambiente Python

Como os arquivos `.python-version`, `poetry.lock` e `pyproject.toml` já existem no projeto, você pode pular a etapa de inicialização do Poetry. Certifique-se de que a versão do Python especificada em `.python-version` está instalada no seu sistema.

##### Verificando a Versão do Python

Veja qual versão do Python está especificada:

```bash
cat .python-version
```

Instale essa versão usando o **pyenv** (se ainda não estiver instalada):

```bash
pyenv install x.x.x  # Substitua x.x.x pela versão listada
pyenv local x.x.x
```

#### 6. Instalando Dependências com o Poetry

Como o `pyproject.toml` e o `poetry.lock` já estão presentes, basta instalar as dependências:

```bash
poetry install
```

Isso criará um ambiente virtual e instalará quaisquer dependências especificadas (mesmo que, neste caso, não haja dependências adicionais).

## Como Executar os Projetos

Para cada projeto, siga os passos abaixo:

1. **Navegue até o diretório do projeto**

   ```bash
   cd nome_do_projeto
   ```

2. **Ative o ambiente virtual do Poetry**

   ```bash
   poetry shell
   ```

3. **Execute o script**

   ```bash
   python main.py
   ```

4. **Saia do ambiente virtual após terminar**

   ```bash
   exit
   ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para relatar bugs ou sugerir melhorias. Se desejar contribuir com código:

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
