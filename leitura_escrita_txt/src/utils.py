def leitura_arquivo_txt(caminho_arquivo_txt: str) -> str:
    """
    Lê o conteúdo de um arquivo de texto e o retorna como uma string.
    
    :param caminho_arquivo_txt: Caminho para o arquivo de texto.
    :return: Conteúdo do arquivo como string.
    """
    try:
        with open(caminho_arquivo_txt, mode="r", encoding="utf-8") as arquivo_txt:
            leitura = arquivo_txt.read()
        return leitura
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo_txt} não foi encontrado.")
        return ""
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return ""

def processar_arquivo_txt(arquivo_txt: str) -> dict:
    """
    Processa o conteúdo de um arquivo de texto dividindo-o em listas para os nomes,
    idades e cidades e o retorna como um dicionário.
    
    :param arquivo_txt: Arquivo de texto formatado como uma string.
    :return: Conteúdo do arquivo de texto como um dicionário.
    """
    linhas = arquivo_txt.strip().split("\n")
    nomes = []
    idades = []
    cidades = []

    for linha in linhas:
        dados = linha.strip().split(",")
        if len(dados) == 3:
            nome, idade, cidade = [dado.strip() for dado in dados]
            nomes.append(nome)
            idades.append(idade)
            cidades.append(cidade)
        else:
            print(f"Linha com formato inválido: {linha}")

    dict_dados = {
        "Nomes": nomes,
        "Idades": idades,
        "Cidades": cidades
    }

    return dict_dados

def escrever_arquivo_txt(caminho_arquivo_saida: str, dados: dict):
    """
    Escreve os dados processados em um novo arquivo de texto
    
    :params:

    caminho_arquivo_saida: Uma string que representa o caminho 
    e o nome do arquivo onde os dados serão salvos.

    dados: Um dicionário contendo listas com os dados que você deseja escrever no arquivo. 
    Espera-se que esse dicionário tenha as chaves "Nomes", "Idades" e "Cidades".

    """
    with open(caminho_arquivo_saida, mode="w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write("Nomes, Idades, Cidades\n")

        for nome, idade, cidade in zip(dados["Nomes"], dados["Idades"], dados["Cidades"]):
            linha = f"{nome}, {idade}, {cidade}\n"
            arquivo_saida.write(linha)

