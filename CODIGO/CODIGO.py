import tkinter as tk
from tkinter import ttk

def converter_texto():
    opcao = combo_opcoes.get()
    texto_formatado.delete(1.0, tk.END)
    texto = entrada_texto.get("1.0", tk.END)
    if opcao == "UPPER":
        texto_formatado.insert(tk.END, texto.upper())
    elif opcao == "LOWER":
        texto_formatado.insert(tk.END, texto.lower())
    elif opcao == "MISTO":
        texto = texto.lower()  
        palavras = texto.split()
        texto_formatado.insert(tk.END, ' '.join([word.capitalize() for word in palavras]))

def copiar_para_area_de_transferencia():
    texto_formatado_clipboard = texto_formatado.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(texto_formatado_clipboard)
    root.update()

def limpar_campos():
    entrada_texto.delete("1.0", tk.END)
    texto_formatado.delete(1.0, tk.END)

root = tk.Tk()
root.title("CONVERSOR DE TEXTO")

footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)
root.state('zoomed')

entrada_texto = tk.Text(root, height=5, width=40)
entrada_texto.pack()

opcoes = ["UPPER", "LOWER", "MISTO"]
combo_opcoes = ttk.Combobox(root, values=opcoes, state="readonly")
combo_opcoes.current(0)
combo_opcoes.pack()

texto_formatado = tk.Text(root, height=5, width=40)
texto_formatado.pack()

btn_converter = tk.Button(root, text="CONVERTER", command=converter_texto)
btn_copiar = tk.Button(root, text="COPIAR", command=copiar_para_area_de_transferencia)
btn_limpar = tk.Button(root, text="LIMPAR", command=limpar_campos)

btn_converter.pack()
btn_copiar.pack()
btn_limpar.pack()

root.mainloop()
