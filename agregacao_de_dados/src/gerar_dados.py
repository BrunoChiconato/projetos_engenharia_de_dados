import random
from faker import Faker # type: ignore
fake = Faker('pt_BR')

def gerar_nome():
    """
    Função que gera nomes aleatórios utilizando a biblioteca 'faker'.
    """
    return fake.name()

def gerar_dados_aleatorios(n: int):
    """
    Função que gera dados aleatórios com chaves específicas recebendo um valor 'n'
    que dita a quantidade de dados que será gerada.

    :params n: Número inteiro que gerará a quantidade de dados do conjunto de dados final.
    :return: Lista de dicionários com dados aleatórios.
    """
    dados: list = []
    
    try:
        if not isinstance(n, int):
            raise TypeError("Forneça um parâmetro do tipo inteiro!")
        
        for _ in range(n):
            funcionario = {
                'nome': gerar_nome(),
                'idade': random.randint(20, 60),
                'salario': round(random.uniform(3000, 15000), 2),
                'anos_experiencia': random.randint(1, 40)
            }
            dados.append(funcionario)

        return dados
    
    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return None