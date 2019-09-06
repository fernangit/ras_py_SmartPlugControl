import sys
import tkinter
import tplink_smartplug_py3 as plug

root = tkinter.Tk()
root.title(u"Sample SmartPlug")
root.geometry("400x300")

def PowerOnEntryValue(event):
    #PowerON
    plug.control('172.41.195.22', 'on')

def PowerOffEntryValue(event):
    #PowerOFF
    plug.control('172.41.195.22', 'off')

#ボタン設定
Button1 = tkinter.Button(text=u'Power ON', width=10)
Button1.bind("<Button-1>",PowerOnEntryValue) 
#左クリック（<Button-1>）されると，PowerOnEntryValue関数を呼び出すようにバインド
Button1.place(x=50, y=60)
#Button1.pack()

Button2 = tkinter.Button(text=u'Power OFF', width=10)
Button2.bind("<Button-1>",PowerOffEntryValue) 
#左クリック（<Button-1>）されると，PowerOffEntryValue関数を呼び出すようにバインド
Button2.place(x=50, y=120)
#Button2.pack()

root.mainloop()

