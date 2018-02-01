import discord
import asyncio
try:
    from Tkinter import *
except:
    from tkinter import *
from threading import Thread

window = Tk()
window.title("Discord Client")
window.wm_state("zoomed")
def Select_Server(event):
    Current = List_Servers.curselection()
    print(Current)
    print(List_Servers.get(ANCHOR))
    for i in range(len(Servers)):
        print(Servers[i])
        if List_Servers.get(List_Servers.curselection()) == Servers[i][1]:
            Server = Servers[i][0]
    List_Channels.delete(0)
    Channels = []
    global Channels
    for channel in Server.channels:
        List_Channels.insert(END,channel.name)
        Channels.append([channel,channel.name])
    
def Select_Channel(event):
    global Channels
    print(List_Channels.get(ANCHOR))
    for i in range(len(Channels)):
        print(Channels[i])
        if List_Channels.get(List_Channels.curselection()) == Channels[i][1]:
            Channel = Channels[i][0]
    messages = client.logs_from(Channel,limit=500)
    print(type(messages))
    Main = ""
    async for message in messages:
        Main = Main + message.content + "\n"
        Messages.configure(text=Main)

List_Servers = Listbox(window,width=20,selectmode=BROWSE,height=window.winfo_reqheight())
List_Servers.bind("<Double-Button-1>",Select_Server)
List_Servers.grid(row=1,column=1)
List_Channels = Listbox(window,width=40,selectmode=BROWSE,height=window.winfo_reqheight())
List_Channels.bind("<Double-Button-1>",Select_Channel)
List_Channels.grid(row=1,column=2)
Messages = Label(window,width=window.winfo_reqwidth()-60,height=window.winfo_reqheight())
Messages.grid(row=1,column=3)
client = discord.Client()

Servers = []

@client.event
async def on_ready():
    for server in client.servers:
        List_Servers.insert(END,server.name)
        Servers.append([server,server.name])



def run_bot():
    client.run("NDA0MzgxNzYzMDg4MDIzNTYz.DUVFVg.Tgz3E_9JZ6KpVfu8xRbZs0qOacY")


Thread(target=run_bot).start()
window.mainloop()
