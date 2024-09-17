import csv
import random
from datetime import datetime, timedelta
import os

def gerar_produtos_csv(caminho_csv: str, num_linhas: int = 100000):
    """
    Gera um arquivo CSV com dados fictícios de produtos.

    :param caminho_csv: Caminho onde o arquivo CSV será salvo.
    :param num_linhas: Número de linhas a serem geradas (padrão: 100000).
    """
    categorias = ["Celular", "Computador", "Televisão", "Tablet", "Acessório", "Wearable"]
    marcas = ["Samsung", "Apple", "Dell", "HP", "LG", "Sony", "Xiaomi", "Acer", "Lenovo", "Asus", "Huawei"]
    modelos = ["Pro", "Plus", "Max", "Ultra", "Mini", "Air", "Series", "Prime", "Edge", "Flex"]
    produtos = ["Galaxy", "iPhone", "MacBook", "ThinkPad", "VivoBook", "Bravia", "Mi", "Spectre", "ZenBook", "Pavilion"]

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date

    with open(caminho_csv, mode="w", newline="", encoding="utf-8") as file:
        cabecalho = ["ID_Produto", "Nome_Produto", "Categoria", "Preco", "Quantidade_Estoque", "Data_Adicao"]
        writer = csv.DictWriter(file, fieldnames=cabecalho)
        writer.writeheader()

        for i in range(1, num_linhas + 1):
            categoria = random.choice(categorias)
            marca = random.choice(marcas)
            produto = random.choice(produtos)
            modelo = random.choice(modelos)
            nome_produto = f"{marca} {produto} {modelo}"
            preco = round(random.uniform(1000.00, 20000.00), 2)
            quantidade_estoque = random.randint(0, 1000)
            data_adicao = start_date + timedelta(days=random.randint(0, delta.days))
            data_adicao_str = data_adicao.strftime("%Y-%m-%d")

            writer.writerow({
                "ID_Produto": i,
                "Nome_Produto": nome_produto,
                "Categoria": categoria,
                "Preco": preco,
                "Quantidade_Estoque": quantidade_estoque,
                "Data_Adicao": data_adicao_str
            })

            if i % 10000 == 0:
                print(f"{i} linhas geradas...")

    print(f"Arquivo CSV gerado com sucesso em {caminho_csv}")

if __name__ == "__main__":
    caminho_csv = os.path.join("data", "raw", "produtos_100k.csv")
    
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
    
    gerar_produtos_csv(caminho_csv)
