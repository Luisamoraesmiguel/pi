from conexao import conectar
from Criptografia import decifrar


def verificar_mesario(titulo, cpf_4digitos, chave):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = "SELECT cpf, mesario FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s "
    cursor.execute(sql, (titulo, chave))
    resultado = cursor.fetchone()

    if resultado is None:
        print("\n[ERRO] Título ou chave de acesso incorretos. Tente novamente.")
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    cpf, mesario = resultado

    if mesario.upper() == 'N':
        print("\n[ERRO] O eleitor com este título não é um mesário. Tente novamente.")
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    cpf_decifrado = decifrar(cpf)
   

    cpf_str = ''
    for c in str(cpf_decifrado):
        if c.isdigit():
            cpf_str += c
    cpf_4digitos = str(cpf_4digitos).strip() # Remove espaços em branco, se houver



    if cpf_str[:4] == cpf_4digitos:
        cursor.close()
        conexao.close()
        return {"nome": titulo} # Retorna um dicionário com o nome do mesário (pode ser expandido para incluir mais informações, se necessário)
    else:
        print("\n[ERRO] CPF incorreto. Tente novamente.")
        cursor.close()
        conexao.close()
        return "CPF_ERRADO"
    
