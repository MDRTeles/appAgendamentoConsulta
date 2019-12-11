from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

NOME_APP = "Menu Cadastro"
root = Tk()
root.configure(bg='#2F4F4F')


def sair(event=NONE):
    if tkinter.messagebox.askokcancel('Sair', "Deseja realmente sair?"):
        root.destroy()


def showSobre(event=None):
    fram()


def montarMenu():
    menu_bar = Menu(root)
    arq_menu = Menu(menu_bar, tearoff=0)
    aux_menu = Menu(menu_bar, tearoff=0)
    cad_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Arquivo", underline=0, menu=arq_menu)
    menu_bar.add_cascade(label="Cliente", underline=0, menu=aux_menu)
    menu_bar.add_cascade(label="Cidade", underline=0, menu=cad_menu)
    root.config(menu=menu_bar)
    arq_menu.add_command(label='Sobre', compound='left', command=showSobre)
    arq_menu.add_separator()
    arq_menu.add_command(label="Sair", accelerator='Alt+F4', compound='left', command=sair)
    aux_menu.add_command(label='Cliente', compound='left', command=fram_cadCli)
    aux_menu.add_command(label='Exibir Clientes', compound='left', command=fram_listCli)
    cad_menu.add_command(label='Agenda', compound='left', command=fram_cadCid)
    cad_menu.add_command(label='Exibir Agenda', compound='left', command=fram_listCid)


def initial():
    montarMenu()
    root.protocol('WM_DELETE_WINDOW', sair)
    root.protocol('WM_DELETE_WINDOW', sair)
    root.title(NOME_APP)

    root.geometry("500x400")
    btn_exit()
    root.mainloop()


def fram():
    INFO_APP = "Informações do Sistema"
    newWindow = Tk()
    newWindow.title(INFO_APP)
    newWindow.configure(bg='#2F4F4F')
    newWindow.geometry("500x400")
    lb1 = Label(newWindow, text="\n           Cadastramento de Usuários\n"
                                "\nO sistema foi desenvolvido para armazenar e organizar todos os tipos de informações, \n"
                                "Sendo possivel incialmente cadastrar clientes e agendar consultas, tudo armazenando em bando de dados.")
    lb1['bg'] = '#2F4F4F'
    lb1.pack()
    newWindow.mainloop()


# frame cadastramento cliente
def func_tit(titulo):
    newWindow = Tk()
    newWindow.configure(bg='#2F4F4F')
    newWindow.geometry("500x400")
    newWindow.title(titulo)


def fram_cadCli():
    func_tit("Cadastrar Clientes")
    newWindow.mainloop()


# frame lista de cliente
def fram_listCli():
    func_tit("Listar Clientes")
    newWindow.mainloop()


def fram_cadCid():
    func_tit("Cadastrar Cidades")
    newWindow.mainloop()


def fram_listCid():
    func_tit("Listar Cidades")
    newWindow.mainloop()


def btn_exit():
    bt = Button(root, width=20, text="LOGOUT", bg="yellow", command=sair)
    bt.place(x=170, y=340)


"""
	lb= Label(root, text="Teste")
	lb.place(x=100,y=150)
"""
if __name__ == '__main__':
    initial()
