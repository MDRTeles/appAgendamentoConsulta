import sqlite3
from tkinter import *
from tkinter import messagebox as ms

#criar banco e usuarios (caso nao exista)
with sqlite3.connect("quit.db") as db:
    c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
db.commit()
db.close()

#classe incial
class inic():
    def __init__(self,master):
        #janela
        self.master = master
        #variaveis usadas
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()
    #funcao login
    def login(self):
        #conecta bd
        with sqlite3.connect("quit.db") as db:
            c = db.cursor()
        #procura usuario
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            self.logf.pack_forget()
            self.head["text"] = self.username.get() + "\nVocê esta logado,"
            self.head['pady'] = 150
        else:
            ms.showerror('opps!! ', "Uuário não confere!")

    # novo usuario bd
    def new_user(self):
        # conecta bd
        with sqlite3.connect("quit.db") as db:
            c = db.cursor()

        find_user = ("SELECT * FROM user WHERE username = ?")
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror("Ops", "Usuário existente, seja criativo!!")
        else:
            ms.showinfo("Sucesso!!", "Conta Criada!")
            self.log()
        #insere no bd novo usuario
        insert = 'INSERT INTO user(username, password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text'] = " LOGIN "
        self.logf.pack()
    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.head['text'] = 'Crie sua Conta!'
        self.crf.pack()
    #Design das jenaleas
    def widgets(self):
        self.head = Label(self.master, text="  LOGIN  ", font = ("freesansbold", 35), pady=40)
        self.head.pack()

        self.logf = Frame(self.master, padx = 10, pady = 10)
        Label(self.logf, text = "Username: ", font = ("freesansbold", 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.logf, textvariable = self.username, bd=8, font = ('calibri', 15, 'bold')).grid(row=0, column=1)
        Label(self.logf, text= "Password: ", font=('freesansbold', 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)

root = Tk()
inic(root)
root.mainloop()