#!/usr/bin/env python3
import sys

def hamming_decode(encoded_str):
    """
    Decodifica a mensagem codificada com o código de Hamming.
    Caso haja erro de 1 bit, ele é detectado e corrigido.
    Em seguida, os bits de dados (não de paridade) são extraídos.
    """
    encoded = [int(b) for b in encoded_str]
    n = len(encoded)

    # Calcula o número de bits de paridade (r) com base no tamanho do código recebido
    r = 0
    while 2**r <= n:
        r += 1

    # Calcula o síndrome para detectar erro
    syndrome = 0
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(parity_pos, n + 1):
            if j & parity_pos:
                parity ^= encoded[j - 1]
        if parity != 0:
            syndrome += parity_pos

    # Se o síndrome for diferente de zero, há erro na posição syndrome
    if syndrome != 0 and syndrome <= n:
        encoded[syndrome - 1] ^= 1  # Corrige o bit com erro

    # Extrai os bits de dados (posições que não são potências de 2)
    data_bits = []
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            data_bits.append(encoded[i - 1])
    return ''.join(str(bit) for bit in data_bits)

def main():
    # Lê o frame completo da entrada padrão (stdin)
    frame = sys.stdin.read().strip()
    
    # Define header e terminador usados na transmissão
    header = "01111110"
    terminator = "01111110"

    # Verifica se o frame possui os marcadores de sincronização
    if not (frame.startswith(header) and frame.endswith(terminator)):
        print("Erro de sincronização do frame")
        sys.exit(1)

    # Extrai a parte de dados codificados removendo o header e o terminador
    encoded_payload = frame[len(header):-len(terminator)]

    # Decodifica a mensagem utilizando o código de Hamming (corrigindo erro de 1 bit, se houver)
    message = hamming_decode(encoded_payload)
    print(message)

if __name__ == '__main__':
    main()
