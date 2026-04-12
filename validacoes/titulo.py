def verificar_titulo(numero):
    numero = str(numero).strip()
    # Contando quantos números tem
    tamanho = len(numero)
     # Vendo se tem 12 números e se é tudo número mesmo
    if tamanho == 12 and numero.isdigit():
        return 1  # Significa que está tudo certo
    else:
        return 0  # Significa que deu erro