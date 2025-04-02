import socket

def cliente_udp(servidor_host='localhost', servidor_port=12345, num1=0, num2=0):
    """
    Cria um cliente UDP que envia dois números ao servidor e exibe o resultado retornado.
    """
    # Cria um socket UDP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Prepara a mensagem com os dois números (separados por espaço)
    mensagem = f"{num1} {num2}"
    
    try:
        # Envia a mensagem para o servidor
        cliente.sendto(mensagem.encode('utf-8'), (servidor_host, servidor_port))
        print(f"Enviado: {mensagem}")
        
        # Aguarda a resposta do servidor (até 1024 bytes)
        dados, _ = cliente.recvfrom(1024)
        resposta = dados.decode('utf-8')
        print(f"Recebido: {resposta}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cliente.close()

if __name__ == '__main__':
    # Exemplo: soma de 8 e 15
    cliente_udp(num1=8, num2=15)
