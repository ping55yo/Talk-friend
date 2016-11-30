from tkinter import *
def sv():
    #s=str(input("Server: "))
    print("OK")
gui=Tk()
gui.geometry("550x550")
gui.title("TF:Talk friend")
mlabel=Label(text="Talk to friends",fg="blue").pack()
mButton=Button(text="connect",command=sv).pack()
#objEntry=Entry().pack()
menubar=Menu(gui)
#เมนูการเชื่อมต่อ
connect=Menu(menubar,tearoff=0)
connect.add_command(label="Add Server ")
connect.add_command(label="Delete Server ")
connect.add_command(label="Connect Server ")
connect.add_command(label="List Server ")
connect.add_command(label="Close")
 #เมนูตั้งค่า
setting=Menu(menubar,tearoff=0)
setting.add_command(label="Microphone ")
setting.add_command(label="Sound ")

menubar.add_cascade(label="Connect",menu=connect)
menubar.add_cascade(label="Setting",menu=setting)

gui.config(menu=menubar)
gui.mainloop()