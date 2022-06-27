import tkinter
from tkinter import *
from modules import install_de as install

root = Tk()
root.title("DE Manager")
root.geometry("500x200")
root.resizable(width=False,height=False)
root.configure(bg="#3B4248")

menu = StringVar()
menu.set("Select Any Desktop Environment")

environments = ["Gnome","Xfce","KDE Plasma","Mate","Budgie","Cinnamon","LXDE","LXQT"]

de_menus = OptionMenu(root,menu,*environments)
de_menus.place(x=135,y=15)

def install_command():
    selected_de = menu.get()
    install.install(de = selected_de)

install_button = Button(text="Install Desktop Environment",fg="red",font=("Arial",12),command=install_command)
install_button.place(x=140,y=95)

def delete_command():
    de_name = menu.get()
    install.uninstall(de = de_name)

uninstall_button = Button(text="Uninstall Desktop Environment",fg="blue",font=("Arial",12),command=delete_command)
uninstall_button.place(x=140,y=135)
root.mainloop()