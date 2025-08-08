import tkinter as tk


#janela
janela = tk.Tk()
janela.title = " "
janela.geometry("600x450")
janela.resizable(False,False)

#Frames
frame_principal = tk.Frame(janela, bg = "#FBD3F9")
frame_principal.pack(fill = "both", expand = True)

#########
frame_inicial = tk.Frame(frame_principal, bg = "#FBD3F9")
frame_inicial.pack(pady=(50,30))

label = tk.Label(frame_inicial, text="Digite a temperatura inicial:",bg="#FBD3F9")
label.pack(side="left", padx = 5)
temp_inicial = tk.Entry(frame_inicial, justify='center',width=15)
temp_inicial.pack(side = "left")
escala_inicial = tk.Spinbox(frame_inicial, justify= "center",width=15)
escala_inicial.pack(side = "left", padx = 5)
label = tk.Label(frame_inicial, text="Escala termométrica inicial",bg="#FBD3F9")
label.pack(side = "left")

########
frame_abaixo = tk.Frame(frame_principal, bg="#FBD3F9")
frame_abaixo.pack()

label1 = tk.Label(frame_abaixo, text="Escala termométrica desejada:", bg="#FBD3F9")
label1.pack(side="left")
escala_desejada = tk.Spinbox(frame_abaixo, justify="center",width=15)
escala_desejada.pack(side = "left", padx = 5, pady = 10)

########
frame_botoes = tk.Frame(frame_principal, bg = "#FBD3F9")
frame_botoes.pack()

btn1 = tk.Button(frame_botoes, width=10, height= 2, text="Converter")
btn1.pack(pady = (20))

label = tk.Label(frame_botoes, text="Temperatura convertida:",bg="#FBD3F9")
label.pack(side = "left", pady = 5)
temp_inicial = tk.Entry(frame_botoes, justify='center')
temp_inicial.pack(side = "left", padx = 5)

btn2 = tk.Button(frame_botoes, width = 10, pady = 5, text="Copiar")
btn2.pack()

janela.mainloop()