from Códigos_fonte import gerador_protocolo as protocolo
from conexao import conectar
from datetime import datetime
import Criptografia

def gravar_voto_no_banco(numero_escolhido, titulo_eleitor): 
    conexao = conectar()
    cursor = conexao.cursor()

    
    protocolo_limpo = protocolo.criar_novo_protocolo(numero_escolhido)
    protocolo_cifrado = Criptografia.cifrar(protocolo_limpo)

   
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Verifica se o candidato existe 
    cursor.execute("SELECT nome FROM candidatos WHERE numero = %s", (numero_escolhido,))
    if cursor.fetchone() is None and numero_escolhido != "00": 
        print('Candidato não encontrado. Voto será computado como Nulo.')

    # 4. Grava o voto na tabela de votos
    comando_sql = "INSERT INTO votos (Candidato, Datahora, Protocolo_votacao) VALUES (%s, %s, %s)"
    cursor.execute(comando_sql, (numero_escolhido, agora, protocolo_cifrado)) 

    
    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) 
    
    conexao.commit()
    print("\nSucesso: Voto registrado!")
    print(f"Protocolo: {protocolo_limpo} - Candidato: {numero_escolhido}")

    cursor.close()
    conexao.close()

    return protocolo_limpo