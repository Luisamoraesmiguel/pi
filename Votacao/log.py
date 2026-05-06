from datetime import datetime

ARQUIVO_LOG = "log_ocorrencias.txt"

def registrar_log(mensagem):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {mensagem}\n"
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(linha)

def exibir_logs():
    print("\n=== LOG DE OCORRÊNCIAS ===")
    try:
        with open(ARQUIVO_LOG, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum log encontrado.")