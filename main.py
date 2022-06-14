import tkinter as tk
import time
from chatbot import answer

s0=answer('0')

# 发送消息
def sendMsg():
    t1_Msg.configure(state=tk.NORMAL)
    strMsg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    t1_Msg.insert("end", strMsg, 'green')
    sendMsg = t2_sendMsg.get('0.0', 'end')
    str=sendMsg
    t1_Msg.insert("end", sendMsg)
    t2_sendMsg.delete('0.0', "end")
    t1_Msg.update()
    strMsg="python:"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    t1_Msg.insert("end", strMsg, 'green')
    str=answer(str)
    if str=='vjjk':
        str='哈人'
    elif str=='dxfhj':
        str='别说了，太哈人了'
    elif str=='我不会因为我一直都看得到你你一直在我心里':
        str='村里刚通网，不知道你在说什么'
    elif str=='个':
        str='差不多得了'
    elif str=='猪操':
        str='操'

    sendMsg=str+'\n'
    t1_Msg.insert("end", sendMsg)
    t1_Msg.config(state=tk.DISABLED)
    # print(strMsg + sendMsg)

def send(self):
    sendMsg()

# 创建窗口
app = tk.Tk()
app.title('与python聊天')

#
w = 800
h = 660
sw = app.winfo_screenwidth()
sh = app.winfo_screenheight()
x = 200
y = (sh - h) / 2
app.geometry("%dx%d+%d+%d" % (w, h, x, y))
app.resizable(0, 0)

# 远程按钮
desktop_btn = tk.Button(text="远程协助")
desktop_btn.place(x=700, y=2)

# 聊天消息预览窗口
t1_Msg = tk.Text(width=113, height=30)
t1_Msg.tag_config('green', foreground='#008C00')  # 创建tag
t1_Msg.place(x=2, y=35)
# t1_Msg.config(state=tk.DISABLED)
# t1_Msg.configure(state='disabled')

# 聊天消息发送
t2_sendMsg = tk.Text(width=112, height=10)
t2_sendMsg.place(x=2, y=485)


photo1 = tk.PhotoImage(file="btn3.PNG")#file：t图片路径
imgLabel1 = tk.Label(app,   image=photo1)#把图片整合到标签类中
imgLabel1.place(x=0, y=435)
photo2 = tk.PhotoImage(file="rob2.PNG")#file：t图片路径
imgLabel2 = tk.Label(app,   image=photo2)#把图片整合到标签类中
imgLabel2.place(x=500, y=70)


# 发送按钮
sendMsg_btn = tk.Button(text="发送（Send）", command=sendMsg)
sendMsg_btn.place(x=665, y=628)
t2_sendMsg.bind('<Return>',send)
# 主事件循环
app.mainloop()