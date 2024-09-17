from utils import (
    ler_arquivo_csv,
    tratar_datas_csv,
    filtrar_produtos_pelo_preco,
    salvar_como_csv         
)

def main():
    caminho_csv_raw: str = "./data/raw/produtos_100k.csv"
    caminho_csv_processed: str = "./data/processed/produtos_filtrados.csv"
    preco: float = 5000

    arquivo_csv: list = ler_arquivo_csv(caminho_csv_raw)
    arquivo_csv_tratado: list = tratar_datas_csv(arquivo_csv)
    arquivo_csv_filtrado: list = filtrar_produtos_pelo_preco(arquivo_csv_tratado, preco)
    salvar_como_csv(caminho_csv_processed, arquivo_csv_filtrado)

    print("Processamento concluído com sucesso!")
    
if __name__ == "__main__":
    main()