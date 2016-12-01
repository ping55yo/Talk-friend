from tkinter import *
from tkinter import messagebox
def sv():
    #s=str(input("Server: "))
    print("OK")
#def discon(event):
    messagebox.showinfo(title='แสดงข้อคววาม',message="ตัดการเชื่อมต่อแล้ว")
#def con(evnet):
    messagebox.showinfo(title='แสดงข้อคววาม', message="เชื่อมต่อแล้ว")

gui=Tk()
gui.geometry("550x550")
gui.title("TF:Talk friend")
mlabel=Label(text="Talk to friends",fg="blue").pack()
mButton=Button(text="connect",command=sv).pack()
#mButton.bind(Button>-1,con).pack()
disconnect=Button(text="disconnect",command=sv).pack()
#disconnect.bind('Button-1',discon).pack()
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