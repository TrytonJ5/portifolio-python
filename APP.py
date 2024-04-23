import customtkinter as ctk
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bd_Rhythme'
)
cursor = conexao.cursor()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("RHYTHME")
janela.iconbitmap("icone.ico")
janela.resizable(width=False,height=False)
janela.geometry("750x450")

frame1 = ctk.CTkFrame(master = janela,width=225,height=420,fg_color="#001f3f").place(x=18.75,y=15)
frame2 = ctk.CTkFrame(master = janela,width=225,height=400,fg_color="#3b0050").place(x=262.5,y=25)
frame3 = ctk.CTkFrame(master = janela,width=225,height=420,fg_color="#001f3f").place(x=506.25,y=15)

ctk.CTkLabel(janela, text="RHYTHME", font=("arial",35), text_color="white").pack(pady=10)

lab_usuario = ctk.CTkLabel(janela, text="Digite seu usuario:",font=("arial", 15), bg_color="#3b0050").pack(pady=10)
usuario = ctk.CTkEntry(janela, width=200,placeholder_text="usuario",font=("arial", 15))
usuario.pack()

lab_email = ctk.CTkLabel(janela, text="Digite seu e-mail:", font=("arial", 15), bg_color="#3b0050").pack(pady=10)
email = ctk.CTkEntry(janela, width=200,placeholder_text="e-mail",font=("arial", 15))
email.pack()

lab_senha = ctk.CTkLabel(janela, text="Digite sua senha:", font=("arial", 15), bg_color="#3b0050").pack(pady=10)
senha = ctk.CTkEntry(janela, width=200,placeholder_text="senha",font=("arial", 15),show="*")
senha.pack()


def entrar():
    usuarios = usuario.get()
    emails = email.get()
    senhas = senha.get()
    nova_janela = ctk.CTkToplevel(janela,fg_color="#001f3f")
    nova_janela.geometry("450x250")
    nova_janela.title("RHYTHME")
    ctk.CTkLabel(nova_janela, text="RHYTHME",font=("arial", 35), text_color="white").pack(pady=5)
    musicatext = ctk.CTkLabel(nova_janela,text="Digite a musica que vc quer ouvir").pack()
    entry_musica = (ctk.CTkEntry(nova_janela,width=150))
    entry_musica.pack()
    artistatext = ctk.CTkLabel(nova_janela, text="Digite qual artista vc procura").pack()
    entry_artista= (ctk.CTkEntry(nova_janela, width=150))
    entry_artista.pack()
    btn_p2 = ctk.CTkButton(nova_janela,width=50,text="ESCUTAR",fg_color="#3b0050", hover_color="#4F0046")
    btn_p2.pack(pady=5)

btn_p1 = (ctk.CTkButton(janela, width=75, text="ENTRAR",fg_color="#001f3f",hover_color="#000C40",command=entrar))
btn_p1.pack(pady=50)

lab_rodape = ctk.CTkLabel(janela,text="CRIADO E DESENVOLVIDO PELOS PUTIFEROS",font=("time new roma",8),text_color="black",bg_color="#001f3f").place(x=530,y=400)

janela.mainloop()
