# 🧠 Analisador de Sentimentos (OpenAI + Tkinter)

Aplicação em Python com interface gráfica que analisa mensagens em português e retorna:

- ✅ Nota de 0 a 10 sobre o teor da mensagem  
- 😊 Sentimento geral (positivo, neutro ou negativo)  
- 🏷️ Categoria da mensagem  
- ⛔ Bloqueio automático de mensagens inadequadas  

O projeto utiliza a **API da OpenAI**, boas práticas de segurança (variáveis de ambiente) e controle de versão com Git.

---

## 🖥️ Interface
Aplicação desktop simples e intuitiva desenvolvida com **Tkinter**, permitindo que o usuário digite uma mensagem e receba a análise em tempo real.

---

## 🛠️ Tecnologias Utilizadas
- Python 3
- OpenAI API
- Tkinter
- Git & GitHub
- CSV (persistência de histórico local)

---

## 🔐 Segurança
A chave da API **não está no código**.  
Ela é carregada via variável de ambiente:

```bash
OPENAI_API_KEY=sua_chave_aqui
