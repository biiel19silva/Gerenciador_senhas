from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# O método join concatena todos os caracteres da lista_senha, usando um separador vazio, que no caso irá juntar
# todos os caracteres simplesmente sem deixar nenhum espaço
def gerar_senha():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letras_senha = [choice(letras) for _ in range(randint(8, 10))]
    simbolos_senha = [choice(simbolos) for _ in range(randint(2, 4))]
    numeros_senha = [choice(numeros) for _ in range(randint(2, 4))]

    lista_senha = letras_senha + simbolos_senha + numeros_senha
    shuffle(lista_senha)

    senha = "".join(lista_senha)

    entrada_senha.insert(0, senha)

def salvar_dados ():
    # O método get faz com que o valor na caixa de texto do site, email e senha sejam armazenados e salvos em
    # variáveis destinadas para cada campo.
    # A funcionalidade with open (nome do arquivo, "a"), faz com que o arquivo seja aberto em modo append, que
    # irá escrever o texto sempre no final do arquivo.
    # O método write irá escrever o valor das variáveis site, email e senha de maneira formatada.
    # O método delete irá deletar todo o texto a partir de um range desejado pelo usuário, sendo o primeiro parâmetro
    # o início do range e o segundo parâmetro o fim do range.
    site = entrada_site.get()
    email = entrada_email.get()
    senha = entrada_senha.get()

    if len(site) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Atenção", message="Você deixou campos obrigatórios em branco!")
        
    else:
        escolha = messagebox.askokcancel(title=site, message=f"Essas são as informações inseridas: \nEmail: {email} \nSenha: {senha} \nDeseja salvar?")

        if escolha:
            with open("senhas.txt", "a") as arquivo_senha:
                arquivo_senha.write(f"{site} | {email} | {senha}\n")
                entrada_site.delete(0, END)
                entrada_senha.delete(0, END)

                messagebox.showinfo(title="Confirmação", message="Dados salvos com sucesso!")

        else:
            messagebox.showinfo(title="Cancelado", message="Nenhuma ação foi realizada.")

janela = Tk()
janela.title("Gerenciador de senhas")
janela.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Identificadores
identificador_site = Label(text="Site:")
identificador_site.grid(row=1, column=0)

identificador_email = Label(text="Email/Nome de usuário:")
identificador_email.grid(row=2, column=0)

identificador_senha = Label(text="Senha:")
identificador_senha.grid(row=3, column=0)

# Entradas
# O argumento columnspan expande o identificador com as unidades de colunas que o usuário deseja.
# O método focus faz com que o cursor ja fique ativo no objeto criado, pronto para digitar algum texto.
# O método insert faz com que a caixa de texto já tenha um texto preenchido quando o usuário execute o programa,
# passando a posição inicial do texto como primeiro parâmetro e o próprio texto como segundo parâmetro.
entrada_site = Entry(width=35)
entrada_site.grid(row=1, column=1, columnspan=2)
entrada_site.focus()

entrada_email = Entry(width=35)
entrada_email.grid(row=2, column=1, columnspan=2)
entrada_email.insert(0, "exemplo@gmail.com")

entrada_senha = Entry(width=23)
entrada_senha.grid(row=3, column=1)

# Botões
bt_gerar_senha = Button(text="Gerar senha", command=gerar_senha)
bt_gerar_senha.grid(row=3, column=2)

bt_adicionar_senha = Button(text="Adicionar senha", width=36, command=salvar_dados)
bt_adicionar_senha.grid(row=4, column=1, columnspan=2)

janela.mainloop()