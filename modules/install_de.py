import subprocess,os
from tkinter import messagebox

def install(de = None):
    if de == None:
        print("[-DE Manager-] You must be select desktop environment. :-)")
    elif not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        messagebox.showerror('Permissions Error', 'You must be root >:(')
        exit()
    else:
        if de == "Xfce":
            subprocess.run(["pacman","-S","--needed","xfce4", "xfce4-goodies","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "Gnome":
            subprocess.run(["pacman","-S","--needed","gnome","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "KDE Plasma":
            subprocess.run(["pacman","-S","--needed","plasma", "kde-applications","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "LXQT":
            subprocess.run(["pacman","-S","--needed","lxqt","xdg-utils","ttf-freefont","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "LXDE":
            subprocess.run(["pacman","-S","--needed","lxde","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "Cinnamon":
            subprocess.run(["pacman","-S","--needed","cinnamon","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "Budgie":
            subprocess.run(["pacman","-S","--needed","budgie-desktop","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        elif de == "Mate":
            subprocess.run(["pacman","-S","--needed","mate", "mate-extra","--noconfirm"])
            messagebox.showinfo('Succes',f"{de} succesfully installed.")
        else:
            messagebox.showerror("Permissions Error", f'[-DE Manager-] I cant found "{de}" in my database :(')