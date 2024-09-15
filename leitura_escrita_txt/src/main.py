from utils import (
    leitura_arquivo_txt,
    processar_arquivo_txt,
    escrever_arquivo_txt,
)
def main():
    caminho_txt = "./data/raw/base_dados.txt"
    caminho_saida = "./data/processed/dados_processados.txt"
    arquivo = leitura_arquivo_txt(caminho_txt)
    if arquivo:
        arquivo_processado = processar_arquivo_txt(arquivo)
        escrever_arquivo_txt(caminho_saida, arquivo_processado)
        print("Processamento concluído com sucesso!")
    else:
        print("Não foi possível ler o arquivo de entrada.")
    
if __name__ == "__main__":
    main()