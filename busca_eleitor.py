import mysql.connector
import Criptografia

def buscar_eleitor(conexão, dado):

    # retirar espaços do dado
    termo = dado.strip()

    cursor = conexão.cursor(dictionary=True)

    # caso for um CPF cifra, se não, é título e não cifra
    if len(termo)==11:
        termo_pesquisa = Criptografia.cifrar(termo)
        campo_sql = "cpf"
    else:
        termo_pesquisa = termo
        campo_sql = "titulo"

    query = f"SELECT nome, cpf, titulo, mesario FROM eleitores WHERE {campo_sql} = %s"

    try:
        # tenta fazer a busca do eleitor
        cursor.execute(query, (termo_pesquisa,))
        resultado = cursor.fetchone()

        if resultado:
            print("\n" + "="*30)
            print("   ELEITOR ENCONTRADO")
            print("="*30)
            print(f"NOME:    {resultado['nome']}")
            print(f"TÍTULO:  {resultado['titulo']}")
            print(f"MESÁRIO: {'SIM' if resultado['mesario'] else 'NÃO'}")
            print("="*30 + "\n")
            return resultado
        else:
            print("\n" + "="*30)
            print("   ELEITOR NÃO ENCONTRADO")
            print("="*30 + "\n")
            return None
    
    except mysql.connector.Error as err:
        print(f"Erro ao buscar eleitor: {err}")
        return None
    finally:
        cursor.close()

    

