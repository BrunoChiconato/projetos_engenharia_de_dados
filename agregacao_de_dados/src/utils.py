def soma(conjunto_dados: list, campo: str) -> float:
    """
    Função que recebe um conjunto de dados com chaves conhecidas, mas com valores aleatórios
    e uma dessas chaves como parâmetros e retorna a soma de todos os valores da chave escolhida.

    :params conjunto_dados: Lista de dicionários com chaves fixas e valores aleatórios.
    :params campo: Uma string que representa uma das chaves do conjunto de dados.

    :return: Número do tipo float que representa a soma da chave escolhida.
    """
    soma_total: float = 0.0

    for dict_dados in conjunto_dados:
        valor = dict_dados.get(campo, 0.0)

        try:
            soma_total += float(valor)
        except (TypeError, ValueError):
            print(f"Valor inválido encontrado: {valor}. Ignorando este valor.")

    return soma_total

def media(conjunto_dados: list, campo: str) -> float:
    """
    Função que recebe um conjunto de dados com chaves conhecidas, mas com valores aleatórios
    e uma dessas chaves como parâmetros e retorna a média dos valores da chave escolhida.

    :params conjunto_dados: Lista de dicionários com chaves fixas e valores aleatórios.
    :params campo: Uma string que representa uma das chaves do conjunto de dados.

    :return: Número do tipo float que representa a média da chave escolhida.
    """
    soma_total: float = 0.0
    contador: int = 0

    for dict_dados in conjunto_dados:
        valor = dict_dados.get(campo, 0.0)

        try:
            soma_total += float(valor)
            contador += 1
        except (TypeError, ValueError):
            print(f"Valor inválido encontrado: {valor}. Ignorando este valor.")

    if contador > 0:
        return soma_total / contador
    
    else:
        print("Nenhum valor válido encontrado para calcular a média.")
        return 0.0


def minimo(conjunto_dados: list, campo: str) -> float:
    """
    Função que recebe um conjunto de dados com chaves conhecidas, mas com valores aleatórios
    e uma dessas chaves como parâmetros e retorna o menor valor dentre todos os valores da chave escolhida.

    :params conjunto_dados: Lista de dicionários com chaves fixas e valores aleatórios.
    :params campo: Uma string que representa uma das chaves do conjunto de dados.

    :return: Número do tipo float que representa o menor valor da chave escolhida.
    """
    valores_validos: list = []

    for dict_dados in conjunto_dados:
        valor = dict_dados.get(campo)

        if isinstance(valor, (int, float)):
            valores_validos.append(valor)
        else:
            print(f"Valor inválido encontrado: {valor}. Ignorando este valor.")

    if valores_validos:
        return min(valores_validos)
    else:
        print("Nenhum valor válido encontrado para calcular o mínimo.")
        return None

def maximo(conjunto_dados: list, campo: str) -> float:
    """
    Função que recebe um conjunto de dados com chaves conhecidas, mas com valores aleatórios
    e uma dessas chaves como parâmetros e retorna o maior valor dentre todos os valores da chave escolhida.

    :params conjunto_dados: Lista de dicionários com chaves fixas e valores aleatórios.
    :params campo: Uma string que representa uma das chaves do conjunto de dados.

    :return: Número do tipo float que representa o maior valor da chave escolhida.
    """
    valores_validos: list = []

    for dict_dados in conjunto_dados:
        valor = dict_dados.get(campo)

        if isinstance(valor, (int, float)):
            valores_validos.append(valor)
        else:
            print(f"Valor inválido encontrado: {valor}. Ignorando este valor.")

    if valores_validos:
        return max(valores_validos)
    else:
        print("Nenhum valor válido encontrado para calcular o máximo.")
        return None