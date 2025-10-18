import tkinter as tk


#janela
janela = tk.Tk()
janela.title = " "
janela.geometry("700x550")
janela.resizable(False,False)

#Lista de escalas termométricas
escalas = ["Celsius", "Fahrenheit", "Kelvin"]

#Frame Principal
frame_principal = tk.Frame(janela, bg = "#340B32")
frame_principal.pack(fill = "both", expand = True)

#Frame Inicial
frame_inicial = tk.Frame(frame_principal, bg = "#340B32")
frame_inicial.pack(pady=(30,30))

label = tk.Label(frame_inicial, text = " \u2728 Conversor de Temperaturas \u2728", fg = "#FFFFFF", bg="#340B32",font = ("Comic Sans MS", 18))
label.pack(side= "top", padx = 10, pady = 15)
label = tk.Label(frame_inicial, text="Temperatura inicial:",fg = "#FFFFFF", bg="#340B32",font = ("Comic Sans MS", 12))
label.pack(side="left", padx = 8)
temp_inicial = tk.Entry(frame_inicial, justify='center',width=15)
temp_inicial.pack(side = "left")
escala_inicial = tk.Spinbox(frame_inicial, justify= "center",width=15, values= escalas, wrap = True)
escala_inicial.pack(side = "left", padx = 5)
label = tk.Label(frame_inicial, text="Escala termométrica inicial",fg = "#FFFFFF", bg="#340B32", font = ("Comic Sans MS", 12))
label.pack(side = "left")


#Frame Abaixo
frame_abaixo = tk.Frame(frame_principal, bg="#340B32")
frame_abaixo.pack()

label1 = tk.Label(frame_abaixo, text="Escala termométrica desejada:", fg = "#FFFFFF",bg="#340B32",font = ("Comic Sans MS", 12))
label1.pack(side="top")
escala_desejada = tk.Spinbox(frame_abaixo, justify="center",width=15, values= escalas, wrap = True)
escala_desejada.pack(side = "bottom", padx = 5, pady = 5)


#LÓGICA DAS CONVERSÕES DE TEMPERATURA

def converter():
    try:
        valor_inicial = float(temp_inicial.get())
        escala_origem = escala_inicial.get()
        escala_destino = escala_desejada.get()

        if escala_origem == escala_destino:
            resultado = valor_inicial
        elif escala_origem == "Celsius" and escala_destino == "Fahrenheit":
            resultado = valor_inicial * (9.0/5.0)+32.0
        elif escala_origem == "Celsius" and escala_destino == "Kelvin":
            resultado =  valor_inicial + 273.15
        elif escala_origem == "Fahrenheit" and escala_destino == "Celsius":
            resultado = 5.0 * (valor_inicial - 32.0)/9.0
        elif escala_origem == "Fahrenheit" and escala_destino == "Kelvin":
            resultado = (((valor_inicial - 32) * 5)/9) + 273.15
        elif escala_origem == "Kelvin" and escala_destino == "Celsius":
            resultado = valor_inicial - 273.15
        elif escala_origem == "Kelvin" and escala_destino == "Fahrenheit":
            resultado = (valor_inicial - 273.15) * 1.8 + 32
        else:
            resultado = "Erro"
        

        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, f"{resultado:.2f}")
    except ValueError:
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, "Entrada inválida!")

# Botão copiar
def copiar():
    texto = resultado_entry.get()
    if texto and texto != "Entrada inválida!":
        janela.clipboard_clear()
        janela.clipboard_append(resultado_entry.get())
        janela.update()

        label_confirmacao = tk.Label(frame_botao_copiar, text="Copiado!",bg="#340B32", fg="#FFFFFF")
        label_confirmacao.pack(pady = 5)
        janela.after(2000, lambda: label_confirmacao.destroy())
    else:
        label_confirmacao = tk.Label(frame_botao_copiar, text="Nada pra copiar!", bg= "#340B32", fg="#FFFFFF")
        label_confirmacao.pack(side = "bottom")
        janela.after(2000, lambda: label_confirmacao.destroy())

#Frame Botões
frame_botoes = tk.Frame(frame_principal, bg = "#340B32" )
frame_botoes.pack()

btn1 = tk.Button(frame_botoes, width=10, height= 2, text="Converter", font = ("Comic Sans MS", 12), activeforeground= "#000000", activebackground= "#FFFFFF", command = converter)
btn1.pack(pady = (50))


label = tk.Label(frame_botoes, text="Temperatura convertida:",fg = "#FFFFFF", bg="#340B32",font = ("Comic Sans MS", 13))
label.pack(side = "left", pady = 8)

#Frame botão copiar
frame_botao_copiar = tk.Frame(frame_principal, bg = "#340B32" )
frame_botao_copiar.pack()

resultado_entry = tk.Entry(frame_botao_copiar, justify='center')
resultado_entry.pack(side = "left", padx = 8)

btn2 = tk.Button(frame_botao_copiar, width = 10, pady = 5, text="Copiar", font = ("Comic Sans MS", 12), activeforeground= "#000000", activebackground= "#FFFFFF", command = copiar)
btn2.pack(side="bottom")


#fórmulas
#celsius para fahrenheit == F = C∗(9.0/5.0)+32.0
#fahrenheit para celsius == C = 5.0 ∗ (F − 32.0)/9.0
#kelvin para celsius == C = K − 273.15
#celsius para kelvin == K = C + 273.15

#Organizar a janela e adicionar lógica 

janela.mainloop()