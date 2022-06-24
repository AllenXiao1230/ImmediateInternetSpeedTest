from tkinter.dnd import dnd_start
import psutil
import time
from tkinter import *

def make_app():
    app =Tk()
    app.geometry('200x100')
    app.config(bg='#303030')
    Label(text='實時網速監控',font=('Hack',23,'bold'),bg='#303030',fg='white').pack()
    Label(name='lb2',text='_kb/s'     ,font=('Hack',20,'bold'),bg='#303030',fg='white').pack()
    Label(name='lb3',text='_kb/s'     ,font=('Hack',20,'bold'),bg='#303030',fg='white').pack()
    return app

def speed_test():

    d1 = psutil.net_io_counters()
    s1 = psutil.net_io_counters()
    time.sleep(0.5)
    d2 = psutil.net_io_counters()
    s2 = psutil.net_io_counters()

    ds = d2.bytes_recv - d1.bytes_recv
    ss = s2.bytes_sent - s1.bytes_sent

    
    return '下載 '+str('%.2f'%(ds / 1024)) + ' kb/s','上傳 '+str('%.2f'%(ss / 1024)) + ' kb/s'

def ui_updata(do):
    data = do()
    #app下名字是lb2的子控件
    lb2  = app.children['lb2']
    lb3  = app.children['lb3']
    
    lb2.config(text=data[0])
    lb3.config(text=data[1])
   
    app.after(500,lambda:ui_updata(do))

app = make_app()
app.after(500,lambda :ui_updata(speed_test))
app.mainloop()