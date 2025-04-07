import socket

def iniciar_servidor_udp(host='localhost', port=12345):
    """
    Inicia um servidor UDP que aguarda mensagens de clientes.
    Espera receber uma string com dois números separados por espaço, soma os números e retorna o resultado.
    """
    # Cria um socket UDP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((host, port)) # Associa o socket a um endereço e porta
    print(f"Servidor UDP rodando em {host}:{port}...")

    while True:
        # Recebe dados do cliente (até 1024 bytes)
        dados, endereco = servidor.recvfrom(1024)
        mensagem = dados.decode('utf-8').strip()
        print(f"Recebido de {endereco}: {mensagem}")

        try:
            # Divide a mensagem para extrair os dois números
            numeros = mensagem.split()
            if len(numeros) != 2:
                resposta = "Erro: envie dois números separados por espaço."
            else:
                # Converte os números para float e realiza a soma
                num1, num2 = map(float, numeros)
                soma = num1 + num2
                resposta = f"Resultado: {soma}"
        except Exception as e:
            resposta = f"Erro no processamento: {e}"

        # Envia a resposta de volta para o cliente
        servidor.sendto(resposta.encode('utf-8'), endereco)
        print(f"Enviado para {endereco}: {resposta}")

if __name__ == '__main__':
    iniciar_servidor_udp()
