from conexao import conectar
from datetime import datetime

def gravar_voto_no_banco(numero_escolhido, titulo_eleitor, data_hora_voto):

    conexao = conectar()
    cursor = conexao.cursor()

    data_hora_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a data e hora atual no formato adequado para o banco de dados
    
    cursor.execute("SELECT id FROM candidatos WHERE numero = %s", (numero_escolhido,))
    resultado = cursor.fetchone()
    if resultado is None:
        print('Eleitor não encontrado.')
        cursor.close()
        conexao.close()
        return

    if resultado[0]== 'S':
        print('Eleitor já votou.')
        cursor.close()
        conexao.close()
        return
    
    comando_sql = "INSERT INTO votos (Candidato, Datahora, Protocolo_votacao) VALUES (%s, %s, %s)"
    cursor.execute(comando_sql, (numero_escolhido, data_hora_voto, data_hora_voto)) 

    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) 
    
    conexao.commit()
    print("\nSucesso: Voto registrado!")
    print(f"Protocolo: {data_hora_voto} - Candidato: {numero_escolhido}")

    cursor.close()
    conexao.close()

