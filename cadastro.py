import mysql.connector

def cadastrar_eleitor(nome, titulo):
    try:
        # 1. Conectar ao banco (as informações vêm do arquivo .sql que vocês têm)
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",      
            password="Beatriz190524",
            database="tabela_bd"    
        )
        
        cursor = conexao.cursor()

        # 2. O comando para inserir no banco
        comando = "INSERT INTO eleitores (nome, titulo) VALUES (%s, %s)"
        valores = (nome, titulo)

        cursor.execute(comando, valores)
        conexao.commit() 
        
        print("Eleitor cadastrado com sucesso!")
        return 1

    except Exception as erro:
        print(f"Erro ao cadastrar: {erro}")
        return 0

    finally:
        # Sempre fechar a conexão para não travar o banco
        if conexao.is_connected():
            cursor.close()
            conexao.close()

cadastrar_eleitor ("Beatriz Teste","12345678")