# 🛰️ Comunicação UDP com Python — Somador

Este projeto implementa um sistema de comunicação baseado no **protocolo UDP**, utilizando **sockets em Python**. A aplicação consiste em dois programas: um **servidor** que recebe dois números, realiza a **soma**, e retorna o resultado ao **cliente**, que os envia.

---

## 📌 Objetivo

Demonstrar, na prática, como funciona a comunicação por datagramas com o **User Datagram Protocol (UDP)**, conforme a especificação do [RFC 768](https://tools.ietf.org/html/rfc768). O sistema foi implementado respeitando o formato e funcionamento descritos no documento original.

---

## 📂 Estrutura do Projeto

```bash
.
├── UDP_Server.py      # Servidor UDP - espera dados e responde com o resultado da soma
├── UDP_Client.py      # Cliente UDP - envia dois números e exibe o resultado
└── Readme.md      # Este documento
```

---

## ⚙️ Como executar

### 1. Clonar o repositório 

```bash
git clone https://github.com/gustavoesteves0/Ponderadas-M09.git
cd UDP
```

### 2. Executar o servidor

Abra um terminal e inicie o servidor:

```bash
python3 UDP_Server.py
```

### 3. Executar o cliente

Em outro terminal, execute o cliente passando dois números:

```bash
python3 UDP_Client.py
```

Ou edite os valores diretamente no script `UDP_Client.py`, nas últimas linhas:

```python
# Exemplo: soma de 8 e 15
cliente_udp(num1=8, num2=15)
```

---

## 🧠 Como funciona

### 📤 Cliente

- Envia uma string com dois números separados por espaço.
- Exemplo: `"8 15"`
- Aguarda a resposta com o resultado.

### 📥 Servidor

- Recebe a mensagem, interpreta os dois números.
- Realiza a soma.
- Retorna o resultado ao endereço de origem.

---

## 🛠️ Tecnologias

- Python 3.x
- `socket` (módulo padrão da biblioteca Python)

---

## 🎓 Aprendizados

- Criação e uso de **sockets UDP**
- Diferença entre TCP e UDP
- Manipulação de strings e conversão de tipos em Python
- Implementação simples de um protocolo de aplicação
- Compreensão do cabeçalho e estrutura de um datagrama UDP (conforme RFC 768)

---

## 🎥 Apresentação em vídeo

Gravei um vídeo de até **5 minutos** explicando:
- O funcionamento geral do sistema
- Os conceitos envolvidos no protocolo UDP
- Como foi feita a implementação em Python
- Demonstração de execução do cliente e servidor

📽️ Link do vídeo [aqui.](https://youtu.be/aDMOGSQBm3s)
