import csv
from datetime import datetime
from typing import List, Dict, Any

def ler_arquivo_csv(caminho_csv: str) -> List[Dict[str, Any]]:
    """
    Lê um arquivo CSV e retorna uma lista de dicionários, onde cada dicionário representa uma linha do CSV.

    :param caminho_csv: Caminho para o arquivo CSV.
    :return: Lista de dicionários contendo os dados do CSV.
    """
    try:
        with open(caminho_csv, mode = "r", encoding = "utf-8") as file:
            arquivo_csv = list(csv.DictReader(file))

            return arquivo_csv
        
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_csv} não foi encontado.")
        return []
    
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")
        return []
    
def tratar_datas_csv(arquivo_csv: List[Dict[str,Any]]) -> List[Dict[str, Any]]:
    """
    Converte a data de adição de cada produto do formato "YYYY-MM-DD" para "DD/MM/YYYY".

    :param arquivo_csv: Lista de dicionários contendo os dados do CSV.
    :return: Lista de dicionários com as datas tratadas.
    """
    for dict_produtos in arquivo_csv:
        data_str: str = dict_produtos.get("Data_Adicao","")
        try:
            data_obj = datetime.strptime(data_str,"%Y-%m-%d")
            dict_produtos["Data_Adicao"] = data_obj.strftime("%d/%m/%Y")
        except ValueError:
            print(f"Formato de data inválido para o produto com ID {dict_produtos.get('ID_Produto')}: {data_str}")
            return []
    
    return arquivo_csv

def filtrar_produtos_pelo_preco(arquivo_csv: List[Dict[str, Any]], preco: float) -> List[Dict[str, Any]]:
    """
    Filtra produtos que estão abaixo de um determinado preço.

    :param arquivo_csv: Lista de dicionários contendo os dados do CSV.
    :param preco: Valor de preço para filtragem.
    :return: Lista de dicionários contendo apenas os produtos com preço abaixo do valor especificado.
    """
    lista_produtos_filtrados: list = []
    for dict_produtos in arquivo_csv:
        try:
            preco_produto = float(dict_produtos.get("Preco",0))
            if preco_produto < preco:
                lista_produtos_filtrados.append(dict_produtos)
        except ValueError:
            print(f"Preço inválido para o produto com ID {dict_produtos.get('ID_Produto')}: {dict_produtos.get('Preco')}")
            return []
   
    return lista_produtos_filtrados

def salvar_como_csv(caminho_csv_processed: str, arquivo_csv: List[Dict[str, Any]]) -> None:
    """
    Salva uma lista de dicionários em um arquivo CSV.

    :param caminho_csv_processed: Caminho para o arquivo CSV de saída.
    :param arquivo_csv: Lista de dicionários contendo os dados a serem salvos.
    """
    cabecalho: List[str] = ["ID_Produto", "Nome_Produto", "Categoria", "Preco", "Quantidade_Estoque", "Data_Adicao"]

    try:
        with open(caminho_csv_processed, mode = "w", newline = "", encoding = "utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = cabecalho)
            writer.writeheader()
            for dict_produtos in arquivo_csv:
                if all(key in dict_produtos for key in cabecalho):
                    writer.writerow(dict_produtos)
                else:
                    print(f"Produto com ID {dict_produtos.get('ID_Produto')} está faltando campos.")

    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")
        