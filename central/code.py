import tkinter as tk


#janela
janela = tk.Tk()
janela.title = " "
janela.geometry("600x450")
janela.resizable(False,False)



#Frames
frame_principal = tk.Frame(janela, bg = "#340B32")
frame_principal.pack(fill = "both", expand = True)

#########
frame_inicial = tk.Frame(frame_principal, bg = "#340B32")
frame_inicial.pack(pady=(50,30))

label = tk.Label(frame_inicial, text="Temperatura inicial:",fg = "#FFFFFF", bg="#340B32",font = ("Comic Sans MS", 12))
label.pack(side="left", padx = 8)
temp_inicial = tk.Entry(frame_inicial, justify='center',width=15)
temp_inicial.pack(side = "left")
escala_inicial = tk.Spinbox(frame_inicial, justify= "center",width=15)
escala_inicial.pack(side = "left", padx = 5)
label = tk.Label(frame_inicial, text="Escala termométrica inicial",fg = "#FFFFFF", bg="#340B32", font = ("Comic Sans MS", 12))
label.pack(side = "left")

########
frame_abaixo = tk.Frame(frame_principal, bg="#340B32")
frame_abaixo.pack()

label1 = tk.Label(frame_abaixo, text="Escala termométrica desejada:", fg = "#FFFFFF",bg="#340B32",font = ("Comic Sans MS", 13))
label1.pack(side="top")
escala_desejada = tk.Spinbox(frame_abaixo, justify="center",width=15)
escala_desejada.pack(side = "bottom", padx = 5, pady = 5)

########
frame_botoes = tk.Frame(frame_principal, bg = "#340B32")
frame_botoes.pack()

btn1 = tk.Button(frame_botoes, width=10, height= 2, text="Converter", font = ("Comic Sans MS", 12), bg= "#FFFFFF")
btn1.pack(pady = (50))

label = tk.Label(frame_botoes, text="Temperatura convertida:",fg = "#FFFFFF", bg="#340B32",font = ("Comic Sans MS", 13))
label.pack(side = "left", pady = 8)
temp_inicial = tk.Entry(frame_botoes, justify='center')
temp_inicial.pack(side = "left", padx = 8)

btn2 = tk.Button(frame_botoes, width = 10, pady = 5, text="Copiar", font = ("Comic Sans MS", 12), bg = "#FFFFFF")
btn2.pack()


#fórmulas
#celsius para fahrenheit == F = C∗(9.0/5.0)+32.0
#fahrenheit para celsius == C = 5.0 ∗ (F − 32.0)/9.0
#kelvin para celsius == C = K − 273.15
#celsius para kelvin == K = C + 273.15

#Organizar a janela e adicionar lógica 

janela.mainloop()