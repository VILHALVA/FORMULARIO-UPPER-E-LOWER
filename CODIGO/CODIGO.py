import tkinter as tk
from tkinter import ttk, messagebox

def converter_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Campo vazio", "Por favor, insira um texto para converter.")
        return

    opcao = combo_opcoes.get()
    
    texto_formatado.config(state="normal")
    texto_formatado.delete("1.0", tk.END)

    if opcao == "UPPER":
        texto_formatado.insert(tk.END, texto.upper())
    elif opcao == "LOWER":
        texto_formatado.insert(tk.END, texto.lower())
    elif opcao == "MISTO":
        palavras = texto.lower().split()
        texto_formatado.insert(tk.END, ' '.join([word.capitalize() for word in palavras]))

    texto_formatado.config(state="disabled")

def copiar_para_area_de_transferencia():
    texto = texto_formatado.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showinfo("Nada para copiar", "O campo de texto formatado está vazio.")
        return

    root.clipboard_clear()
    root.clipboard_append(texto)
    root.update()
    mostrar_popup_copiado()

def limpar_campos():
    entrada = entrada_texto.get("1.0", tk.END).strip()
    saida = texto_formatado.get("1.0", tk.END).strip()
    if not entrada and not saida:
        messagebox.showinfo("Nada para limpar", "Nenhum conteúdo para limpar.")
        return

    entrada_texto.delete("1.0", tk.END)

    texto_formatado.config(state="normal")
    texto_formatado.delete("1.0", tk.END)
    texto_formatado.config(state="disabled")

def mostrar_popup_copiado():
    popup = tk.Toplevel(root)
    popup.overrideredirect(True)
    popup.configure(bg="black")
    popup.geometry("200x50+{}+{}".format(root.winfo_x() + 100, root.winfo_y() + 100))

    label = tk.Label(popup, text="TEXTO COPIADO", fg="white", bg="black", font=("Arial", 12, "bold"))
    label.pack(expand=True)

    popup.after(1500, popup.destroy)

root = tk.Tk()
root.title("FORMULARIO UPPER E LOWER")
root.state('zoomed')

footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)

entrada_texto = tk.Text(root, height=5, width=60)
entrada_texto.pack(pady=10)

opcoes = ["UPPER", "LOWER", "MISTO"]
combo_opcoes = ttk.Combobox(root, values=opcoes, state="readonly")
combo_opcoes.current(0)
combo_opcoes.pack(pady=5)

texto_formatado = tk.Text(root, height=5, width=60, state="disabled")
texto_formatado.pack(pady=10)

btn_converter = tk.Button(root, text="CONVERTER", command=converter_texto)
btn_copiar = tk.Button(root, text="COPIAR", command=copiar_para_area_de_transferencia)
btn_limpar = tk.Button(root, text="LIMPAR", command=limpar_campos)

btn_converter.pack(pady=5)
btn_copiar.pack(pady=5)
btn_limpar.pack(pady=5)

root.mainloop()
