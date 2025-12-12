import os
import csv
from datetime import datetime

from openai import OpenAI
import tkinter as tk
from tkinter import messagebox

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analisar_sentimento(texto: str) -> dict:
    pre_prompt = (
        "Você é um analisador de mensagens em português.\n"
        "Dado o texto de uma mensagem, você deve:\n"
        "1) Atribuir uma nota de 0 a 10 para o teor da mensagem.\n"
        "2) Classificar o sentimento geral como: positivo, neutro ou negativo.\n"
        "3) Classificar a categoria da mensagem.\n\n"
        "Responda APENAS no formato:\n"
        "nota;sentimento;categoria\n\n"
        "Mensagem:\n"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=pre_prompt + texto,
        temperature=0.0,
        max_output_tokens=32
    )

    partes = response.output_text.strip().split(";")

    return {
        "nota": int(partes[0]),
        "sentimento": partes[1],
        "categoria": partes[2],
    }

def salvar_historico(texto, nota, sentimento, categoria, status):
    arquivo = "historico_sentimentos.csv"
    novo = not os.path.exists(arquivo)

    with open(arquivo, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if novo:
            writer.writerow(["data", "texto", "nota", "sentimento", "categoria", "status"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            texto, nota, sentimento, categoria, status
        ])

def analisar_mensagem():
    texto = caixa_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite uma mensagem.")
        return

    resultado = analisar_sentimento(texto)
    nota = resultado["nota"]

    if nota >= 6:
        status = "Aprovada"
        cor = "green"
    else:
        status = "Bloqueada"
        cor = "red"

    resultado_label.config(text=f"Nota: {nota} ({status})", fg=cor)
    detalhe_label.config(
        text=f'Sentimento: {resultado["sentimento"]} | Categoria: {resultado["categoria"]}',
        fg=cor
    )

    salvar_historico(
        texto,
        nota,
        resultado["sentimento"],
        resultado["categoria"],
        status
    )

    caixa_texto.delete("1.0", tk.END)

root = tk.Tk()
root.title("Analisador de Sentimento")
root.geometry("350x200")

tk.Label(root, text="Digite uma mensagem:", font=("Segoe UI", 10)).pack(pady=5)

caixa_texto = tk.Text(root, height=4, width=30)
caixa_texto.pack(pady=5)

tk.Button(root, text="Analisar Mensagem", command=analisar_mensagem).pack(pady=5)

resultado_label = tk.Label(root, text="Nota: -", font=("Segoe UI", 10, "bold"))
resultado_label.pack(pady=5)

detalhe_label = tk.Label(root, text="")
detalhe_label.pack()

root.mainloop()
