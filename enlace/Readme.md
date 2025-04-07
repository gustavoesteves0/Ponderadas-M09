# Implementação da Camada de Enlace com Correção de Erros

Este projeto implementa dois programas em Python simulando uma comunicação de camada de enlace entre um **remetente** e um **destinatário**, utilizando:

- Codificação de Hamming para **correção de erros de 1 bit**
- **Sincronização de frames** com cabeçalho e terminador
- Comunicação via **pipes** (`|`) para redirecionamento de saída/entrada

---

## 📄 Estrutura do Frame

Cada mensagem enviada pelo remetente segue o seguinte formato:

```
<HEADER> + <DADOS_CODIFICADOS> + <TERMINADOR>
```

- **HEADER e TERMINADOR:** `"01111110"` (sequência de sincronização, baseada no HDLC)
- **DADOS_CODIFICADOS:** sequência de bits do payload codificada com o **código de Hamming**

---

## 📥 Requisitos

- Python 3
- Terminal Bash/Linux/MacOS (ou Git Bash no Windows)

---

## 🔧 Permissão de Execução

Para tornar os scripts executáveis no terminal, execute:

```
chmod +x sender.py  
chmod +x receiver.py
```

---

## 🚀 Como Executar

Use o pipe (`|`) para conectar o sender ao destinatário:

```
./sender.py "01101001" | ./receiver.py
```

- O `sender` envia a mensagem `"01101001"` como payload.
- O `receiver` sincroniza, corrige possíveis erros e imprime a mensagem original.

---

## 🧠 Funcionalidades

✅ Sincronização de mensagens com cabeçalho e terminador  
✅ Codificação com **código de Hamming**  
✅ Correção de **erros de 1 bit**  
✅ Comunicação entre processos via `stdin/stdout`

---

## 🧪 Exemplo com Erro Simulado

Para testar a correção de erro manualmente, você pode editar o frame gerado pelo remetente e mudar um bit (1 para 0 ou vice-versa), depois colar esse frame no `stdin` do destinatário:

```
echo "01111110010101101101011001111110" | ./receiver.py
```

Neste exemplo, há um erro proposital no frame que será corrigido automaticamente.

---

## 📚 Explicação em Vídeo


Para assistir o vídeo de explicação, clique [aqui.](https://youtu.be/CXzDBQ_ygmE)

---

## 🏆 Critérios de Avaliação

- [x] Documentação do protocolo  
- [x] Implementação do remetente  
- [x] Implementação do destinatário  
- [x] Sincronização entre os dois nós  
- [x] Correção de erros de 1 bit  
- [x] Vídeo explicativo

---

## 📁 Arquivos

- `sender.py`: Envia um frame com dados codificados
- `receiver.py`: Recebe, decodifica e corrige a mensagem

---

## 👨‍💻 Autor

Feito por Gustavo Machado Esteves para a atividade de Camada de Enlace – Redes de Computadores.
