from utils import soma, media, minimo, maximo
from gerar_dados import gerar_dados_aleatorios

def main():
    conjunto_dados = gerar_dados_aleatorios(1000)
    campo = "salario"

    soma_valor = soma(conjunto_dados, campo)
    media_valor = media(conjunto_dados, campo)
    minimo_valor = minimo(conjunto_dados, campo)
    maximo_valor = maximo(conjunto_dados, campo)

    print(f"Soma de {campo}: {soma_valor}")
    print(f"Média de {campo}: {media_valor}")
    print(f"Valor mínimo de {campo}: {minimo_valor}")
    print(f"Valor máximo de {campo}: {maximo_valor}")

if __name__ == "__main__":
    main()