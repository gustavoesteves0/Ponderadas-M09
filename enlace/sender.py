import sys

def hamming_encode(bit_str):
    """
    Codifica a sequência de bits utilizando o código de Hamming.
    Os bits de paridade são inseridos nas posições que são potências de 2.
    """
    # Converte a string para lista de inteiros (0 ou 1)
    bits = [int(b) for b in bit_str]
    m = len(bits)
    
    # Calcula o número mínimo de bits de paridade (r) que satisfaz a inequação 2^r >= m + r + 1
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    n = m + r
    encoded = [None] * n

    # Insere os bits de dados nas posições que não são potências de 2.
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:  # Se i é potência de 2, reserva para bit de paridade
            encoded[i - 1] = 0
        else:
            encoded[i - 1] = bits[j]
            j += 1

    # Calcula os bits de paridade para cada posição de potência de 2
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        # Verifica os blocos de bits cujo índice possui o bit i ligado
        for j in range(parity_pos, n + 1):
            if j & parity_pos:
                parity ^= encoded[j - 1]
        encoded[parity_pos - 1] = parity

    return ''.join(str(bit) for bit in encoded)

def create_frame(payload):
    """
    Cria o frame completo, acrescentando header, dados codificados com Hamming e terminador.
    """
    # Define header e terminador (mesma sequência para sincronização)
    header = "01111110"
    terminator = "01111110"
    # Codifica o payload com Hamming para possibilitar a correção de erros
    encoded_payload = hamming_encode(payload)
    # Monta o frame: header + dados codificados + terminador
    frame = header + encoded_payload + terminator
    return frame

def main():
    if len(sys.argv) < 2:
        print("Uso: {} <payload (sequência de 0s e 1s)>".format(sys.argv[0]))
        sys.exit(1)

    payload = sys.argv[1]
    # Valida se o payload contém somente 0s e 1s
    if not all(c in "01" for c in payload):
        print("Erro: o payload deve ser uma sequência de 0s e 1s")
        sys.exit(1)

    frame = create_frame(payload)
    # Imprime o frame para a saída padrão (stdout)
    print(frame)

if __name__ == '__main__':
    main()
